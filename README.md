# AutoRecon

[![AutoRecon Scan](https://github.com/RACHA193/AutoRecon/actions/workflows/scan.yml/badge.svg)](https://github.com/RACHA193/AutoRecon/actions/workflows/scan.yml)
[![Build Status](https://img.shields.io/github/actions/workflow/status/RACHA193/AutoRecon/scan.yml?branch=main)](https://github.com/RACHA193/AutoRecon/actions)


This initial release delivers a lean, “minimal viable” version distilled from a range of popular recon frameworks, just enough core scanning, banner‑grabbing, and JSON/CSV output to get you started. It’s intentionally basic, inspired by the best community tools, and built in one day

## What AutoRecon Does

1. **Host Discovery**: Supports single IP/domain or entire networks (CIDR).
2. **Service & Version Enumeration**: Scans common TCP ports (e.g. 21,22,80,443,8080) using Nmap, with automatic fallback if root privileges are not available.
3. **Web Vulnerabilitys Scanning**: Runs Nikto against HTTP/HTTPS endpoints (including port 8080) with built-in timeout and result capping.
4. **Automated Reporting**: Generates a clean Markdown report summarizing discoveries and vulnerabilities.


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AutoRecon.git
   cd AutoRecon
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies and tools:
   ```bash
   pip install -r requirements.txt
   sudo apt update && sudo apt install -y nmap nikto
   chmod +x main.py
   ```

## Usage

Run a complete reconnaissance and vulnerability scan with a single command:
```bash
./main.py --target example.com
```

To skip the web vulnerability phase (for large or sensitive targets):
```bash
./main.py --target example.com --skip-vuln
```

Reports are saved to the `reports/` directory as `report_<target>.md`.

## Why This Matters

AutoRecon demonstrates my ability to:
- Rapidly prototype and deliver a functional security tool
- Automate complex workflows using Python and common pentesting utilities 
- Produce clear, actionable reports that bridge technical and business audiences

I’m eager to bring this same drive and skill set to a forward-thinking security team. If you’re hiring for penetration testing, red teaming, or security automation roles, let’s connect!
