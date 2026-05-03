
<div align="center">
  <img src="static/IMG_MindVault_logo.png" alt="MindVault Logo" width="100" height="100" />
</div>

# MindVault v2.0

> A privacy-first creative workspace for writers, researchers, and creators.

**MindVault** is a secure, offline-first writing vault with encrypted storage, character development tools, draft versioning, and distraction-free focus mode. All your data stays on your device—zero tracking, zero cloud sync, complete control.

## Table of Contents

- [Vision](#vision)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Usage Guide](#usage-guide)
- [PWA Installation](#pwa-installation)
- [Security & Privacy](#security--privacy)
- [Project Architecture](#project-architecture)
- [Developer Guide](#developer-guide)
- [Future Roadmap](#future-roadmap)
- [Contributing](#contributing)
- [License](#license)

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

---

## Features

### 🔐 Security & Privacy First
- **Zero-Knowledge Encryption**: Entries encrypted client-side using Fernet (AES-128 + HMAC)
- **Local-First**: All data stored on your machine by default; no cloud sync
- **Open Source**: Audit the code yourself; transparency is built-in
- **Biometric Auth**: Face ID, Touch ID, Windows Hello, and Android biometric support

### ✍️ Professional Writing Tools
- **Character Matrix**: Develop rich character profiles with personality traits, backstories, relationships, motivations, and color-coded avatars
- **Draft Versioning**: Save unlimited snapshots with custom version numbers (e.g., "1.0", "1.1", "2.0"). Restore any version instantly
- **Zen Mode**: Distraction-free focus writing with real-time word/character counter. Preference persists across sessions
- **Auto-Save**: Draft protection every 30 seconds to prevent accidental loss

### 📱 Mobile & Offline-First
- **Progressive Web App**: Install on phone, tablet, or desktop like a native app
- **Offline Mode**: Full functionality without internet; automatic sync when reconnected
- **Background Sync**: Pending entries queue and sync automatically when connection returns
- **App Shortcuts**: Quick access to "New Entry" and "Character Matrix" from home screen

### 🎨 Design & UX
- **Cyberpunk Aesthetic**: High-intensity dark interface with cyan/violet/pink gradients
- **Global Design System**: 20+ CSS variables for consistent colors, spacing, typography, and transitions
- **SVG Icon Library**: 14 custom-coded icons (Shield, Matrix, Character, Version, Zen, Lock, etc.) that scale at any size
- **Responsive Design**: Optimized for mobile, tablet, and desktop

## Tech Stack

| Layer | Technology | Details |
|-------|-----------|---------|
| **Backend** | Flask, SQLAlchemy ORM | 25+ routes, session management, user auth |
| **Database** | SQLite3 | Local file-based, encrypted at rest |
| **Encryption** | Fernet (cryptography) | AES-128-CBC with HMAC authentication |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript | Service Worker, Web Authentication API |
| **Authentication** | Bcrypt + WebAuthn | Password hashing + biometric support |
| **PWA** | Service Worker + Web Manifest | Offline caching, app shortcuts, installation |

---

## Security & Privacy

MindVault is designed with security as the foundation, not an afterthought.

### Current Security Architecture

- **Password Hashing**: Bcrypt with salting (not reversible)
- **Entry Encryption**: Fernet (AES-128 + HMAC) before database storage
- **Route Protection**: Flask-Login session management with `@login_required` for sensitive endpoints
- **Biometric Authentication**: Web Authentication API (WebAuthn) using platform hardware
- **Local Storage**: SQLite database stored on your system; no cloud sync by default
- **Transport Security**: HTTPS recommended for production
- **Service Worker Integrity**: Script controls cache and only allows whitelisted assets

### What's Protected

- ✅ Journal entry content (encrypted)
- ✅ Character profiles and relationships (encrypted)
- ✅ Snapshot history (encrypted)
- ✅ User passwords (hashed)
- ✅ Offline draft storage (IndexedDB)
- ✅ Auto-save revisions (localStorage)

### Important Notes for Production

- Store encryption key in environment variable (`.env`), not in code
- Use HTTPS for all production deployments
- Add database backups to your security checklist
- Consider database encryption at rest (depending on hosting environment)
- Keep Flask debug mode disabled in production
- Regularly update dependencies for security patches

### Data Ownership

- **You own all your data** — stored locally on your device
- **No analytics tracking** — we don't know who you are or what you write
- **No AI training** — your entries are not used to train LLMs or any models
- **No advertising** — MindVault is not monetized through your data
- **Open source** — audit the code yourself; no hidden functionality
- **Portable data** — export and take your vault elsewhere anytime

---

## Project Architecture

```text
mindvault/
├── app.py                           # Flask + SQLAlchemy models + 25+ routes
├── security.py                      # Fernet encryption utilities
├── manifest.json                    # PWA metadata & configuration
├── templates/                       # Jinja2 HTML templates
│   ├── base.html, index.html, login.html, register.html
│   ├── dashboard.html, entry.html, characters.html
│   ├── snapshots.html, character_form.html, offline.html
│   └── ...
├── static/
│   ├── css/
│   │   ├── style.css               # Main styles + 20+ CSS variables
│   │   └── expansion.css           # v2.0 features (Zen, Matrix, Snapshots)
│   ├── js/
│   │   ├── service-worker.js       # PWA offline + caching
│   │   ├── enhanced-main.js        # Zen Mode + auto-save
│   │   ├── biometric-auth.js       # WebAuthn (Face ID/Touch ID)
│   │   └── main.js                 # General features
│   └── svg-icons.html              # 14 custom icons
└── instance/database.db            # SQLite (local storage)
├── EXPANSION.md                        # v2.0 feature documentation
├── MIGRATION.md                        # Upgrade guide for v1 → v2
│
├── templates/
│   ├── base.html                      # Base template (PWA + new scripts)
│   ├── index.html                     # Homepage
│   ├── login.html                     # Login form (with biometric option)
│   ├── register.html                  # Registration (with biometric setup)
│   ├── dashboard.html                 # Main vault interface
│   ├── characters.html                # Character matrix grid
│   ├── character_form.html            # Create/edit character
│   ├── snapshots.html                 # Version history timeline
│   ├── view_entry.html                # Entry detail + snapshot creation
│   ├── offline.html                   # Offline fallback
│   └── submit_review.html             # Community review form
│
├── static/
│   ├── css/
│   │   ├── style.css                  # Main styles (with global variables)
│   │   └── expansion.css              # v2.0: Zen Mode, Character, Snapshots
│   ├── js/
│   │   ├── service-worker.js          # PWA offline + caching
│   │   ├── biometric-auth.js          # Web Authentication API
│   │   ├── enhanced-main.js           # Zen Mode + auto-save + init
│   │   └── main.js                    # (legacy - for existing features)
│   ├── svg-icons.html                 # SVG icon library (14 icons)
│   └── images/                        # App icons for PWA
│
└── instance/
    └── mindvault.db                   # SQLite database (gitignored)

```
### Key Files & Responsibilities
**Backend:**
 * app.py - Flask app, 25+ routes including character/snapshot management.
 * security.py - Fernet encryption helpers.
**Frontend - Styling:**
 * style.css - Main styles with 20+ CSS variables (colors, spacing, transitions, fonts, z-index).
 * expansion.css - v2.0 features (Zen Mode, Character Matrix, Snapshots, Timeline UI).
**Frontend - JavaScript:**
 * service-worker.js - PWA offline support, caching strategy, background sync.
 * biometric-auth.js - WebAuthn implementation for Face ID/Touch ID.
 * enhanced-main.js - Zen Mode toggle, auto-save manager, SW registration, app initialization.
 * main.js - (legacy features).
**Frontend - UI:**
 * svg-icons.html - Reusable SVG icon components with size/color variants.
 * base.html - Base template with PWA manifest, flash messages, CSS/JS loading.
**PWA Configuration:**
 * manifest.json - App metadata, icons, shortcuts, theme colors, share target API.
 * Service Worker enables offline mode and installation.
**Documentation:**
 * README.md - This file.
 * EXPANSION.md - Detailed v2.0 feature guide (500+ lines).
 * MIGRATION.md - Upgrade path from v1 to v2 (fully backward compatible).
## Getting Started
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
