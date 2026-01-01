# MedIntel Dependency Governance

## Policy
- All Python dependencies are pinned
- `requirements.lock` is mandatory
- No implicit upgrades allowed

## Security Guarantees
- Deterministic builds
- Reproducible environments
- Reduced supply-chain attack surface

Any dependency change requires audit and version review.

