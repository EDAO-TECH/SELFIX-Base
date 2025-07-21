#!/usr/bin/env python3

import json
import os
import platform
import hashlib
import sys
from datetime import datetime

def get_license_path():
    if platform.system() == "Windows":
        return "C:\\SELFIX\\license.json"
    return os.path.expanduser("~/.selfix/license.json")

def read_license(path=None):
    path = path or get_license_path()
    if not os.path.exists(path):
        raise FileNotFoundError(f"❌ License file not found at: {path}")
    
    with open(path, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            raise ValueError("❌ Malformed license.json")

def verify_signature(license_data):
    # Simplified hash-based check for example; use real public key sig in prod
    signature = license_data.get("signature", "")
    temp = dict(license_data)
    temp.pop("signature", None)
    expected = hashlib.sha256(json.dumps(temp, sort_keys=True).encode()).hexdigest()
    return signature == f"sha256:{expected}"

def check_expiry(license_data):
    expiry_str = license_data.get("valid_until", "1970-01-01")
    try:
        expiry = datetime.strptime(expiry_str, "%Y-%m-%d")
        return datetime.utcnow() <= expiry
    except ValueError:
        raise ValueError("❌ Invalid license expiry format")

def check_module_enabled(license_data, module_key):
    return license_data.get("modules", {}).get(module_key, False)

def validate_license(path=None):
    try:
        data = read_license(path)
        if not verify_signature(data):
            return (False, "⚠️ Invalid signature.")
        if not check_expiry(data):
            return (False, "❌ License has expired.")
        return (True, data)
    except Exception as e:
        return (False, str(e))
