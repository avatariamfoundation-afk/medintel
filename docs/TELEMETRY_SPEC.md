# TELEMETRY.md

## MedIntel — Deterministic Telemetry Specification  
**Status:** Mandatory  
**Scope:** MedIntel Enhancement Phase  
**Applies To:** All compute nodes, inference pipelines, cross-chain relays, and governance observers  

---

## 1. Purpose

This document defines the **Telemetry Contract** for MedIntel.

Telemetry exists to ensure:
- Deterministic observability
- Fault attribution
- Slashing enforcement
- Audit-grade traceability
- Cross-node and cross-chain consistency

Telemetry is **not optional**, **not best-effort**, and **not advisory**.  
Telemetry is a **consensus-critical subsystem**.

---

## 2. Telemetry Principles

All telemetry MUST be:

1. **Deterministic** – identical events emit identical telemetry
2. **Non-invasive** – telemetry MUST NOT affect inference outcomes
3. **Canonical** – normalized, schema-locked, versioned
4. **Tamper-evident** – cryptographically verifiable
5. **Minimal** – no excess data, no PII, no raw payloads

---

## 3. Telemetry Domains

Telemetry is emitted across **six domains**:

1. Node Lifecycle
2. Inference Execution
3. Deterministic Validation
4. Fault & Slashing Events
5. Cross-Chain State Sync
6. Governance & Policy Enforcement

---

## 4. Telemetry Architecture

### 4.1 Emission Flow
Event Trigger
→ Canonical Struct Encoding
→ Hashing
→ Local Persistence
→ Signed Emission
→ Relay / On-Chain Commit


Telemetry MUST be emitted **after state finalization**, never mid-execution.

---

## 5. Telemetry Event Structure

All telemetry events MUST conform to the following canonical schema:

```json
{
  "event_id": "UUIDv7",
  "event_type": "STRING",
  "event_version": "SEMVER",
  "timestamp": "RFC3339",
  "node_id": "HASH",
  "domain": "ENUM",
  "severity": "ENUM",
  "payload_hash": "SHA256",
  "context_hash": "SHA256",
  "signature": "ED25519"
}

6. Severity Levels
Level	Meaning
INFO	Normal operation
WARN	Degraded but recoverable
ERROR	Deterministic failure
CRITICAL	Slashing-eligible violation

Severity levels are immutable once emitted.

7. Node Lifecycle Telemetry

Emitted events include:

NODE_BOOT

NODE_SHUTDOWN

NODE_HEALTHCHECK

NODE_ATTESTATION_REFRESH

NODE_EVICTION

Each event includes:

Runtime hash

Hardware class

Policy version

8. Inference Telemetry
8.1 Mandatory Inference Events

INFERENCE_REQUEST_RECEIVED

INFERENCE_CANONICALIZED

INFERENCE_EXECUTED

INFERENCE_OUTPUT_HASHED

INFERENCE_ATTESTED

8.2 Prohibited Content

Telemetry MUST NOT include:

Raw inputs

Raw outputs

Patient identifiers

Intermediate activations

9. Deterministic Validation Telemetry

Validation checkpoints emit:

DETERMINISM_CHECK_PASSED

DETERMINISM_CHECK_FAILED

Failure telemetry MUST reference:

Determinism domain

Deterministic fault code

Slashing tier

10. Fault Telemetry
10.1 Fault Emission Rules

Faults MUST be emitted immediately

Fault telemetry MUST precede slashing

Faults are immutable once emitted

10.2 Fault Fields
{
  "fault_code": "STRING",
  "fault_domain": "ENUM",
  "violation_hash": "SHA256",
  "severity": "ENUM"
}

11. Slashing Telemetry

Slashing telemetry is consensus-relevant.

Emitted events:

SLASH_WARNING

SLASH_EXECUTED

STAKE_REDUCTION

NODE_BLACKLISTED

Each slashing event MUST reference:

Fault code

Evidence hash

Governance policy hash

12. Cross-Chain Telemetry

Telemetry MAY be mirrored across chains for:

Validator accountability

Governance synchronization

Regulatory archiving

Cross-chain telemetry MUST:

Preserve original hashes

Include source chain ID

Maintain ordering guarantees

13. Telemetry Storage Rules

Local persistence REQUIRED

Retention period: minimum 7 years

Immutable append-only logs

Merkle-root anchoring recommended

14. Cryptographic Guarantees

All telemetry MUST be:

Signed by emitting node

Verifiable without trust assumptions

Resistant to replay attacks

Invalid signatures invalidate telemetry entirely.

15. Privacy & Compliance

Telemetry is designed to be:

LGPD-compliant

GDPR-compatible

HIPAA-safe by construction

No personal or biometric data is ever emitted.

16. Failure Modes
Failure	Action
Telemetry omission	Immediate slashing
Invalid schema	Event rejection
Signature failure	Node quarantine
Replay detected	Critical fault

Telemetry failure is treated as protocol failure.

17. Governance Controls

Telemetry schema changes require governance approval

Emergency schema overrides disabled

Backward compatibility is mandatory

18. Non-Negotiable Rule

If it is not observable, it is not trusted.
If it is not deterministic, it is not telemetry.
