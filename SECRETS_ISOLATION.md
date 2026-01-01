# Secrets Isolation — MedIntel

## Never Stored In Code
- Private keys
- Model signing secrets
- API tokens

## Allowed Storage
- Local `.env`
- CI secrets
- Production secret manager

## AI Models
- Model weights are not secrets
- Model signing keys ARE secrets

