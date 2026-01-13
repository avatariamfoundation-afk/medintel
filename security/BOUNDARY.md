# BOUNDARY.md  
**Repository:** neurogrid-medintel  
**Audience:** Hackathon Judges · Security Reviewers · System Architects  
**Status:** Canonical / Execution-Ready  
**Last Updated:** 2026-01-13

---

## 1. Purpose

This document defines the **hard operational boundaries** of the NeuroGrid MedIntel system.

MedIntel is **not** a medical device, **not** a diagnostic engine, and **not** a clinical decision system.  
It is a **medical intelligence orchestration layer** designed to coordinate, route, and audit AI-based medical tools **without producing clinical judgments**.

These boundaries are explicit, enforced, and non-negotiable.

---

## 2. Core Boundary Statement

> **MedIntel does not diagnose, prescribe, predict outcomes, or replace clinicians.**

The system operates strictly within:
- Research
- Simulation
- Decision-support infrastructure
- AI orchestration and governance

Any interpretation beyond this is a violation of design intent.

---

## 3. Functional Boundaries

### 3.1 What MedIntel IS

MedIntel is allowed to:
- Orchestrate multiple AI models or tools
- Normalize inputs and outputs
- Route tasks based on metadata
- Track execution telemetry
- Generate audit artifacts
- Operate entirely on synthetic data
- Provide non-clinical risk signals (abstracted, non-actionable)

---

### 3.2 What MedIntel IS NOT

MedIntel will never:
- Diagnose diseases
- Recommend treatments
- Prescribe medications
- Generate clinical decisions
- Provide patient-specific medical advice
- Interface with real patient data
- Replace licensed professionals

---

## 4. Medical Boundary Enforcement

### 4.1 Output Constraints

All outputs must satisfy:
- Abstracted scoring only (no thresholds tied to diagnoses)
- Non-actionable classifications
- Research-only labeling
- Explicit disclaimers embedded in artifacts

Example allowed output:
```json
{
  "status": "OBSERVATIONAL",
  "signal_strength": 0.42,
  "context": "synthetic research signal"
}
Disallowed output:

```json

{
  "diagnosis": "Hypertension",
  "treatment": "Start ACE inhibitor"
}
4.2 Language Restrictions
Prohibited terminology in code, docs, and UI:

"diagnose"

"treat"

"prescribe"

"cure"

"medical advice"

Allowed terminology:

"signal"

"indicator"

"observation"

"research output"

"non-clinical inference"

---

## 5. Data Boundary
MedIntel strictly enforces:

Synthetic-only data inputs

No personal identifiers

No real-world telemetry

No integration with clinical systems

Violations automatically invalidate the system’s safety posture.

---

## 6. AI Boundary
AI components are constrained to:

Narrow, deterministic roles

Transparent input/output contracts

No autonomous decision authority

No continuous learning from live data

AI is treated as a tool, not an agent.

---

## 7. Regulatory Boundary
MedIntel is intentionally positioned:

Outside medical device classification

Outside regulated clinical AI systems

Outside patient-facing applications

This avoids:

FDA / SAHPRA / CE classification

Clinical validation requirements

Medical liability exposure

---

## 8. Enforcement Mechanisms
Boundary compliance is enforced through:

Documentation hard constraints

Output schema validation

CI checks for restricted language

Explicit runtime mode flags (e.g., RESEARCH_ONLY)

---

## 9. Judge-Facing Summary
This boundary framework demonstrates:

High regulatory awareness

Ethical foresight

Mature system governance

Responsible AI usage

The system is safe to judge, safe to fork, and safe to explore.

---

10. Non-Negotiable Clause
Any modification that violates these boundaries is a forked system, not MedIntel.

End of Document
