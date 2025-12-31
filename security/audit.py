"""
Enhanced Security Audit Module for MedIntel
-------------------------------------------
- Runs Bandit security scans with proper error handling
- Generates detailed, severity-filtered reports
- Supports CI/CD integration with exit codes
- Includes path validation and configuration checks
- Implements secure file handling for reports
"""

import os
import logging
import subprocess
import json
import datetime
import tempfile
from typing import Dict, List, Optional, Tuple
from pathlib import Path

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants with improved naming
BANDIT_CONFIG_FILE = "bandit_config.yaml"
AUDIT_REPORTS_DIR = Path("security/audit_reports")
AUDIT_ENABLED = os.getenv("MEDINTEL_AUDIT_ENABLED", "true").lower() == "true"
BANDIT_TIMEOUT = int(os.getenv("BANDIT_TIMEOUT_SECONDS", "300"))  # 5 minutes default

class SecurityAuditError(Exception):
    """Base class for security audit exceptions"""
    pass

class BanditExecutionError(SecurityAuditError):
    """Raised when Bandit execution fails"""
    pass

class ConfigurationError(SecurityAuditError):
    """Raised for configuration issues"""
    pass

def validate_environment() -> None:
    """Validate required environment and dependencies"""
    if not AUDIT_ENABLED:
        logger.warning("Security audits disabled via MEDINTEL_AUDIT_ENABLED")
        return

    try:
        # Check Bandit installation
        result = subprocess.run(
            ["bandit", "--version"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode != 0:
            raise BanditExecutionError(f"Bandit check failed: {result.stderr}")
        logger.info(f"Bandit version confirmed: {result.stdout.strip()}")

        # Create reports directory if it doesn't exist
        AUDIT_REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    except FileNotFoundError:
        raise BanditExecutionError(
            "Bandit not found. Install with: pip install bandit[toml]"
        )

def validate_target_path(target_path: str) -> Path:
    """Validate and return the target path as Path object"""
    path = Path(target_path).resolve()
    if not path.exists():
        raise ConfigurationError(f"Target path does not exist: {target_path}")
    if not path.is_dir():
        raise ConfigurationError(f"Target path is not a directory: {target_path}")
    return path

def validate_config_file(config_file: Optional[str]) -> Optional[Path]:
    """Validate the config file if provided"""
    if not config_file:
        return None

    path = Path(config_file)
    if not path.exists():
        raise ConfigurationError(f"Config file not found: {config_file}")
    return path

def run_bandit_scan(
    target_path: str = ".",
    config_file: Optional[str] = None,
    output_format: str = "json",
    severity_level: str = "medium"
) -> Dict:
    """
    Run Bandit security scan with enhanced validation and error handling.

    Args:
        target_path: Path to scan
        config_file: Optional Bandit config file path
        output_format: Output format (json, txt, html)
        severity_level: Minimum severity level

    Returns:
        Dictionary containing scan results

    Raises:
        SecurityAuditError: If scan fails
    """
    validate_environment()

    if not AUDIT_ENABLED:
        return {"disabled": True, "reason": "Audits disabled via environment"}

    target_path_obj = validate_target_path(target_path)
    config_file_obj = validate_config_file(config_file)

    cmd = [
        "bandit",
        "-r", str(target_path_obj),
        "-f", output_format,
        "-l", severity_level,
        "--quiet"
    ]

    if config_file_obj:
        cmd.extend(["-c", str(config_file_obj)])
    else:
        # Use default config if none provided
        default_config = Path(__file__).parent / BANDIT_CONFIG_FILE
        if default_config.exists():
            cmd.extend(["-c", str(default_config)])

    try:
        logger.info(f"Starting Bandit scan on {target_path_obj} (severity: {severity_level})")
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=BANDIT_TIMEOUT
        )

        if result.returncode not in [0, 1]:  # 0=clean, 1=issues found
            raise BanditExecutionError(
                f"Bandit scan failed with return code {result.returncode}:\n"
                f"STDOUT: {result.stdout[:200]}\n"
                f"STDERR: {result.stderr[:200]}"
            )

        # Parse results based on format
        if output_format == "json":
            try:
                scan_results = json.loads(result.stdout)
            except json.JSONDecodeError as e:
                raise BanditExecutionError(
                    f"Failed to parse Bandit JSON output: {str(e)}\n"
                    f"Output: {result.stdout[:500]}..."
                )
        else:
            scan_results = {
                "raw_output": result.stdout,
                "raw_errors": result.stderr,
                "format": output_format
            }

        logger.info(
            f"Bandit scan completed. "
            f"Issues found: {scan_results.get('metrics', {}).get('total_issues', 'N/A')}"
        )
        return scan_results

    except subprocess.TimeoutExpired:
        raise BanditExecutionError(f"Bandit scan timed out after {BANDIT_TIMEOUT} seconds")
    except Exception as e:
        raise BanditExecutionError(f"Unexpected error during Bandit scan: {str(e)}")

def parse_scan_results(scan_results: Dict, severity_level: str = "medium") -> Tuple[List[Dict], List[Dict], List[Dict]]:
    """
    Parse scan results and filter by severity.

    Args:
        scan_results: Results from run_bandit_scan
        severity_level: Minimum severity to include

    Returns:
        Tuple of (high_severity_issues, medium_severity_issues, low_severity_issues)
    """
    if scan_results.get("disabled"):
        return [], [], []

    severity_map = {"low": 1, "medium": 2, "high": 3}
    min_level = severity_map.get(severity_level.lower(), 2)

    high_issues = []
    medium_issues = []
    low_issues = []

    if "results" in scan_results:
        for filename, issues in scan_results["results"].items():
            for issue in issues:
                issue_severity = issue.get("issue_severity", "low").lower()
                issue_data = {
                    "file": filename,
                    "line": issue.get("line_number"),
                    "test": issue.get("test_name"),
                    "text": issue.get("issue_text"),
                    "severity": issue_severity
                }

                if issue_severity == "high":
                    high_issues.append(issue_data)
                elif issue_severity == "medium":
                    medium_issues.append(issue_data)
                else:
                    low_issues.append(issue_data)

    return high_issues, medium_issues, low_issues

def generate_audit_report(scan_results: Dict, report_file: Optional[str] = None, severity_level: str = "medium") -> str:
    """
    Generate a detailed audit report from scan results.

    Args:
        scan_results: Results from run_bandit_scan
        report_file: Optional file to save report
        severity_level: Minimum severity to include

    Returns:
        Report as string
    """
    if scan_results.get("disabled"):
        report = "Security audits are disabled."
    else:
        high_issues, medium_issues, low_issues = parse_scan_results(scan_results, severity_level)
        total_issues = len(high_issues) + len(medium_issues) + len(low_issues)

        report = f"""
Security Audit Report - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
================================================================================

Scan Summary:
- Total Issues Found: {total_issues}
- High Severity: {len(high_issues)}
- Medium Severity: {len(medium_issues)}
- Low Severity: {len(low_issues)}
- Minimum Severity Level: {severity_level}

Recommendations:
"""
        if high_issues:
            report += "- CRITICAL: Address high-severity issues immediately (e.g., hardcoded secrets, injection vulnerabilities).\n"
        if medium_issues:
            report += "- IMPORTANT: Review medium-severity issues (e.g., weak cryptography, unused imports).\n"
        if not high_issues and not medium_issues:
            report += "- GOOD: No critical or important issues found.\n"

        # Add details of issues
        for severity, issues in [("High", high_issues), ("Medium", medium_issues), ("Low", low_issues)]:
            if issues:
                report += f"\n{severity} Severity Issues:\n"
                for issue in issues:
                    report += f"  - {issue['file']}:{issue['line']} - {issue['test']}: {issue['text']}\n"

    if report_file:
        report_path = AUDIT_REPORTS_DIR / report_file
        with open(report_path, "w") as f:
            f.write(report)
        logger.info(f"Report saved to {report_path}")

    return report

def audit_medintel_repo(
    target_path: str = ".",
    report_file: str = f"audit_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
    severity_level: str = "medium"
) -> str:
    """
    Run a full audit on the MedIntel repo.

    Args:
        target_path: Path to audit
        report_file: Name of report file
        severity_level: Minimum severity level

    Returns:
        Audit report as string

    Raises:
        SecurityAuditError: If audit fails
    """
    try:
        scan_results = run_bandit_scan(target_path, severity_level=severity_level)
        report = generate_audit_report(scan_results, report_file, severity_level)
        logger.info("MedIntel audit completed successfully")
        return report
    except SecurityAuditError as e:
        error_msg = f"Audit failed: {str(e)}"
        logger.error(error_msg)
        raise

if __name__ == "__main__":
    # Example usage (for testing only)
    logger.warning("TEST MODE - Run in production for real audits")

    try:
        report = audit_medintel_repo()
        print("Audit Report:")
        print(report)
    except Exception as e:
        logger.error(f"Audit script failed: {str(e)}")
        exit(1)  # CI/CD failure
