# MindVault v2.0: Author's Archive & PWA Expansion

## Overview

MindVault has been expanded with enterprise-grade features designed for creative professionals, researchers, and writers. This document covers all new capabilities introduced in v2.0.

---

## 🎭 Feature 1: Author's Archive - Character Matrix

### What It Does

The Character Matrix is a dedicated hub for storing and managing character profiles for your creative fiction projects. Track personality traits, backstories, relationships, and visual appearance in an organized matrix.

### How to Use

1. **Navigate to Characters**
   - Click "Characters" in the main navigation (logged in only)
   - View all your created character profiles in a grid layout

2. **Create a New Character**
   - Click "+ Create Character"
   - Fill in character details:
     - **Name**: Character identifier
     - **Archetype**: Protagonist, Antagonist, Mentor, Support, or Other
     - **Personality Traits**: Key character qualities (e.g., "Mysterious, Strategic, Loyal")
     - **Backstory**: Character history and origin
     - **Physical Description**: Appearance and distinctive features
     - **Motivations & Goals**: What drives the character
     - **Key Relationships**: Connections to other characters (JSON format optional)
     - **Avatar Color**: Visual identifier color (hex code)

3. **Manage Characters**
   - Click "Edit" to modify character details
   - Click "Delete" to remove a character
   - Use avatar colors to quickly identify characters

### Technical Details

- **Database**: Character model stores all profile data linked to user
- **UI**: CSS Grid with hover effects and color-coded avatars
- **API Routes**:
  - `GET /characters` - View all characters
  - `POST /character/new` - Create character
  - `POST /character/<id>/edit` - Update character
  - `POST /character/<id>/delete` - Remove character

---

## 📸 Feature 2: Draft Versioning - Snapshots

### What It Does

The Snapshots feature allows you to save multiple versions of your work without overwriting previous iterations. Think of it as Git for your writing—track evolution, compare versions, and restore any previous state.

### How to Use

1. **Create a Snapshot**
   - While editing an entry, specify:
     - **Version Number**: E.g., "1.0", "1.1", "2.0"
     - **Description**: Optional note about changes (e.g., "Fixed chapter 3")
   - Click "Create Snapshot" to save current content
   - Current version remains editable; snapshot is frozen

2. **View Version History**
   - Click "Versions" button on any entry
   - Browse timeline of all snapshots
   - See version number, description, and creation date
   - Auto-save snapshots are marked separately

3. **Restore a Version**
   - Select desired version from timeline
   - Click "Restore This Version"
   - Current working version will update to restored content
   - Original snapshot remains in history

### Auto-Save Feature

- Automatically saves draft every 30 seconds to browser storage
- No manual action required
- Accessible even offline
- "Draft saved" indicator appears briefly after each auto-save

### Technical Details

- **Database**: EntrySnapshot model with version tracking
- **Encryption**: All snapshot content encrypted with Fernet
- **UI**: Timeline visualization with gradient line
- **API Routes**:
  - `POST /entry/<id>/snapshot` - Create snapshot
  - `GET /entry/<id>/snapshots` - View history
  - `POST /snapshot/<id>/restore` - Restore version

---

## 🧘 Feature 3: Zen Mode - Focus Writing Environment

### What It Does

Zen Mode creates a distraction-free writing environment by hiding navigation, sidebars, and UI chrome. Perfect for immersive creative work.

### How to Use

1. **Enter Zen Mode**
   - Click "🧘 Zen Mode" button (available on dashboard and entry view)
   - Navigation and sidebars fade away
   - "Exit Zen" button appears in top-right

2. **While in Zen Mode**
   - Write uninterrupted in the editor
   - Word count and character count visible in bottom-right
   - Real-time counter updates as you type
   - All formatting and editing functions remain available

3. **Exit Zen Mode**
   - Click "Exit Zen" button
   - Full UI returns
   - Your preference is saved for next session

### Features

- **Word/Character Counter**: Real-time stats
- **Preference Persistence**: Returns to Zen Mode next session if you saved in it
- **Responsive**: Works on desktop and tablet
- **Keyboard Friendly**: Can toggle with JS console: `zenMode.toggleZenMode()`

### Technical Details

- **CSS**: `.zen-mode` class hides nav and sidebars via `transform: translateY/X()`
- **JavaScript**: ZenMode class manages state and counter updates
- **Storage**: Preference saved to localStorage
- **Performance**: No rendering overhead; uses CSS translation instead of removal

---

## 📱 Feature 4: Progressive Web App (PWA)

### What It Does

MindVault can now be installed on your device like a native app, works offline, and provides push notifications. Full parity to desktop experience on mobile.

### Installation

