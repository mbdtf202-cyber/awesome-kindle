# Security Policy

## Supported scope

This project is a **documentation / index repository**. It does not ship executable
software; the security-relevant surface is the static site under `docs/` and the
GitHub Actions workflows.

## Reporting

If you find a security issue in the site, the workflows, or a malicious link listed
here, please **do not open a public issue**. Use GitHub's private vulnerability
reporting (Security → Advisories → "Report a vulnerability") or contact the maintainer
directly.

Please include:

- a description and impact,
- steps to reproduce (or the exact URL),
- any suggested fix.

## What is in scope

- `docs/` static site (XSS, unsafe links, dependency issues)
- GitHub Actions / CI configuration
- Any listed resource that points to malware, phishing, or an impersonating site

## What is out of scope

- Issues in third-party tools/sites listed here (report them upstream)
- "Jailbreaking voids warranty" style concerns — see the README's risk notes
