# MODEL_ABSTRACTION_LAYER.md  
**MedIntel — Model Abstraction Layer (MAL) Specification**

---

## 1. Purpose (Judge-Readable)

This document defines the **Model Abstraction Layer (MAL)** used by MedIntel.

Its purpose is to make **heterogeneous AI models interchangeable, auditable, and safely composable** without exposing MedIntel to:
- Model-specific risk
- Vendor lock-in
- Undeclared clinical behavior

This is a **past-read execution document** — judges should understand exactly how models are integrated, constrained, and swapped.

---

## 2. What the Model Abstraction Layer Is

The MAL is a **strict interface contract** between:
- External AI models (imaging, NLP, scoring)
- The MedIntel Orchestration Engine

It ensures that **all models look the same from the system’s perspective**, regardless of:
- Architecture
- Vendor
- Deployment environment

---

## 3. What the MAL Is Not

The MAL:
- Does **not** train models
- Does **not** optimize models
- Does **not** alter model internals
- Does **not** bypass safety checks

It is a **control and normalization layer only**.

---

## 4. Architectural Position

┌─────────────────────────────┐
│ External AI Models │
│ (Any Vendor / Any Stack) │
└──────────────┬──────────────┘
│
▼
┌─────────────────────────────┐
│ Model Abstraction Layer │
│ (This Document) │
└──────────────┬──────────────┘
│
▼
┌─────────────────────────────┐
│ Orchestration Engine │
└─────────────────────────────┘

No component can access a model **outside** the MAL.

---

## 5. Standardized Model Contract

Every model must conform to the following contract:

### Required Inputs
- `input_payload` (validated schema)
- `task_type` (classification / extraction / scoring)
- `execution_context` (non-clinical)

### Required Outputs
- `raw_output`
- `confidence_metadata`
- `execution_metadata`
- `model_identifier`

Any missing field → execution rejected.

---

## 6. Input Normalization

Before model invocation:
- Inputs are schema-validated
- Clinical language is removed
- Unsupported modalities are rejected
- Provenance tags are attached

This prevents **hidden behavior injection**.

---

## 7. Output Normalization

After model execution:
- Outputs are mapped to a shared schema
- Free-form text is constrained
- Confidence inflation is capped
- Unsupported claims are stripped

Models cannot escalate authority.

---

## 8. Deterministic Execution Rules

The MAL enforces:
- No temperature parameters
- No sampling randomness
- Fixed execution paths
- Version-pinned models

This guarantees reproducibility.

---

## 9. Safety Interlocks

If a model:
- Produces clinical recommendations
- Emits unsupported confidence claims
- Attempts to bypass schema constraints

The MAL:
- Rejects the output
- Logs the violation
- Signals the Orchestration Engine to halt

---

## 10. Model Registration Process

To add a new model:
1. Declare model metadata
2. Define input/output schema mapping
3. Pass dry-run validation
4. Pass safety boundary tests
5. Register version hash

Unregistered models cannot execute.

---

## 11. Vendor Independence

Because of the MAL:
- Models can be replaced without code changes
- Vendors can be swapped without risk
- Open-source and proprietary models coexist

This is critical for long-term sustainability.

---

## 12. Blockchain Compatibility

The MAL produces:
- Execution hashes
- Version identifiers
- Deterministic outputs

These artifacts are suitable for:
- On-chain anchoring
- Audit proofs
- Validator review

---

## 13. Hackathon Relevance

Judges should note:
- This layer enables **AI composability**
- It directly supports **DeSci principles**
- It reduces systemic AI risk
- It is designed for BNB Chain integration

---

## 14. Why This Matters

Without an abstraction layer:
- AI systems become fragile
- Safety becomes unenforceable
- Reproducibility collapses

The MAL makes MedIntel **engineering-grade**, not experimental.

---

## 15. Final Judge Note

> MedIntel treats models as replaceable components, not sources of truth.

The system remains sovereign.

---

**End of Document**
