from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt
from cryptography.fernet import Fernet
from datetime import datetime

app = Flask(__name__)

# --- CONFIG ---
app.config['SECRET_KEY'] = 'mindvault_pro_ultra_secure_999'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mindvault.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# --- ENCRYPTION ---
ENCRYPTION_KEY = Fernet.generate_key() 
cipher = Fernet(ENCRYPTION_KEY)

# --- MODELS ---
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    entries = db.relationship('DiaryEntry', backref='author', lazy=True)

class DiaryEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), default="New Reflection")
    category = db.Column(db.String(50), default="General")
    encrypted_content = db.Column(db.LargeBinary, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(50), nullable=False)
    occupation = db.Column(db.String(50))
    content = db.Column(db.Text, nullable=False)
    is_approved = db.Column(db.Boolean, default=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# --- CHARACTER MATRIX FOR CREATIVE FICTION ---
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    archetype = db.Column(db.String(50), default="Protagonist")  # Protagonist, Antagonist, Support, etc.
    personality_traits = db.Column(db.Text)  # JSON or comma-separated
    backstory = db.Column(db.Text)
    relationships = db.Column(db.Text)  # JSON for interpersonal dynamics
    physical_description = db.Column(db.Text)
    motivations = db.Column(db.Text)
    avatar_color = db.Column(db.String(7), default="#5DADE2")  # Hex color for matrix display
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    author = db.relationship('User', backref='characters')

# --- ENTRY SNAPSHOTS FOR DRAFT VERSIONING ---
class EntrySnapshot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entry_id = db.Column(db.Integer, db.ForeignKey('diary_entry.id'), nullable=False)
    version = db.Column(db.String(50), default="1.0")  # e.g., "1.0", "1.1", "2.0"
    encrypted_content = db.Column(db.LargeBinary, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(255))  # Optional snapshot label
    is_autosave = db.Column(db.Boolean, default=False)
    entry = db.relationship('DiaryEntry', backref='snapshots')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --- AUTH ROUTES (Crucial to fix your BuildError) ---
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        hashed_pw = bcrypt.generate_password_hash(request.form.get('password')).decode('utf-8')
        user = User(username=request.form.get('username'), email=request.form.get('email'), password_hash=hashed_pw)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form.get('email')).first()
        if user and bcrypt.check_password_hash(user.password_hash, request.form.get('password')):
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

# --- APP ROUTES ---
@app.route('/')
def home():
    reviews = Review.query.filter_by(is_approved=True).order_by(Review.timestamp.desc()).limit(3).all()
    return render_template('index.html', reviews=reviews)

@app.route('/dashboard')
@login_required
def dashboard():
    entries = DiaryEntry.query.filter_by(user_id=current_user.id).order_by(DiaryEntry.timestamp.desc()).all()
    return render_template('dashboard.html', entries=entries)

@app.route('/save-entry', methods=['POST'])
@login_required
def save_entry():
    content = request.form.get('content')
    encrypted = cipher.encrypt(content.encode())
    new_entry = DiaryEntry(
        title=request.form.get('title'),
        category=request.form.get('category'),
        encrypted_content=encrypted,
        user_id=current_user.id
    )
    db.session.add(new_entry)
    db.session.commit()
    return redirect(url_for('dashboard'))

# --- CHARACTER MATRIX ROUTES ---
@app.route('/characters')
@login_required
def characters():
    user_characters = Character.query.filter_by(user_id=current_user.id).all()
    return render_template('characters.html', characters=user_characters)

@app.route('/character/new', methods=['GET', 'POST'])
@login_required
def new_character():
    if request.method == 'POST':
        character = Character(
            user_id=current_user.id,
            name=request.form.get('name'),
            archetype=request.form.get('archetype', 'Protagonist'),
            personality_traits=request.form.get('personality_traits'),
            backstory=request.form.get('backstory'),
            relationships=request.form.get('relationships'),
            physical_description=request.form.get('physical_description'),
            motivations=request.form.get('motivations'),
            avatar_color=request.form.get('avatar_color', '#5DADE2')
        )
        db.session.add(character)
        db.session.commit()
        flash(f"Character '{character.name}' created!", 'success')
        return redirect(url_for('characters'))
    return render_template('character_form.html', character=None)

