# ON-CHAIN_REGISTRY.md  
**Clinical AI Registry Anchoring & Traceability Specification**

---

## 1. Purpose

This document defines the **MedIntel On-Chain Registry interface** used to anchor and reference clinical AI system artifacts in a tamper-evident manner.

The registry provides **verifiable traceability** for:
- Model governance
- Safety documentation
- Performance disclosures
- Regulatory artifacts

It does **not** store clinical data, model weights, or patient information.

---

## 2. Scope

The MedIntel registry covers:

- AI model identifiers
- Model version hashes
- Safety case references
- Performance metric disclosures
- Calibration and confidence artifacts
- Regulatory review markers
- Deployment state changes

Excluded from scope:
- Patient data
- RPM streams
- Inference outputs
- Real-time clinical decisions

---

## 3. Design Constraints

- Hash-only anchoring
- Append-only lifecycle
- Human-readable off-chain documents
- Machine-verifiable on-chain proofs
- Mandatory human-in-the-loop separation

The registry exists for **accountability**, not execution.

---

## 4. Registry Record Categories

### A. Model Identity Records
- Model name
- Unique model ID
- Initial registration hash

### B. Model Version Records
- Version number
- Architecture summary hash
- Training data lineage hash
- Release timestamp

### C. Safety & Governance Records
- AI_MODEL_SAFETY_CASE hash
- CHANGE_IMPACT_ASSESSMENT hash
- BIAS_SURVEILLANCE hash
- OVERRIDE_PROTOCOL hash

### D. Performance & Confidence Records
- Primary metric disclosure
- F1-score or equivalent
- Calibration references
- Confidence threshold definitions

### E. Regulatory Records
- Review simulation results
- Audit checkpoints
- Approval state markers
- Suspension or rollback flags

---

## 5. Record Structure (Abstract)

Each registry entry must include:

- Registry record ID
- Record category
- Content hash
- Model ID reference
- Version reference (if applicable)
- Timestamp
- Authorizing role
- Cross-repository pointer (Core / DeSci)

---

## 6. Submission Workflow

1. Artifact finalized and approved
2. Compliance and safety validation completed
3. Cryptographic hash generated
4. Hash submitted to Core registry contract
5. Transaction confirmed
6. Reference stored in MedIntel index

No artifact may be deployed without a valid registry anchor.

---

## 7. Versioning & Supersession

- Registry entries are immutable
- Updates require new entries
- Supersession must reference prior record
- Rollbacks must be explicitly logged

Historical lineage is mandatory.

---

## 8. Access Control

- Read access: public
- Write access: restricted to authorized governance roles
- Emergency write access: Safety Council only
- All writes are auditable

---

## 9. Emergency Registry Mode

During declared emergencies:
- Suspension markers may be written
- Rollback references may be anchored
- Post-event DAO and clinical ratification required

Emergency records are permanently flagged.

---

## 10. Cross-System Integration

The MedIntel registry links to:
- NeuroGrid Core contracts (integrity anchor)
- DeSci governance registry (oversight trace)
- External audit systems (read-only verification)

Clinical systems may reference registry IDs but **must not depend on chain state at runtime**.

---

## 11. Regulatory Alignment

This registry supports alignment with:

- FDA GMLP traceability expectations
- EU AI Act model governance requirements
- ISO 62304 (software lifecycle)
- ISO 14971 (risk management)
- LGPD / GDPR data minimization

---

## 12. Prohibited Actions

The registry must never:
- Store patient identifiers
- Gate clinical decision execution
- Replace human clinical judgment
- Encode medical advice

---

## 13. Audit & Retention

All registry entries:
- Are immutable and timestamped
- Support independent verification
- Are retained indefinitely
- Are admissible as audit evidence

---

### Status  
**Active – Binding MedIntel Infrastructure Specification**

