#!/bin/bash

echo "🔧 Creating full SELFIX HomeGuard project structure..."

# Core folders
mkdir -p scripts
mkdir -p frontend/src
mkdir -p frontend/public
mkdir -p assets
mkdir -p ~/.selfix

# Core placeholder files
touch install_full.sh
touch install_win.ps1
touch selfix-uninstall.sh
touch bootstrap_selfix.py
touch license_check.py
touch license_validator.py
touch selfix_installer.py
touch .gitignore
touch netlify.toml
touch README.md
touch frontend/package.json
touch frontend/vite.config.ts
touch assets/logo.png
touch scripts/build-linux.sh
touch scripts/build-mac.sh
touch scripts/build-win.bat

# Add license file
cat > ~/.selfix/license.json <<EOF
{
  "tier": "homeguard",
  "modules": {
    "antivirus": false,
    "vpn": false,
    "rollback": "1_day",
    "vault": false,
    "seeder": false
  },
  "valid_until": "2026-01-01",
  "signature": "sha256:e7b0d8a546f26b88a8a6f5f0a9c3f6c25cb37d647f56df9b71be3b7b44586a03"
}
EOF

echo "✅ All folders and placeholder files created."
echo "📁 License file saved to ~/.selfix/license.json"
