// MindVault Main Application Script
// Handles Zen Mode, Service Worker, and UI enhancements

// --- SERVICE WORKER REGISTRATION ---
function registerServiceWorker() {
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', async () => {
      try {
        const registration = await navigator.serviceWorker.register('/static/js/service-worker.js', {
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
    background: rgba(0, 242, 255, 0.12);
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
    this.saveInterval = 30000; // 30 seconds
    this.initializeAutoSave();
  }

  initializeAutoSave() {
    const textarea = document.querySelector('textarea[name="content"]');
    const titleInput = document.querySelector('input[name="title"]');
    
    if (textarea || titleInput) {
      setInterval(() => this.saveDraft(), this.saveInterval);
      
      // Also save on blur
      if (textarea) textarea.addEventListener('blur', () => this.saveDraft());
      if (titleInput) titleInput.addEventListener('blur', () => this.saveDraft());
    }
  }

  saveDraft() {
    const textarea = document.querySelector('textarea[name="content"]');
    const titleInput = document.querySelector('input[name="title"]');
    
    if (!textarea || !titleInput) return;

    const draft = {
      title: titleInput.value,
      content: textarea.value,
      timestamp: new Date().toISOString()
    };

    localStorage.setItem('mindvault_draft', JSON.stringify(draft));
    this.showSaveIndicator();
  }

  showSaveIndicator() {
    let indicator = document.getElementById('save-indicator');
    if (!indicator) {
      indicator = document.createElement('div');
      indicator.id = 'save-indicator';
      indicator.style.cssText = `
        position: fixed;
        bottom: 1.5rem;
        left: 1.5rem;
        background: rgba(0, 242, 255, 0.12);
        border: 1px solid var(--clr-cyan);
        color: var(--clr-cyan);
        padding: 0.75rem 1.5rem;
        border-radius: 4px;
        font-size: 0.85rem;
        z-index: 999;
      `;
      document.body.appendChild(indicator);
    }

    indicator.textContent = '✓ Draft saved';
    indicator.style.opacity = '1';

    setTimeout(() => {
      indicator.style.opacity = '0';
    }, 2000);
  }

  loadDraft() {
    const savedDraft = localStorage.getItem('mindvault_draft');
    if (savedDraft) {
      const draft = JSON.parse(savedDraft);
      const textarea = document.querySelector('textarea[name="content"]');
      const titleInput = document.querySelector('input[name="title"]');
      
      if (textarea) textarea.value = draft.content;
      if (titleInput) titleInput.value = draft.title;
      
      console.log('✓ Draft loaded from auto-save');
    }
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
  // Register Service Worker
  registerServiceWorker();

  // Initialize Zen Mode
  const zenMode = new ZenMode();
  window.zenMode = zenMode;

  // Initialize Auto-Save
  const autoSave = new DraftAutoSave();
  autoSave.loadDraft();
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
