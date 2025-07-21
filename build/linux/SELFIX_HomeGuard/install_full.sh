#!/bin/bash

echo "🛠️ Starting SELFIX HomeGuard Installation..."

# Root check
if [ "$EUID" -ne 0 ]; then
  echo "❌ Please run as root or with sudo."
  exit 1
fi

# Target installation dir
INSTALL_DIR="/opt/SELFIX"
BIN_PATH="/usr/local/bin/selfix"

# Step 1: Create directory
mkdir -p "$INSTALL_DIR"
echo "📁 Created install directory at $INSTALL_DIR"

# Step 2: Copy core files
cp selfix_installer.py "$INSTALL_DIR/"
cp license_validator.py "$INSTALL_DIR/"
cp license_check.py "$INSTALL_DIR/"
cp -r assets "$INSTALL_DIR/"
echo "📄 Copied installer and assets"

# Step 3: (Optional) Create CLI launcher
cat > "$BIN_PATH" <<EOF
#!/bin/bash
python3 $INSTALL_DIR/selfix_installer.py "\$@"
EOF
chmod +x "$BIN_PATH"
echo "🔗 CLI launcher installed: type 'selfix' to run"

# Step 4: Dependencies
echo "📦 Installing Python dependencies (if required)..."
pip3 install --upgrade pip
pip3 install pyinstaller > /dev/null 2>&1

echo "✅ SELFIX HomeGuard installed successfully."
