## API_READ_SURFACE_SPECIFICATION.md

Repository: neurogrid-medintel
Audience: Hackathon Judges, Reviewers, Open‑Source Contributors
Purpose: Define a clear, inspectable, non‑deceptive API surface that exposes MedIntel’s capabilities without implying medical diagnosis, treatment, or regulatory overreach.

---

## 1. Design Principles (Judge‑Facing)

Read‑Only by Default
No endpoint performs irreversible actions on patient data.

Non‑Diagnostic Output
All responses are analytical signals or model metadata, never medical advice.

Composable + Auditable
APIs expose structured artifacts suitable for chaining, logging, and test replay.

Fail‑Closed
If upstream models or data are unavailable, endpoints return deterministic errors.

Hackathon‑Safe Scope
No claims of clinical accuracy, regulatory approval, or real‑world deployment.

---

## 2. API Surface Overview
Category	Purpose	Exposure
/health	System sanity & CI checks	Public
/capabilities	Declared AI tooling	Public
/analyze	Analytical inference	Restricted
/models	Model registry	Public
/telemetry	Read‑only logs	Restricted
/docs	Self‑describing API	Public

---

## 3. Authentication Model
X‑API‑KEY: optional (demo mode)
Authorization: Bearer <token> (future‑ready)

For hackathon review, authentication is soft‑enforced to allow inspection.

---

## 4. Endpoint Specifications
### 4.1 Health Check
GET /health

Response

{
  "status": "ok",
  "service": "medintel",
  "version": "0.1.0",
  "timestamp": "ISO‑8601"
}

### 4.2 Capability Declaration
GET /capabilities

Purpose
Discloses what the system can do — not what it promises.

{
  "modalities": ["text", "tabular"],
  "analysis_types": [
    "risk_pattern_detection",
    "signal_clustering",
    "trend_extraction"
  ],
  "excluded": ["diagnosis", "treatment", "prescription"]
}

### 4.3 Analytical Inference (Core)
POST /analyze

Request

{
  "input_type": "text",
  "payload": "<redacted medical‑style input>",
  "analysis_profile": "non_clinical"
}

Response

{
  "analysis_id": "uuid",
  "signals": [
    {
      "label": "anomaly_cluster",
      "confidence": 0.72
    }
  ],
  "disclaimer": "Non‑diagnostic analytical output"
}

### 4.4 Model Registry
GET /models
{
  "models": [
    {
      "name": "risk‑encoder‑v1",
      "type": "embedding",
      "status": "active"
    }
  ]
}

### 4.5 Telemetry (Read‑Only)
GET /telemetry?limit=50
{
  "events": [
    {
      "event": "analyze_call",
      "timestamp": "ISO‑8601",
      "status": "success"
    }
  ]
}

No raw inputs or personal data are exposed.

## 4.6 API Self‑Documentation
GET /docs

Returns OpenAPI / Swagger schema auto‑generated from source.

---

## 5. Error Model
Code	Meaning
400	Invalid input schema
401	Unauthorized
422	Analysis rejected (scope violation)
500	Internal failure
{
  "error": "ScopeViolation",
  "message": "Clinical diagnosis is explicitly disabled"
}

---

## 6. Testing & CI Hooks

All endpoints covered by contract tests

/health used as CI pipeline gate

/analyze tested with synthetic inputs only

---

## 7. Judge‑Facing Assurance

✔ No medical advice
✔ Transparent capability disclosure
✔ Deterministic, inspectable outputs
✔ Open‑source friendly schema
✔ Safe for hackathon demonstration

---

## 8. Future Extensions (Post‑Hackathon)

Role‑based access control

Federated model routing

On‑chain inference attestations

## Status: Hackathon‑Ready · Scope‑Hardened · Judge‑Safe
