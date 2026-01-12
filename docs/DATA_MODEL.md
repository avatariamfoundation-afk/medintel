# DATA_MODEL.md

## 1. Purpose

This document defines the **canonical data model** for MedIntel.  
It specifies *what* data exists, *where* it is allowed to live, and *how* it flows through the system.

This is a **contract document**:
- Architecture depends on it
- Tests depend on it
- APIs depend on it
- DeSci depends on it

No implicit fields. No leaky abstractions.

---

## 2. Core Data Design Principles

1. **No Raw Medical Data at Rest**
   - Raw inputs are transient
   - Persisted data is always transformed or abstracted

2. **Immutability First**
   - Intelligence artifacts are append-only
   - Corrections create new versions, never overwrite

3. **Explicit Lineage**
   - Every output is traceable to:
     - Input hash
     - Model version
     - Execution context

4. **Minimal Identifiability**
   - Identifiers are hashed, salted, or tokenized
   - No direct patient identifiers are stored

---

## 3. Data Domains

MedIntel data is divided into **five domains**:

1. Ingestion
2. Canonical Medical Representation
3. Intelligence Artifacts
4. Model & Execution Metadata
5. Audit & Compliance

Each domain is isolated by design.

---

## 4. Ingestion Domain (Ephemeral)
### 4.1 IngestedPayload (Transient)

> Exists only in memory or short-lived processing queues.

```json
{
  "payload_id": "uuid",
  "source_type": "EHR | DEVICE | DATASET",
  "received_at": "timestamp",
  "raw_schema_version": "string",
  "payload_checksum": "sha256"
}
Rules

Never persisted

Destroyed after validation + normalization

Used only to derive canonical records

---

## 5. Canonical Medical Representation
### 5.1 CanonicalRecord
This is the internal normalized representation of medical data.

```json
{
  "canonical_id": "uuid",
  "subject_token": "hashed_identifier",
  "record_type": "observation | lab | imaging | event",
  "attributes": {
    "key": "value"
  },
  "event_timestamp": "timestamp",
  "ingested_at": "timestamp"
}

## Notes
subject_token cannot be reversed
attributes follow strict internal schemas
No free-form text unless explicitly allowed

---

## 6. Intelligence Artifacts (Persistent)
### 6.1 IntelligenceResult (Core Object)
This is the primary persistent output of MedIntel.

```json
{
  "intelligence_id": "uuid",
  "canonical_id": "uuid",
  "model_id": "string",
  "model_version": "semver",
  "result_type": "risk_score | classification | embedding | flag",
  "result_value": {},
  "confidence_score": 0.0,
  "generated_at": "timestamp"
}

Characteristics
Immutable
Deterministic
Versioned by model + execution

### 6.2 IntelligenceVersionLink
Used to track supersession and evolution.

```json
{
  "intelligence_id": "uuid",
  "supersedes": "uuid | null",
  "reason": "model_update | correction | reprocessing"
}

---

## 7. Model & Execution Metadata
### 7.1 ModelRegistryEntry
```json
{
  "model_id": "string",
  "model_version": "semver",
  "model_type": "ml | rules | hybrid",
  "training_data_hash": "sha256",
  "approved_for_use": true,
  "registered_at": "timestamp"
}

###7.2 ExecutionContext
json
{
  "execution_id": "uuid",
  "model_id": "string",
  "model_version": "semver",
  "input_checksum": "sha256",
  "runtime_environment": "container_hash",
  "executed_at": "timestamp"
}
This guarantees full reproducibility.

---

## 8. Audit & Compliance Domain
### 8.1 AuditLogEntry
```json
{
  "audit_id": "uuid",
  "entity_type": "intelligence | model | api",
  "entity_id": "uuid",
  "action": "create | access | deprecate",
  "actor": "system | user | service",
  "timestamp": "timestamp"

}

Properties
Append-only
Immutable
Queryable for regulators

---

## 9. Forbidden Data (Hard Rules)
The following must never exist in MedIntel persistence:
Names
Government IDs
Addresses
Raw imaging files
Free-form clinician notes (unless fully anonymized and approved)
Violations are system faults, not bugs.

---

## 10. Relationships Overview
```java
IngestedPayload (transient)
        ↓
CanonicalRecord
        ↓
IntelligenceResult
        ↓
API / Consumers

Supporting links:
IntelligenceResult → ModelRegistryEntry
IntelligenceResult → ExecutionContext
All → AuditLogEntry

---

## 11. API Alignment (Preview)
Data Object	API Exposure
CanonicalRecord	Internal only
IntelligenceResult	Read-only
ModelRegistryEntry	Read-only
AuditLogEntry	Restricted

---

## 12. Testability Guarantees
Each data object enforces:
Schema validation
Version compatibility
Serialization determinism
No dynamic or inferred fields.

---

## 13. Final Assertion
The MedIntel data model is not a database schema.
It is a trust boundary.

### Everything downstream inherits its discipline.