@app.route('/character/<int:character_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_character(character_id):
    character = Character.query.get_or_404(character_id)
    if character.user_id != current_user.id:
        flash('Unauthorized', 'error')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        character.name = request.form.get('name')
        character.archetype = request.form.get('archetype')
        character.personality_traits = request.form.get('personality_traits')
        character.backstory = request.form.get('backstory')
        character.relationships = request.form.get('relationships')
        character.physical_description = request.form.get('physical_description')
        character.motivations = request.form.get('motivations')
        character.avatar_color = request.form.get('avatar_color')
        db.session.commit()
        flash(f"Character '{character.name}' updated!", 'success')
        return redirect(url_for('characters'))
    return render_template('character_form.html', character=character)

@app.route('/character/<int:character_id>/delete', methods=['POST'])
@login_required
def delete_character(character_id):
    character = Character.query.get_or_404(character_id)
    if character.user_id != current_user.id:
        flash('Unauthorized', 'error')
        return redirect(url_for('dashboard'))
    db.session.delete(character)
    db.session.commit()
    flash('Character deleted', 'success')
    return redirect(url_for('characters'))

# --- SNAPSHOT/VERSIONING ROUTES ---
@app.route('/entry/<int:entry_id>/snapshot', methods=['POST'])
@login_required
def create_snapshot(entry_id):
    entry = DiaryEntry.query.get_or_404(entry_id)
    if entry.user_id != current_user.id:
        flash('Unauthorized', 'error')
        return redirect(url_for('dashboard'))
    
    version = request.form.get('version', '1.0')
    description = request.form.get('description', '')
    
    snapshot = EntrySnapshot(
        entry_id=entry_id,
        version=version,
        encrypted_content=entry.encrypted_content,
        description=description,
        is_autosave=False
    )
    db.session.add(snapshot)
    db.session.commit()
    flash(f"Snapshot '{version}' created!", 'success')
    return redirect(url_for('view_entry', entry_id=entry_id))

@app.route('/entry/<int:entry_id>/snapshots')
@login_required
def view_snapshots(entry_id):
    entry = DiaryEntry.query.get_or_404(entry_id)
    if entry.user_id != current_user.id:
        flash('Unauthorized', 'error')
        return redirect(url_for('dashboard'))
    
    snapshots = EntrySnapshot.query.filter_by(entry_id=entry_id).order_by(EntrySnapshot.timestamp.desc()).all()
    return render_template('snapshots.html', entry=entry, snapshots=snapshots)

@app.route('/snapshot/<int:snapshot_id>/restore', methods=['POST'])
@login_required
def restore_snapshot(snapshot_id):
    snapshot = EntrySnapshot.query.get_or_404(snapshot_id)
    entry = snapshot.entry
    
    if entry.user_id != current_user.id:
        flash('Unauthorized', 'error')
        return redirect(url_for('dashboard'))
    
    entry.encrypted_content = snapshot.encrypted_content
    db.session.commit()
    flash(f"Entry restored to version {snapshot.version}", 'success')
    return redirect(url_for('view_entry', entry_id=entry.id))

# --- VIEW ENTRY ROUTE ---
@app.route('/entry/<int:entry_id>')
@login_required
def view_entry(entry_id):
    entry = DiaryEntry.query.get_or_404(entry_id)
    if entry.user_id != current_user.id:
        flash('Unauthorized', 'error')
        return redirect(url_for('dashboard'))
    
    try:
        decrypted = cipher.decrypt(entry.encrypted_content).decode()
    except:
        decrypted = "[Content could not be decrypted]"
    
    return render_template('view_entry.html', entry=entry, content=decrypted)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)