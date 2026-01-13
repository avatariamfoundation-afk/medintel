# INTEGRATION_BOUNDARIES.md  
**Repository:** neurogrid-medintel    
**Audience:** Hackathon Judges · System Integrators · Security & Compliance Reviewers  
**Status:** Execution-Ready / Paste-Ready  
**Last Updated:** 2026-01-13  

---

## 1. Purpose

This document defines the **explicit integration boundaries** for the NeuroGrid MedIntel system.

MedIntel is designed to **integrate with external tools in a constrained, auditable, and non-invasive manner**.  
All integrations are intentionally limited to prevent scope creep into regulated medical, financial, or autonomous decision domains.

These boundaries are enforced by architecture, documentation, and operational controls.

---

## 2. Core Integration Principle

> **MedIntel integrates systems — it does not merge responsibilities.**

Each external system remains:
- Functionally independent
- Legally independent
- Responsibility-isolated

MedIntel never inherits the regulatory or operational burden of integrated tools.

---

## 3. Allowed Integration Classes

### 3.1 AI / ML Tools (Non-Clinical)

Permitted integrations:
- Research-grade ML models
- Open-source inference engines
- Rule-based analysis tools
- Deterministic scoring engines

Constraints:
- No clinical labeling
- No autonomous decision authority
- No continuous learning from live data

---

### 3.2 Data Sources (Synthetic Only)

Allowed:
- Synthetic datasets
- Simulated telemetry
- Generated test signals

Disallowed:
- Real patient data
- Live medical telemetry
- Electronic Health Records (EHRs)
- Wearable data streams from real users

---

### 3.3 Blockchain / Web3 Systems

Permitted:
- Testnet deployments (e.g., BNB testnet)
- Artifact anchoring (hashes only)
- Metadata proofs
- Audit trail publication

Prohibited:
- Storage of medical data on-chain
- Patient identity linkage
- Financial automation tied to health outcomes

---

### 3.4 Frontend / UI Integrations

Allowed:
- Read-only dashboards
- Demo visualizations
- Telemetry viewers
- Artifact explorers

Prohibited:
- Patient-facing clinical interfaces
- Decision-making controls
- Medical guidance displays

---

## 4. Explicitly Prohibited Integrations

MedIntel must **never** integrate with:
- Hospital systems
- Clinical decision support systems
- Prescription platforms
- Insurance systems
- Emergency response systems
- Medical IoT devices in live environments

These are **hard exclusions**.

---

## 5. Integration Responsibility Model

Each integration follows a **clear ownership boundary**:

| Layer | Responsibility |
|-----|---------------|
| External Tool | Domain logic & outcomes |
| MedIntel | Orchestration & audit |
| User | Interpretation & decision-making |
| Clinician | Medical judgment (outside system) |

MedIntel is never the final authority.

---

## 6. Technical Boundary Controls

Integration safety is enforced via:
- Strict API schemas
- Read-only adapters
- Input/output validation
- Non-clinical naming conventions
- CI checks against forbidden keywords

---

## 7. Failure Containment

If an integrated system:
- Fails
- Produces malformed output
- Emits prohibited data

MedIntel will:
- Quarantine the artifact
- Emit a fault code
- Preserve the audit trail
- Continue operating without escalation

---

## 8. Regulatory Isolation

Integration boundaries ensure:
- No regulatory inheritance
- No cross-domain liability
- No implicit certification claims

This keeps MedIntel safely outside:
- Medical device regulation
- Financial compliance regimes
- Autonomous system governance frameworks

---

## 9. Judge-Oriented Clarity

For judges, these boundaries demonstrate:
- Architectural maturity
- Risk-aware integration design
- Responsible system composition
- Strong open-source safety posture

This is a **composable system**, not a monolith.

---

## 10. Non-Negotiable Clause

> Any integration that violates this document invalidates MedIntel’s safety and compliance guarantees.

Such changes constitute a separate, unsupported fork.

---

**End of Document**
