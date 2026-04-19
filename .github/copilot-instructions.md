---
name: mindvault-workspace-instructions
description: "MindVault v2.0 workspace conventions. Use when: working on any MindVault feature, fixing bugs, adding API routes, or modifying frontend/backend code. Covers Flask architecture, encryption patterns, authentication flow, database models, and PWA/frontend development."
---

# MindVault Workspace Instructions

**MindVault v2.0** is a privacy-first creative workspace built for writers, researchers, and creatives. This guide ensures consistent development across the entire codebase.

## Project Overview

```
app.py                                 # Flask app + SQLAlchemy models + 25+ routes
security.py                            # Encryption utilities (VaultSecurity class)
requirements.txt                       # Python dependencies
manifest.json                          # PWA configuration

templates/
├── base.html                          # Base layout with PWA metadata, flash messages, navigation
├── login.html, register.html          # Auth pages (password + biometric UI)
├── dashboard.html                     # Main entry point after login
├── entry.html                         # Rich text editor with auto-save
├── characters.html, character_form.html  # Character Matrix interface
├── snapshots.html, view_entry.html    # Draft versioning and history
└── offline.html                       # Fallback when service worker offline

static/
├── css/
│   ├── style.css                      # Main stylesheet + 20+ CSS variables
│   └── expansion.css                  # v2.0 features (Zen Mode, Matrix, Snapshots)
├── js/
│   ├── main.js                        # Entry point, event listeners
│   ├── enhanced-main.js               # Zen Mode, auto-save, app init (v2.0)
│   ├── service-worker.js              # PWA offline support, caching
│   └── biometric-auth.js              # WebAuthn Face ID / Touch ID
└── svg-icons.html                     # 14 reusable SVG icons (Shield, Star, Zen, etc.)

Database:
├── User                               # Account + bcrypt hash
├── DiaryEntry                         # Encrypted content, categories, timestamps
├── EntrySnapshot                      # Versioned content (auto-save and manual)
├── Character                          # Character profiles for fiction
└── Review                             # Public testimonials (homepage display)
```

## Development Workflow

### Start Development Server

```bash
python3 app.py
# App runs on http://127.0.0.1:5000
```

- Flask debug mode is enabled by default in development
- SQLite database stored locally (`instance/database.db`)
- Hot reload on file changes

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Key Tech Stack

- **Backend**: Flask, SQLAlchemy ORM, Flask-Login, Flask-Bcrypt
- **Frontend**: Vanilla HTML/CSS/JS, Service Worker (PWA), SVG icons
- **Encryption**: Fernet (cryptography library) — AES-128-CBC with HMAC
- **Database**: SQLite3 (local, file-based)
- **Auth**: Bcrypt password hashing + WebAuthn API (Face ID / Touch ID)

---

## Database & Models

### Model Structure

All models are defined in `app.py`. Relationships use SQLAlchemy backrefs for easy navigation.

#### User Model
```python
class User(db.Model, UserMixin):
    id                          # Primary key
    username                    # Unique
    email                       # Unique
    password_hash               # Bcrypt hash (never store plaintext)
    entries = relationship('DiaryEntry')
    characters = relationship('Character')
```

**When adding**: Always include password hashing via `bcrypt.generate_password_hash()`

#### DiaryEntry Model
```python
class DiaryEntry(db.Model):
    id
    title                       # "New Reflection" default
    category                    # "General" default (e.g., "Fiction", "Research")
    encrypted_content           # NEVER store plaintext; always encrypt before saving
    timestamp                   # Created timestamp
    release_date                # For time-locked entries
    is_time_locked              # Boolean flag
    user_id                     # Foreign key to User
    author = relationship('User')
```

**Encryption pattern**: 
```python
cipher = Fernet(ENCRYPTION_KEY)
encrypted = cipher.encrypt(content.encode())
db.session.add(DiaryEntry(encrypted_content=encrypted))
```

#### EntrySnapshot Model
```python
class EntrySnapshot(db.Model):
    id
    entry_id                    # Foreign key to DiaryEntry
    version                     # String like "1.0", "1.1", "2.0"
    encrypted_content           # Frozen version (never modify in-place)
    timestamp                   # When snapshot was created
    description                 # Optional label (e.g., "Draft 1 - Complete")
    is_autosave                 # True for 30-sec auto-saves; False for manual
    entry = relationship('DiaryEntry', backref='snapshots')
```

**Guidelines**: Each snapshot is independent and immutable. When restoring, create a *new* DiaryEntry with restored content, don't overwrite.

#### Character Model
```python
class Character(db.Model):
    id
    user_id                     # Foreign key to User
    name                        # Character identifier
    archetype                   # "Protagonist", "Antagonist", "Mentor", "Support", "Other"
    personality_traits          # Text (JSON or comma-separated)
    backstory                   # Long text
    relationships               # JSON object (e.g., {"father": "Lord Stark", ...})
    physical_description        # Appearance details
    motivations                 # Goals and drives
    avatar_color                # Hex code (e.g., "#5DADE2") for matrix display
    created_at, updated_at      # Timestamps
    author = relationship('User')
```

