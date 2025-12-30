# MedIntel Clinical AI Infrastructure Container
# Purpose: Non-inference runtime environment for governance, evaluation,
# validation, and audit tooling ONLY.
# This container MUST NOT execute autonomous clinical decisions.

FROM python:3.11-slim

# -----------------------------
# Security & Compliance Defaults
# -----------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV MEDINTEL_ENV=regulated
ENV TZ=UTC

# Create non-root user
RUN groupadd -r medintel && useradd -r -g medintel medintel

# -----------------------------
# System Dependencies
# -----------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    curl \
    git \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------
# Working Directory
# -----------------------------
WORKDIR /opt/medintel

# -----------------------------
# Python Dependencies
# -----------------------------
# Requirements file must be explicitly reviewed for regulatory suitability
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# -----------------------------
# Application Files
# -----------------------------
COPY . .

# -----------------------------
# Permissions
# -----------------------------
RUN chown -R medintel:medintel /opt/medintel
USER medintel

# -----------------------------
# Runtime Contract
# -----------------------------
# This container is NOT permitted to:
# - Perform autonomous inference
# - Access live patient data
# - Execute clinical decisions
#
# Runtime usage is limited to:
# - Model evaluation
# - Metric computation (e.g., F1-score)
# - Validation & audit tooling
# - Documentation & registry preparation

CMD ["python", "-m", "medintel"]

