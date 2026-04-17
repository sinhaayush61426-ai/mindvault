# MindVault v2.0 Migration Guide

## For Existing Users

### What You Need to Do

**Almost Nothing!** MindVault v2.0 is fully backward compatible. Your existing entries and account are completely safe and unchanged.

### What Happens Automatically

1. **Character Matrix**: New empty matrix created for you (no action needed)
2. **Service Worker**: Automatically installs on first use
3. **Draft Auto-Save**: Starts saving your drafts automatically
4. **PWA**: Can install anytime from browser menu
5. **Biometric**: Optionally set up on login/register

### Breaking Changes

**None!** All existing features work exactly as before.

---

## For Developers / Self-Hosted Instances

### Database Migration

New tables required:

```bash
# These are created automatically on first run
# But you can pre-create if needed:

cd /path/to/mindvault
python3
>>> from app import app, db
>>> app.app_context().push()
>>> db.create_all()
>>> exit()
```

### File Changes

**New files to deploy:**
```
manifest.json
templates/
  - characters.html
  - character_form.html
  - snapshots.html
  - view_entry.html
  - offline.html
static/css/
  - expansion.css
static/js/
  - service-worker.js
  - biometric-auth.js
  - enhanced-main.js
static/
  - svg-icons.html
```

**Modified files:**
```
app.py                (new models + routes)
templates/base.html   (new links + scripts)
static/css/style.css  (new CSS variables)
```

### Installation Steps for Fresh/Existing Deploy

1. **Backup existing database** (if upgrading)
   ```bash
   cp instance/mindvault.db instance/mindvault.db.backup
   ```

2. **Update code**
   ```bash
   git pull origin main
   # or update files manually
   ```

3. **Create new tables**
   ```bash
   python3 -c "
   from app import app, db
   app.app_context().push()
   db.create_all()
   print('✓ Database ready')
   "
   ```

4. **Test application**
   ```bash
   python3 app.py
   # Visit http://localhost:5000
   # Test features: Characters, Snapshots, Zen Mode
   ```

5. **Install PWA (mobile testing)**
   - Use DevTools device emulation
   - Or test on actual mobile device

### Environment Variables (No Changes)

Continue using existing `.env` or configuration:
```
SECRET_KEY=your_key
DATABASE_URL=sqlite:///mindvault.db  # unchanged
DEBUG=False  # recommended for production
```

### Breaking API Changes

**None!** Existing API routes remain unchanged:
- `/` - homepage
- `/login`, `/register` - authentication
- `/dashboard` - vault view
- `/save-entry` - create entry

**New routes added** (non-breaking):
- `/characters` - character management
- `/character/new`, `/edit`, `/delete` - CRUD operations
- `/entry/<id>/snapshot` - create version
- `/entry/<id>/snapshots` - view versions
- `/entry/<id>` - view entry detail

### Dependency Changes

**No new dependencies!** All new features use:
- **Backend**: Existing Flask/SQLAlchemy
- **Frontend**: Browser APIs (Service Workers, Web Authentication, IndexedDB)

All expansions use zero external JavaScript libraries.

### Rollback Plan (If Issues)

If you need to revert to v1.0:

```bash
# Preserve new data
cp instance/mindvault.db instance/mindvault-v2.db

# Restore old version
git checkout v1.0
# or restore files from backup

# Old database still works (new tables ignored)
python3 app.py
```

The application will function normally without new features but v2.0 data is safely stored.

---

## Troubleshooting Migration

### Issue: "No such table: character"

**Solution**: Database schema not updated
```python
from app import app, db
with app.app_context():
    db.create_all()
```

### Issue: Service Worker not loading

**Solution**: 
- Clear browser cache: DevTools → Application → Clear site data
- Check `/static/js/service-worker.js` exists
- Verify HTTPS/localhost (required for Service Workers)

### Issue: Characters page shows 404

**Solution**:
- Confirm `app.py` has been updated with character routes
- Check `/characters` route exists: `grep "def characters" app.py`
- Restart Flask application

### Issue: Manifest not found

**Solution**:
- Verify `manifest.json` exists in project root
- Check `base.html` link tag: `<link rel="manifest" href="{{ url_for('static', filename='../manifest.json') }}">`
- Manifest must be web-accessible at `/manifest.json`

### Issue: Existing entries not visible

**Solution**:
- Old entries still exist in database
- Check user is logged in to same account
- Verify `DiaryEntry` table not corrupted (backup + restore if needed)

---

## Performance Considerations

### New Feature Impact

| Feature | Storage | Load Latency | Notes |
|---------|---------|--------------|-------|
| Character Matrix | ~5KB per character | <50ms | Minimal |
| Snapshots | Varies (duplicates content) | <10ms | Plan for storage |
| Zen Mode | 0 additional storage | Instant | Pure CSS |
| PWA/Service Worker | ~100KB cache | First load only | Improves on repeat |
| Biometric Auth | 0 server storage | Instant | Device-native |

### Recommendations

1. **Database Size**: Each snapshot duplicates encrypted entry content
   - Typical: 100 entries × 5 snapshots each = moderate growth
   - Monitor `database.db` size
   - Plan backup strategy

2. **Browser Cache**: Service Worker caches ~100KB of assets
   - Should be fine for most modern devices
   - Consider target device specifications

3. **Auto-Save**: Triggers every 30 seconds
   - Light operation (LocalStorage write)
   - Browser throttling handles optimization automatically

---

## Feature Enablement

All v2.0 features are enabled by default. To disable specific features, modify `base.html`:

### Disable Zen Mode
```html
<!-- Comment out in base.html -->
<!-- <script src="{{ url_for('static', filename='js/enhanced-main.js') }}"></script> -->
```

### Disable Service Worker
```javascript
// In enhanced-main.js, comment out:
// registerServiceWorker();
```

### Disable Biometric Auth
```html
<!-- Remove from base.html -->
<!-- <script src="{{ url_for('static', filename='js/biometric-auth.js') }}"></script> -->
```

### Disable Character Matrix
```python
# In app.py, comment out character routes:
# @app.route('/characters')
# def characters():
```

---

## Production Checklist

Before deploying v2.0 to production:

- [ ] Database properly migrated with new tables
- [ ] All new files deployed to server
- [ ] SSL/HTTPS enabled (required for Service Workers)
- [ ] Manifest URL accessible at `/manifest.json`
- [ ] Service Worker script accessible at `/static/js/service-worker.js`
- [ ] Existing user data backed up
- [ ] Tested character creation/editing
- [ ] Tested snapshot restoration
- [ ] Tested Zen Mode on intended browsers
- [ ] PWA installs correctly on mobile
- [ ] Biometric auth tested on supported device
- [ ] Network offline scenarios tested
- [ ] Performance acceptable on target devices
- [ ] No console errors or warnings

---

## Support

For migration issues:
1. Check this guide and EXPANSION.md
2. Review application logs: `tail -f app.log`
3. Check browser console for JavaScript errors
4. Verify database integrity: `sqlite3 database.db "PRAGMA integrity_check;"`

---

**Upgrade Version**: 1.0 → 2.0  
**Estimated Time**: <5 minutes  
**Complexity**: Low  
**Risk**: None (fully backward compatible)
