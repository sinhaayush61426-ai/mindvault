// MindVault Main Application Script
// Handles Zen Mode, Service Worker, and UI enhancements

// --- SERVICE WORKER REGISTRATION ---
function registerServiceWorker() {
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', async () => {
      try {
        const registration = await navigator.serviceWorker.register('/service-worker.js', {
          scope: '/'
        });
        console.log('✓ Service Worker registered:', registration);

        // Check for updates periodically
        setInterval(() => {
          registration.update();
        }, 60000); // Check every minute

        // Handle service worker updates
        registration.addEventListener('updatefound', () => {
          const newWorker = registration.installing;
          newWorker.addEventListener('statechange', () => {
            if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
              console.log('✓ New Service Worker available - refresh recommended');
              showUpdateNotification();
            }
          });
        });
      } catch (error) {
        console.warn('Service Worker registration failed:', error);
      }
    });
  }
}

function showUpdateNotification() {
  const notification = document.createElement('div');
  notification.style.cssText = `
    position: fixed;
    bottom: 2rem;
    right: 2rem;
    background: rgba(91, 145, 255, 0.12);
    border: 2px solid var(--clr-cyan);
    border-radius: 8px;
    padding: 1.5rem;
    color: var(--clr-cyan);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    z-index: 10000;
    max-width: 300px;
  `;
  notification.innerHTML = `
    <div style="margin-bottom: 1rem;">✓ Update Available</div>
    <button onclick="location.reload()" style="
      background: var(--clr-cyan);
      color: #050608;
      border: none;
      padding: 0.5rem 1rem;
      border-radius: 4px;
      cursor: pointer;
      font-weight: 600;
      width: 100%;
    ">Refresh Now</button>
  `;
  document.body.appendChild(notification);
}

// --- ZEN MODE (FOCUS MODE) ---
class ZenMode {
  constructor() {
    this.isActive = false;
    this.wordCount = 0;
    this.characterCount = 0;
    this.initializeZenMode();
    this.loadZenPreference();
  }

  initializeZenMode() {
    const zenToggle = document.getElementById('zen-toggle');
    if (zenToggle) {
      zenToggle.addEventListener('click', () => this.toggleZenMode());
    }

    const textarea = document.querySelector('textarea[name="content"]');
    if (textarea) {
      textarea.addEventListener('input', () => this.updateWordCount(textarea));
      this.updateWordCount(textarea);
    }
  }

  toggleZenMode() {
    this.isActive = !this.isActive;
    document.documentElement.style.setProperty('--nav-height', this.isActive ? '0' : '80px');
    
    // Apply zen-mode class
    if (this.isActive) {
      document.body.classList.add('zen-mode');
      this.showZenUI();
    } else {
      document.body.classList.remove('zen-mode');
      this.hideZenUI();
    }

    // Save preference
    localStorage.setItem('mindvault_zen_mode', this.isActive);
  }

  showZenUI() {
    let counter = document.getElementById('zen-counter');
    if (!counter) {
      counter = document.createElement('div');
      counter.id = 'zen-counter';
      counter.className = 'zen-counter';
      document.body.appendChild(counter);
    }
    counter.style.display = 'block';

    let toggleBtn = document.getElementById('zen-toggle');
    if (!toggleBtn) {
      toggleBtn = document.createElement('button');
      toggleBtn.id = 'zen-toggle';
      toggleBtn.className = 'zen-toggle-btn';
      toggleBtn.textContent = 'Exit Zen';
      toggleBtn.addEventListener('click', () => this.toggleZenMode());
      document.body.appendChild(toggleBtn);
    }
    toggleBtn.textContent = 'Exit Zen';
  }

  hideZenUI() {
    const counter = document.getElementById('zen-counter');
    const toggleBtn = document.getElementById('zen-toggle');
    if (counter) counter.style.display = 'none';
    if (toggleBtn) toggleBtn.textContent = 'Zen Mode';
  }

  updateWordCount(textarea) {
    const text = textarea.value.trim();
    this.wordCount = text === '' ? 0 : text.split(/\s+/).length;
    this.characterCount = text.length;

    const counter = document.getElementById('zen-counter');
    if (counter) {
      counter.innerHTML = `
        <div>Words: <strong>${this.wordCount}</strong></div>
        <div>Characters: <strong>${this.characterCount}</strong></div>
      `;
    }
  }

