# MODEL_PRIMARY_PERFORMANCE_METRIC.md
**Clinical AI Performance Definition & Enforcement Standard**

---

## 1. Purpose

This document defines the **primary performance metric** governing AI models within the MedIntel system.  
It establishes a mandatory, auditable standard for how model performance is measured, interpreted, enforced, and acted upon across the full model lifecycle.

The objective is to ensure that **clinical safety, diagnostic reliability, and regulatory defensibility** are preserved at all times.

---

## 2. Scope

This standard applies to:

- All clinical and decision-support AI models
- Pre-deployment validation
- Model updates and retraining
- Post-market surveillance
- Incident investigation and rollback decisions

This metric is binding wherever model performance is referenced.

---

## 3. Designated Primary Metric

### Primary Metric: **F1-Score**

The **F1-score** is designated as the system’s primary performance metric.

**Rationale:**
- Balances precision and recall
- Controls for false positives and false negatives
- Suitable for imbalanced clinical datasets
- Interpretable by clinicians, regulators, and auditors

> Accuracy alone is insufficient in clinical environments.

---

## 4. Metric Definition

The F1-score is defined as:

F1 = 2 × (Precision × Recall) / (Precision + Recall)

Where:
- **Precision** = True Positives / (True Positives + False Positives)
- **Recall (Sensitivity)** = True Positives / (True Positives + False Negatives)

All reported F1-scores must include:
- Dataset description
- Class distribution
- Evaluation methodology

---

## 5. Minimum Acceptance Thresholds

Minimum acceptable F1-score thresholds are defined per risk tier:

| Model Risk Class | Minimum F1 |
|------------------|------------|
| Informational    | ≥ 0.75     |
| Decision Support | ≥ 0.82     |
| Clinical Impact  | ≥ 0.88     |
| Safety-Critical  | ≥ 0.92     |

Thresholds are **non-negotiable** unless superseded by stricter regulatory requirements.

---

## 6. Promotion & Deployment Gates

A model may only be:
- Promoted to production
- Deployed to clinical environments
- Used in patient-facing workflows

If:
- The primary F1-score meets or exceeds its class threshold
- Supporting metrics do not indicate compensatory failure
- Validation is independently reproducible

Failure to meet the threshold results in **automatic rejection**.

---

## 7. Change Impact Enforcement

Any model change triggering:
- Architecture modification
- Data source update
- Feature redefinition
- Retraining with new datasets

Requires:
- Recalculation of F1-score
- Comparison against prior baseline
- Documented justification for any variance

Performance regression beyond tolerance triggers rollback.

---

## 8. Post-Market Surveillance Coupling

Live monitoring must track:
- Rolling F1-score estimates
- Drift indicators impacting precision or recall
- Subgroup-specific F1 degradation

Sustained degradation below threshold mandates:
- Escalation
- Human review
- Temporary suspension if unresolved

---

## 9. Audit & Traceability

All F1-score evaluations must be:
- Timestamped
- Version-linked
- Dataset-referenced
- Retained indefinitely

Auditors must be able to trace:
Model Version → Dataset → Evaluation → Decision Outcome

---

## 10. Regulatory Alignment

This standard aligns with:
- FDA GMLP performance monitoring expectations
- EU AI Act risk-based system controls
- ISO 13485 software validation principles
- Post-market surveillance obligations

---

## 11. Prohibited Practices

The following are prohibited:
- Metric substitution without approval
- Threshold lowering for expediency
- Selective reporting of favorable F1 results
- Concealment of subgroup performance failures

Violations constitute a governance breach.

---

## 12. Status

**Active – Mandatory Performance Governance Standard**

