# MEDINTEL_SCOPE.md

## Purpose

MedIntel is the **intelligence execution layer** of the NeuroGrid ecosystem.  
Its sole responsibility is to perform **deterministic, auditable AI inference** over validated biomedical or biosync data and emit **verifiable artifacts and telemetry** to NeuroGrid Core.

MedIntel is **not** a governance system, **not** a trust authority, and **not** a blockchain controller.

This document defines the **hard scope boundaries** of MedIntel.

---

## In-Scope Responsibilities

MedIntel is explicitly responsible for:

### 1. Deterministic Inference
- Execute AI/ML models with:
  - Fixed seeds
  - Version-pinned models
  - Deterministic preprocessing
- Guarantee reproducibility for identical inputs

### 2. Model Execution & Registry
- Maintain a local, versioned model registry
- Enforce model immutability once registered
- Reject unregistered or mutable models

### 3. Input Validation
- Enforce strict input schemas
- Reject malformed, incomplete, or non-conforming data
- Perform normalization prior to inference

### 4. Artifact Generation
- Produce inference artifacts containing:
  - Output data
  - Model identifier and version
  - Input hash
  - Execution metadata
- Generate cryptographic hashes for all artifacts

### 5. Telemetry Emission
- Emit structured telemetry events for:
  - Successful inference
  - Rejected inputs
  - Execution failures
- Align telemetry formats with NeuroGrid Core expectations

### 6. Cryptographic Attestation
- Sign inference outputs and telemetry
- Provide verifiable proof of origin and integrity
- Support replay detection via nonces or timestamps

### 7. Adapter-Based Integration
- Communicate with NeuroGrid Core exclusively through:
  - Defined adapters
  - Explicit interfaces
- No direct smart contract calls without Core mediation

---

## Explicitly Out of Scope

MedIntel **must never** perform or attempt:

### Governance & Authority
- ❌ No voting logic
- ❌ No proposal creation or execution
- ❌ No DAO interaction logic

### Economic Control
- ❌ No token minting or burning
- ❌ No reward calculation
- ❌ No slashing or penalty enforcement

### Trust Arbitration
- ❌ No validator judgment
- ❌ No dispute resolution
- ❌ No trust score assignment

### On-Chain State Control
- ❌ No direct state mutation
- ❌ No privileged contract access
- ❌ No ownership of Core contracts

### Data Custody
- ❌ No long-term storage of raw biomedical data
- ❌ No PII retention
- ❌ No patient identity management

---

## Authority Model

| Layer | Authority |
|-----|----------|
| MedIntel | Inference execution only |
| NeuroGrid Core | Validation, trust, slashing, governance |
| DAO / Governance | Human and protocol decision-making |

MedIntel **emits facts**.  
NeuroGrid Core **interprets and enforces**.

---

## Trust Boundary

MedIntel operates as a **stateless, attestable compute service**.

- It can be replaced, replicated, or audited
- It holds no irreversible authority
- All outputs are subject to Core verification

---

## Design Invariant

> If MedIntel is compromised, **NeuroGrid Core must remain secure**.

This invariant governs all MedIntel design decisions.

---

## Scope Lock

This scope definition is **final for the current phase**.

Any expansion of MedIntel responsibilities **requires**:
- Explicit governance approval
- Updated trust and security documentation
- Independent review

---

**Status:** Scope Locked  
**Applies To:** MedIntel Enhancement Phase  
**Owner:** Execution Lead  
**Last Updated:** 2026-01

