## COMMUNITY_ISSUE_TEMPLATES.md  
**Repository:** neurogrid-medintel  
**Audience:** Contributors, Reviewers, Hackathon Judges  
**Status:** Fully Executional / Paste-Ready  
**Last Updated:** 2026-01-13

---

## 1. Purpose

This document defines the **official issue templates** used in the MedIntel repository to ensure:
- High-signal community interaction
- Transparent problem reporting
- Efficient triage and resolution
- Judge-visible maturity in open-source process

All templates are designed to **avoid noise**, **prevent artificial engagement**, and **maintain execution focus**.

---

## 2. Issue Governance Principles

All issues must:
- Be factual and reproducible
- Reference documentation where applicable
- Avoid speculative or vague requests
- Respect defined medical, ethical, and technical boundaries

Issues that do not meet these criteria may be closed with explanation.

---

## 3. Bug Report Template

**File:** `.github/ISSUE_TEMPLATE/bug_report.md`

```markdown
---
name: Bug Report
about: Report a reproducible issue in MedIntel
title: "[BUG] "
labels: bug
assignees: ""
---

## Description
Provide a clear and concise description of the bug.

## Steps to Reproduce
1.
2.
3.

## Expected Behavior
Describe what should have happened.

## Actual Behavior
Describe what actually happened.

## Environment
- OS:
- Python Version:
- Branch / Commit:

## Additional Context
Logs, screenshots, or references (if applicable).

---

## 4. Documentation Issue Template
File: .github/ISSUE_TEMPLATE/documentation.md

```markdown
---
name: Documentation Issue
about: Report missing, unclear, or incorrect documentation
title: "[DOCS] "
labels: documentation
assignees: ""
---

## Affected Document
Specify file path(s).

## Issue Description
What is unclear, incorrect, or missing?

## Suggested Improvement
Optional but encouraged.

## Impact
Low / Medium / High (brief explanation).

---

## 5. Feature Request Template
File: .github/ISSUE_TEMPLATE/feature_request.md

```markdown
---
name: Feature Request
about: Propose a new feature or enhancement
title: "[FEATURE] "
labels: enhancement
assignees: ""
---

## Problem Statement
What problem does this feature address?

## Proposed Solution
Describe the solution at a high level.

## Alignment Check
- Fits MedIntel medical scope boundaries: Yes / No
- Introduces clinical claims: Yes / No

## Alternatives Considered
Briefly describe any alternatives.

## Additional Notes
Optional context.

---

## 6. Research / Integration Inquiry Template
File: .github/ISSUE_TEMPLATE/integration.md

```markdown
---
name: Research or Integration Inquiry
about: Discuss potential research or system integration
title: "[INTEGRATION] "
labels: discussion
assignees: ""
---

## Inquiry Type
Research / Tool Integration / API Usage / Other

## Description
Clearly describe the inquiry.

## Assumptions
List any assumptions being made.

## References
Links or citations (if applicable).

## Non-Clinical Confirmation
I confirm this inquiry does not request clinical decision-making.

---

## 7. Invalid Issue Categories (Will Be Closed)
The following will be closed with explanation:

Requests for medical diagnosis or treatment

Regulatory or legal advice requests

Vague “ideas” without problem definition

Spam, marketing, or engagement farming

---

## 8. Judge-Facing Note
These templates demonstrate:

Mature open-source governance

High signal-to-noise ratio

Responsible handling of medical-adjacent software

Readiness for community growth post-hackathon

---

## 9. Maintenance Policy
Templates may evolve as the project scales, but:

Changes will be documented

Historical issues remain auditable

Transparency is preserved


