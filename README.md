
<div align="center">
  <img src="static/IMG_MindVault_logo.png" alt="MindVault Logo" width="120" height="120" />
</div>

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
- [Developer Setup & Conventions](#developer-setup--conventions)
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

## Key Features

### 🔐 Security & Privacy
- **Zero-Knowledge Encryption**: Your entries are encrypted client-side using Fernet.
- **Local-First**: All data stored on your machine by default.
- **Open Source**: Audit the code yourself; no black boxes.
- **Biometric Auth**: Face ID / Touch ID / Windows Hello for quick secure access.

### ✍️ Creative Tools
- **Character Matrix**: Build rich character profiles with personality traits, backstories, and relationship maps.
- **Draft Versioning**: Save unlimited snapshots with version history; restore any version anytime.
- **Zen Mode**: Distraction-free focus writing with real-time word/character counter.
- **Auto-Save**: Draft protection every 30 seconds to localStorage.

### 📱 Mobile & Offline
- **Progressive Web App**: Install on phone, tablet, or desktop like a native app.
- **Offline Mode**: Full functionality without internet; automatic sync when connected.
- **App Shortcuts**: Quick access to "New Entry" and "Character Matrix" from home screen.
- **Background Sync**: Pending entries queue and sync automatically.

### 🎨 Beautiful & Intentional
- **Cyberpunk Aesthetic**: High-intensity, dark interface with cyan/violet/pink gradients.
- **Global Design System**: Consistent spacing, colors, and transitions across all features.
- **SVG Icon Library**: 14 custom icons that scale perfectly at any size.
- **Responsive Design**: Optimized for mobile, tablet, and desktop.

---

## What's New in v2.0

### 🎭 Author's Archive
**Character Matrix** - Professional character development for fiction writers. Create detailed character profiles including personality traits, backstory, physical description, motivations, and relationship dynamics. Organize characters with color-coded avatars and quick-access matrix layout.

**Draft Versioning** - Never lose your work again. Save unlimited snapshots of your entries with custom version numbers (e.g., "1.0", "1.1", "2.0"). Each snapshot is frozen in time with optional descriptions. Restore any previous version with one click.

### 🧘 Zen Mode
Pure writing focus. Hide all navigation and sidebars. Real-time word/character counter in the corner. Your preference persists—next time you write, Zen Mode returns automatically.

### 📲 Progressive Web App
- Install MindVault on any device like a native app.
- Works offline with automatic sync when connection returns.
- Push notifications for vault updates.
- App shortcuts for quick access.
- Service Worker caching for instant load times.

### 🔐 Biometric Authentication
- Face ID on iPhone/iPad.
- Touch ID on Mac.
- Windows Hello (iris/face/PIN).
- Android biometric scanner.
- No passwords needed for daily access.

### 🎨 Global Design System
- 20+ CSS variables for colors, spacing, transitions, and layout.
- Light variant color palette for the register page.
- Consistent typography system with font weights.
- Z-index layer system for proper stacking.
- Transition timing for predictable animations.

### 🖼️ SVG Icon Library
14 custom-coded SVG icons: Shield, Star, Matrix, Character, Version, Zen, Lock, Biometric, Download, Snapshot, Edit, Trash, Settings, Export, and Refresh. Sized from small (1rem) to extra-large (3.5rem) with customizable colors.

---

## How It Works

The application is built using **Flask** on the backend and modern browser APIs on the frontend. All data encryption happens before storage. Offline-first architecture means you own your data completely.

### Core Application Flow

1. **User Registration** - Sign up with username, email, and password (hashed with Bcrypt).
2. **Authentication** - Login with password OR biometric (Face ID/Touch ID).
3. **Create Entries** - Write in the editor; auto-save saves drafts every 30 seconds.
4. **Versioning** - Take snapshots at any point; each snapshot is encrypted and immutable.
5. **Organization** - Create character profiles for fiction projects; tag and categorize entries.
6. **Focus Writing** - Toggle Zen Mode for distraction-free writing with word counter.
7. **Offline Access** - Service Worker caches app; continue working without internet.
8. **Sync & Backup** - Pending entries queue up offline; sync automatically on reconnection.

### Data Model (v2.0)

- **User**: Account metadata, relationships to entries and characters.
- **DiaryEntry**: Encrypted content, title, category, timestamp, author reference.
- **EntrySnapshot**: Version number, frozen encrypted content, description, timestamp, auto-save flag.
- **Character**: Name, archetype, personality traits, backstory, relationships, motivations, physical description, avatar color.
- **Review**: Public testimonials shown on homepage.

### Encryption Model

- **Fernet Symmetric Encryption**: AES-128 in CBC mode with HMAC authentication.
- **Client-Side Encryption**: Content encrypted in memory before transmission.
- **Key Management**: Encryption key (production use: load from secure environment variable).
- **Zero-Knowledge**: Server never has plaintext access to entry content.
- **Snapshot Integrity**: Each version snapshot independently encrypted and authenticated.

### Service Worker & Offline

- **Network-First Strategy**: Try server first; fallback to cache on failure.
- **Cache Versioning**: Old caches automatically cleared on app update.
- **Background Sync**: Pending entries stored in IndexedDB; sync when online.
- **Offline Fallback**: `/offline.html` page shows connection status with auto-retry.

---

## Security & Privacy

MindVault is designed with security as the foundation, not an afterthought.

### Current Security Architecture

- **Password Hashing**: Bcrypt with salting (not reversible).
- **Entry Encryption**: Fernet (AES-128 + HMAC) before database storage.
- **Route Protection**: Flask-Login session management; `@login_required` for sensitive endpoints.
- **Biometric Authentication**: Web Authentication API (WebAuthn) using platform hardware.
- **Local Storage**: SQLite database stored on your system; no cloud sync by default.
- **Transport Security**: HTTPS recommended for production.
- **Service Worker Integrity**: Script controls cache and only allows whitelisted assets.

### What's Protected

- ✅ Journal entry content (encrypted)
- ✅ Character profiles and relationships (encrypted)
- ✅ Snapshot history (encrypted)
- ✅ User passwords (hashed)
- ✅ Offline draft storage (IndexedDB)
- ✅ Auto-save revisions (localStorage)

### Important Notes for Production

- Store encryption key in environment variable (`.env`), not in code.
- Use HTTPS for all production deployments.
- Add database backups to your security checklist.
- Consider database encryption at rest (depending on hosting environment).
- Keep Flask debug mode disabled in production.
- Regularly update dependencies for security patches.

### Data Ownership

- **You own all your data** - stored locally on your device.
- **No analytics tracking** - we don't know who you are or what you write.
- **No AI training** - your entries are not used to train LLMs or any models.
- **No advertising** - MindVault is not monetized through your data.
- **Open source** - audit the code yourself; no hidden functionality.
- **Portable data** - export and take your vault elsewhere anytime.

---

## Project Architecture

```text
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
 * **Python 3.11+** (or 3.10 with compatibility adjustments)
 * **pip** package manager
 * **Optional**: virtualenv or venv for environment isolation
### Installation
```bash
# Clone the repository
git clone [https://github.com/sinhaayush61426-ai/mindvault.git](https://github.com/sinhaayush61426-ai/mindvault.git)
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
```text
[http://127.0.0.1:5000](http://127.0.0.1:5000)

```
### First-Time Setup
 1. **Register** - Go to /register and create an account.
 2. **Set Biometric** (Optional) - Click "🔐 Biometric Setup" if your device supports it.
 3. **Login** - Use password or biometric to login.
 4. **Dashboard** - Start writing entries, create characters, explore features.
 5. **Install PWA** (Optional) - See PWA Installation below.
### Environment Variables
Create a .env file in the project root (optional for development):
```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///mindvault.db
DEBUG=False
FLASK_ENV=production

```
For production, use a strong SECRET_KEY and secure DATABASE_URL.
## Usage Guide
### 📝 Writing Entries
 1. Go to **Dashboard** (main vault interface).
 2. Enter a **title** and select a **category**:
   * General
   * Novella/Fiction
   * Science Research
 3. Write freely in the editor.
 4. **Auto-save** saves your draft every 30 seconds (look for "✓ Draft saved" indicator).
 5. Click **"Seal Entry"** to encrypt and permanently save.
### 🎭 Character Matrix
 1. Click **"Characters"** in navigation.
 2. Click **"+ Create Character"** to add a character:
   * **Name**: Character identifier
   * **Archetype**: Protagonist, Antagonist, Mentor, Support, or Other
   * **Personality Traits**: Key qualities (e.g., "mysterious, strategic, loyal")
   * **Backstory**: Origin and history
   * **Physical Description**: Appearance and distinctive features
   * **Motivations**: What drives the character
   * **Relationships**: Connections to other characters
   * **Avatar Color**: Visual identifier (hex color code)
 3. View all characters in the matrix grid.
 4. Click character cards to view details.
 5. Use **Edit** to modify or **Delete** to remove.
### 📸 Draft Versioning (Snapshots)
 1. Open any entry (click from dashboard).
 2. Make changes to the content.
 3. Scroll to **"Save as New Version"** section.
 4. Enter version number (e.g., "1.1", "2.0").
 5. Optionally add a description (e.g., "Fixed chapter 3").
 6. Click **"📸 Create Snapshot"**.
 7. Click **"📸 Versions"** button to see full timeline.
 8. View all snapshots in chronological order.
 9. Click **"↩️ Restore This Version"** to reload any past version.
### 🧘 Zen Mode (Focus Writing)
 1. Click **"🧘 Zen Mode"** button (on dashboard or entry view).
 2. Navigation and sidebars fade away.
 3. **Word/Character Counter** appears in bottom-right.
 4. Write uninterrupted—counter updates in real-time.
 5. Click **"Exit Zen"** button (top-right) to return to normal view.
 6. Your Zen preference persists—next session returns to Zen if saved in Zen.
### 💾 Auto-Save & Draft Recovery
 * Auto-save triggers every 30 seconds while editing.
 * Drafts are stored locally in browser storage.
 * **"✓ Draft saved"** indicator appears briefly after each save.
 * If you accidentally close the page, draft is recovered on return.
 * Click **"Seal Entry"** to encrypt and save permanently.
### 🌐 Offline Access
 1. Open MindVault and use normally.
 2. Service Worker automatically caches all pages and assets.
 3. **Disconnect from internet**—MindVault continues working.
 4. Create new entries; they queue in IndexedDB.
 5. **Reconnect to internet**—pending entries sync automatically.
 6. Offline indicator shows connection status; auto-retries every 3 seconds.
## PWA Installation
MindVault works as a **Progressive Web App** (PWA), meaning you can install it on any device like a native app.
### Desktop Installation (Chrome, Edge, Safari)
 1. Open MindVault in your browser: http://127.0.0.1:5000
 2. Look for the **"Install"** button in your browser's address bar (or menu).
 3. Click **"Install"** and confirm.
 4. MindVault now appears on your desktop like a native application.
 5. Launch it anytime from your app drawer or desktop shortcut.
### Mobile Installation (iOS & Android)
**iPhone/iPad (iOS 16.4+):**
 1. Open MindVault in Safari.
 2. Tap the **Share** button (square with arrow).
 3. Scroll down and tap **"Add to Home Screen"**.
 4. Customize the name if desired.
 5. Tap **"Add"**.
 6. MindVault now appears as an icon on your home screen.
**Android:**
 1. Open MindVault in Chrome or Firefox.
 2. Tap the **menu** button (⋮) in top-right.
 3. Tap **"Install app"** or **"Add to Home screen"**.
 4. Confirm and tap **"Install"**.
 5. MindVault now appears on your home screen.
### PWA Features
Once installed, MindVault works like a native app:
 * ✅ Offline access to all cached pages and entries
 * ✅ Automatic background sync when reconnected
 * ✅ App shortcuts for "New Entry" and "Character Matrix"
 * ✅ No address bar or browser chrome—full-screen experience
 * ✅ App icon pinned to home screen or dock
 * ✅ Push notifications for vault updates (future)
 * ✅ Service Worker caching for instant load times
## Developer Setup & Conventions
Before working on MindVault, review the **Workspace Instructions** for comprehensive development guidelines covering:
 * Flask architecture and route patterns.
 * Database model structure and relationships.
 * Encryption patterns and security best practices.
 * Frontend CSS variables and styling system.
 * PWA/Service Worker implementation.
 * Common development tasks and checklists.
### Quick Developer Setup
 1. **Clone and install** (see Getting Started).
 2. **Start development server**:
   ```bash
   python3 app.py
   
   ```
 3. **Open browser**: http://127.0.0.1:5000
 4. **Check browser console** (F12) for any JavaScript errors.
 5. **Verify encryption** by checking database with SQLite viewer.
### Key Development Resources
| Resource | Purpose |
|---|---|
| Workspace Instructions | AI-friendly development guide with architecture, patterns, and checklists |
| EXPANSION.md | Detailed v2.0 feature documentation (500+ lines) |
| MIGRATION.md | Upgrade guide for v1 → v2 (backward compatible) |
| requirements.txt | Python dependencies and versions |
| manifest.json | PWA configuration and metadata |
### Understanding the Codebase
**Backend (app.py):**
 * User model: Account with bcrypt-hashed passwords.
 * DiaryEntry model: Encrypted content with categories and timestamps.
 * EntrySnapshot model: Versioned content snapshots (immutable).
 * Character model: Character profiles for fiction projects.
 * Review model: Public testimonials for homepage.
 * 25+ Flask routes organized by feature (auth, entries, characters, snapshots).
**Security (security.py):**
 * generate_key(): Creates Fernet encryption keys.
 * VaultSecurity class: Encryption/decryption helpers.
**Frontend CSS:**
 * static/css/style.css: Main styles with 20+ CSS variables (colors, spacing, typography, z-index).
 * static/css/expansion.css: v2.0 features (Zen Mode, Character Matrix, Snapshots, Timeline UI).
**Frontend JavaScript:**
 * static/js/service-worker.js: PWA offline support, caching strategy, background sync.
 * static/js/biometric-auth.js: WebAuthn implementation for Face ID/Touch ID.
 * static/js/enhanced-main.js: Zen Mode toggle, auto-save manager, SW registration, app initialization.
 * static/js/main.js: Legacy feature support.
**PWA & Offline:**
 * manifest.json: App metadata, icons, shortcuts, theme colors.
 * static/js/service-worker.js: Network-first caching with IndexedDB for pending entries.
 * templates/offline.html: Fallback page shown when offline.
### Database & Encryption
**Key patterns:**
 * **Never store plaintext** — always encrypt content with Fernet before saving to database.
 * **Encryption key** — store securely in .env (production) or generate in app.py (development).
 * **Ownership verification** — check entry.user_id == current_user.id before allowing access.
 * **Snapshots are immutable** — each version is a frozen copy; restore creates a new entry.
### Common Tasks
**Add a new route:**
```python
@app.route('/new-path', methods=['GET', 'POST'])
@login_required  # Add if user auth required
def new_route():
    if request.method == 'POST':
        # Encrypt sensitive data before saving
        encrypted_content = cipher.encrypt(data.encode())
        # Save to database...
    return render_template('new_template.html')

```
**Encrypt content before saving:**
```python
cipher = Fernet(ENCRYPTION_KEY)
encrypted = cipher.encrypt(content.encode())
db.session.add(DiaryEntry(encrypted_content=encrypted, user_id=current_user.id))
db.session.commit()

```
**Verify user ownership:**
```python
entry = DiaryEntry.query.get_or_404(entry_id)
if entry.user_id != current_user.id:
    abort(403)  # Forbidden

```
**Add CSS styles:**
 * Use global variables: background-color: var(--primary-color);
 * Define new variables in :root block of style.css.
 * Keep consistent with existing color palette.
### Testing
```bash
# Manual testing
python3 app.py
# Register account, create entry, check encryption in database

# Check Python syntax
python -m py_compile app.py

# Inspect database
sqlite3 instance/database.db
sqlite> SELECT * FROM user;
sqlite> SELECT * FROM diary_entry LIMIT 1;

```
## Future Roadmap
The project is intended to grow into a more complete journaling and emotional wellness workspace.
### In Progress / v2.1+
 * ✨ Full-text search and tagging system for better entry organization.
 * 📊 Local sentiment analysis and emotion trend visualizations (on-device, no tracking).
 * 🔐 Time-locked "Letters to the Future" with release dates.
 * 📤 Secure export/import of encrypted journal archives.
 * 🔑 Advanced authentication with 2FA and recovery keys.
 * 🔔 Push notifications for vault updates.
 * 🎯 Mood labels, daily prompts, and habit tracking.
### Long-term Vision
MindVault is more than a diary: it is a personal vault for self-reflection, emotional awareness, and safe record-keeping. Over time, the app should help users see patterns, recall meaningful moments, and cultivate lasting emotional habits without sacrificing privacy.
**Core principles for all future features:**
 * Zero cloud sync—data stays on your device.
 * No analytics or tracking—ever.
 * Privacy-first architecture.
 * Backward compatibility maintained.
## Contributing
Contributions are welcome to MindVault. If you want to help strengthen the project, please:
 1. **Review the guidelines** - Read Workspace Instructions for development conventions.
 2. **Open an issue** - Describe the bug or feature before starting work.
 3. **Submit a pull request** - Include clear commits and reference the issue.
 4. **Maintain security** - Always encrypt sensitive data; never store plaintext.
### Suggested Contribution Areas
**Development tasks:**
 * Add full-text search with encrypted index.
 * Implement local NLP sentiment scoring.
 * Build emotion trend visualizations and heatmaps.
 * Create time-locked letters with release scheduling.
 * Develop secure export/import with encrypted archives.
 * Add advanced authentication (2FA, recovery keys).
**Testing & QA:**
 * Write unit tests for encryption, authentication, and routes.
 * Test PWA functionality on different devices and browsers.
 * Verify offline sync works correctly.
 * Test across different screen sizes.
**Documentation:**
 * Expand https://www.google.com/search?q=EXPANSION.md with use cases.
 * Add troubleshooting guides.
 * Create video tutorials.
 * Document API endpoints formally.
**Design & UX:**
 * Design 2FA flow or recovery key UI.
 * Improve character matrix UX.
 * Build emotion trend dashboard mockups.
 * Design time-locked letter calendar view.
### Code Standards
 * **Follow conventions** in Workspace Instructions.
 * **Encrypt all sensitive data** before storage—no exceptions.
 * **Use Python 3.11+** and modern JavaScript (no IE support needed).
 * **Test manually** before submitting PR.
 * **Keep pull requests focused** on one feature or fix.
 * **Write clear commit messages** describing the change.
## License
This project is open source and available for learning, experimentation, and personal use. Feel free to fork, modify, and adapt MindVault to your secure journaling needs.
```

```
