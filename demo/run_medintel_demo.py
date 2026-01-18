"""
NeuroGrid MedIntel — Runnable Demo
Purpose:
- Demonstrate orchestration of medical AI components
- No diagnostics
- No predictions
- Deterministic, explainable output
"""

import json
from datetime import datetime
import hashlib

def now():
    return datetime.utcnow().isoformat() + "Z"

def deterministic_hash(data):
    return hashlib.sha256(
        json.dumps(data, sort_keys=True).encode("utf-8")
    ).hexdigest()

def ingest_data():
    return {
        "patient_id": "SYNTH-001",
        "source": "synthetic",
        "signals": {
            "heart_rate": 72,
            "spo2": 98
        },
        "timestamp": now()
    }

def run_orchestration(input_data):
    return {
        "engine": "MedIntel-Orchestrator",
        "status": "PASS",
        "notes": "Signals routed to downstream AI modules (mock)",
        "timestamp": now()
    }

def emit_telemetry(input_data, orchestration_result):
    artifact = {
        "type": "MEDINTEL_DEMO_ARTIFACT",
        "input": input_data,
        "result": orchestration_result,
        "generated_at": now()
    }
    artifact["hash"] = deterministic_hash(artifact)
    return artifact

def main():
    print("\n=== MEDINTEL DEMO START ===\n")

    input_data = ingest_data()
    print("Input:")
    print(json.dumps(input_data, indent=2))

    result = run_orchestration(input_data)
    print("\nOrchestration Result:")
    print(json.dumps(result, indent=2))

    artifact = emit_telemetry(input_data, result)
    print("\nTelemetry Artifact:")
    print(json.dumps(artifact, indent=2))

    print("\n=== DEMO COMPLETE ===\n")

if __name__ == "__main__":
    main()