#### On iPhone/iPad
1. Open MindVault in Safari
2. Tap "Share" button
3. Select "Add to Home Screen"
4. Tap "Add"
5. MindVault appears as native app icon

#### On Android
1. Open MindVault in Chrome
2. Tap menu (three dots)
3. Select "Install app" or "Add to Home screen"
4. Tap "Install"
5. MindVault appears in app drawer

#### On Desktop (Windows/Mac)
1. Open Chrome and navigate to MindVault
2. Click install icon in address bar (if available)
3. Click "Install"
4. App window opens separately from browser

### Offline Support

- Service Worker automatically caches essential assets
- Access previously loaded pages without internet
- All entry data remains accessible (encrypted locally)
- Pending entries sync automatically when connection returns
- Offline notification appears with connection status

### App Shortcuts (Mobile)

From home screen, long-press MindVault app icon:
- **New Reflection**: Jump directly to create new entry
- **Character Matrix**: Access character library

### Push Notifications

- Configurable push notifications for vault updates
- Respects device notification settings
- Requires PWA installation

### Technical Details

**Manifest** (`manifest.json`):
- App name, description, theme colors
- Icon configuration for all platforms
- App shortcuts
- Widget metadata

**Service Worker** (`service-worker.js`):
- Network-first caching strategy
- Background sync for offline entries
- Push event handling
- Periodic cache updates

**Offline Page**: Auto-loads `/offline.html` when no connection
- Shows connection status
- Periodic reconnection checks
- Auto-refresh when online

---

## 🔐 Feature 5: Biometric Authentication (Web Authentication API)

### What It Does

WebAuthn integration allows seamless biometric login using device capabilities: Face ID, Touch ID, Windows Hello, or Android Biometric. Eliminates password fatigue for daily access.

### How to Use

#### First Time Setup (Registration)
1. Go to Register page
2. Fill in username and email
3. Click "🔐 Biometric Setup" button (if device supports)
4. Follow device's biometric prompt (scan face, fingerprint, etc.)
5. Credential is registered to your account
6. Complete registration normally

#### Logging In with Biometric
1. Go to Login page
2. Click "🔐 [Face ID/Touch ID/Windows Hello]" button
3. Trigger biometric on your device
4. Vault unlocks automatically
5. No password needed

### Device Support

| Device | Method | Support |
|--------|--------|---------|
| iPhone/iPad | Face ID / Touch ID | ✓ |
| Android | Fingerprint / Face Unlock | ✓ |
| Windows | Windows Hello (Iris/Face/PIN) | ✓ |
| Mac | Touch ID | ✓ |
| Linux | System dependent | ~ |

### Security Notes

- Biometric data never leaves your device
- Server stores cryptographic credential, not biometric
- Separate registration from password
- Can use biometric + password or just one
- Credentials stored securely per platform standards

### Technical Details

- **API**: `navigator.credentials` (PublicKeyCredential interface)
- **Attestation**: Direct attestation for highest security
- **Authenticator**: Platform authenticator (device hardware)
- **Key Algorithm**: ES256 (default) or RS256
- **Storage**: LocalStorage (simplified; production uses server-side secure storage)

---

## 🎨 Feature 6: Global CSS Variables System

### What It Does

Complete CSS architecture refactor moves all design tokens into CSS variables for consistency, maintainability, and easy theming.

### Available Variables

#### Colors
```css
--clr-cyan: #00f2ff          /* Primary accent */
--clr-cyan-light: #5DADE2    /* Light variant */
--clr-violet: #7000ff        /* Secondary accent */
--clr-violet-light: #DA70D6  /* Light variant */
--clr-pink: #ff007a          /* Tertiary accent */
--clr-pink-light: #FF69B4    /* Light variant */
--clr-gold: #ffc400          /* Success/gold */
--clr-gold-light: #ffdd57    /* Light variant */
```

#### Spacing
```css
--spacing-xs: 0.25rem
--spacing-sm: 0.5rem
--spacing-md: 1rem
--spacing-lg: 1.5rem
--spacing-xl: 2rem
--spacing-2xl: 3rem
```

#### Transitions
```css
--transition-fast: 0.15s ease
--transition-normal: 0.3s ease
--transition-slow: 0.5s ease
```

#### Layout
```css
--nav-height: 80px
--sidebar-width: 280px
--container-gap: 2rem
```

### How to Use in Custom CSS

```css
.my-element {
  background: var(--bg-surface);
  padding: var(--spacing-lg);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  transition: all var(--transition-normal);
  color: var(--text-primary);
  font-family: var(--font-primary);
  font-weight: var(--font-weight-bold);
}
```

### Theming

Simply override variables in `:root`:
```css
:root {
  --clr-primary: #your-color;
  --bg-deep: #your-bg;
}
```

---

## 📚 SVG Icon Library

### Available Icons

