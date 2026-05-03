<div align="center">
  <img src="static/IMG_MindVault_logo.png" alt="MindVault Logo" width="120" height="120" />
</div>

# MindVault v2.0

**MindVault** is a privacy-first, high-intensity creative workspace designed for secure reflections, professional research, and fiction writing projects. Built for writers, researchers, and creatives who demand both security and flexibility.

MindVault provides encrypted storage, version control for your work, an immersive focus mode, and works offline as a progressive web app. All your data is yours—stored locally with zero-knowledge encryption.

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

---

## Vision

MindVault is your **personal sanctuary for creation and reflection**. We believe that writers, researchers, and creative professionals deserve:

- A **secure vault** that never syncs to the cloud
- **Complete creative control** over character development, drafts, and iterations
- A **focus-first environment** that eliminates distractions
- **Offline-first access** that works anywhere, anytime
- **Zero tracking**—no analytics, no third-party services, no compromise

Whether you're journaling, writing a novel, researching, or developing complex characters, MindVault keeps your work private, organized, and always within reach.

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
├── app.py                              # Flask app + SQLAlchemy models + 25+ routes
├── security.py                         # Fernet encryption utilities
├── migrate_db.py                       # Database migration script
├── requirements.txt                    # Python dependencies
├── manifest.json                       # PWA manifest (icons, shortcuts, metadata)
│
├── templates/                          # Jinja2 templates
│   ├── base.html                      # Base layout with PWA metadata
│   ├── login.html, register.html      # Authentication pages
│   ├── dashboard.html                 # Main vault interface
│   ├── entry.html                     # Rich text editor for entries
│   ├── characters.html                # Character matrix grid
│   ├── character_form.html            # Create/edit character profile
│   ├── view_entry.html                # View entry with snapshots
│   ├── snapshots.html                 # Version history timeline
│   ├── offline.html                   # Offline fallback page
│   └── index.html, submit_review.html # Homepage and review form
│
├── static/
│   ├── css/
│   │   ├── style.css                  # Main styles (20+ CSS variables)
│   │   └── expansion.css              # v2.0 features (Zen, Matrix, Snapshots)
│   ├── js/
│   │   ├── service-worker.js          # PWA: offline support, caching
│   │   ├── biometric-auth.js          # WebAuthn (Face ID, Touch ID)
│   │   ├── enhanced-main.js           # Zen Mode, auto-save, app init
│   │   └── main.js                    # Legacy feature support
│   └── svg-icons.html                 # 14 reusable SVG icons
│
└── instance/
    └── database.db                    # SQLite database (local, gitignored)
```

### Database Models

- **User**: Account data with bcrypt-hashed passwords
- **DiaryEntry**: Encrypted content, title, category, timestamp, author reference
- **EntrySnapshot**: Versioned content (frozen, immutable, independently encrypted)
- **Character**: Character profiles with archetype, traits, backstory, relationships
- **Review**: Public testimonials displayed on homepage

### Encryption & Security

- **Fernet Symmetric Encryption**: AES-128-CBC with HMAC authentication
- **Client-Side Encryption**: Content encrypted in memory before transmission
- **Bcrypt Password Hashing**: Non-reversible, salted password storage
- **Route Protection**: `@login_required` for authenticated endpoints
- **Ownership Verification**: Users can only access their own entries
- **Snapshot Integrity**: Each version independently encrypted and authenticated

---

## Getting Started

### Prerequisites

- **Python 3.11+** (or 3.10 with compatibility adjustments)
- **pip** package manager
- **Optional**: virtualenv or venv for environment isolation

### Installation

```bash
# Clone the repository
git clone https://github.com/sinhaayush61426-ai/mindvault.git
cd mindvault

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run MindVault

```bash
python3 app.py
```

Open your browser to: `http://127.0.0.1:5000`

### First-Time Setup

1. **Register** — Go to `/register` and create an account
2. **Set Biometric** (Optional) — Click "🔐 Biometric Setup" if your device supports it
3. **Login** — Use password or biometric to login
4. **Dashboard** — Start writing entries, create characters, explore features
5. **Install PWA** (Optional) — See PWA Installation section below

### Environment Variables

Create a `.env` file in the project root (optional for development):

```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///mindvault.db
DEBUG=False
FLASK_ENV=production
```

For production, use a strong SECRET_KEY and secure DATABASE_URL.

---

## Usage Guide

### 📝 Writing Entries

1. Go to **Dashboard** (main vault interface)
2. Enter a **title** and select a **category**: General, Novella/Fiction, or Science Research
3. Write freely in the editor
4. **Auto-save** saves your draft every 30 seconds (look for "✓ Draft saved" indicator)
5. Click **"Seal Entry"** to encrypt and permanently save

