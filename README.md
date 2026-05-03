
<div align="center">
  <img src="static/IMG_MindVault_logo.png" alt="MindVault Logo" width="100" height="100" />
</div>

# MindVault v2.0

> A privacy-first creative workspace for writers, researchers, and creators.

**MindVault** is a secure, offline-first writing vault with encrypted storage, character development tools, draft versioning, and distraction-free focus mode. All your data stays on your device—zero tracking, zero cloud sync, complete control.

## ✨ Key Highlights

🔐 **Zero-Knowledge Encryption** — Client-side AES-128 encryption; server never sees plaintext  
✍️ **Creative Workspace** — Character profiles, unlimited draft snapshots, auto-save every 30 seconds  
🧘 **Zen Mode** — Distraction-free writing with live word counter  
📲 **Progressive Web App** — Works offline, installs on any device, syncs automatically  
🔑 **Biometric Auth** — Face ID / Touch ID / Windows Hello (no passwords needed)  
🎨 **Beautiful & Fast** — Dark cyberpunk UI with global design system

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run development server
python3 app.py

# Open http://127.0.0.1:5000
```

## 📚 Documentation

- **[AUDIT_REPORT.md](./AUDIT_REPORT.md)** — Comprehensive audit report and testing results
- **[EXPANSION.md](./EXPANSION.md)** — Detailed v2.0 feature guide
- **[MIGRATION.md](./MIGRATION.md)** — Upgrade path from v1 to v2

## What's Included

### 🎭 Author's Archive
- **Character Matrix**: Build rich character profiles with personality traits, backstories, relationships
- **Draft Versioning**: Unlimited snapshots with custom version numbers and restoration

### 🛡️ Security
- **Password**: Bcrypt-hashed accounts
- **Entries**: AES-128 encrypted before storage
- **Sessions**: Flask-Login with `@login_required` protection
- **Offline**: IndexedDB + Service Worker for secure offline access

### 🎨 Design System
- 20+ CSS variables (colors, spacing, transitions)
- 14 custom SVG icons with multiple sizes
- Responsive across mobile, tablet, desktop
- Cyberpunk aesthetic with cyan/violet/pink gradients

## 📂 Project Structure

```
mindvault/
├── app.py                           # Flask app + SQLAlchemy models + 25+ routes
├── security.py                      # Fernet encryption utilities
├── manifest.json                    # PWA metadata & configuration
├── requirements.txt                 # Python dependencies
├── templates/                       # Jinja2 HTML templates
│   ├── base.html                    # Base layout with PWA support
│   ├── dashboard.html               # Main writing interface
│   ├── characters.html              # Character matrix grid
│   ├── view_entry.html              # Entry detail + snapshots
│   └── ...                          # Additional templates
├── static/
│   ├── css/
│   │   ├── style.css                # Main styles + CSS variables
│   │   └── expansion.css            # v2.0 features (Zen, Matrix, Snapshots)
│   ├── js/
│   │   ├── service-worker.js        # PWA offline support
│   │   ├── enhanced-main.js         # Zen Mode + auto-save
│   │   ├── biometric-auth.js        # WebAuthn authentication
│   │   └── main.js                  # General features
│   └── svg-icons.html               # 14 custom SVG icons
└── instance/database.db             # SQLite database (local storage)
```

### Key Components

**Backend (app.py):**
- User, DiaryEntry, EntrySnapshot, Character, Review models
- 25+ Flask routes for authentication, content management, and features
- SQLAlchemy ORM with relationship management

**Security (security.py):**
- Fernet encryption/decryption helpers
- AES-128 encryption for all sensitive content
- Key generation and management utilities

**Frontend:**
- **CSS**: Global design system with 20+ variables, responsive breakpoints
- **JavaScript**: PWA service worker, biometric auth, Zen mode, auto-save
- **Templates**: Jinja2 with consistent layout and component structure

## 🚀 Getting Started

### Prerequisites
- **Python 3.11+** (or 3.10 with compatibility adjustments)
- **pip** package manager
- **Optional**: virtualenv or venv for environment isolation

### Installation
```bash
# Clone repository
git clone https://github.com/sinhaayush61426-ai/mindvault.git
cd mindvault

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
python3 app.py
```

### First-Time Setup
1. **Register**: Create an account at `/register`
2. **Login**: Use password or biometric authentication
3. **Dashboard**: Start writing entries and creating characters
4. **PWA Install**: Optional - install as native app (see PWA section)

### Environment Variables
Create `.env` file for production:
```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///mindvault.db
DEBUG=False
FLASK_ENV=production
```

## 📖 Usage Guide

### Writing Entries
1. Navigate to **Dashboard**
2. Enter title and select category (General, Novella/Fiction, Research)
3. Write in the editor with auto-save every 30 seconds
4. Click **"Seal Entry"** to encrypt and save permanently

### Character Matrix
1. Click **"Characters"** in navigation
2. Create characters with name, archetype, personality traits, backstory, relationships
3. View all characters in grid layout
4. Edit or delete characters as needed

### Draft Versioning (Snapshots)
1. Open any entry from dashboard
2. Create snapshots with version numbers and descriptions
3. View version timeline and restore previous versions
4. All snapshots are encrypted and immutable

### Zen Mode
1. Click **"🧘 Zen Mode"** button
2. Navigation hides for distraction-free writing
3. Word/character counter appears in bottom-right
4. Exit with button or Escape key

### Offline Access
- Works completely offline with Service Worker caching
- New entries queue in IndexedDB
- Automatic sync when connection restored
- No data loss during offline periods

## 📱 PWA Installation

MindVault installs as a native app on any device.

### Desktop (Chrome, Edge, Safari)
1. Open http://127.0.0.1:5000 in browser
2. Click **"Install"** button in address bar
3. App appears in desktop app drawer

### Mobile (iOS/Android)
**iOS**: Safari → Share → "Add to Home Screen"  
**Android**: Chrome → Menu → "Install app"

### PWA Features
- ✅ Offline access to all cached content
- ✅ Automatic background sync
- ✅ App shortcuts for quick actions
- ✅ Native app experience (no browser chrome)
- ✅ Service Worker caching for instant loads

## 🛠️ Development

### Quick Setup
```bash
# Install and run
pip install -r requirements.txt
python3 app.py

