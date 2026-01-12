# SECURITY_MODEL.md

## 1. Purpose

This document defines the **enforceable security posture** of MedIntel.  
It specifies **what must be protected, from whom, how, and why**, in a way that is:

- Auditable
- Testable
- Judge-readable
- Post-hackathon extensible

This is a **pass/fail document**, not a philosophy.

---

## 2. Security Objectives (Non-Negotiable)

MedIntel enforces the following guarantees:

1. **No patient-identifiable data at rest**
2. **Deterministic, reproducible intelligence**
3. **Strict read/write boundaries**
4. **Verifiable execution lineage**
5. **Regulatory-aligned auditability (LGPD/GDPR-ready)**

Failure in any objective is a **system-level failure**.

---

## 3. Threat Model

### 3.1 In-Scope Threats

| Threat | Description |
|------|-------------|
| Data leakage | Exposure of sensitive medical inputs |
| Model tampering | Unauthorized model or output manipulation |
| Replay attacks | Reuse of inputs to falsify intelligence |
| API abuse | Unauthorized data extraction |
| Supply chain | Malicious dependency injection |

---

### 3.2 Out-of-Scope (Explicit)

- Physical data center compromise  
- Nation-state attacks  
- Side-channel hardware attacks  

These are documented but not addressed at hackathon scope.

---

## 4. Trust Boundaries

MedIntel defines **four hard trust zones**:

[ Ingestion ] → [ Canonical Core ] → [ Intelligence Layer ] → [ API Surface ]

yaml
Copy code

Rules:
- Data only flows **forward**
- No lateral access
- No backward mutation

---

## 5. Identity & Access Control

### 5.1 Identity Types

| Actor | Capabilities |
|-----|--------------|
| System | Full internal execution |
| Service | Scoped API access |
| User | Read-only intelligence |
| Auditor | Read-only + logs |

---

### 5.2 Access Enforcement

- Role-Based Access Control (RBAC)
- Token-scoped permissions
- No shared credentials
- No implicit trust between services

---

## 6. Data Security Controls

### 6.1 Data at Rest

- **No raw medical data persisted**
- All stored objects:
  - Hashed identifiers
  - Immutable records
  - Versioned artifacts

### 6.2 Data in Transit

- TLS 1.3 mandatory
- No plaintext internal APIs
- Mutual TLS for service-to-service calls

---

## 7. Model & Execution Integrity

### 7.1 Model Registry Protections

- Models are **append-only**
- Version immutability enforced
- Training data referenced by hash only

### 7.2 Execution Context Guarantees

Every intelligence output is bound to:

- Input checksum
- Model version
- Runtime environment hash
- Timestamp

This enables **full replay verification**.

---

## 8. API Security

### 8.1 API Surface Rules

- Read-only intelligence access
- No mutation endpoints exposed
- Strict schema validation
- Rate limiting enforced

### 8.2 Forbidden API Actions

- Raw data access
- Bulk export without audit
- Free-form query execution

---

## 9. Audit & Compliance

### 9.1 Audit Logging

All critical actions generate immutable logs:

- Intelligence creation
- Model registration
- API access
- Deprecation events

Logs are:
- Append-only
- Timestamped
- Actor-attributed

---

### 9.2 Regulatory Alignment

Designed to align with:
- LGPD (Brazil)
- GDPR (EU)
- HIPAA principles (non-certified)

No compliance claims are made — **only readiness**.

---

## 10. Dependency & Supply Chain Security

- Minimal dependency surface
- Pinned versions
- No runtime dependency downloads
- CI enforces dependency integrity

---

## 11. CI/CD Security Gates

Pipeline must fail if:
- Schema validation fails
- Test coverage drops below threshold
- Security linting fails
- Unauthorized file changes detected

---

## 12. Security Testing Requirements

Mandatory tests:
- Access control enforcement
- Schema validation
- Immutability checks
- Unauthorized mutation attempts

Optional (post-hackathon):
- Fuzzing
- Penetration testing
- Formal verification

---

## 13. Incident Response (Minimal)

If a violation occurs:
1. Halt processing
2. Invalidate affected outputs
3. Preserve audit trail
4. Notify maintainers

No silent failures allowed.

---

## 14. Final Assertion

> MedIntel does not promise perfect security.  
> It guarantees **controlled failure, traceability, and containment**.
