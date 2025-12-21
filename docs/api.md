# MedIntel API Documentation

## Overview
The MedIntel API provides secure, AI-driven endpoints for medical data predictions on the BNB Chain. It integrates with decentralized smart contracts for privacy-focused analytics, supporting hackathon goals and long-term company scalability. Built with Node.js and Python, it uses off-chain AI (e.g., Hugging Face) for predictions while ensuring compliance with basic medical data standards.

Key Features:
- AI predictions for symptoms/diagnostics.
- Rate-limited for performance.
- Encrypted data handling.
- P2P networking support for decentralized sharing.

## Endpoints

### POST /predict
Handles AI-based medical predictions from input data (e.g., symptoms).

- **URL**: `http://localhost:3000/predict` (or deployed URL)
- **Method**: POST
- **Headers**:
  - `Content-Type: application/json`
- **Body** (JSON):
  ```json
  {
    "data": "string"  // Required: Description of symptoms (e.g., "fever, cough, fatigue")
  }
