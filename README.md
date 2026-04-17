# MindVault v2.0

**MindVault** is a privacy-first, high-intensity creative workspace designed for secure reflections, professional research, and fiction writing projects. Built for writers, researchers, and creatives who demand both security and flexibility.

MindVault provides encrypted storage, version control for your work, an immersive focus mode, and works offline as a progressive web app. All your data is yours—stored locally with zero-knowledge encryption.

**✨ New in v2.0**: Character Matrix, Draft Versioning, Zen Mode, Progressive Web App, Biometric Auth, Global CSS Variables.

## Table of Contents

- [Vision](#vision)
- [Key Features](#key-features)
- [What's New in v2.0](#whats-new-in-v20)
- [How It Works](#how-it-works)
- [Security & Privacy](#security--privacy)
- [Project Architecture](#project-architecture)
- [Getting Started](#getting-started)
- [Usage Guide](#usage-guide)
- [PWA Installation](#pwa-installation)
- [Developer Guide](#developer-guide)
- [Future Roadmap](#future-roadmap)
- [Contributing](#contributing)
- [License](#license)

## Vision

MindVault is your **personal sanctuary for creation and reflection**. We believe that writers, researchers, and creative professionals deserve:

- A **secure vault** that never syncs to the cloud
- **Complete creative control** over character development, drafts, and iterations
- A **focus-first environment** that eliminates distractions
- **Offline-first access** that works anywhere, anytime
- **Zero tracking**—no analytics, no third-party services, no compromise

Whether you're journaling, writing a novel, researching, or developing complex characters, MindVault keeps your work private, organized, and always within reach.

## Key Features

### 🔐 Security & Privacy
- **Zero-Knowledge Encryption**: Your entries are encrypted client-side using Fernet
- **Local-First**: All data stored on your machine by default
- **Open Source**: Audit the code yourself; no black boxes
- **Biometric Auth**: Face ID / Touch ID / Windows Hello for quick secure access

### ✍️ Creative Tools
- **Character Matrix**: Build rich character profiles with personality traits, backstories, and relationship maps
- **Draft Versioning**: Save unlimited snapshots with version history; restore any version anytime
- **Zen Mode**: Distraction-free focus writing with real-time word/character counter
- **Auto-Save**: Draft protection every 30 seconds to localStorage

### 📱 Mobile & Offline
- **Progressive Web App**: Install on phone, tablet, or desktop like a native app
- **Offline Mode**: Full functionality without internet; automatic sync when connected
- **App Shortcuts**: Quick access to "New Entry" and "Character Matrix" from home screen
- **Background Sync**: Pending entries queue and sync automatically

### 🎨 Beautiful & Intentional
- **Cyberpunk Aesthetic**: High-intensity, dark interface with cyan/violet/pink gradients
- **Global Design System**: Consistent spacing, colors, and transitions across all features
- **SVG Icon Library**: 14 custom icons that scale perfectly at any size
- **Responsive Design**: Optimized for mobile, tablet, and desktop

## What's New in v2.0

### 🎭 Author's Archive
**Character Matrix** - Professional character development for fiction writers. Create detailed character profiles including personality traits, backstory, physical description, motivations, and relationship dynamics. Organize characters with color-coded avatars and quick-access matrix layout.

**Draft Versioning** - Never lose your work again. Save unlimited snapshots of your entries with custom version numbers (e.g., "1.0", "1.1", "2.0"). Each snapshot is frozen in time with optional descriptions. Restore any previous version with one click.

### 🧘 Zen Mode
Pure writing focus. Hide all navigation and sidebars. Real-time word/character counter in the corner. Your preference persists—next time you write, Zen Mode returns automatically.

### 📲 Progressive Web App
- Install MindVault on any device like a native app
- Works offline with automatic sync when connection returns
- Push notifications for vault updates
- App shortcuts for quick access
- Service Worker caching for instant load times

### 🔐 Biometric Authentication
- Face ID on iPhone/iPad
- Touch ID on Mac
- Windows Hello (iris/face/PIN)
- Android biometric scanner
- No passwords needed for daily access

### 🎨 Global Design System
- 20+ CSS variables for colors, spacing, transitions, and layout
- Light variant color palette for the register page
- Consistent typography system with font weights
- Z-index layer system for proper stacking
- Transition timing for predictable animations

### 🖼️ SVG Icon Library
14 custom-coded SVG icons: Shield, Star, Matrix, Character, Version, Zen, Lock, Biometric, Download, Snapshot, Edit, Trash, Settings, Export, and Refresh. Sized from small (1rem) to extra-large (3.5rem) with customizable colors.

## How It Works

The application is built using **Flask** on the backend and modern browser APIs on the frontend. All data encryption happens before storage. Offline-first architecture means you own your data completely.

### Core Application Flow

1. **User Registration** - Sign up with username, email, and password (hashed with Bcrypt)
2. **Authentication** - Login with password OR biometric (Face ID/Touch ID)
3. **Create Entries** - Write in the editor; auto-save saves drafts every 30 seconds
4. **Versioning** - Take snapshots at any point; each snapshot is encrypted and immutable
5. **Organization** - Create character profiles for fiction projects; tag and categorize entries
6. **Focus Writing** - Toggle Zen Mode for distraction-free writing with word counter
7. **Offline Access** - Service Worker caches app; continue working without internet
8. **Sync & Backup** - Pending entries queue up offline; sync automatically on reconnection

### Data Model (v2.0)

- **User**: Account metadata, relationships to entries and characters
- **DiaryEntry**: Encrypted content, title, category, timestamp, author reference
- **EntrySnapshot**: Version number, frozen encrypted content, description, timestamp, auto-save flag
- **Character**: Name, archetype, personality traits, backstory, relationships, motivations, physical description, avatar color
- **Review**: Public testimonials shown on homepage

### Encryption Model

- **Fernet Symmetric Encryption**: AES-128 in CBC mode with HMAC authentication
- **Client-Side Encryption**: Content encrypted in memory before transmission
- **Key Management**: Encryption key (production use: load from secure environment variable)
- **Zero-Knowledge**: Server never has plaintext access to entry content
- **Snapshot Integrity**: Each version snapshot independently encrypted and authenticated

### Service Worker & Offline

- **Network-First Strategy**: Try server first; fallback to cache on failure
- **Cache Versioning**: Old caches automatically cleared on app update
- **Background Sync**: Pending entries stored in IndexedDB; sync when online
- **Offline Fallback**: `/offline.html` page shows connection status with auto-retry

## Security & Privacy

MindVault is designed with security as the foundation, not an afterthought.

### Current Security Architecture

- **Password Hashing**: Bcrypt with salting (not reversible)
- **Entry Encryption**: Fernet (AES-128 + HMAC) before database storage
- **Route Protection**: Flask-Login session management; @login_required for sensitive endpoints
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

- **You own all your data** - stored locally on your device
- **No analytics tracking** - we don't know who you are or what you write
- **No AI training** - your entries are not used to train LLMs or any models
- **No advertising** - MindVault is not monetized through your data
- **Open source** - audit the code yourself; no hidden functionality
- **Portable data** - export and take your vault elsewhere anytime

## Project Architecture

```
mindvault/
├── app.py                              # Flask app + SQLAlchemy models + routes
├── security.py                         # Encryption utilities
├── requirements.txt                    # Python dependencies
├── manifest.json                       # PWA configuration
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
- `app.py` - Flask app, 25+ routes including character/snapshot management
- `security.py` - Fernet encryption helpers

**Frontend - Styling:**
- `style.css` - Main styles with 20+ CSS variables (colors, spacing, transitions, fonts, z-index)
- `expansion.css` - v2.0 features (Zen Mode, Character Matrix, Snapshots, Timeline UI)

**Frontend - JavaScript:**
- `service-worker.js` - PWA offline support, caching strategy, background sync
- `biometric-auth.js` - WebAuthn implementation for Face ID/Touch ID
- `enhanced-main.js` - Zen Mode toggle, auto-save manager, SW registration, app initialization
- `main.js` - (legacy features)

**Frontend - UI:**
- `svg-icons.html` - Reusable SVG icon components with size/color variants
- `base.html` - Base template with PWA manifest, flash messages, CSS/JS loading

**PWA Configuration:**
- `manifest.json` - App metadata, icons, shortcuts, theme colors, share target API
- Service Worker enables offline mode and installation

**Documentation:**
- `README.md` - This file
- `EXPANSION.md` - Detailed v2.0 feature guide (500+ lines)
- `MIGRATION.md` - Upgrade path from v1 to v2 (fully backward compatible)

## Getting Started

### Prerequisites

- **Python 3.11+** (or 3.10 with compatibility adjustments)
- **pip** package manager
- **Optional**: `virtualenv` or `venv` for environment isolation

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

Open your browser to:

```
http://127.0.0.1:5000
```

### First-Time Setup

1. **Register** - Go to `/register` and create an account
2. **Set Biometric** (Optional) - Click "🔐 Biometric Setup" if your device supports it
3. **Login** - Use password or biometric to login
4. **Dashboard** - Start writing entries, create characters, explore features
5. **Install PWA** (Optional) - See [PWA Installation](#pwa-installation) below

### Environment Variables

Create a `.env` file in the project root (optional for development):

```
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///mindvault.db
DEBUG=False
FLASK_ENV=production
```

For production, use a strong `SECRET_KEY` and secure `DATABASE_URL`.

## Usage Guide

### 📝 Writing Entries

1. Go to **Dashboard** (main vault interface)
2. Enter a **title** and select a **category**:
   - General
   - Novella/Fiction
   - Science Research
3. Write freely in the editor
4. **Auto-save** saves your draft every 30 seconds (look for "✓ Draft saved" indicator)
5. Click **"Seal Entry"** to encrypt and permanently save

### 🎭 Character Matrix

1. Click **"Characters"** in navigation
2. Click **"+ Create Character"** to add a character:
   - **Name**: Character identifier
   - **Archetype**: Protagonist, Antagonist, Mentor, Support, or Other
   - **Personality Traits**: Key qualities (e.g., "mysterious, strategic, loyal")
   - **Backstory**: Origin and history
   - **Physical Description**: Appearance and distinctive features
   - **Motivations**: What drives the character
   - **Relationships**: Connections to other characters
   - **Avatar Color**: Visual identifier (hex color code)
3. View all characters in the matrix grid
4. Click character cards to view details
5. Use **Edit** to modify or **Delete** to remove

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
3. **Disconnect from internet**—MindVault continues working
4. Create new entries; they queue in IndexedDB
5. **Reconnect to internet**—pending entries sync automatically
6. Offline indicator shows connection status; auto-retries every 3 seconds

## Developer Notes

### Understanding `app.py`

- `@app.route('/register')` handles account creation.
- `@app.route('/login')` handles authentication.
- `@app.route('/dashboard')` displays the user's private entries.
- `@app.route('/save-entry')` encrypts and saves journal content.

### Understanding `security.py`

- `generate_key()` returns a new `Fernet` encryption key.
- `VaultSecurity` provides `encrypt_text` and `decrypt_text` helpers for string encryption.

### Local development tips

- Add `.env` support for secret configuration.
- Switch the runtime-generated key to a persistent secret in `.env`.
- Add a `.gitignore` file for sensitive files and local SQLite databases.

### Suggested improvements

- Add search, tags, and categories for richer journal organization.
- Add local analytics dashboards for emotional trends over time.
- Add support for time-locked entries that unlock on a future date.
- Add tests for authentication, encryption, and form handling.

## Future Roadmap

The project is intended to grow into a more complete journaling and emotional wellness workspace.

### Planned features

- Local sentiment analysis powered entirely on-device
- Emotion trend visualizations and heatmaps
- Time-locked "Letters to the Future" with release dates
- Secure export/import of encrypted journal archives
- Advanced authentication with 2FA and recovery keys
- Privacy-preserving reminder and habit features

### Long-term vision

MindVault is more than a diary: it is a personal vault for self-reflection, emotional awareness, and safe record-keeping. Over time, the app should help users see patterns, recall meaningful moments, and cultivate lasting emotional habits without sacrificing privacy.

## Contributing

Contributions are welcome. If you want to help make MindVault stronger, please:

- Open issues for bugs or new feature ideas
- Submit pull requests with clean, documented code
- Keep security and privacy at the center of every enhancement

### Good contribution ideas

- Add local NLP sentiment scoring
- Implement graph-based emotional dashboards
- Expand the entry model with tags, mood labels, and prompts
- Build time-locked letters and future notes
- Improve authentication, encryption, and key storage

## License

This project is open source and available for learning, experimentation, and personal use. Feel free to fork, modify, and adapt MindVault to your secure journaling needs.
