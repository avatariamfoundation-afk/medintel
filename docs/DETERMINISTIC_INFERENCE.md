# DETERMINISTIC_INFERENCE.md

## MedIntel — Deterministic Inference Specification  
**Status:** Enforced  
**Scope:** MedIntel Enhancement Phase  
**Applies To:** All inference-producing pipelines, models, and compute nodes  

---

## 1. Purpose

This document defines the **Deterministic Inference Contract** for MedIntel.  
Its objective is to ensure that **identical inputs, model artifacts, and execution context always yield identical outputs**, independent of node, time, or geographic location.

Deterministic inference is mandatory for:

- Clinical-grade decision support
- Regulatory defensibility
- Slashing and trust enforcement
- Cross-node reproducibility
- Audit and attestation integrity

Non-deterministic inference is explicitly **disallowed**.

---

## 2. Determinism Definition

An inference is considered **deterministic** if and only if:

Input Payload

Model Artifact (hash)

Execution Context

Inference Policy


Any deviation constitutes a **protocol violation**.

---

## 3. Determinism Domains

Determinism is enforced across **five domains**:

### 3.1 Model Determinism
- Model weights MUST be immutable
- Model artifact MUST be content-addressed (SHA-256)
- No dynamic weight updates during inference
- No stochastic layers at inference time

### 3.2 Input Determinism
- Inputs MUST be canonicalized
- Floating-point normalization REQUIRED
- Ordering of structured data MUST be stable
- No optional fields allowed without defaults

### 3.3 Execution Determinism
- Fixed inference runtime version
- Fixed hardware execution class
- Deterministic math libraries only
- CPU-only inference by default (GPU optional with strict constraints)

### 3.4 Environment Determinism
- Containerized execution REQUIRED
- No access to system time, randomness, or entropy pools
- No network access during inference
- Locale, timezone, and OS entropy locked

### 3.5 Policy Determinism
- Inference policies versioned and hashed
- Policy changes require governance approval
- No dynamic thresholding during inference

---

## 4. Deterministic Inference Pipeline

### 4.1 High-Level Flow

Input → Canonicalization → Validation
→ Model Hash Resolution
→ Deterministic Runtime
→ Inference Execution
→ Output Hashing
→ Attestation


---

## 5. Canonicalization Rules

### 5.1 Numeric Inputs
- Float precision fixed (IEEE 754)
- Explicit rounding rules applied
- NaN, ±Inf rejected

### 5.2 Structured Data
- JSON keys sorted lexicographically
- Arrays MUST preserve order
- Null handling standardized

### 5.3 Metadata
- All metadata fields mandatory
- Missing fields = rejection
- Defaults must be explicit

---

## 6. Randomness Prohibition

The following are **strictly forbidden** during inference:

- Random seeds
- Dropout layers
- Sampling-based decoding
- Temperature scaling
- Beam randomness
- Time-based branching

Any attempt to invoke randomness triggers **FAULT_CODE_DET_003**.

---

## 7. Floating Point Discipline

To prevent cross-platform drift:

- Fixed precision enforced
- No mixed-precision inference
- No hardware-specific acceleration without approval
- Deterministic BLAS libraries only

---

## 8. Hardware Constraints

### 8.1 Approved Execution Classes
- CPU (x86_64) — default
- GPU — allowed only if determinism-certified

### 8.2 Hardware Declaration
Each inference node MUST declare:

- CPU model
- Instruction set
- Runtime hash
- Determinism certification ID

Mismatch = inference rejection.

---

## 9. Output Determinism

### 9.1 Output Requirements
- Output MUST be canonicalized
- Output MUST include:
  - Output hash
  - Model hash
  - Policy hash
  - Node ID
  - Execution timestamp (post-inference only)

### 9.2 Bitwise Equality
Outputs are compared using **bitwise equality**, not tolerance-based similarity.

---

## 10. Attestation & Verification

Each inference emits an **Inference Attestation** containing:

- Input hash
- Model artifact hash
- Runtime hash
- Output hash
- Node signature

Attestations are:

- Signed by the node
- Verifiable on-chain
- Used for slashing enforcement

---

## 11. Fault Conditions

| Condition | Description |
|---------|-------------|
| DET_001 | Input canonicalization failure |
| DET_002 | Model hash mismatch |
| DET_003 | Randomness detected |
| DET_004 | Runtime mismatch |
| DET_005 | Output divergence |
| DET_006 | Hardware class violation |

Fault codes map directly to **slashing severity tiers**.

---

## 12. Slashing Implications

- First violation: warning + telemetry flag
- Second violation: stake reduction
- Third violation: node eviction

Deterministic violations are **non-appealable**.

---

## 13. Governance Controls

- Determinism rules are immutable at runtime
- Changes require governance vote
- Emergency overrides disabled by default

---

## 14. Regulatory Alignment

Deterministic inference aligns with:

- FDA Software as a Medical Device (SaMD)
- EU MDR auditability requirements
- LGPD data integrity mandates
- ISO 13485 traceability standards

---

## 15. Non-Negotiable Rule

> **If inference cannot be deterministic, it does not belong in MedIntel.**

---

## 16. File Location
/medintel/
└── inference/
└── DETERMINISTIC_INFERENCE.md

---

**End of File**

