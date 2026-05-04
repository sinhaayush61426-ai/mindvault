
<div align="center">
  <img src="static/IMG_MindVault_logo.png" alt="MindVault Logo" width="120" height="120" />
  
  # MindVault v2.0
  
  **A Privacy-First Creative Workspace for Writers, Researchers & Creators**
  
  Secure encrypted journal with character development tools, draft versioning, and distraction-free writing mode.  
  All data stays on your device—**zero tracking, zero cloud, complete control.**
</div>

---

> **MindVault is a philosophy**: *Your thoughts belong to you. Your vault is impenetrable. Your data is portable.*

---

## Status & Badges

| Badge | Details |
|-------|---------|
| ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg) | Open source under MIT license |
| ![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white) | Backend runtime |
| ![Flask](https://img.shields.io/badge/Flask-3.1.3-000000?logo=flask&logoColor=white) | Web framework with 25+ routes |
| ![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?logo=javascript&logoColor=black) | Frontend interactivity |
| ![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite&logoColor=white) | Local encrypted database |
| ![Fernet](https://img.shields.io/badge/Fernet-AES128--HMAC-4CAF50?logo=lock&logoColor=white) | Military-grade encryption |
| ![PWA](https://img.shields.io/badge/PWA-Native%20Install-5A67D8?logo=pwa&logoColor=white) | Service Worker + Web Manifest |
| ![Status](https://img.shields.io/badge/Status-Production%20Ready-27ae60?logo=checkmark) | v2.0 fully tested & audited |

---

## Quick Start

```bash
# Clone & install
git clone https://github.com/sinhaayush61426-ai/mindvault.git
cd mindvault && pip install -r requirements.txt

# Run development server
python3 app.py

# Open in browser
open http://127.0.0.1:5000
```

---

## Core Documentation

- **[EXPANSION.md](./EXPANSION.md)** — Complete v2.0 features guide (Character Matrix, Snapshots, Zen Mode, PWA)
- **[MIGRATION.md](./MIGRATION.md)** — Upgrade path from v1 to v2 (fully backward compatible)
- **[COMPREHENSIVE_AUDIT.md](./COMPREHENSIVE_AUDIT.md)** — Security audit, testing results, and deployment checklist
- **[.github/copilot-instructions.md](./.github/copilot-instructions.md)** — Developer workspace conventions

---

## Table of Contents

1. [Vision & Philosophy](#-vision--philosophy)
2. [Core Features](#-core-features)
3. [Release Highlights](#-v20-release-highlights)
4. [Tech Stack](#-complete-tech-stack)
5. [Getting Started](#-getting-started)
6. [Usage Guide](#-usage-guide)
7. [Security & Privacy](#-security--privacy-architecture)
8. [PWA Installation & Offline](#-pwa-installation)
9. [Project Architecture](#-project-architecture)
10. [Development Guide](#-development-guide)
11. [Testing & Quality](#-testing--quality-assurance)
12. [Roadmap & Vision](#-future-roadmap--vision)
13. [Contributing](#-contributing)
14. [License](#-license)

---

## Vision & Philosophy

MindVault is built on a simple principle: **Your thoughts are yours alone.**

In an age of surveillance capitalism and AI-driven data harvesting, we believe your creative work—journals, stories, characters, research—should never be monetized or analyzed without your explicit consent. 

**Core Philosophy:**
- **Zero-Knowledge**: Even we cannot read your encrypted entries
- **Local-First**: Data lives on your device by default; cloud is optional
- **Open Source**: Audit the code, fork it, adapt it to your needs
- **Anonymous**: No mandatory sign-in with Google/Microsoft; no analytics tracking
- **Portable**: Export your vault; take your writing anywhere
- **Progressive**: Works offline; syncs when reconnected; never loses data

---

## Core Features
### Encryption & Privacy
- **Zero-Knowledge Encryption**: Client-side Fernet encryption (AES-128-CBC + HMAC) before any database storage
- **Local-First Architecture**: All data stored on your machine by default; no mandatory cloud sync
- **Open Source**: Full source code available for security audits
- **Biometric Authentication**: Face ID, Touch ID, Windows Hello, Android biometrics without vendor lock-in
- **No Tracking**: No analytics, no cookies, no telemetry, no AI training on your data

### Professional Writing & Authorship Tools
- **Character Matrix**: Rich character profiles with personality traits, backstories, relationships, physical descriptions, motivations, and color-coded avatars for visual organization
- **Draft Versioning with Snapshots**: Unlimited version snapshots with semantic versioning (1.0, 1.1, 2.0). Restore any version instantly and keep full history
- **30-Second Auto-Save**: Automatic draft protection with explicit save control; never lose unsaved work due to crashes
- **Zen Mode**: Immersive distraction-free editor with hidden navigation and real-time word/character counter persistent across sessions
- **Rich Entry Organization**: Categorize entries (General, Fiction, Research) with timestamps and search compatibility

### Mobile & Offline-First
- **Progressive Web App**: Installable on iOS, Android, macOS, Windows, and Linux as a native app
- **Complete Offline Mode**: Full functionality without internet; automatic sync when connection returns
- **Background Sync Queue**: Pending entries stored in IndexedDB; syncs transparently when online
- **App Shortcuts**: Home screen shortcuts for "New Entry" and "Character Matrix" on mobile devices
- **Responsive Design**: Touch-optimized interface for tablets and phones

### User Experience & Design
- **Cyberpunk Aesthetic**: High-contrast dark interface with cyan/violet/pink color gradients for visual intensity
- **CSS Design System**: 20+ CSS variables (--primary-color, --spacing, --font-size) ensuring design consistency
- **14 Custom SVG Icons**: Scalable vector icons (Shield, Matrix, Character, Version, Zen, Lock, Star, Archive, etc.)
- **WCAG AA Accessibility**: Keyboard navigation, screen reader support, color contrast compliance
- **Smooth Animations**: Frictionless transitions using CSS transforms and GPU acceleration

---

## v2.0 Release Highlights

MindVault v2.0 introduces **enterprise-grade creative features** while maintaining 100% backward compatibility with v1 data:

| Feature | Impact | Status |
|---------|--------|--------|
| **Character Matrix** | Track character development with visual grid | [Complete] |
| **Draft Versioning** | Git-like snapshots for creative iterations | [Complete] |
| **Zen Mode** | Distraction-free writing with focus metrics | [Complete] |
| **Progressive Web App** | Install as native app on any device | [Complete] |
| **Auto-Save System** | 30-second draft protection | [Complete] |
| **Material Design Icons** | 14 custom SVG icons | [Complete] |
| **Offline Support** | Full functionality without internet | [Complete] |
| **Security Audit** | 9 critical loopholes fixed | [Complete] |
| **Dashboard Redesign** | Content-first, minimal UI | [Complete] |

### No Breaking Changes
- [YES] All v1 entries remain encrypted and accessible
- [YES] User accounts fully compatible
- [YES] Database automatically migrates on first run
- [YES] Existing biometric auth continues to work
- [YES] All v1 routes remain functional

---

## Complete Tech Stack

### Backend & Server
| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **Web Framework** | Flask | 3.1.3 | Lightweight Python web framework; 25+ routes |
| **ORM & Database Abstraction** | SQLAlchemy | Latest | Object-relational mapping for SQLite |
| **Server WSGI** | Werkzeug | 3.1.8 | WSGI application server (Flask dependency) |
| **User Session Management** | Flask-Login | (via Flask) | Authentication, session persistence |
| **Password Hashing** | Flask-Bcrypt | (via Bcrypt) | Secure password hashing with salt |
| **Database Driver** | SQLite3 | 3 | Lightweight, serverless SQL database |

### Encryption & Security
| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **Symmetric Encryption** | Fernet (cryptography) | Latest | AES-128-CBC with HMAC authentication |
| **Password Hashing** | Bcrypt | ~10 rounds | Industry-standard password security |
| **Web Authentication** | WebAuthn API | Browser native | Face ID, Touch ID, Windows Hello |
| **HTTPS Support** | ssl/tls | Standard | Transport layer security (production) |

### Frontend & Client
| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **Markup** | HTML5 | ES2020 | Semantic, accessible structure |
| **Styling** | CSS3 | Modern | CSS Grid, Flexbox, 20+ variables |
| **Scripting** | Vanilla JavaScript | ES6+ | Zero framework; 4 core scripts |
| **PWA Runtime** | Service Worker | W3C Standard | Offline caching, background sync |
| **Icons** | SVG | Scalable | 14 custom vectors, no external fonts |
| **Web Manifest** | PWA Manifest | W3C Standard | App metadata, installation config |
| **Template Engine** | Jinja2 | 3.1.6 | Server-side HTML rendering |

### Development & Documentation
| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **Package Management** | pip + requirements.txt | Standard | Reproducible dependency management |
| **Version Control** | Git | Standard | Commit history and collaboration |
| **Code Documentation** | Markdown | Standard | README, guides, API docs |
| **Testing Documentation** | COMPREHENSIVE_AUDIT.md | v2.0 | Complete quality assurance report |

### Database Models & Relationships
```python
User                    # Accounts with bcrypt password hash
├── DiaryEntry         # Encrypted journal entries
│   └── EntrySnapshot  # Versioned snapshots (auto-save + manual)
├── Character          # Character profiles for fiction
└── Review             # Community testimonials
```

---

## Getting Started

### System Requirements
- **Python**: 3.12+ (tested); 3.11 compatible; 3.10 with modifications
- **OS**: Linux, macOS, Windows (any modern OS with Python support)
- **Browser**: Chrome/Edge/Firefox/Safari (ES6+ JavaScript support)
- **Storage**: ~50MB for app + database (grows with entries)
- **RAM**: Minimal (~128MB during operation)

### Installation & Setup

**Step 1: Clone Repository**
```bash
git clone https://github.com/sinhaayush61426-ai/mindvault.git
cd mindvault
```

**Step 2: Create Virtual Environment (Recommended)**
```bash
python3 -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

**Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 4: Verify Installation**
```bash
python3 -c "from flask import Flask; from flask_sqlalchemy import SQLAlchemy; print('Dependencies OK')"
```

**Step 5: Run Application**
```bash
python3 app.py
```

**Step 6: Open in Browser**
```
http://127.0.0.1:5000
```

### First-Time User Flow
1. **Register**: Create account with email and password (or biometric)
2. **Login**: Authenticate with credentials
3. **Dashboard**: See empty vault (zero existing entries)
4. **Create Entry**: Write first journal entry with auto-save
5. **Seal Entry**: Encrypt and store permanently
6. **Explore Features**: Try Zen Mode, Character Matrix, Snapshots
7. **Install PWA**: (Optional) Install as native app

### Environment Configuration

#### Development (Default)
```bash
# No .env file needed; defaults are secure for local testing
python3 app.py  # Flask debug mode enabled automatically
```

#### Production Deployment
Create `.env` file in project root:
```env
# Security
SECRET_KEY=your-cryptographically-secure-random-string-here
ENCRYPTION_KEY=Fernet-compatible-key-base64-encoded
FLASK_ENV=production
DEBUG=False

# Database
DATABASE_URL=sqlite:///instance/mindvault.db
SQLALCHEMY_ECHO=False

# Session
SESSION_TIMEOUT=3600  # 1 hour
MAX_CONTENT_LENGTH=16777216  # 16MB file uploads

# Logging
LOG_LEVEL=WARNING
```

**Generate Secure Keys:**
```bash
python3 -c "
from cryptography.fernet import Fernet
key = Fernet.generate_key().decode()
print(f'ENCRYPTION_KEY={key}')
"

python3 -c "
import secrets
key = secrets.token_hex(32)
print(f'SECRET_KEY={key}')
"
```

---

## Usage Guide

### Writing & Managing Entries

**Create New Entry:**
1. From **Dashboard**, click "+ New Entry"
2. Add title (e.g., "Reflection on Chapter 3")
3. Select category: General | Fiction | Research
4. Write freely in the rich text editor
5. Auto-save engages every 30 seconds (silent notification)
6. Click **"Seal Entry"** to encrypt and save permanently

**Edit Existing Entry:**
1. From Dashboard, click entry title
2. Modify content (auto-save active)
3. Change category or title as needed
4. Create snapshots for versioning (see below)
5. Entry updates automatically every 30 seconds

**Delete Entry:**
1. Open entry details
2. Click **"Delete"** button (with confirmation)
3. Entry and all snapshots removed permanently
4. Action cannot be undone—consider snapshots as backup

### Character Matrix (Fiction Development)

**Create Character:**
1. Click **"Characters"** in navigation
2. Click **"+ Create Character"**
3. Fill required + optional fields:
   - **Name**: Character identifier (e.g., "Elara Thorne")
   - **Archetype**: Protagonist | Antagonist | Mentor | Support | Other
   - **Traits**: Comma-separated list (e.g., "Mysterious, Strategic, Loyal")
   - **Backstory**: Character history (rich text, multi-paragraph OK)
   - **Physical Description**: Appearance, distinguishing features
   - **Relationships**: JSON object for character connections
     ```json
     {
       "father": "Lord Thorne",
       "rival": "Marcus Stone",
       "mentor": "Sage Elvira"
     }
     ```
   - **Motivations**: Primary and secondary goals
   - **Avatar Color**: Hex code for matrix display (e.g., #5DADE2)
4. Click **"Save Character"**
5. Character appears in grid with color badge

**Edit Character:**
1. From Characters grid, click **"Edit"**
2. Modify any field
3. Click **"Update Character"**

**Delete Character:**
1. From Characters grid, click **"Delete"**
2. Confirm action
3. Character removed; snapshots preserved

### Draft Versioning (Snapshots)

**Create Manual Snapshot:**
1. While editing entry, click **"Save Version"**
2. Enter version number (e.g., "1.0", "1.5", "2.0")
3. Optional: Add description (e.g., "Completed dialogue pass")
4. Click **"Create Snapshot"**
5. Current version frozen; editing continues on working copy

**Auto-Save Snapshots:**
- Triggered automatically every 30 seconds
- Stored in snapshots table with `is_autosave=true`
- Version tagged as "auto"
- Helps recover from crashes or accidental deletions

**View Version History:**
1. Click **"Versions"** on any entry
2. Timeline displays all snapshots in chronological order
3. Latest version highlighted; auto-saves marked separately
4. Each snapshot shows: version, timestamp, creator, description

**Restore Previous Version:**
1. From timeline, select desired version
2. Click **"Restore This Version"**
3. Content loads; you can review before committing
4. Click **"Confirm Restore"** to make live
5. Working version updates; snapshot remains in history

**Compare Versions (via inspection):**
- Open version A, note key phrases
- Switch to version B, compare changes
- Future: side-by-side diff viewer planned

### Zen Mode (Focus Writing)

**Enter Zen Mode:**
1. From Dashboard or Entry, click **"Zen Mode"** button
2. Navigation sidebar slides away
3. UI chrome hidden; only editor visible
4. Word count appears bottom-right

**While Writing in Zen Mode:**
- Editor takes full viewport
- Word counter: updates real-time
- Character counter: includes all text
- All formatting tools remain accessible
- No distractions; maximum focus

**Exit Zen Mode:**
1. Click **"Exit"** button (top-right)
2. Full UI returns
3. Preference auto-saved for next session
4. Re-entering uses same preference

**Keyboard Shortcuts (Future):**
- Cmd+Z / Ctrl+Z — Toggle Zen Mode
- Escape — Exit Zen Mode

### Authentication & Security

**Password Login:**
1. Navigate to `/login`
2. Enter email and password
3. Click **"Sign In"**
4. 30-minute session timeout; auto-logout for security

**Biometric Authentication (Optional):**
1. During registration, enable biometric
2. Use Face ID (iPhone/Mac), Touch ID (iPhone/Mac/iPad), or Windows Hello
3. Biometric credentials stored on device; server never sees biometric data
4. Password remains fallback option

**Password Reset:**
- Currently: No automated reset (future feature)
- Temporary: Delete account and create new one
- Production: Implement email-based verification

**Session Management:**
- Auto-logout after 30 minutes inactivity
- Login persists across browser refreshes
- Logout clears session; requires re-authentication

---

## Security & Privacy Architecture

### Encryption at Rest

**Entry Content Encryption:**
```python
# Client-side encryption before database storage
from cryptography.fernet import Fernet

cipher = Fernet(ENCRYPTION_KEY)
plaintext = entry_content
encrypted = cipher.encrypt(plaintext.encode())

# Stored as binary blob in DiaryEntry.encrypted_content
# Database sees only ciphertext; plaintext never persisted
```

- **Algorithm**: Fernet (AES-128-CBC with HMAC)
- **Auth Tag**: HMAC-SHA256 prevents tampering
- **Key Derivation**: Cryptographically random 32-byte keys
- **Decryption**: Only when explicitly requested by authenticated user
- **Memory**: Plaintext cleared from memory after encryption

**Character Data Encryption:**
- Character profiles stored encrypted (like entries)
- Relationships (JSON) encrypted before storage
- Avatar colors and metadata not encrypted (non-sensitive)

**Snapshot Encryption:**
- Each snapshot independently encrypted
- Content frozen at encryption time; immutable
- Version history never exposable unencrypted

### Authentication & Session Security

**Password Storage:**
- **Algorithm**: Bcrypt with 10 salt rounds
- **Never Stored Plaintext**: Password_hash only
- **Verification**: `bcrypt.check_password_hash()` on login
- **Rotation**: Change password via settings (future)

**Session Management:**
- **Session Key**: Flask-Login with SECRET_KEY
- **TTL**: 30 minutes inactivity (configurable)
- **Scope**: Per-user, tied to browser cookie
- **CSRF Protection**: Token on all state-changing forms
- **HTTP-Only Cookies**: Prevents JavaScript access

**Biometric Authentication:**
- **Web Standard**: W3C WebAuthn / FIDO2
- **Storage**: Credential stored on device hardware
- **Server-Side**: Server never receives biometric data
- **Challenge-Response**: Cryptographic verification only
- **Fallback**: Password option always available

### Route Protection & Authorization

**Protected Routes:**
```python
@app.route('/entry/<id>')
@login_required  # Redirects unauthenticated users to /login
def view_entry(id):
    entry = DiaryEntry.query.get_or_404(id)
    
    # Ownership verification (prevent User A accessing User B data)
    if entry.user_id != current_user.id:
        abort(403)  # Forbidden
    
    # Decrypt entry content
    plaintext = cipher.decrypt(entry.encrypted_content).decode()
    return render_template('entry.html', content=plaintext)
```

**All Sensitive Routes Protected:**
- [YES] Dashboard (`/dashboard`)
- [YES] Entry creation/editing/deletion (`/entry/*`)
- [YES] Character management (`/character/*`)
- [YES] Snapshots (`/snapshot/*`)
- [YES] User settings (future)

**Unprotected (Public) Routes:**
- Home page (`/`)
- Authentication (`/register`, `/login`)
- Review submission (`/submit-review`)

### Data Ownership Verification

Every protected route verifies:
```python
# Pattern: Verify user owns the requested resource
entry = DiaryEntry.query.get_or_404(entry_id)
if entry.user_id != current_user.id:
    abort(403)

character = Character.query.get_or_404(char_id)
if character.user_id != current_user.id:
    abort(403)
```

- **Prevents**: Cross-user data access
- **Enforced**: On every route
- **Audited**: In COMPREHENSIVE_AUDIT.md

### What's Encrypted & Protected

[ENCRYPTED]
- Journal entry content
- Character profiles and relationships
- Snapshot versions
- (User passwords are hashed, not encrypted)

[HASHED & SALTED]
- User passwords (bcrypt)

[PROTECTED BY SESSION]
- User authentication status
- CSRF tokens on forms

[NOT ENCRYPTED - NON-SENSITIVE]
- Entry title (for searchability in future)
- Entry category (General, Fiction, Research)
- Timestamps
- Avatar colors
- Character names (searchable)

### Production Deployment Security Checklist

- [] **Environment Variables**: Store SECRET_KEY, ENCRYPTION_KEY in `.env` (never commit)
- [ ] **HTTPS/TLS**: Enable SSL certificates (Let's Encrypt free option)
- [ ] **Debug Mode**: Set `DEBUG=False` in production
- [ ] **Database Backups**: Regular encrypted backups with versioning
- [ ] **Access Control**: If self-hosted, restrict deployment environment access
- [ ] **Dependency Updates**: Monthly security patch checks
- [ ] **Log Monitoring**: Monitor for failed login attempts, errors
- [ ] **Key Rotation**: Plan annual encryption key rotation (with data re-encryption)
- [ ] **CORS Headers**: Restrict cross-origin requests
- [ ] **Rate Limiting**: Implement login attempt rate limiting

### Important Notes & Limitations

**Current Limitations (v2.0):**
- Password reset: No automated recovery (plan email verification for v2.1)
- Data export: No encrypted archive export (planned v2.1)
- 2FA: Not yet implemented (roadmap v2.1)
- Recovery keys: Not available (future security feature)

**Production Considerations:**
- Encryption key is global; stored in `.env` on server
- Database file permissions should restrict non-root access
- Consider database-level encryption (depends on hosting)
- Biometric auth requires HTTPS in production
- Service Worker cache must be cleared on logout (implemented)

### Data Ownership & Privacy

- **You Own Your Data**: Stored locally on your device by default
- **No Tracking**: Zero analytics, no Google Analytics, no Mixpanel
- **No AI Training**: Your entries never used to train LLMs or models
- **No Ads**: MindVault is not monetized through your data
- **No Third-Party Sharing**: No vendor tracking, no data brokers
- **Portable**: Export your vault anytime (encrypted archives planned v2.1)
- **Deletable**: Purge account and all associated data on demand
- **Transparent**: Open source code available for audit

---

## PWA Installation

### Installation Steps by Platform

#### iOS (iPhone/iPad)
1. Open MindVault in Safari (http://127.0.0.1:5000 or deployed URL)
2. Tap **Share** icon (square with arrow)
3. Select **"Add to Home Screen"**
4. Name: "MindVault" (or custom name)
5. Tap **"Add"**
6. MindVault appears as app icon in home screen

#### Android (Chrome)
1. Open MindVault in Chrome
2. Tap **Menu** (three dots top-right)
3. Select **"Install app"** or **"Add to Home Screen"**
4. Confirm app name
5. MindVault app appears in app drawer

#### Desktop (Chrome/Edge/Firefox)
1. Open MindVault at http://127.0.0.1:5000
2. Address bar shows **"Install"** button or icon
3. Click to open install dialog
4. Choose installation location or use default
5. App launches with app window (no browser chrome)

#### macOS (Safari)
1. Open MindVault in Safari
2. Tap **Share** icon (or cmd+Y)
3. Select **"Add to Dock"**
4. MindVault appears in macOS Dock
5. Click to launch as PWA

### PWA Offline Features

**Service Worker Caching:**
- Core app shell cached on first load
- JavaScript, CSS, SVG icons cached
- Subsequent loads use cache-first strategy
- Network fetch only for fresh data

**Offline Capabilities:**
- [YES] Read existing entries (all cached)
- [YES] Create new entries (queued in IndexedDB)
- [YES] Edit drafts (cached auto-save)
- [YES] View character matrix
- [YES] Access settings
- [NO] Sync until connection returns

**Automatic Sync on Reconnect:**
- Background sync API triggers when online restored
- Pending entries uploaded to server
- Conflicts handled by server-side merge logic
- User notified of successful sync

**Cache Versioning:**
- Service Worker versioned (`vX.Y.Z`)
- Old caches cleared on app update
- Zero manual cache clearing needed

**Storage Limits:**
- Service Worker cache: ~50MB typical
- IndexedDB (offline queue): ~5-50MB depending on browser
- LocalStorage (preferences): <1MB
- Total: Practical for 1000+ entries

---

## Project Architecture

### Directory Structure

```
mindvault/
│
├── Root Configuration & Documentation
│   ├── .env                            # Environment variables (secrets - gitignored)
│   ├── .env.example                    # Example environment template
│   ├── .gitignore                      # Git ignore rules
│   ├── app.py                          # Flask application + SQLAlchemy models + 25+ routes
│   ├── app.py.backup                   # Backup of original app.py
│   ├── security.py                     # Encryption utilities (Fernet wrapper)
│   ├── security.py                     # Encryption utilities (Fernet wrapper)
│   ├── migrate_db.py                   # Database migration helper
│   ├── generate_pwa_icons.py           # PWA icon generation utility
│   ├── requirements.txt                # Python dependencies (pip freeze format)
│   ├── manifest.json                   # Web App Manifest (PWA metadata)
│   └── database.db                     # SQLite database (root level, gitignored)
│
├── Documentation Files
│   ├── README.md                       # Main project README (this file)
│   ├── README_NEW.md                   # Archive of previous README version
│   ├── EXPANSION.md                    # v2.0 feature deep-dive guide (500+ lines)
│   ├── MIGRATION.md                    # v1 to v2 upgrade path, backward compatibility
│   └── COMPREHENSIVE_AUDIT.md          # Security audit, testing results, deployment
│
├── .github/                            # GitHub configuration directory
│   └── copilot-instructions.md         # Developer workspace conventions & patterns
│
├── instance/                           # Flask instance folder (application runtime)
│   └── mindvault.db                    # Primary SQLite database (local, encrypted)
│
├── templates/                          # Jinja2 HTML templates (server-side rendering)
│   ├── base.html                       # Base layout (PWA meta, nav, footer)
│   ├── index.html                      # Homepage (public, displays reviews)
│   ├── login.html                      # Login form + biometric authentication
│   ├── register.html                   # Registration form + biometric setup
│   ├── dashboard.html                  # Main dashboard (user's vault, entry list)
│   ├── entry.html                      # Create/edit single entry with editor
│   ├── view_entry.html                 # View entry details (read-only display)
│   ├── characters.html                 # Character matrix grid display
│   ├── character_form.html             # Create/edit character profile form
│   ├── snapshots.html                  # Version history timeline visualization
│   ├── submit_review.html              # Public review submission form
│   ├── offline.html                    # Fallback page when offline/unreachable
│   └── footer.html                     # Footer component (reusable)
│
├── static/                             # Static assets (frontend resources)
│   │
│   ├── css/                            # Stylesheets
│   │   ├── style.css                   # Main design system (20+ CSS variables)
│   │   │                               # - Colors: primary, secondary, accent, background
│   │   │                               # - Spacing scale: --spacing-xs to --spacing-xl
│   │   │                               # - Typography: font-size, font-weight, line-height
│   │   │                               # - Transitions: animations, transforms, opacity
│   │   │                               # - Z-index management for stacking context
│   │   │                               # - Responsive breakpoints for mobile/tablet
│   │   └── expansion.css               # v2.0 feature styles
│   │                                   # - Zen Mode (hidden states, full-screen)
│   │                                   # - Character Matrix (grid layout)
│   │                                   # - Snapshots (timeline visualization)
│   │                                   # - Auto-save notifications
│   │                                   # - Focus metrics display
│   │
│   ├── js/                             # JavaScript files (client-side logic)
│   │   ├── main.js                     # Legacy entry point (general features)
│   │   │                               # - Form handling and validation
│   │   │                               # - Event listeners
│   │   │                               # - UI interactions
│   │   ├── enhanced-main.js            # v2.0: Advanced features initialization
│   │   │                               # - Zen Mode toggle functionality
│   │   │                               # - Auto-save timer (30-second intervals)
│   │   │                               # - Service Worker registration
│   │   │                               # - App initialization logic
│   │   │                               # - PWA installation detection
│   │   ├── service-worker.js           # PWA Service Worker (offline support)
│   │   │                               # - Cache management strategy
│   │   │                               # - Network-first/cache-first behavior
│   │   │                               # - Offline fallback routes
│   │   │                               # - Background sync for pending entries
│   │   │                               # - Cache versioning and cleanup
│   │   └── biometric-auth.js           # WebAuthn authentication
│   │                                   # - Face ID (iOS/macOS)
│   │                                   # - Touch ID (iOS/macOS/iPad)
│   │                                   # - Windows Hello
│   │                                   # - Android biometric sensors
│   │                                   # - Credential registration/verification
│   │
│   ├── svg-icons.html                  # SVG icon library (14 reusable icons)
│   │                                   # - Shield (security)
│   │                                   # - Lock (encryption)
│   │                                   # - Character (persona)
│   │                                   # - Matrix (grid)
│   │                                   # - Version (snapshot)
│   │                                   # - Zen (distraction-free)
│   │                                   # - Star (favorite)
│   │                                   # - Archive (storage)
│   │                                   # - Plus (add)
│   │                                   # - Trash (delete)
│   │                                   # - Edit (modify)
│   │                                   # - Search (find)
│   │                                   # - Bell (notification)
│   │                                   # - Settings (preferences)
│   │
│   ├── IMG_MindVault_logo.png          # Main MindVault logo (120x120, PNG)
│   ├── logo_mindvault.png              # Alternative logo variant (PNG)
│   │
│   └── [future]/                       # Planned static assets
│       ├── images/                     # PWA app icons (multiple sizes)
│       │   ├── icon-192.png            # PWA icon 192x192px
│       │   ├── icon-512.png            # PWA icon 512x512px
│       │   └── favicon.ico             # Browser favicon
│       │
│       └── fonts/                      # Custom web fonts (future)
│
└── [Excluded from Source Control]
    ├── __pycache__/                    # Python bytecode cache (gitignored)
    ├── venv/                           # Virtual environment (gitignored)
    ├── *.pyc                           # Compiled Python files (gitignored)
    └── .git/                           # Git repository metadata
```

### Key Files & Responsibilities

**Backend Core (`app.py`):**
- Flask application initialization
- SQLAlchemy model definitions (User, DiaryEntry, EntrySnapshot, Character, Review)
- 25+ routes for auth, entries, characters, snapshots, reviews
- Session management and user verification
- Error handling and redirects

**Security Module (`security.py`):**
- Fernet encryption utilities
- Encrypt/decrypt functions with error handling
- Key management helpers

**Frontend Styling:**
- **style.css**: Main design system with 20+ CSS variables
  - Color palette (primary, secondary, accent, background)
  - Spacing scale (--spacing-xs to --spacing-xl)
  - Typography (--font-size, --font-weight, --line-height)
  - Transitions and animations
  - Z-index management
  - Responsive breakpoints
- **expansion.css**: v2.0 feature styles
  - Zen Mode hidden states
  - Character Matrix grid layout
  - Snapshots timeline
  - Auto-save notifications
  - Zen mode metrics display

**Frontend JavaScript:**
- **main.js**: Legacy features, form handling
- **enhanced-main.js**: Zen Mode toggle, auto-save timer, Service Worker registration, app initialization
- **service-worker.js**: Cache management, offline fallback, background sync
- **biometric-auth.js**: WebAuthn challenge/response, credential management

**Database Models:**
- User: Account with bcrypt password hash
- DiaryEntry: Encrypted journal entries with categories
- EntrySnapshot: Versioned snapshots (manual + auto-save)
- Character: Character profiles with relationships
- Review: Public testimonials for homepage

**Templates:**
- base.html: Navigation, flash messages, CSS/JS includes, PWA metadata
- index.html: Public homepage with features and reviews
- entry.html: Rich text editor for creating/editing entries
- characters.html: Grid of character profiles with edit/delete
- snapshots.html: Timeline visualization of entry versions
- dashboard.html: Main vault interface (entry list + quick actions)

---

## Development Guide

### Project Setup for Developers

**Clone & Enter Directory:**
```bash
git clone https://github.com/sinhaayush61426-ai/mindvault.git
cd mindvault
```

**Install Python Dependencies:**
```bash
pip install -r requirements.txt
```

### Key Development Patterns

**Encryption Pattern** (Always use before saving)
```python
from security import encrypt_content, decrypt_content

# Encrypt before storing
plaintext = "My journal entry..."
encrypted = encrypt_content(plaintext)
entry = DiaryEntry(encrypted_content=encrypted)

# Decrypt when retrieving
plaintext = decrypt_content(entry.encrypted_content)
```

**User Authorization Pattern** (Always verify ownership)
```python
@app.route('/entry/<id>/edit', methods=['GET', 'POST'])
@login_required
def edit_entry(id):
    entry = DiaryEntry.query.get_or_404(id)
    
    # Verify current user owns this entry
    if entry.user_id != current_user.id:
        abort(403)  # Forbidden
    
    # Safe to proceed
    ...
```

**CSS Variable Usage** (Use design system)
```css
/* Good: Use CSS variables */
.my-component {
  background-color: var(--primary-color);
  padding: var(--spacing-md);
  font-size: var(--font-size-base);
  transition: var(--transition);
}

/* Bad: Hardcoded values */
.my-component {
  background-color: #5DADE2;
  padding: 12px;
}
```

**SVG Icon Usage** (Use icon library)
```html
<!-- Good: Use SVG icons from library -->
<svg class="icon icon-lock">
  <use xlink:href="#icon-lock"></use>
</svg>

<!-- Bad: External icon fonts or images -->
<img src="lock.png" />
<i class="fas fa-lock"></i>
```

### Adding New Routes

**Template:**
```python
@app.route('/new-feature', methods=['GET', 'POST'])
@login_required  # Add if user-specific
def new_feature():
    if request.method == 'POST':
        # Handle form submission
        # Always encrypt sensitive data
        # Verify user authorization
        return redirect(url_for('success_page'))
    
    return render_template('new_feature.html')
```

### Running the Application

**Development Server:**
```bash
python3 app.py
# Flask debug mode enabled
# Watch for code changes and auto-reload
# Open http://127.0.0.1:5000
```

**Production Server** (using gunicorn):
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Testing with Service Worker

**Check Service Worker (DevTools):**
1. Open DevTools (`F12`)
2. Application tab → Service Workers
3. Verify "mindvault" SW is registered and active
4. Check cache storage for "mindvault-cache"

**Test Offline:**
1. Open DevTools → Network tab
2. Check "Offline" checkbox
3. Refresh page → app should work with cached content
4. Uncheck "Offline" → connection restored

### Database Inspection

**View Database Contents:**
```bash
sqlite3 instance/database.db

# List tables
sqlite> .tables

# Show schema
sqlite> .schema diary_entry

# Query entries (encrypted content shown as binary)
sqlite> SELECT id, title, timestamp FROM diary_entry LIMIT 5;

# Exit
sqlite> .exit
```

### Debugging Tips

**Flask Debug Output:**
- Check terminal for route calls and SQL queries
- Set `app.config['SQLALCHEMY_ECHO'] = True` for SQL logging
- Use `print()` or Python debugger (pdb)

**Browser Console:**
- `F12` → Console tab for JavaScript errors
- Check Network tab for failed requests
- Application tab for Service Worker, Cache, LocalStorage issues

**Encryption Issues:**
- Verify `ENCRYPTION_KEY` consistency across encrypt/decrypt
- Check ciphertext is binary (not string)
- Ensure `ENCRYPTION_KEY` environment variable is set in production

---

## Testing & Quality Assurance
### Audit Coverage & Findings

See **[COMPREHENSIVE_AUDIT.md](./COMPREHENSIVE_AUDIT.md)** for:
- 100% route testing (all 25+ endpoints verified)
- Security audit (critical issues identified and fixed)
- 9 loopholes discovered and resolved
- Dashboard redesign before/after comparison
- Complete hyperlink and navigation mapping
- WCAG AA accessibility compliance

### Manual Testing Procedures

**User Registration & Login:**
```
1. Navigate to /register
2. Create new account with email + password
3. Log in with credentials
4. Verify redirect to dashboard
5. Check session persistence (refresh page)
6. Log out; verify redirect to home
```

**Entry Creation & Encryption:**
```
1. From dashboard, click "+ New Entry"
2. Add title, select category, write content
3. Click "Seal Entry"
4. Check database: SELECT * FROM diary_entry LIMIT 1
5. Verify encrypted_content is binary (not plaintext)
6. Reopen entry from dashboard
7. Verify content displays correctly (decrypted)
```

**Character Matrix:**
```
1. Navigate to /characters
2. Create new character with all fields
3. Verify grid display with avatar color
4. View, edit, delete operations
5. Check database: SELECT * FROM character WHERE user_id=1
```

**Snapshots & Versioning:**
```
1. Open entry from dashboard
2. Make edits; auto-save triggers every 30 seconds
3. Click "Save Version" with custom version number
4. Make more edits; save another version
5. Click "View Versions" tab
6. Verify timeline displays all versions
7. Restore old version; confirm content reverted
8. Check restored version appears in timeline
```

**Zen Mode:**
```
1. Click "🧘 Zen Mode" button
2. Verify nav sidebar hidden
3. Write text; check word count updates
4. Exit Zen Mode
5. Full UI returns
6. Refresh page; verify Zen preference persisted
```

**Offline Functionality:**
```
1. Open DevTools → Network
2. Check "Offline" checkbox
3. Navigate existing pages (should load from cache)
4. Try create new entry (should queue)
5. Uncheck "Offline"
6. Refresh page; verify sync completes
```

**Biometric Authentication (iOS/macOS):**
```
1. On /register or /login, enable biometric
2. Follow platform prompts (Face ID/Touch ID)
3. On subsequent login, biometric option appears
4. Verify password fallback still works
```

### Performance Testing

**Metrics:**
- First Load: <2 seconds (with cache)
- Service Worker Registration: <1 second
- Encryption/Decryption: <100ms per entry
- Database Query: <50ms average
- UI Transitions: 60fps (no jank)

**Stress Testing:**
- 1000+ entries: Responsive dashboard
- 100+ characters: Grid renders smoothly
- 50 snapshots per entry: Timeline smooth
- 8-hour session: No memory leaks

### Browser Compatibility

| Browser | Desktop | Mobile | Notes |
|---------|---------|--------|-------|
| Chrome | [YES] Full | [YES] Full | Best overall; all features |
| Firefox | [YES] Full | [YES] Full | Full support; PWA via WebExtension |
| Safari | [YES] Full | [Limited] | iOS PWA works; no SW background sync |
| Edge | [YES] Full | [YES] Full | Chromium-based; identical to Chrome |
| IE 11 | [NO] None | N/A | Requires ES5 polyfills (not supported) |

### Known Issues & Workarounds

| Issue | Platform | Workaround | Status |
|-------|----------|-----------|--------|
| Private browsing PWA install | Safari (iOS) | Use regular browsing | [Expected behavior] |
| Service Worker updates | Chrome | Hard refresh (Ctrl+Shift+R) | [Normal lifecycle] |
| Biometric prompt timeout | Android | Re-enable biometric in Settings | [Device-specific] |

---

## Future Roadmap & Vision

### Planned for v2.1 (Q3 2026)

- **Full-Text Search**: Encrypted search indexing for entries and characters
- **Export/Import**: Download encrypted archives; restore in new instance
- **Email Password Reset**: Secure recovery flow with verification
- **Sentiment Analysis**: Real-time mood tracking from journal entries
- **Writing Analytics**: Word count trends, streak tracking, productivity graphs
- **Time-Locked Entries**: "Letters to the Future" that unlock on specified dates
- **Import from Competitors**: One-click import from Day One, Reflectly, Day Diary

### Planned for v2.2+ (2026-2027)

- **Two-Factor Authentication (2FA)**: TOTP + backup recovery codes
- **End-to-End Sync**: Optional cloud backup with E2E encryption (user's cloud provider)
- **Collaborative Features**: Shared character worlds for fiction writers
- **Mobile Apps**: Native iOS (Swift) and Android (Kotlin) apps
- **Template Library**: Writing prompts, journaling frameworks, character templates
- **Advanced Filtering**: Filter by mood, category, word count, date ranges
- **AI Integration (Optional)**: Local tiny-LLM for grammar, tone suggestions (no data sent)
- **Dark Mode Themes**: Additional color schemes (cyberpunk, dark, solarized, nord)

### Long-Term Vision (2027+)

**Privacy-First Platform Ecosystem:**
- MindVault Core (encrypted journaling) — foundation
- MindVault Stories (fiction manuscript management)
- MindVault Research (collaborative research organization)
- MindVault Sync (user-controlled encrypted cloud)

**Community & Business:**
- Optional anonymous publishing platform for stories/essays
- Creator toolkit for professional writers
- Educational institution licensing (student research vaults)
- Non-profit funding model (no VC, sustainable)

**Technology Evolution:**
- Rust backend for cryptography (future performance)
- WebAssembly encryption (client-side speed)
- Distributed storage support (IPFS, blockchain)
- Verifiable privacy guarantees (formal security proofs)

---

## Contributing to MindVault

We welcome contributions from developers, designers, and security researchers.

### Before Starting

1. **Review** [.github/copilot-instructions.md](./.github/copilot-instructions.md) for workspace conventions
2. **Check** [EXPANSION.md](./EXPANSION.md) for feature deep-dives
3. **Read** [COMPREHENSIVE_AUDIT.md](./COMPREHENSIVE_AUDIT.md) for security context
4. **Open Issue** for bugs/features before starting work

### Contribution Types

**Bug Fixes**
- Open issue with reproduction steps
- Verify in latest main branch
- Submit PR with test case
- Update COMPREHENSIVE_AUDIT.md if security-related

**New Features**
- Discuss in issue first (avoid wasted work)
- Follow security patterns from codebase
- Always encrypt sensitive data
- Add tests and documentation
- Update roadmap if applicable

**Documentation**
- Improve README clarity
- Add code examples
- Update troubleshooting guide
- Translate to other languages (future)

**Security**
- Report vulnerabilities via email (not public issues)
- Provide proof-of-concept
- Suggest remediation
- We'll work with you on fix

### Development Workflow

1. **Fork** repository on GitHub
2. **Clone** your fork
3. **Create feature branch** (`git checkout -b feat/feature-name`)
4. **Make changes** with descriptive commits
5. **Test** thoroughly (manual + automated)
6. **Push** to your fork
7. **Open PR** with clear description
8. **Address review feedback**
9. **Merge** when approved

### Code Style

- **Python**: PEP 8 (use `black` or `flake8`)
- **JavaScript**: ES6+, avoid global scope pollution
- **CSS**: Use design system variables, mobile-first
- **HTML**: Semantic, accessible (WCAG AA)
- **Git**: Meaningful commit messages ("Add character search" vs "fix stuff")

### Areas Without Maintenance
- [NO] No active Android/iOS native app development (focus: PWA)
- [NO] No Windows/macOS native app (focus: web + PWA)
- [NO] No backend-as-a-service cloud offering (focus: self-hosting)
- [NO] No AI integration for now (future decision)

### Funding & Sustainability

MindVault is funded by:
- Open source passion (primarily volunteer)
- Educational institution partnerships (future)
- Optional donations (no pressure; app stays free)
- Grant funding for privacy research

We're **NOT** seeking VC funding or advertising. MindVault remains independent.

---

## License

**MIT License** — See [LICENSE](./LICENSE) file

### Key Terms
- [YES] Use for personal projects
- [YES] Use for commercial applications
- [YES] Modify and distribute
- [YES] Use privately
- [NO] Hold liable
- [NO] No warranty

### Open Source Attribution

MindVault uses excellent open source projects:
- **Flask**: Lightweight web framework
- **SQLAlchemy**: ORM and SQL toolkit
- **Fernet (cryptography)**: Industry-standard encryption
- **Bcrypt**: Password hashing
- Other dependencies listed in requirements.txt

---

## Acknowledgments

- **Security**: Inspired by differential privacy and zero-knowledge proofs
- **UX**: Influenced by Obsidian, Day One, and Notion
- **Architecture**: Draws from Signal, Element, and other privacy-first apps
- **Community**: Thanks to all testers, contributors, and users

---

## Support & Contact

**Bugs & Issues:**
- Open GitHub issue with reproduction steps
- Check existing issues first (may be duplicate)
- Include browser/system info

**Security Vulnerabilities:**
- Do NOT open public GitHub issue
- Email: [security contact — add when deploying]
- Include: description, reproduction, suggested fix

**Feature Requests:**
- Open GitHub discussion (not issue)
- Check roadmap first (may be planned)
- Explain use case and priority

**General Questions:**
- Check README, EXPANSION.md, and docs first
- Search existing GitHub issues/discussions
- Ask in GitHub discussions thread

---

## Thanks for Using MindVault

Your privacy matters. Your thoughts are yours alone. Welcome to a vault without walls.

**Happy Writing!**