# Vulnerable Dependencies Test Project

This is a test Python project intentionally created with known vulnerable package versions for security testing and vulnerability scanning purposes.

## ⚠️ WARNING

**This project contains intentionally vulnerable dependencies. Do NOT use in production environments.**

## Vulnerable Dependencies

| Package | Version | Vulnerability |
|---------|---------|--------------|
| `urllib3` | 1.26.0 | CVE-2021-33503, CVE-2021-23336 |
| `cryptography` | 43.0.3 | GHSA-79v4-65xg-pq4g (Vulnerable OpenSSL) |
| `pillow` | 8.2.0 | CVE-2021-27921 |
| `jinja2` | 2.11.3 | CVE-2020-28493 |
| `pyyaml` | 5.4.1 | CVE-2020-14343 |

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run the main application:

```bash
python main.py
```

## Project Structure

```
dummy/
├── main.py           # Main application demonstrating all dependencies
├── utils.py          # Utility functions using vulnerable packages
├── config.yaml       # Configuration file (parsed with PyYAML)
├── requirements.txt  # Vulnerable package versions
└── README.md         # This file
```

## Purpose

This project is designed for:
- Testing vulnerability scanners
- Security research
- Educational purposes
- Testing dependency management tools

## Security Notes

All packages in this project have known security vulnerabilities. This is intentional for testing purposes only.