# Verify setup
# - Open http://127.0.0.1:5000
# - Check browser console for errors
# - Test encryption in database
```

### Key Patterns

**Encryption** (always encrypt before saving):
```python
cipher = Fernet(ENCRYPTION_KEY)
encrypted = cipher.encrypt(content.encode())
db.session.add(DiaryEntry(encrypted_content=encrypted))
```

**User Verification** (check ownership):
```python
entry = DiaryEntry.query.get_or_404(entry_id)
if entry.user_id != current_user.id:
    abort(403)  # Forbidden
```

**CSS Variables** (use design system):
```css
background-color: var(--primary-color);
padding: var(--spacing-md);
```

### Testing
```bash
# Manual testing
python3 app.py
# Register → Create entry → Verify encryption

# Database inspection
sqlite3 instance/database.db
sqlite> SELECT * FROM diary_entry LIMIT 1;
```

## 🗺️ Roadmap

### v2.1+ Features
- Full-text search with encrypted indexing
- Local sentiment analysis and emotion trends
- Time-locked "Letters to the Future"
- Secure export/import of encrypted archives
- Advanced authentication (2FA, recovery keys)
- Push notifications for vault updates

### Vision
MindVault evolves into a complete emotional wellness workspace focused on self-reflection, pattern recognition, and secure record-keeping—always prioritizing privacy and local storage.

## 🤝 Contributing

Contributions welcome! Please:
1. Review Workspace Instructions for development guidelines
2. Open issues for bugs/features before starting work
3. Submit focused pull requests with clear commits
4. Maintain security: always encrypt sensitive data

### Areas for Contribution
- **Development**: Search, NLP analysis, export/import features
- **Testing**: Unit tests, PWA compatibility, responsive design
- **Documentation**: Tutorials, troubleshooting guides
- **Design**: UX improvements, new feature mockups

## 📄 License

Open source for learning, experimentation, and personal use. Fork, modify, and adapt MindVault to your secure journaling needs.
```

```
