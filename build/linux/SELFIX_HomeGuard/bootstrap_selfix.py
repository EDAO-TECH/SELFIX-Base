#!/usr/bin/env python3

import os
import shutil
import json
import sys
from pathlib import Path

INSTALL_DIR = "/opt/SELFIX"
LICENSE_PATH = os.path.expanduser("~/.selfix/license.json")

def reset_config():
    print("🔁 Resetting configuration...")
    # Placeholder: config.json reset
    config_path = os.path.join(INSTALL_DIR, "config.json")
    if os.path.exists(config_path):
        os.remove(config_path)
        print("🧹 config.json removed.")
    else:
        print("ℹ️ No config found.")

def reset_license():
    print("🔐 Removing local license...")
    if os.path.exists(LICENSE_PATH):
        os.remove(LICENSE_PATH)
        print("✅ License removed.")
    else:
        print("ℹ️ No license found.")

def main():
    if "--repair" in sys.argv:
        print("🛠️ Running SELFIX repair utility...")
        reset_config()
        reset_license()
        print("✅ Repair complete.")
    else:
        print("Usage: python3 bootstrap_selfix.py --repair")

if __name__ == "__main__":
    main()