  loadZenPreference() {
    const savedPref = localStorage.getItem('mindvault_zen_mode') === 'true';
    if (savedPref) {
      this.isActive = true;
      document.body.classList.add('zen-mode');
      this.showZenUI();
    }
  }
}

// --- DRAFT AUTO-SAVE ---
class DraftAutoSave {
  constructor() {
    this.form = document.querySelector('form[data-autosave-url]');
    if (!this.form) return;

    this.saveInterval = 30000;
    this.isDirty = false;
    this.pendingSave = null;
    this.allowNextSubmit = false;
    this.lastSavedValue = this.currentValue();
    this.initializeAutoSave();
  }

  initializeAutoSave() {
    this.form.addEventListener('input', () => {
      this.isDirty = true;
    });
    this.form.addEventListener('focusout', () => this.saveDraft());
    window.setInterval(() => this.saveDraft(), this.saveInterval);

    this.form.addEventListener('submit', (event) => {
      if (this.allowNextSubmit) {
        this.allowNextSubmit = false;
        return;
      }

      const save = this.saveDraft();
      if (!save) return;

      event.preventDefault();
      const submitter = event.submitter;
      save.finally(() => {
        this.allowNextSubmit = true;
        if (submitter) {
          this.form.requestSubmit(submitter);
        } else {
          this.form.requestSubmit();
        }
      });
    });
  }

  currentValue() {
    const formData = new FormData(this.form);
    return JSON.stringify({
      title: formData.get('title') || '',
      content: formData.get('content') || '',
      category: formData.get('category') || 'General'
    });
  }

  saveDraft() {
    if (this.pendingSave) return this.pendingSave;
    const savedValue = this.currentValue();
    if (!this.isDirty || savedValue === this.lastSavedValue) {
      this.isDirty = false;
      return null;
    }

    const title = this.form.elements.namedItem('title');
    const content = this.form.elements.namedItem('content');
    const category = this.form.elements.namedItem('category');
    const csrfToken = this.form.querySelector('[name="csrfmiddlewaretoken"]')?.value;
    if (!title || !content || !csrfToken) {
      this.showSaveIndicator('Automatic save is unavailable. Save your changes manually.');
      return null;
    }

    const body = new FormData();
    body.set('title', title.value);
    body.set('content', content.value);
    body.set('category', category?.value || 'General');
    const entryId = this.form.dataset.entryId;
    const draftId = this.form.elements.namedItem('draft_id')?.value;
    if (entryId) body.set('entry_id', entryId);
    if (draftId) body.set('draft_id', draftId);

    this.pendingSave = (async () => {
      try {
        const response = await fetch(this.form.dataset.autosaveUrl, {
          method: 'POST',
          credentials: 'same-origin',
          headers: {'X-CSRFToken': csrfToken},
          body
        });

        if (response.status === 204) {
          this.lastSavedValue = savedValue;
          this.isDirty = this.currentValue() !== savedValue;
          this.showSaveIndicator('Your changes are saved in the encrypted vault.');
          return true;
        }

        const contentType = response.headers.get('content-type') || '';
        if (!contentType.includes('application/json')) {
          throw new Error('The server did not return a save confirmation.');
        }
        const result = await response.json();
        if (!response.ok) {
          throw new Error(result.error || 'The server rejected the draft.');
        }

        if (result.draft_id) {
          const draftIdInput = this.form.elements.namedItem('draft_id');
          if (draftIdInput) draftIdInput.value = result.draft_id;
        }
        this.lastSavedValue = savedValue;
        this.isDirty = this.currentValue() !== savedValue;
        this.showSaveIndicator('Your changes are saved in the encrypted vault.');
        return true;
      } catch (error) {
        console.error('MindVault could not save the current draft.', error);
        this.isDirty = true;
        this.showSaveIndicator('Automatic save failed. Save manually and check your connection.');
        return false;
      } finally {
        this.pendingSave = null;
      }
    })();

    return this.pendingSave;
  }

  showSaveIndicator(message) {
    const indicator = document.getElementById('save-indicator');
    if (indicator) indicator.textContent = message;
  }
}

// --- CHARACTER MATRIX UI ---
class CharacterMatrix {
  constructor() {
    this.initializeCharacterGrid();
  }