### 🎭 Character Matrix

1. Click **"Characters"** in navigation
2. Click **"+ Create Character"** to add a character with:
   - **Name**: Character identifier
   - **Archetype**: Protagonist, Antagonist, Mentor, Support, or Other
   - **Personality Traits**: Key qualities (e.g., "mysterious, strategic, loyal")
   - **Backstory**: Origin and history
   - **Physical Description**: Appearance and distinctive features
   - **Motivations**: What drives the character
   - **Relationships**: Connections to other characters
   - **Avatar Color**: Visual identifier (hex color code)
3. View all characters in the matrix grid
4. Click character cards to view details; use **Edit** or **Delete** as needed

### 📸 Draft Versioning (Snapshots)

1. Open any entry (click from dashboard)
2. Make changes to the content
3. Scroll to **"Save as New Version"** section
4. Enter version number (e.g., "1.1", "2.0")
5. Optionally add a description (e.g., "Fixed chapter 3")
6. Click **"📸 Create Snapshot"**
7. Click **"📸 Versions"** button to see full timeline
8. View all snapshots in chronological order
9. Click **"↩️ Restore This Version"** to reload any past version

### 🧘 Zen Mode (Focus Writing)

1. Click **"🧘 Zen Mode"** button (on dashboard or entry view)
2. Navigation and sidebars fade away
3. **Word/Character Counter** appears in bottom-right
4. Write uninterrupted—counter updates in real-time
5. Click **"Exit Zen"** button (top-right) to return to normal view
6. Your Zen preference persists—next session returns to Zen if saved in Zen

### 💾 Auto-Save & Draft Recovery

- Auto-save triggers every 30 seconds while editing
- Drafts are stored locally in browser storage
- **"✓ Draft saved"** indicator appears briefly after each save
- If you accidentally close the page, draft is recovered on return
- Click **"Seal Entry"** to encrypt and save permanently

### 🌐 Offline Access

1. Open MindVault and use normally
2. Service Worker automatically caches all pages and assets
3. **Disconnect from internet** — MindVault continues working
4. Create new entries; they queue in IndexedDB
5. **Reconnect to internet** — pending entries sync automatically
6. Offline indicator shows connection status; auto-retries every 3 seconds

---

## PWA Installation

MindVault works as a **Progressive Web App** (PWA), meaning you can install it on any device like a native app.

### Desktop Installation (Chrome, Edge, Safari)

1. Open MindVault in your browser: `http://127.0.0.1:5000`
2. Look for the **"Install"** button in your browser's address bar (or menu)
3. Click **"Install"** and confirm
4. MindVault now appears on your desktop like a native application
5. Launch it anytime from your app drawer or desktop shortcut

### Mobile Installation (iOS & Android)

**iPhone/iPad (iOS 16.4+):**
1. Open MindVault in Safari
2. Tap the **Share** button (square with arrow)
3. Scroll down and tap **"Add to Home Screen"**
4. Customize the name if desired
5. Tap **"Add"**

**Android:**
1. Open MindVault in Chrome or Firefox
2. Tap the **menu** button (⋮) in top-right
3. Tap **"Install app"** or **"Add to Home screen"**
4. Confirm and tap **"Install"**

### PWA Features

Once installed, MindVault works like a native app:

- ✅ Offline access to all cached pages and entries
- ✅ Automatic background sync when reconnected
- ✅ App shortcuts for "New Entry" and "Character Matrix"
- ✅ Full-screen experience without address bar or browser chrome
- ✅ App icon pinned to home screen or dock
- ✅ Service Worker caching for instant load times

---

## Developer Guide

For comprehensive development guidelines, see [.github/copilot-instructions.md](.github/copilot-instructions.md) which covers:
- Flask architecture and 25+ route patterns
- Database model structure and relationships
- Encryption patterns and security best practices
- Frontend CSS variables and styling system
- PWA/Service Worker implementation
- Common development tasks and implementation checklists

### Quick Start for Developers

```bash
# Clone and install
git clone https://github.com/sinhaayush61426-ai/mindvault.git
cd mindvault

# Create environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run development server
python3 app.py
# Open http://127.0.0.1:5000
```

### Key Architecture

**Backend**: Flask + SQLAlchemy ORM
- User, DiaryEntry, EntrySnapshot, Character, Review models
- 25+ routes organized by feature (auth, entries, characters, snapshots, reviews)
- All sensitive data encrypted before storage

**Security**: Bcrypt + Fernet encryption
- Client-side encryption (AES-128 + HMAC)
- Route protection with `@login_required`
- Ownership verification on all user data

