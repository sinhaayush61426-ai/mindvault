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

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)