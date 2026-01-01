# Static Security Scanning — MedIntel

## Tooling
- Bandit (Python static analysis)

## Policy
- No HIGH severity issues allowed
- MEDIUM issues require justification
- LOW issues tracked but non-blocking

## Execution
bandit -r medintel -c bandit.yaml

