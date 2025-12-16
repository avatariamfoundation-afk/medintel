class RPMPostOpAssessor:
    """
    NeuroGrid MedIntel – Post-Operative Remote Patient Monitoring Assessor

    Evaluates post-operative patient data from wearables or
    bio-cybernetic devices and produces a structured health assessment.
    """

    def assess(self, vitals: dict) -> dict:
        risk_score = 0

        if vitals.get("heart_rate", 0) > 110:
            risk_score += 2
        if vitals.get("oxygen_saturation", 100) < 92:
            risk_score += 3
        if vitals.get("temperature", 36.5) > 38.0:
            risk_score += 2

        status = "stable"
        if risk_score >= 4:
            status = "requires_attention"
        if risk_score >= 6:
            status = "high_risk"

        return {
            "risk_score": risk_score,
            "status": status,
            "recommended_action": self._recommend_action(status)
        }

    def _recommend_action(self, status: str) -> str:
        if status == "stable":
            return "Continue remote monitoring"
        if status == "requires_attention":
            return "Notify healthcare professional"
        if status == "high_risk":
            return "Immediate clinical intervention recommended"