#### Review Model
```python
class Review(db.Model):
    id
    author_name                 # Reviewer's name (not User account)
    occupation                  # Optional
    content                     # Review text
    is_approved                 # Display on homepage only if True
    timestamp                   # Created timestamp
```

### Encryption Pattern

**NEVER** store plaintext diary entries or snapshots. Always use the Fernet cipher:

```python
from cryptography.fernet import Fernet

cipher = Fernet(ENCRYPTION_KEY)

# Encrypting (frontend or backend)
encrypted_bytes = cipher.encrypt(plaintext.encode())
# Store as binary in database

# Decrypting
plaintext = cipher.decrypt(encrypted_bytes).decode()
```

---

## API Routes & Endpoints

### Authentication Routes

| Route | Method | Purpose |
|-------|--------|---------|
| `/register` | GET, POST | Registration form; creates User with bcrypt hash |
| `/login` | GET, POST | Authentication with password or biometric fallback |
| `/logout` | GET | Destroys session; redirects to home |

**Guards**: Use `@login_required` decorator on protected routes.

### Content Routes

| Route | Purpose | Notes |
|-------|---------|-------|
| `/` | Home page | Public; displays reviews |
| `/dashboard` | Main dashboard | @login_required; lists user's entries |
| `/seal-letter` (POST) | Create or update entry | Encrypts content; creates DiaryEntry |
| `/entry/<id>` | View single entry | @login_required; decrypts and displays |

### Character Matrix Routes (v2.0)

| Route | Method | Purpose |
|-------|--------|---------|
| `/characters` | GET | List all characters for logged-in user |
| `/character/new` | GET, POST | Create new character profile |
| `/character/<id>/edit` | GET, POST | Edit existing character |
| `/character/<id>/delete` | POST | Delete character (removes all snapshots) |

### Snapshot Routes (v2.0)

| Route | Method | Purpose |
|-------|--------|---------|
| `/entry/<id>/snapshot` | POST | Create manual snapshot with version label |
| `/entry/<id>/snapshots` | GET | View all snapshots for an entry (timeline) |
| `/snapshot/<id>/restore` | POST | Restore snapshot; creates new DiaryEntry |

**Auto-save**: The frontend (`enhanced-main.js`) auto-saves every 30 seconds; these are snapshots with `is_autosave=True` and version="auto".

---

## Frontend Architecture

### CSS System

Global CSS variables defined in `static/css/style.css`:

```css
:root {
  --primary-color: #5DADE2;          /* Cyan */
  --secondary-color: #E74C3C;        /* Accent red */
  --dark-bg: #0B0E27;                /* Deep dark for cyberpunk feel */
  --text-primary: #ECF0F1;           /* Light text */
  --border-radius: 8px;
  --transition: all 0.3s ease;
}
```

**When styling**: Use CSS variables for consistency. Avoid hardcoding colors/spacing.

### PWA & Service Worker

**Service Worker** (`static/js/service-worker.js`) handles:
- **Network-first strategy**: Try server first; fallback to cache
- **Cache versioning**: Clears old caches on app update
- **Background sync**: Stores pending entries in IndexedDB; syncs when online
- **Offline fallback**: Shows `/offline.html` if unreachable

**Manifest** (`manifest.json`): Enables installation on mobile/desktop; includes app shortcuts.

### Zen Mode

**Feature**: Hide all navigation and UI; show word/character counter in corner.

**Implementation**:
- **CSS**: `expansion.css` has `.zen-mode` class that hides elements
- **JavaScript**: `enhanced-main.js` toggles Zen Mode; persists preference to localStorage
- **Frontend**: Button in navigation to toggle Zen Mode

**Pattern**:
```javascript
function toggleZenMode() {
  document.body.classList.toggle('zen-mode');
  localStorage.setItem('zenMode', document.body.classList.contains('zen-mode'));
  updateWordCounter();
}
```

### Auto-Save

**30-second auto-save** (`enhanced-main.js`):
1. Capture current content from editor
2. Encrypt content
3. POST to `/entry/<id>/snapshot` with `is_autosave=True`
4. Show toast notification "Auto-saved"

**Implementation**:
```javascript
setInterval(() => {
  const content = editor.value;
  saveSnapshot(currentEntryId, content, true); // is_autosave=True
}, 30000);
```

### Web Authentication (Biometric)

**File**: `static/js/biometric-auth.js`

Provides mock implementation of WebAuthn for Face ID / Touch ID:
- **Challenge/Response**: Simulates credential registration
- **Fallback**: Falls back to password if biometric unavailable
- **Device support**: Works on iPhone, Mac, Android, Windows Hello

**Usage**: Biometric login option on `/login` page; falls back to password form.

---

## Common Development Tasks

### Add a New Route

