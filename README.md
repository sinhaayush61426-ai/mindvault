# MindVault

MindVault is a privacy-first digital journaling and emotional reflection platform designed to provide a psychologically safe, distraction-free space for introspection.

Built with a minimal dark aesthetic, MindVault lets users write, encrypt, and store private reflections securely on their own machine. This repository is an open-source prototype for a personal wellness tool that can evolve into a full emotional intelligence workspace with local NLP, sentiment tracking, and future-dated letters.

## Table of Contents

- [Vision](#vision)
- [Why MindVault?](#why-mindvault)
- [What MindVault Does Today](#what-mindvault-does-today)
- [How MindVault Works](#how-mindvault-works)
- [Security and Privacy](#security-and-privacy)
- [Project Architecture](#project-architecture)
- [Getting Started](#getting-started)
- [Usage Guide](#usage-guide)
- [Developer Notes](#developer-notes)
- [Future Roadmap](#future-roadmap)
- [Contributing](#contributing)
- [License](#license)

## Vision

MindVault is built to be a digital sanctuary for people who want to journal, reflect, and track emotional patterns without compromising privacy.

The core idea is to create a secure, self-hosted space where personal data stays local, and sensitive thoughts never leave the vault. MindVault aims to remove noise and external tracking, focusing instead on meaningful, private self-reflection.

## Why MindVault?

- Privacy-first: your words are encrypted before being written to disk.
- Low distraction: a clean, dark interface keeps the writing flow uninterrupted.
- Trustworthy foundations: no external AI APIs are required to use the app.
- Progress-focused: the platform is intentionally designed to grow toward emotional insights over time.

## What MindVault Does Today

MindVault currently provides a working prototype for the following capabilities:

- User registration and login with secure password hashing
- Encrypted diary entries stored in a local SQLite database
- A personal dashboard showing the user's recent entries
- A lightweight home page with approved community reviews
- Server-side encryption using `cryptography.Fernet`
- Basic route protection with `Flask-Login`

## How MindVault Works

The application is built using Flask and stores data in SQLite for a lightweight local experience.

### Core application flow

1. A user registers with a username, email, and password.
2. The password is hashed using `Flask-Bcrypt` and stored in the database.
3. The user logs in and accesses a protected dashboard.
4. When the user saves a journal entry, the entry text is encrypted before persisting.
5. Encrypted content is stored in the database and only decrypted when needed.

### Data model

- `User` stores account metadata and relationships to entries.
- `DiaryEntry` stores encrypted content together with metadata like title, category, timestamp, and author.
- `Review` stores public reviews shown on the front page.

### Encryption model

- The app uses `Fernet` symmetric encryption from `cryptography`.
- Text content is encrypted server-side and stored as binary data.
- The current key is generated at runtime for demo purposes; a production deployment should load a persistent key from secure configuration.

## Security and Privacy

MindVault is designed to keep private data out of the cloud and away from third-party service providers.

### Current security protections

- Password hashing with `Flask-Bcrypt`
- Encrypted journal content using `Fernet`
- Protected pages with `Flask-Login`
- Local SQLite storage for easy self-hosting

### Important security notes

- This implementation is a prototype, not a fully hardened production system.
- The encryption key should be stored in an environment variable or secure key manager.
- Secrets and database files such as `.env`, `mindvault.db`, `database.db`, and other sensitive assets should be excluded from version control.

## Project Architecture

```
mindvault/
├─ app.py
├─ security.py
├─ requirements.txt
├─ README.md
├─ templates/
│  ├─ base.html
│  ├─ dashboard.html
│  ├─ entry.html
│  ├─ index.html
│  ├─ login.html
│  ├─ register.html
│  ├─ submit_review.html
├─ static/
│  ├─ css/style.css
│  ├─ js/main.js
├─ instance/
│  └─ mindvault.db
```

### File responsibilities

- `app.py` - main Flask application and route handlers.
- `security.py` - encryption helper utilities and key generation.
- `requirements.txt` - pinned Python dependencies for the environment.
- `templates/` - HTML views rendered by Flask.
- `static/` - styling and client-side behavior.
- `instance/` - SQLite database and other runtime-generated files.

## Getting Started

### Prerequisites

- Python 3.11 or later
- `pip` package manager
- Optional: `virtualenv` or `venv` for environment isolation

### Installation

```bash
git clone https://github.com/sinhaayush61426-ai/mindvault.git
cd mindvault
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open the app in a browser at:

```text
http://127.0.0.1:5000
```

### First-time setup

- Navigate to `/register` and create a new user.
- Use `/login` to sign in.
- Write entries from the dashboard and see them saved securely.

## Usage Guide

### Writing a reflection

- Add a title and category for your entry.
- Type freely in the journal content area.
- Save the entry to encrypt it and store it securely.

### Reviewing entries

- Your encrypted entries are displayed on the dashboard.
- The app currently displays entries in reverse chronological order so your latest reflections are easiest to access.

### Managing account access

- Log out anytime using the logout route.
- Because content is encrypted, the data remains protected while stored locally.

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
