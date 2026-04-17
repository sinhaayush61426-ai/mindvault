// MindVault Web Authentication API Mock for Biometric Login
// Simulates Touch ID / Face ID login experience

class BiometricAuth {
  constructor() {
    this.isAvailable = this.checkAvailability();
    this.credentials = [];
  }

  // Check if WebAuthn is available
  checkAvailability() {
    return window.PublicKeyCredential !== undefined &&
           navigator.credentials !== undefined;
  }

  // Register a new biometric credential
  async registerBiometric(username, displayName) {
    if (!this.isAvailable) {
      console.warn('WebAuthn not available on this device');
      return false;
    }

    try {
      const challengeArray = new Uint8Array(32);
      crypto.getRandomValues(challengeArray);

      const publicKeyOptions = {
        challenge: challengeArray,
        rp: {
          name: "MindVault",
          id: window.location.hostname,
        },
        user: {
          id: new Uint8Array(16),
          name: username,
          displayName: displayName,
        },
        pubKeyCredParams: [
          { alg: -7, type: "public-key" },  // ES256
          { alg: -257, type: "public-key" }  // RS256
        ],
        authenticatorSelection: {
          authenticatorAttachment: "platform",  // Use device's native authenticator
          userVerification: "preferred",
          residentKey: "preferred"
        },
        timeout: 60000,
        attestation: "direct"
      };

      const credential = await navigator.credentials.create({
        publicKey: publicKeyOptions
      });

      if (!credential) {
        throw new Error('Failed to create credential');
      }

      // Store credential locally
      this.credentials.push({
        id: credential.id,
        username: username,
        credentialPublicKey: credential.response.getPublicKey(),
        timestamp: new Date().toISOString()
      });

      // Save to localStorage (in production, send to server)
      this.saveCredentialsToStorage();
      
      console.log('✓ Biometric credential registered');
      return true;
    } catch (error) {
      console.error('Biometric registration failed:', error);
      return false;
    }
  }

  // Authenticate using biometric
  async authenticateBiometric() {
    if (!this.isAvailable) {
      console.warn('WebAuthn not available on this device');
      return false;
    }

    try {
      const challengeArray = new Uint8Array(32);
      crypto.getRandomValues(challengeArray);

      const publicKeyOptions = {
        challenge: challengeArray,
        timeout: 60000,
        userVerification: "preferred"
      };

      const assertion = await navigator.credentials.get({
        publicKey: publicKeyOptions
      });

      if (!assertion) {
        throw new Error('Authentication cancelled');
      }

      console.log('✓ Biometric authentication successful');
      return true;
    } catch (error) {
      console.error('Biometric authentication failed:', error);
      return false;
    }
  }

  // Save credentials to localStorage (simplified - use secure server storage in production)
  saveCredentialsToStorage() {
    try {
      localStorage.setItem('mindvault_biometric_creds', JSON.stringify(this.credentials));
    } catch (error) {
      console.warn('Could not save credentials to localStorage:', error);
    }
  }

  // Load credentials from localStorage
  loadCredentialsFromStorage() {
    try {
      const stored = localStorage.getItem('mindvault_biometric_creds');
      if (stored) {
        this.credentials = JSON.parse(stored);
      }
    } catch (error) {
      console.warn('Could not load credentials from localStorage:', error);
    }
  }

  // Check if user has registered biometric
  hasRegisteredBiometric(username) {
    return this.credentials.some(cred => cred.username === username);
  }

  // Remove biometric registration
  removeBiometric(username) {
    this.credentials = this.credentials.filter(cred => cred.username !== username);
    this.saveCredentialsToStorage();
    console.log(`✓ Removed biometric credential for ${username}`);
  }

  // Get device info
  getDeviceInfo() {
    return {
      platform: navigator.platform,
      userAgent: navigator.userAgent,
      webauthnSupported: this.isAvailable,
      touch: () => navigator.maxTouchPoints > 0,
      faceIdSupported: /Face ID|face_unlock|iris/.test(navigator.userAgent),
      touchIdSupported: /Touch ID|fingerprint/.test(navigator.userAgent)
    };
  }
}

// Initialize biometric auth
const biometricAuth = new BiometricAuth();
biometricAuth.loadCredentialsFromStorage();

// Export for use in templates
if (typeof module !== 'undefined' && module.exports) {
  module.exports = BiometricAuth;
}

// UI Integration
document.addEventListener('DOMContentLoaded', () => {
  // Show biometric button if available
  const biometricBtn = document.getElementById('biometric-login-btn');
  if (biometricBtn && biometricAuth.isAvailable) {
    biometricBtn.style.display = 'block';
    biometricBtn.addEventListener('click', handleBiometricLogin);
  }

  // Show biometric setup on registration form
  const bioRegisterBtn = document.getElementById('biometric-register-btn');
  if (bioRegisterBtn && biometricAuth.isAvailable) {
    bioRegisterBtn.style.display = 'block';
    bioRegisterBtn.addEventListener('click', handleBiometricSetup);
  }
});

async function handleBiometricLogin() {
  const btn = document.getElementById('biometric-login-btn');
  const originalText = btn.textContent;
  btn.textContent = 'Scanning...';
  btn.disabled = true;

  try {
    const success = await biometricAuth.authenticateBiometric();
    if (success) {
      btn.textContent = '✓ Authenticated!';
      setTimeout(() => {
        document.querySelector('form').submit();
      }, 600);
    } else {
      btn.textContent = 'Try Again';
      setTimeout(() => {
        btn.textContent = originalText;
        btn.disabled = false;
      }, 1500);
    }
  } catch (error) {
    console.error('Biometric login error:', error);
    btn.textContent = 'Failed - Try Again';
    setTimeout(() => {
      btn.textContent = originalText;
      btn.disabled = false;
    }, 1500);
  }
}

async function handleBiometricSetup() {
  const btn = document.getElementById('biometric-register-btn');
  const username = document.querySelector('input[name="username"]')?.value;
  
  if (!username) {
    alert('Please enter a username first');
    return;
  }

  const originalText = btn.textContent;
  btn.textContent = 'Setting up...';
  btn.disabled = true;

  try {
    const success = await biometricAuth.registerBiometric(username, username);
    if (success) {
      btn.textContent = '✓ Biometric Registered!';
      btn.style.borderColor = 'var(--clr-gold)';
      btn.style.color = 'var(--clr-gold)';
    } else {
      throw new Error('Registration failed');
    }
  } catch (error) {
    console.error('Biometric setup error:', error);
    btn.textContent = 'Failed - Try Again';
    setTimeout(() => {
      btn.textContent = originalText;
      btn.disabled = false;
    }, 1500);
  }
}
