# CROSS-LINK_REGISTRY.md  
**MedIntel Cross-Domain Reference & Governance Boundary Specification**

---

## 1. Purpose

This document defines how **MedIntel artifacts are cross-linked** to external governance, research, and core integrity records within the NeuroGrid ecosystem.

The MedIntel Cross-Link Registry exists to:
- Preserve **clinical independence**
- Enable **traceable oversight**
- Support **regulatory audit reconstruction**
- Prevent governance or DAO overreach into clinical decision-making

MedIntel participates in cross-linking **as a referenced domain**, never as a controlling authority.

---

## 2. Scope

This specification applies to cross-links involving:

- AI model safety documentation
- Model versioning and lifecycle records
- Post-market surveillance reports
- Emergency suspensions or rollbacks
- Regulatory review artifacts
- Human oversight and override records

Excluded from scope:
- Patient data
- RPM raw signals
- Inference outputs
- Real-time clinical workflows

---

## 3. Core Principle

> **Clinical logic remains sovereign.  
> Cross-links provide traceability, not permission.**

All MedIntel cross-links are **non-executable references**.

---

## 4. Permitted Cross-Link Directions

### A. MedIntel → Core
- Anchor model lifecycle events
- Reference emergency suspensions
- Register safety case updates

### B. MedIntel → DeSci
- Acknowledge governance oversight
- Reference ethics or compliance approvals
- Link research transparency artifacts

### C. Core / DeSci → MedIntel
- Governance acknowledgment of clinical events
- Post-hoc ratification of emergency actions
- Audit or regulatory references

Bidirectional links must be explicit and independently authorized.

---

## 5. Cross-Link Record Structure

Each MedIntel cross-link record must include:

- Cross-link ID
- MedIntel artifact identifier
- Artifact type (model, safety, surveillance, override)
- External registry reference (Core or DeSci)
- External artifact hash or registry ID
- Relationship classification
- Timestamp
- Authorizing clinical governance role

---

## 6. Relationship Classifications

Permitted classifications include:

- SAFETY_ACKNOWLEDGMENT
- GOVERNANCE_REFERENCE
- REGULATORY_TRACE
- EMERGENCY_NOTIFICATION
- AUDIT_SUPPORT
- POST_MARKET_REPORT

Unclassified relationships are prohibited.

---

## 7. Creation Workflow

1. MedIntel artifact finalized and approved
2. Internal clinical governance validation
3. External artifact verified (Core / DeSci)
4. Cross-link metadata assembled
5. Hash anchored via Core registry
6. Reference indexed locally in MedIntel

No cross-link may be created without completed internal approval.

---

## 8. Emergency Cross-Linking

During declared clinical emergencies:
- Emergency notifications may be cross-linked immediately
- Links must be flagged as emergency-context
- Post-event governance acknowledgment is mandatory
- Emergency links remain permanently visible

---

## 9. Immutability & Supersession

- Cross-links are append-only
- Supersession requires a new cross-link record
- Deprecated links remain accessible
- Lineage reconstruction must be possible without ambiguity

---

## 10. Authority & Access Control

- Read access: public
- Write access: restricted to MedIntel clinical governance roles
- DAO members may not initiate MedIntel cross-links
- All actions are logged and auditable

---

## 11. Regulatory Alignment

This specification supports alignment with:

- FDA GMLP traceability requirements
- EU AI Act governance separation
- ISO 14971 risk management
- ISO 62304 software lifecycle controls
- LGPD / GDPR data minimization

---

## 12. Prohibited Uses

The MedIntel Cross-Link Registry must never:
- Enable DAO control of clinical decisions
- Act as a runtime dependency
- Substitute for clinician judgment
- Conceal safety or audit findings

---

## 13. Audit & Evidence Use

Cross-link records:
- Support regulatory inspections
- Enable decision lineage reconstruction
- Provide admissible audit evidence
- Persist indefinitely

---

### Status  
**Active – Binding MedIntel Reference Specification**

