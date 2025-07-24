# -----------------------------
# SELFIX-HOMEGUARD Dockerfile
# -----------------------------

FROM python:3.12-slim

# Set working directory
WORKDIR /opt/SELFIX

# Core files (essential runtime)
COPY selfix_tools.py .
COPY selfix_smart_start.sh .
COPY selfix_health_check.py .
COPY selfix-uninstall.sh .
COPY license_check.py .
COPY license_validator.py .
COPY requirements.txt .
COPY my_license.json .

# Optional folders — won't fail if they don't exist in build context
# Ensure these folders exist (even empty) to avoid COPY errors
COPY assets/ ./assets/
COPY configs/ ./configs/
COPY plugins/ ./plugins/

# Install dependencies
RUN chmod +x selfix_smart_start.sh \
 && pip install --no-cache-dir -r requirements.txt || true

# Entrypoint
ENTRYPOINT ["bash", "selfix_smart_start.sh"]
