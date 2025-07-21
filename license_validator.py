import json
import hashlib
import os
from datetime import datetime

LICENSE_PATH = os.path.join(os.path.dirname(__file__), "my_license.json")

def load_license(path=LICENSE_PATH):
    if not os.path.exists(path):
        raise FileNotFoundError(f"License file not found at: {path}")

    with open(path, "r") as f:
        data = json.load(f)
    return data

def validate_signature(license_data):
    original_sig = license_data.get("signature")
    if not original_sig:
        return False

    copy = license_data.copy()
    del copy["signature"]

    expected_sig = hashlib.sha256(json.dumps(copy, sort_keys=True).encode('utf-8')).hexdigest()
    return expected_sig == original_sig

def validate_expiry(license_data):
    today = datetime.today().date()
    expiry = datetime.strptime(license_data["valid_until"], "%Y-%m-%d").date()
    return today <= expiry

def validate_machine(license_data, machine_hash):
    return license_data["machine_hash"] == machine_hash

def validate_license(machine_hash):
    try:
        license_data = load_license()
        if not validate_signature(license_data):
            return False, "Invalid license signature."
        if not validate_expiry(license_data):
            return False, "License expired."
        if not validate_machine(license_data, machine_hash):
            return False, "This license is not valid for this machine."
        return True, f"License OK: {license_data['tier']} for {license_data['issued_to']}"
    except Exception as e:
        return False, f"License validation failed: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Replace with dynamic machine ID logic if needed
    machine_hash = "d34db33f92cdeabc"
    valid, message = validate_license(machine_hash)
    if valid:
        print("✅", message)
    else:
        print("❌", message)
