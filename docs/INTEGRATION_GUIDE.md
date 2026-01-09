## INTEGRATION_GUIDE.md

**Deterministic Medical Intelligence → NeuroGrid Core
**Audience:** Hackathon Judges · Integrators · Core/DeSci Developers  
**Scope:** MedIntel ↔ NeuroGrid-Core ↔ DeSci  
**Last Updated:** 2026-01-07  

---

## 1. Purpose

This document explains **exactly how MedIntel integrates** with the rest of the NeuroGrid system.

MedIntel is the **deterministic AI inference layer**.  
It does **not** store state, govern users, or manage incentives.  
Its sole responsibility is to:

> Convert validated biomedical inputs into **deterministic inference artifacts** that can be trusted, verified, and consumed by on-chain and DeSci systems.

This guide is written so that **non-AI judges** and **non-Solidity developers** can still understand the full integration flow.

---

## 2. MedIntel’s Role in the System

MedIntel sits **between raw data and on-chain truth**.

| Layer | Responsibility |
|----|----|
| Input Sources | Biosignals, datasets, simulated health data |
| **MedIntel** | Deterministic inference & artifact generation |
| NeuroGrid-Core | Canonical storage, governance, incentives |
| DeSci Layer | Provenance, reproducibility, collaboration |

MedIntel **never writes directly to chain**.  
It emits **signed artifacts** that are then ingested by NeuroGrid-Core.

---

## 3. High-Level Integration Flow

[Input Data]
↓
[MedIntel Inference Engine]
↓
[Signed Inference Artifact]
↓
[NeuroGrid-Core ArtifactRegistry]
↓
[DeSci Provenance & Validation]


Every arrow is **explicit, auditable, and deterministic**.

---

## 4. Integration Entry Points

MedIntel exposes **three integration surfaces**:

### 4.1 Input Interface
- Accepts:
  - Structured datasets
  - Sensor-like time-series data
  - Simulated or anonymized medical signals
- Rejects:
  - Malformed data
  - Non-deterministic payloads
  - Missing schema identifiers

---

### 4.2 Inference Execution Interface
- Runs deterministic inference pipelines
- Uses:
  - Fixed model versions
  - Locked preprocessing steps
  - Version-pinned dependencies
- Produces:
  - Inference result
  - Confidence metadata
  - Deterministic hash

---

### 4.3 Artifact Emission Interface
- Outputs a **signed inference artifact** containing:
  - Artifact ID
  - Input hash
  - Model ID + version
  - Inference output
  - Timestamp
  - Telemetry signals
  - Fault codes (if any)

This artifact is the **only object** that leaves MedIntel.

---

## 5. Integration With NeuroGrid-Core

### 5.1 Artifact Submission

MedIntel artifacts are submitted to:

- `ArtifactRegistry` (NeuroGrid-Core)

Submission guarantees:
- Artifact immutability
- Hash-based verification
- Event-driven ingestion

MedIntel **does not need private keys** for governance actions.  
Submission authority is **explicitly scoped**.

---

### 5.2 Deterministic Guarantees

NeuroGrid-Core assumes:
- Identical inputs → identical artifact hash
- Any deviation is a **fault condition**

If determinism breaks:
- Artifact is rejected
- Fault telemetry is emitted
- No incentives are issued

---

## 6. Integration With DeSci Layer

Once accepted on-chain, MedIntel artifacts are:

- Referenced by DeSci provenance records
- Used for:
  - Reproducibility checks
  - Peer review
  - Validator attestation
  - Research lineage tracking

MedIntel itself:
- Does **not** judge correctness
- Does **not** assign truth
- Supplies **verifiable computation evidence**

---

## 7. Telemetry & Observability Integration

MedIntel emits telemetry for:

- Inference success
- Inference failure
- Determinism violations
- Resource bounds
- Execution timing

Telemetry is:
- Deterministic
- Forward-compatible
- Consumable by:
  - NeuroGrid-Core
  - Cross-chain observers
  - Hackathon evaluators

---

## 8. Failure Modes & Integration Safety

| Failure Type | MedIntel Action | Core Reaction |
|-------------|----------------|---------------|
| Invalid input | Reject locally | No artifact |
| Non-determinism | Emit fault | Artifact rejected |
| Model mismatch | Emit fault | Governance visibility |
| Timeout | Emit telemetry | Retry allowed |

MedIntel **never silently fails**.

---

## 9. Security Boundaries

MedIntel is intentionally **non-custodial**:

- No token custody
- No governance authority
- No irreversible actions

Security assumptions:
- Inputs may be adversarial
- Outputs must be verifiable
- Trust is derived from determinism, not reputation

---

## 10. Hackathon Context (Important)

For hackathon purposes:

- MedIntel uses **simulated / anonymized data**
- Models are intentionally constrained
- Focus is on:
  - System design
  - Deterministic execution
  - Integration correctness

This ensures:
- Ethical compliance
- Regulatory safety
- Clear judging criteria

---

## 11. Post-Hackathon Expansion (Forward-Looking)

Following a successful hackathon outcome:

- MedIntel will expand to:
  - Real-world medical wearables
  - Secure IoT ingestion
  - Companion mobile applications
- A portion of awarded funds will be allocated to:
  - Wearable health device prototyping
  - E-commerce distribution infrastructure
  - Consumer-facing app development

Judges are evaluating **a foundation**, not a toy demo.

---

## 12. Summary

MedIntel is:

- Deterministic
- Non-custodial
- Verifiable
- Auditable
- Designed for real-world biomedical systems

It integrates cleanly with NeuroGrid-Core and DeSci without violating trust boundaries.

> **If MedIntel cannot prove what it computed, the system does not accept it.**

---

**End of Document**



