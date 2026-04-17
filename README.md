# MindVault

MindVault is a privacy-first digital journaling and emotional reflection platform built for secure self-expression.

It is designed to provide a psychologically safe, distraction-free space for introspection with a minimal dark aesthetic and server-side encryption. MindVault is intended as an open-source sanctuary for mental wellness, long-term reflection, and private journaling.

## What MindVault Is

MindVault is:

- A secure, encrypted journal powered by Flask and SQLite.
- A private place for reflections, mood tracking, and self-awareness.
- A minimal interface that reduces cognitive load and encourages consistent writing.
- A foundation for future local NLP sentiment analysis, emotional dashboards, and time-locked letters.

## What MindVault Is Not

- It is not a deployed production-ready service yet.
- It does not currently rely on external AI APIs to analyze private content.
- It is not a substitute for professional mental health care.

## Core Concepts

### Privacy by Design

- User accounts are protected with password hashing using `Flask-Bcrypt`.
- Journal entries are encrypted in the database using `cryptography.Fernet`.
- The app avoids sending private journal content to third-party services.

### Minimal Dark UI

- The interface is designed to be calm and distraction-free.
- Dark mode and minimal styling help keep focus on reflection.

### Journal Vault

- Entries are stored behind a login wall and encrypted at rest.
- This creates a vault-like feeling for personal ideas, notes, and emotional processing.

## Features Included Today

- User registration and login
- Secure password hashing
- Encrypted diary entry storage
- Personal dashboard with an entry listing
- Review section on the home page
- SQLite database backend for easy local setup

## Future Enhancements

MindVault is poised for more advanced features such as:

- Local Natural Language Processing (NLP) sentiment analysis
- Emotional trend dashboards with charts and insights
- Time-locked "Letters to the Future"
- Smart vault access controls and optional recovery keys
- Secure export / backup of encrypted journals
- Multi-factor authentication and stronger key management

## Project Structure

- `app.py` - Flask application logic, user auth, entry creation, and database models
- `security.py` - Encryption utilities for text at rest
- `requirements.txt` - Python dependencies
- `templates/` - HTML templates for pages like login, register, dashboard, and reviews
- `static/` - CSS and JavaScript assets
- `instance/` - Local instance-specific data files

## Getting Started

### Prerequisites

- Python 3.11 or later
- `pip` package manager
- Optional: a virtual environment for isolation

### Install

1. Clone the repository:

```bash
git clone https://github.com/sinhaayush61426-ai/mindvault.git
cd mindvault
```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### Run MindVault

Start the application:

```bash
python app.py
```

Then open your browser at:

```text
http://127.0.0.1:5000
```

### Register and Use

1. Create a new account via `/register`.
2. Log in at `/login`.
3. Save journal entries from the dashboard.
4. Your content is encrypted before it is stored in `mindvault.db`.

## How It Works

- `Flask-Login` manages secure sessions and protected routes.
- `Flask-Bcrypt` hashes user passwords before storage.
- `cryptography.Fernet` encrypts journal content using a generated key.
- Entries are saved in an SQLite database (`mindvault.db`) in the project root.

## Notes on Security

- The current encryption key is generated at runtime for demonstration purposes.
- For production, store keys and secrets in environment variables or a secure vault.
- Add a `.gitignore` file to keep `.env`, database files, and other secrets outside version control.

## Contributing

Contributions are welcome. Suggested improvements include:

- Adding local NLP sentiment scoring
- Implementing graph-based emotion dashboards
- Expanding the entry model with tags, moods, and private prompts
- Building a time-locked letter feature
- Improving authentication and key storage

## License

This project is open source. Feel free to fork, experiment, and adapt MindVault for your own secure journaling workflow.
