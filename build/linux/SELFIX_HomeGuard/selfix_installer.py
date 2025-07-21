#!/usr/bin/env python3

import platform
import subprocess
import os
import sys
import argparse
import json
from datetime import datetime

# --- Constants ---
BASE_DIR = "/opt/SELFIX"
INSTALL_FULL_SYSTEM = os.path.join(BASE_DIR, "install_full.sh")
INSTALL_WIN = os.path.join(BASE_DIR, "install_win.ps1")
INSTALL_UNINSTALL = os.path.join(BASE_DIR, "selfix-uninstall.sh")
BOOTSTRAP_SCRIPT = os.path.join(BASE_DIR, "bootstrap_selfix.py")
LOCAL_INSTALL = "./install_full.sh"
LICENSE_PATH_LINUX = os.path.expanduser("~/.selfix/license.json")
LICENSE_PATH_WIN = "C:\\SELFIX\\license.json"


# --- Utilities ---
def detect_os():
    return platform.system()

def install_selfix():
    os_type = detect_os()
    print(f"🛠️ Detected platform: {os_type}")

    if os_type in ["Linux", "Darwin"]:
        # Fallback to local script if system path missing
        script = INSTALL_FULL_SYSTEM if os.path.exists(INSTALL_FULL_SYSTEM) else LOCAL_INSTALL
        if not os.path.exists(script):
            print(f"❌ Installer not found at: {script}")
            sys.exit(1)
        subprocess.run(["sudo", "bash", script], check=True)

    elif os_type == "Windows":
        if not os.path.exists(INSTALL_WIN):
            print("❌ Windows install script missing.")
            sys.exit(1)
        subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", INSTALL_WIN], check=True)

    else:
        print(f"❌ Unsupported OS: {os_type}")
        sys.exit(1)


def activate_license(license_file=None):
    print("🔐 Activating SELFIX license...")

    if not license_file:
        license_file = input("📄 Enter path to license.json: ").strip()

    if not os.path.exists(license_file):
        print(f"❌ License file not found at: {license_file}")
        sys.exit(1)

    try:
        with open(license_file, 'r') as f:
            license_data = json.load(f)
    except json.JSONDecodeError:
        print("❌ Invalid license.json format.")
        sys.exit(1)

    os_type = detect_os()
    target = LICENSE_PATH_WIN if os_type == "Windows" else LICENSE_PATH_LINUX
    os.makedirs(os.path.dirname(target), exist_ok=True)

    with open(target, 'w') as f:
        json.dump(license_data, f, indent=2)

    print(f"✅ License successfully saved to: {target}")


def uninstall_selfix():
    print("��️ Uninstalling SELFIX...")

    if not os.path.exists(INSTALL_UNINSTALL):
        print("❌ Uninstall script not found.")
        sys.exit(1)

    subprocess.run(["sudo", "bash", INSTALL_UNINSTALL], check=True)
    print("✅ SELFIX has been uninstalled.")


def repair_selfix():
    if not os.path.exists(BOOTSTRAP_SCRIPT):
        print("❌ Repair/bootstrap script not found.")
        sys.exit(1)
    subprocess.run(["python3", BOOTSTRAP_SCRIPT, "--repair"], check=True)
    print("✅ Repair process complete.")


# --- Main Entry ---
def main():
    parser = argparse.ArgumentParser(description="SELFIX Unified Installer")
    parser.add_argument('--activate', help='Activate license with license.json path', nargs='?', const=True)
    parser.add_argument('--uninstall', action='store_true', help='Uninstall SELFIX')
    parser.add_argument('--repair', action='store_true', help='Repair SELFIX system')

    args = parser.parse_args()

    if args.activate:
        activate_license(license_file=args.activate if isinstance(args.activate, str) else None)
    elif args.uninstall:
        uninstall_selfix()
    elif args.repair:
        repair_selfix()
    else:
        install_selfix()


if __name__ == "__main__":
    print("🛡️ Welcome to the SELFIX™ Unified Installer by EDAO-TECH")
    main()
