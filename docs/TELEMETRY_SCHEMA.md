# TELEMETRY_SCHEMA.md  
**MedIntel — Deterministic Telemetry Specification**

---

## 1. Purpose (Judge-Facing)
This document defines the **exact telemetry schema** emitted by MedIntel during execution.

It exists to demonstrate:
- Transparency without data leakage
- Deterministic, inspectable system behavior
- Clear observability boundaries
- Compliance-aware logging

Telemetry is **non-clinical**, **non-diagnostic**, and **non-identifying**.

---

## 2. Telemetry Design Principles
MedIntel telemetry is built on the following rules:

- **Deterministic** — same execution → same telemetry structure
- **Minimal** — only execution-relevant signals
- **Non-sensitive** — no medical or personal data
- **Append-only** — events are never mutated
- **Human-readable** — judges can inspect logs directly

Telemetry ≠ Analytics  
Telemetry ≠ Monitoring user behavior  
Telemetry = **Execution accountability**

---

## 3. Telemetry Emission Lifecycle
Telemetry events are emitted at **well-defined pipeline boundaries** only.

PIPELINE_START
↓
STAGE_ENTER
↓
STAGE_EXIT
↓
ARTIFACT_EMITTED
↓
PIPELINE_COMPLETE | PIPELINE_FAILURE

No background telemetry is generated.

---

## 4. Global Telemetry Envelope
Every telemetry event conforms to this top-level schema:

```json
{
  "event_type": "STRING",
  "timestamp_utc": "ISO-8601",
  "pipeline_id": "STRING",
  "execution_mode": "DEMO | TEST | PROD",
  "severity": "INFO | WARN | ERROR",
  "payload": {}
}

---

## 5. Core Field Definitions
Field	Description
event_type	Type of telemetry event
timestamp_utc	UTC timestamp of emission
pipeline_id	Deterministic execution identifier
execution_mode	Declared runtime mode
severity	Log severity classification
payload	Event-specific data

---

## 6. Event Types (Canonical)
### 6.1 PIPELINE_START
Emitted once per execution.

{
  "event_type": "PIPELINE_START",
  "payload": {
    "input_hash": "sha256",
    "declared_scope": "SYNTHETIC_MEDICAL_DEMO"
  }
}
### 6.2 STAGE_ENTER
Emitted when entering a pipeline stage.

{
  "event_type": "STAGE_ENTER",
  "payload": {
    "stage_name": "VALIDATION_GATE"
  }
}
### 6.3 STAGE_EXIT
Emitted on successful stage completion.

{
  "event_type": "STAGE_EXIT",
  "payload": {
    "stage_name": "VALIDATION_GATE",
    "status": "SUCCESS"
  }
}

### 6.4 ARTIFACT_EMITTED
Emitted when an execution artifact is created.

{
  "event_type": "ARTIFACT_EMITTED",
  "payload": {
    "artifact_type": "EXECUTION_RESULT",
    "artifact_hash": "sha256",
    "artifact_version": "v1"
  }
}

### 6.5 PIPELINE_COMPLETE
Emitted on clean termination.

{
  "event_type": "PIPELINE_COMPLETE",
  "payload": {
    "execution_status": "OK",
    "duration_ms": 842
  }
}

### 6.6 PIPELINE_FAILURE
Emitted on hard stop.

{
  "event_type": "PIPELINE_FAILURE",
  "severity": "ERROR",
  "payload": {
    "failure_stage": "MODEL_ROUTING",
    "fault_code": "MI-FLT-003"
  }
}

---

## 7. Telemetry Payload Constraints
Telemetry payloads MUST NOT include:

Raw medical data
Patient identifiers
Images or signals
Model weights or parameters
Free-text medical interpretation
Violations trigger immediate pipeline halt.

---

## 8. Fault Code Coupling
Telemetry failure events must reference a registered fault code from:
FAULT_CODE_MAPPING.md
No unregistered fault codes are allowed.

---

## 9. Determinism Rules
Telemetry order is fixed
Telemetry fields are sorted
Payload structure is immutable per version
Hashes are reproducible
This enables:
- Replay validation
- Audit verification
- Judge-side reproduction

---

## 10. Telemetry Transport (Demo Scope)
In demo mode, telemetry is emitted via:
- Command-line stdout
- Structured JSON logs

No external logging services are used.

---

## 11. Versioning Strategy
Telemetry schema versions are explicit.

"telemetry_schema_version": "1.0.0"
Breaking changes require:
- New version
- Explicit migration note
- Judge-visible changelog

---

## 12. Security Posture
Telemetry is:
- Stateless
- Non-networked by default
- Local-only in demo mode
- No telemetry is transmitted externally unless explicitly enabled.

---

## 13. Judge Verification Checklist
Judges can verify:
- Telemetry output in demo logs
- Schema conformance
- Absence of sensitive data
- Deterministic ordering
- No credentials or keys required.

---

## 14. Final Assurance Statement
Telemetry in MedIntel exists to explain execution — not to observe users.

It is transparent, minimal, and safe by design.

## End of Telemetry Schema Document## 