1. **Define the route** in `app.py`:
   ```python
   @app.route('/path', methods=['GET', 'POST'])
   @login_required  # If user authentication required
   def route_handler():
       if request.method == 'POST':
           # Handle form submission
           pass
       return render_template('template.html')
   ```

2. **Create template** in `templates/` using Jinja2
3. **Link from navigation** in `base.html`
4. **Encrypt sensitive data** before storing

### Add a New Database Model

1. **Define class** in `app.py` (inherit from `db.Model`)
2. **Add columns** with appropriate types and constraints
3. **Define relationships** using `db.relationship()` and foreign keys
4. **Run migrations**: `python migrate_db.py` or recreate database
5. **Update routes** to interact with the new model

### Create a Character Matrix Feature

1. **Use existing Character model** (already in `app.py`)
2. **Create character_form.html** template with form fields
3. **Add routes**: `/characters`, `/character/new`, `/character/<id>/edit`, `/character/<id>/delete`
4. **Style with CSS variables** from `style.css`
5. **Use SVG icons** from `svg-icons.html` for visual consistency

### Add Frontend Validation

- **HTML5** built-in validation (required, minlength, pattern)
- **JavaScript** for real-time feedback before submission
- **Server-side** validation in Flask route (never trust client)

Example:
```html
<input type="text" name="character_name" required minlength="2" maxlength="100">
```

---

## Security Best Practices

### Passwords
- **Hash immediately** with `bcrypt.generate_password_hash(password, 10)` — never store plaintext
- **Verify during login**: `bcrypt.check_password_hash(stored_hash, submitted_password)`
- **Never log passwords** — sanitize error messages

### Encryption
- **Encrypt before database storage** — use Fernet cipher
- **Keep ENCRYPTION_KEY safe** — store in `.env` file (never commit to repo)
- **Decrypt only when needed** — don't cache plaintext in memory longer than necessary

### Routes
- **Protect with @login_required** — redirect unauthenticated users to login
- **Verify ownership** — don't let User A access User B's entries
  ```python
  entry = DiaryEntry.query.get_or_404(entry_id)
  if entry.user_id != current_user.id:
      abort(403)  # Forbidden
  ```

### CSRF & Forms
- **Use Flask-WTF** for forms (or include CSRF token manually)
- **Validate all input** — don't trust client-side validation alone

---

## File Organization Summary

### Backend Organization
- **Route handlers**: Grouped by feature (`/register`, `/characters`, `/entry/<id>/snapshot`)
- **Models**: Defined near top of `app.py` with relationships clearly marked
- **Utilities**: Security functions in `security.py`; helper functions in `app.py`

### Frontend Organization
- **CSS**: Global variables in `style.css`; v2.0 additions in `expansion.css`
- **JavaScript**: Entry point in `main.js`; feature-specific code in `enhanced-main.js`, `service-worker.js`, `biometric-auth.js`
- **Templates**: Base layout in `base.html`; feature-specific in `characters.html`, `snapshots.html`, etc.
- **Icons**: All 14 icons centralized in `svg-icons.html`; included via `<use xlink:href="#icon-name">`

---

## Testing & Debugging

### Manual Testing
1. Run `python3 app.py`
2. Open `http://127.0.0.1:5000` in browser
3. Register new account
4. Create entry with encrypted content
5. Check database (`instance/database.db`) with SQLite viewer to confirm encryption

### Debugging
- **Flask debug output**: Check terminal for errors
- **Browser console**: `F12` → Console tab for JavaScript errors
- **Service Worker**: DevTools → Application → Service Workers
- **Encryption issues**: Verify `ENCRYPTION_KEY` matches across encrypt/decrypt calls

### Database Inspection
```bash
sqlite3 instance/database.db
sqlite> .tables
sqlite> SELECT * FROM user;
sqlite> SELECT * FROM diary_entry LIMIT 1;
```

---

## Implementation Checklist

When starting work on a feature, verify:

- [ ] **Model**: Does the database model exist in `app.py`?
- [ ] **Routes**: Are all necessary endpoints defined with `@login_required` where needed?
- [ ] **Encryption**: Is sensitive data encrypted before storage?
- [ ] **Templates**: Does the Jinja2 template exist with proper form handling?
- [ ] **Styling**: Used CSS variables from `:root`?
- [ ] **Icons**: SVG icons used from `svg-icons.html` for consistency?
- [ ] **Frontend validation**: Both HTML5 and server-side checks?
- [ ] **Ownership verification**: Can't access other users' data?
- [ ] **Auto-save**: Does the editor auto-save if expected?
- [ ] **Offline support**: Service Worker cache updated if new files added?

---

## Related Documentation

- **[README.md](../../README.md)** — Project overview, features, architecture, security
- **[EXPANSION.md](../../EXPANSION.md)** — Detailed v2.0 feature guide (Character Matrix, Draft Versioning, Zen Mode, PWA)
- **[MIGRATION.md](../../MIGRATION.md)** — Upgrade path from v1 to v2 (backward compatible)
- **[requirements.txt](../../requirements.txt)** — Python dependencies

