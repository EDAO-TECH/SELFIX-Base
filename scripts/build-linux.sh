#!/bin/bash

echo "📦 Building SELFIX HomeGuard package for Linux..."

# Variables
APP_NAME="SELFIX_HomeGuard"
VERSION="1.0.0"
BUILD_DIR="build/linux"
PACKAGE_NAME="${APP_NAME}_v${VERSION}_linux"

# Clean previous build
rm -rf "$BUILD_DIR"
mkdir -p "$BUILD_DIR/$APP_NAME"

# Copy necessary files
cp selfix_installer.py "$BUILD_DIR/$APP_NAME/"
cp license_validator.py "$BUILD_DIR/$APP_NAME/"
cp license_check.py "$BUILD_DIR/$APP_NAME/"
cp -r assets "$BUILD_DIR/$APP_NAME/"
cp install_full.sh "$BUILD_DIR/$APP_NAME/"
cp selfix-uninstall.sh "$BUILD_DIR/$APP_NAME/"
cp bootstrap_selfix.py "$BUILD_DIR/$APP_NAME/"

# Optional: include license file
echo "⚠️ Remember: Do NOT include 'my_license.json' in production."
# cp my_license.json "$BUILD_DIR/$APP_NAME/"

# Create zip package
cd "$BUILD_DIR"
zip -r "${PACKAGE_NAME}.zip" "$APP_NAME" > /dev/null
cd ../../

echo "✅ Package created at: $BUILD_DIR/${PACKAGE_NAME}.zip"
