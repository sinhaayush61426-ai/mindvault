# ================================
# DATABASE MIGRATION UTILITY [DEPRECATED]
# ================================
#
# WARNING: This file is NOT actively used.
#
# Previous Purpose:
#   Old database migration script for v1 to v2 upgrade
#   handling schema changes and column additions.
#
# Current Status:
#   - Deprecated: app.py now uses db.create_all() for schema
#   - Kept for reference only
#   - Can be safely deleted
#
# If you need to run migrations:
#   Modify app.py or create alembic-based migrations
#
# See Also:
#   - MIGRATION.md for v1→v2 upgrade guide
#   - COMPREHENSIVE_AUDIT.md for changes
#
# Last Modified: May 2026
#

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Import models or define them minimally
class DiaryEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), default="New Reflection")
    category = db.Column(db.String(50), default="General")
    encrypted_content = db.Column(db.LargeBinary, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    release_date = db.Column(db.DateTime, nullable=True)
    is_time_locked = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, nullable=False)

with app.app_context():
    # Check if column exists, if not add it
    from sqlalchemy import text
    try:
        db.session.execute(text("ALTER TABLE diary_entry ADD COLUMN title VARCHAR(100) DEFAULT 'New Reflection'"))
        db.session.commit()
        print("Column 'title' added successfully.")
    except Exception as e:
        print(f"Error or column already exists: {e}")