**Frontend**: Vanilla JavaScript, CSS Grid, Service Worker
- Zen Mode: distraction-free writing with word counter
- Auto-save: every 30 seconds to prevent data loss
- Service Worker: offline support and caching strategy
- Biometric auth: WebAuthn (Face ID, Touch ID, Windows Hello)

**PWA**: manifest.json + Service Worker
- Network-first caching strategy
- IndexedDB for offline entry queue
- Background sync on reconnection
- App shortcuts and installation support

### Development Resources

| File | Purpose |
|------|---------|
| [.github/copilot-instructions.md](.github/copilot-instructions.md) | Complete development handbook |
| [EXPANSION.md](EXPANSION.md) | Detailed v2.0 feature documentation |
| [MIGRATION.md](MIGRATION.md) | Upgrade path from v1 to v2 |
| [requirements.txt](requirements.txt) | Python dependencies and versions |
| [manifest.json](manifest.json) | PWA metadata and configuration |

### Key Patterns

**Never store plaintext** — always encrypt before database storage:
```python
cipher = Fernet(ENCRYPTION_KEY)
encrypted = cipher.encrypt(content.encode())
db.session.add(DiaryEntry(encrypted_content=encrypted, user_id=current_user.id))
```

**Verify user ownership** — before returning user data:
```python
entry = DiaryEntry.query.get_or_404(entry_id)
if entry.user_id != current_user.id:
    abort(403)
```

**Use CSS variables** — for consistent styling:
```css
background-color: var(--primary-color);
color: var(--text-primary);
border-radius: var(--border-radius);
```

### Testing

```bash
# Manual testing
python3 app.py
# Register account, create entry, verify encryption in database

# Inspect database
sqlite3 instance/database.db
sqlite> SELECT * FROM user;
sqlite> SELECT * FROM diary_entry LIMIT 1;
```

---

## Future Roadmap

The project is intended to grow into a more complete journaling and emotional wellness workspace.

### In Progress / v2.1+

- ✨ Full-text search and tagging system for better entry organization
- 📊 Local sentiment analysis and emotion trend visualizations (on-device, no tracking)
- 🔐 Time-locked "Letters to the Future" with release dates
- 📤 Secure export/import of encrypted journal archives
- 🔑 Advanced authentication with 2FA and recovery keys
- 🔔 Push notifications for vault updates
- 🎯 Mood labels, daily prompts, and habit tracking

### Long-term Vision

MindVault is more than a diary: it is a personal vault for self-reflection, emotional awareness, and safe record-keeping. Over time, the app should help users see patterns, recall meaningful moments, and cultivate lasting emotional habits without sacrificing privacy.

**Core principles for all future features:**
- Zero cloud sync—data stays on your device
- No analytics or tracking—ever
- Privacy-first architecture
- Backward compatibility maintained

---

## Contributing

Contributions are welcome to MindVault. If you want to help strengthen the project, please:

1. **Review the guidelines** — Read [.github/copilot-instructions.md](.github/copilot-instructions.md) for development conventions
2. **Open an issue** — Describe the bug or feature before starting work
3. **Submit a pull request** — Include clear commits and reference the issue
4. **Maintain security** — Always encrypt sensitive data; never store plaintext

### Suggested Contribution Areas

**Development tasks:**
- Add full-text search with encrypted index
- Implement local NLP sentiment scoring
- Build emotion trend visualizations and heatmaps
- Create time-locked letters with release scheduling
- Develop secure export/import with encrypted archives
- Add advanced authentication (2FA, recovery keys)

**Testing & QA:**
- Write unit tests for encryption, authentication, and routes
- Test PWA functionality on different devices and browsers
- Verify offline sync works correctly
- Test across different screen sizes

**Documentation:**
- Expand [EXPANSION.md](EXPANSION.md) with use cases
- Add troubleshooting guides
- Create video tutorials
- Document API endpoints formally

**Design & UX:**
- Design 2FA flow or recovery key UI
- Improve character matrix UX
- Build emotion trend dashboard mockups
- Design time-locked letter calendar view

### Code Standards

- **Follow conventions** in [.github/copilot-instructions.md](.github/copilot-instructions.md)
- **Encrypt all sensitive data** before storage—no exceptions
- **Use Python 3.11+** and modern JavaScript (no IE support needed)
- **Test manually** before submitting PR
- **Keep pull requests focused** on one feature or fix
- **Write clear commit messages** describing the change

---

## License

This project is open source and available for learning, experimentation, and personal use. Feel free to fork, modify, and adapt MindVault to your secure journaling needs.
