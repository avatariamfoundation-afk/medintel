# ARCHITECTURE_OVERVIEW.md
## 1. Purpose and Scope

MedIntel is the **core intelligence layer** of the broader ecosystem.  
It is designed to ingest, normalize, analyze, and serve medical intelligence in a **regulatory-aware, testable, and extensible** manner.

This document defines:
- System boundaries
- Core architectural principles
- Logical and physical component layout
- Data flow and control flow
- Security, compliance, and scalability considerations

This is a **hardening document**. No shortcuts. All downstream repos (including DeSci) depend on this architecture being correct.

---

## 2. Architectural Principles

### 2.1 First Principles

1. **MedIntel is upstream of DeSci**
   - MedIntel produces validated intelligence
   - DeSci consumes intelligence, not raw medical data

2. **Separation of Concerns**
   - Data ingestion ≠ intelligence inference ≠ governance ≠ presentation

3. **Compliance-by-Design**
   - LGPD / HIPAA / GDPR constraints shape architecture, not bolt-ons

4. **Deterministic Intelligence Pipelines**
   - Same input → same output (unless model version explicitly changes)

5. **Testability Over Cleverness**
   - Every boundary is testable
   - Every module has explicit contracts

---

## 3. System Boundary Definition

### In-Scope
- Medical data ingestion (structured + semi-structured)
- Intelligence extraction and scoring
- Model orchestration and versioning
- Secure API exposure
- Audit logging and traceability
- Open-source–ready modular design

### Out-of-Scope
- Tokenomics
- DAO governance
- DeSci incentive mechanisms
- Consumer-facing monetization logic

---

## 4. High-Level Architecture

┌─────────────────────────────┐
│ External Sources │
│ (EHR, Devices, Datasets) │
└─────────────┬───────────────┘
│
▼
┌─────────────────────────────┐
│ Ingestion Layer │
│ (Validation + Normalization│
└─────────────┬───────────────┘
│
▼
┌─────────────────────────────┐
│ Intelligence Core │
│ (Models, Rules, Scoring) │
└─────────────┬───────────────┘
│
▼
┌─────────────────────────────┐
│ Intelligence Registry │
│ (Versioned, Auditable) │
└─────────────┬───────────────┘
│
▼
┌─────────────────────────────┐
│ API Surface │
│ (Secure + Typed) │
└─────────────┬───────────────┘
│
▼
┌─────────────────────────────┐
│ Consumers (UI / DeSci) │
└─────────────────────────────┘

---

## 5. Core Layers

### 5.1 Ingestion Layer

**Responsibility**
- Accept external medical data
- Validate schema + integrity
- Strip or hash identifiers
- Normalize into canonical internal format

**Key Properties**
- Stateless
- Idempotent
- Rejects invalid data early

**Examples**
- HL7 / FHIR adapters
- Device telemetry adapters
- Batch dataset loaders

---

### 5.2 Intelligence Core

**Responsibility**
- Execute inference pipelines
- Apply medical logic
- Generate intelligence artifacts (scores, flags, embeddings)

**Subcomponents**
- Model Orchestrator
- Rules Engine
- Feature Extraction
- Inference Runtime

**Non-Negotiables**
- Explicit model versioning
- Deterministic execution
- Reproducible outputs

---

### 5.3 Intelligence Registry

**Responsibility**
- Store **results**, not raw data
- Maintain version lineage
- Enable audit and rollback

**Stored Objects**
- Intelligence Result
- Model Version
- Execution Metadata
- Confidence Scores

This layer is the **source of truth** for MedIntel outputs.

---

### 5.4 API Surface

**Responsibility**
- Serve intelligence safely
- Enforce access control
- Provide typed contracts

**Design Rules**
- Read-heavy
- No raw patient data
- Versioned endpoints
- OpenAPI-first

**Consumers**
- Internal UI
- Analytics
- DeSci Repo
- External partners (future)

---

## 6. Data Flow Guarantees

| Property | Guaranteed |
|--------|-----------|
| Data integrity | Yes |
| Determinism | Yes |
| Traceability | Yes |
| Explainability hooks | Yes |
| Regulatory auditability | Yes |

---

## 7. Security & Compliance Architecture

### 7.1 Data Minimization
- Raw medical data is ephemeral
- Intelligence artifacts are abstracted

### 7.2 Encryption
- At rest: AES-256
- In transit: TLS 1.3

### 7.3 Audit Logging
- Immutable execution logs
- Model + input hash linking
- Timestamped access records

---

## 8. Deployment Model

### Environments
- `local`
- `staging`
- `production`

### Characteristics
- Containerized
- CI/CD enforced
- Infrastructure-as-Code compatible

---

## 9. Test Architecture Alignment

Every layer maps directly to test categories:

| Layer | Test Type |
|-----|----------|
| Ingestion | Contract + Validation Tests |
| Intelligence Core | Deterministic Inference Tests |
| Registry | Consistency + Rollback Tests |
| API | Schema + Auth + Load Tests |

No component exists without tests.

---

## 10. Open Source Readiness

MedIntel is structured so that:
- Core logic is inspectable
- Sensitive configs are isolated
- Contributors can run locally without medical data

This is **intentional signaling**, not accidental openness.

---

## 11. Dependency Order (Critical)

1. **MedIntel Documentation (this phase)**
2. Test Coverage & Pipeline Validation
3. API Surface Specification
4. Frontend Usability
5. Open Source Signal Enhancements
6. DeSci Repo (only after MedIntel stabilizes)

---

## 12. Final Architectural Assertion

> MedIntel is not an app.  
> It is an **intelligence substrate**.

Everything downstream inherits its correctness—or its flaws.

This document defines the ground truth.
