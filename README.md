
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

- **[EXPANSION.md](./EXPANSION.md)** — Detailed feature guide (Character Matrix, Snapshots, Zen Mode, PWA)
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
```
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
