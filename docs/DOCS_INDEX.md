# DOCUMENTATION_INDEX.md

**Repository:** neurogrid-medintel  
**Audience:** Hackathon Judges, Technical Reviewers, Open-Source Contributors  
**Status:** Execution-Ready / Judge-Safe  
**Last Updated:** 2026-01-13

---

## 1. Purpose of This Index

This document provides a **single authoritative navigation map** for the MedIntel repository.  
It is designed to:

- Eliminate reviewer confusion
- Demonstrate architectural maturity
- Surface compliance, safety, and scope boundaries early
- Enable judges to validate functionality **without running code**
- Signal production discipline from a solo builder

No document listed below is speculative. Each is **post-read executable**: after reading, a reviewer understands exactly what exists, what is enforced, and what is intentionally excluded.

---

## 2. Core Orientation (Start Here)

These documents define *what MedIntel is* and *why it exists*.

| Document | Purpose |
|--------|--------|
| `README.md` | Project overview, value proposition, repo structure, and hackathon alignment |
| `ARCHITECTURE_OVERVIEW.md` | System-level design, data flow, and component boundaries |
| `MEDICAL_SCOPE_BOUNDARIES.md` | Explicit declaration of non-diagnostic, non-clinical constraints |

---

## 3. System Design & Execution Flow

These documents prove **systems thinking and execution discipline**.

| Document | Purpose |
|--------|--------|
| `PIPELINE_EXECUTION_FLOW.md` | Step-by-step runtime flow from input → orchestration → output |
| `ORCHESTRATION_ENGINE.md` | Control logic, execution ordering, and failure handling |
| `MODEL_ABSTRACTION_LAYER.md` | How external AI/ML tools are stitched safely and replaceably |
| `DATA_MODEL.md` | Canonical data structures and schema contracts |

---

## 4. API & Integration Surface

These documents define **how MedIntel can be safely consumed**.

| Document | Purpose |
|--------|--------|
| `API_READ_SURFACE.md` | Read-only, non-mutative API surface exposed to integrators |
| `TELEMETRY_SCHEMA.md` | Observable signals, metrics, and execution traces |

---

## 5. Security, Privacy & Ethics (Judge-Critical)

These documents directly address **risk, misuse, and compliance**.

| Document | Purpose |
|--------|--------|
| `SECURITY_MODEL.md` | Threat model, attack surfaces, and enforced constraints |
| `DATA_HANDLING_AND_PRIVACY.md` | Data lifecycle, storage assumptions, and privacy posture |
| `ETHICS_AND_SAFETY_CONSTRAINTS.md` | AI safety rules, refusal policies, and ethical limits |

---

## 6. Validation & Confidence Signals

These documents increase **reviewer confidence without demos**.

| Document | Purpose |
|--------|--------|
| `COVERAGE_REPORT.md` | Test coverage scope and validation philosophy |
| `JUDGE_ADDENDUM.md` | Explicit mapping to hackathon criteria and judging shortcuts |

---

## 7. Reading Paths (For Judges)

### ⏱️ 5-Minute Validation Path
1. README.md  
2. MEDICAL_SCOPE_BOUNDARIES.md  
3. API_READ_SURFACE.md  

### 🧠 Technical Review Path
1. ARCHITECTURE_OVERVIEW.md  
2. PIPELINE_EXECUTION_FLOW.md  
3. MODEL_ABSTRACTION_LAYER.md  
4. SECURITY_MODEL.md  

### 🛡️ Risk & Compliance Path
1. MEDICAL_SCOPE_BOUNDARIES.md  
2. DATA_HANDLING_AND_PRIVACY.md  
3. ETHICS_AND_SAFETY_CONSTRAINTS.md  

---

## 8. What Is Intentionally Not Included

To avoid false claims and overreach:

- ❌ No medical diagnosis
- ❌ No treatment recommendations
- ❌ No patient data ingestion
- ❌ No regulatory assertions (FDA, ANVISA, etc.)
- ❌ No black-box AI behavior

These exclusions are **design choices**, not omissions.

---

## 9. Final Note to Reviewers

MedIntel is designed as a **composable intelligence layer**, not a medical product.  
Its strength lies in:

- Clear boundaries
- Safe AI orchestration
- Open-source inspectability
- Deployment readiness without regulatory risk

This index exists so you never have to guess.

---