  initializeCharacterGrid() {
    const characterCards = document.querySelectorAll('.character-card');
    characterCards.forEach(card => {
      card.addEventListener('click', (e) => {
        if (!e.target.classList.contains('character-btn')) {
          this.selectCharacter(card);
        }
      });
    });
  }

  selectCharacter(card) {
    document.querySelectorAll('.character-card').forEach(c => c.classList.remove('active'));
    card.classList.add('active');
  }
}

// --- SNAPSHOT MANAGEMENT ---
class SnapshotManager {
  constructor() {
    this.initializeSnapshotUI();
  }

  initializeSnapshotUI() {
    const snapshotBtn = document.getElementById('create-snapshot-btn');
    if (snapshotBtn) {
      snapshotBtn.addEventListener('click', () => this.promptSnapshotVersion());
    }
  }

  promptSnapshotVersion() {
    const version = prompt('Enter snapshot version (e.g., 1.1, 2.0):', '1.0');
    if (version) {
      const description = prompt('Optional snapshot description:');
      this.createSnapshot(version, description);
    }
  }

  createSnapshot(version, description) {
    const form = document.getElementById('snapshot-form');
    if (form) {
      const versionInput = document.createElement('input');
      versionInput.type = 'hidden';
      versionInput.name = 'version';
      versionInput.value = version;

      const descInput = document.createElement('input');
      descInput.type = 'hidden';
      descInput.name = 'description';
      descInput.value = description || '';

      form.appendChild(versionInput);
      form.appendChild(descInput);
      form.submit();
    }
  }
}

// --- FLASH MESSAGE AUTO-DISMISS ---
function setupFlashMessageDismissal() {
  const flashMessages = document.querySelectorAll('.flash');
  
  flashMessages.forEach(flash => {
    if (
      flash.classList.contains('flash-error') ||
      flash.classList.contains('flash-warning')
    ) {
      return;
    }

    setTimeout(() => {
      flash.style.opacity = '0';
      flash.style.transform = 'translateX(420px)';
      flash.style.transition = 'all 0.3s ease';
      
      // Remove from DOM after animation completes
      setTimeout(() => {
        flash.remove();
      }, 300);
    }, 3500); // 3.5 seconds
  });
}

// --- BIOMETRIC AUTH UI ---
function setupBiometricUI() {
  const deviceInfo = biometricAuth.getDeviceInfo();
  
  if (deviceInfo.webauthnSupported) {
    const bioContainer = document.getElementById('biometric-container');
    if (bioContainer) {
      let methodText = 'Biometric';
      if (deviceInfo.faceIdSupported) methodText = 'Face ID';
      if (deviceInfo.touchIdSupported) methodText = 'Touch ID';

      bioContainer.innerHTML = `
        <p style="color: var(--text-muted); margin-bottom: 1rem;">Or use ${methodText}</p>
        <button type="button" id="biometric-login-btn" class="btn btn-secondary" style="display: none; width: 100%;">
          🔐 ${methodText} Login
        </button>
      `;
    }
  }
}

// --- GLOBAL INITIALIZATION ---
document.addEventListener('DOMContentLoaded', () => {
  // Setup Flash Message Auto-Dismiss
  setupFlashMessageDismissal();

  // Register Service Worker
  registerServiceWorker();

  // Initialize Zen Mode
  const zenMode = new ZenMode();
  window.zenMode = zenMode;

  // Initialize encrypted server-side draft saving
  const autoSave = new DraftAutoSave();
  window.autoSave = autoSave;

  // Initialize Character Matrix
  const charMatrix = new CharacterMatrix();
  window.charMatrix = charMatrix;

  // Initialize Snapshot Manager
  const snapshotMgr = new SnapshotManager();
  window.snapshotMgr = snapshotMgr;

  // Setup Biometric UI
  setupBiometricUI();

  // Log app version
  console.log('✓ MindVault v2.0 Loaded with PWA support');
});

// Handle online/offline status
window.addEventListener('online', () => {
  console.log('✓ Connection restored');
  document.body.style.opacity = '1';
});

window.addEventListener('offline', () => {
  console.log('⚠ Connection lost - offline mode active');
  document.body.style.opacity = '0.8';
});