- `icon-shield` - Security/protection
- `icon-star` - Favorite/rating
- `icon-matrix` - Grid/organization
- `icon-character` - User profile
- `icon-version` - History/versioning
- `icon-zen` - Meditation/focus
- `icon-lock` - Security lock
- `icon-biometric` - Fingerprint authentication
- `icon-download` - Export/download
- `icon-snapshot` - Photo/snapshot
- `icon-edit` - Editing
- `icon-trash` - Delete
- `icon-settings` - Configuration
- `icon-export` - Share/export
- `icon-refresh` - Reload/sync

### How to Use

```html
<!-- In your template -->
<svg class="icon icon-lg icon-cyan">
  <use xlink:href="#icon-shield"></use>
</svg>

<!-- Size classes -->
<svg class="icon icon-sm">...</svg>   <!-- 1rem -->
<svg class="icon">...</svg>           <!-- 1.5rem default -->
<svg class="icon icon-lg">...</svg>   <!-- 2.5rem -->
<svg class="icon icon-xl">...</svg>   <!-- 3.5rem -->

<!-- Color classes -->
<svg class="icon icon-gold">...</svg>
<svg class="icon icon-cyan">...</svg>
<svg class="icon icon-violet">...</svg>
<svg class="icon icon-pink">...</svg>
```

---

## 🛠️ Developer Guide

### File Structure

```
mindvault/
├── app.py                          # Flask app with new routes
├── manifest.json                   # PWA configuration
├── templates/
│   ├── base.html                  # Updated with PWA, new CSS/JS
│   ├── characters.html            # Character grid
│   ├── character_form.html        # Create/edit character
│   ├── snapshots.html             # Version history timeline
│   ├── view_entry.html            # Entry detail view
│   └── offline.html               # Fallback for offline mode
├── static/
│   ├── css/
│   │   ├── style.css              # Main styles (with new variables)
│   │   └── expansion.css          # Zen Mode, Character, Snapshot styles
│   ├── js/
│   │   ├── service-worker.js      # PWA offline support
│   │   ├── biometric-auth.js      # WebAuthn implementation
│   │   └── enhanced-main.js       # Zen Mode, auto-save, initialization
│   └── svg-icons.html             # Icon library
```

### Database Models

```python
class Character(db.Model):
    id, user_id, name, archetype, personality_traits, backstory,
    relationships, physical_description, motivations, avatar_color,
    created_at, updated_at

class EntrySnapshot(db.Model):
    id, entry_id, version, encrypted_content, timestamp,
    description, is_autosave
```

### New Routes

**Characters**
- `GET /characters` - List all characters
- `GET /character/new` - Character creation form
- `POST /character/new` - Save new character
- `GET /character/<id>/edit` - Edit form
- `POST /character/<id>/edit` - Save changes
- `POST /character/<id>/delete` - Delete character

**Snapshots**
- `POST /entry/<id>/snapshot` - Create snapshot
- `GET /entry/<id>/snapshots` - View version history
- `POST /snapshot/<id>/restore` - Restore version
- `GET /entry/<id>` - View entry (new)

### Environment Setup

No new dependencies required beyond existing:
- Flask, SQLAlchemy, Flask-Login, Bcrypt
- Cryptography (Fernet)
- All PWA features use browser APIs (no npm packages)

### Testing Checklist

- [ ] Create character, verify in matrix
- [ ] Edit character, confirm updates
- [ ] Create entry snapshot, verify version appears
- [ ] Restore snapshot, confirm entry updates
- [ ] Toggle Zen Mode, verify UI hides/shows
- [ ] Test offline: disable network, create entry, restore connection
- [ ] Install as PWA on mobile
- [ ] Test biometric registration/login
- [ ] View all icon library sizes and colors

---

## 🔮 Future Expansion Ideas

1. **AI Writing Assistant**: Generate character suggestions, plot outlines
2. **Collaboration**: Real-time collaborative editing with invite system
3. **Export**: PDF, EPUB, Markdown export with formatting
4. **Analytics**: Word count trends, writing streaks, productivity insights
5. **Backup**: Cloud sync with E2E encryption
6. **Mobile App**: Native iOS/Android with local-first sync
7. **Plugin System**: Community themes and extensions
8. **Advanced Search**: Full-text search across all entries
9. **Social Features**: Share stories, get feedback from community
10. **AI Analysis**: Sentiment analysis, character consistency checker

---

## 📞 Support & Documentation

For issues or questions:
1. Check repository issues/discussions
2. Review database migrations (if needed)
3. Verify Service Worker registration in DevTools
4. Test in incognito mode to isolate cache issues

---

**Version**: 2.0  
**Release Date**: April 2026  
**Status**: Stable  
**License**: See repository LICENSE file
