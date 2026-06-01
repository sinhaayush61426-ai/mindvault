# 🚀 MindVault Setup Guide - Quick Start

**Problem Found:** Missing Python dependencies (Flask, Flask-Login, etc.)

---

## ✅ Solution: Install Dependencies

### Step 1: Install Required Packages

Run this command in your terminal:

```bash
pip install -r requirements.txt
```

**What it does:**
- Installs Flask web framework
- Installs Flask-SQLAlchemy (database ORM)
- Installs Flask-Login (session management)
- Installs Flask-Bcrypt (password hashing)
- Installs cryptography (encryption)
- Plus 30+ other dependencies

**Time required:** 2-5 minutes (depending on internet speed)

### Step 2: Verify Installation

```bash
python3 -c "import flask; print(f'✅ Flask {flask.__version__} installed')"
```

**Expected output:** `✅ Flask 3.1.3 installed`

### Step 3: Run the Application

```bash
python3 app.py
```

**Expected output:**
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

---

## 📋 Missing Dependencies Error Explained

**Error:** `ModuleNotFoundError: No module named 'flask_login'`

**Cause:** Python can't find the Flask-Login package

**Why it happened:**
1. Fresh workspace/installation
2. Dependencies not yet installed
3. Virtual environment not activated (if using one)

**Fixed by:** Running `pip install -r requirements.txt`

---

## 🎯 Core Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| Flask | 3.1.3 | Web framework |
| Flask-SQLAlchemy | 3.1.1 | Database ORM |
| Flask-Login | 0.6.3 | Session management |
| Flask-Bcrypt | 1.0.1 | Password hashing |
| cryptography | 42.0.2 | Fernet encryption |
| Pillow | 10.0.0 | Image processing |

---

## ⚠️ Common Issues

### Issue: "pip command not found"
**Solution:** Use `pip3` instead:
```bash
pip3 install -r requirements.txt
```

### Issue: "Permission denied"
**Solution:** Add `--user` flag:
```bash
pip install --user -r requirements.txt
```

### Issue: Takes very long to install
**Solution:** This is normal for first install. Be patient or use `-q` for quiet mode:
```bash
pip install -q -r requirements.txt
```

---

## ✅ After Installation

Once dependencies are installed:

1. ✅ Run `python3 app.py`
2. ✅ Open `http://127.0.0.1:5000` in browser
3. ✅ Register a new account
4. ✅ Start creating encrypted entries

---

## 📚 Additional Help

**In terminal, to see what's installed:**
```bash
pip list | grep -i flask
```

**To uninstall and start fresh:**
```bash
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

**To check specific package:**
```bash
python3 -c "import flask_login; print('✅ Flask-Login installed')"
```

---

**Status:** 🟢 Ready to install  
**Time to fix:** < 5 minutes
