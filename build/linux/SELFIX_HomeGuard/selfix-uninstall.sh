#!/bin/bash

echo "🗑️ Uninstalling SELFIX HomeGuard..."

# Confirm
read -p "Are you sure? This will delete all SELFIX files. (y/N): " confirm
if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
    echo "❌ Uninstall canceled."
    exit 1
fi

# Paths
INSTALL_DIR="/opt/SELFIX"
BIN_PATH="/usr/local/bin/selfix"
LICENSE_FILE="$HOME/.selfix/license.json"

# Remove
rm -rf "$INSTALL_DIR"
rm -f "$BIN_PATH"
rm -f "$LICENSE_FILE"

echo "✅ SELFIX HomeGuard uninstalled completely."
