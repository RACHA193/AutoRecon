# AutoRecon

[![AutoRecon Scan](https://github.com/RACHA193/AutoRecon/actions/workflows/scan.yml/badge.svg)](https://github.com/RACHA193/AutoRecon/actions/workflows/scan.yml)
[![Build Status](https://img.shields.io/github/actions/workflow/status/RACHA193/AutoRecon/scan.yml?branch=main)](https://github.com/RACHA193/AutoRecon/actions)
[![License](https://img.shields.io/github/license/RACHA193/AutoRecon)](LICENSE)


**AutoRecon** is a one‑command, Python‑based active reconnaissance and web vulnerability scanning framework designed for penetration testers and security researchers. It automates:

1. **Host discovery** (ping sweep or single host) via Nmap
2. **Service & version enumeration** on common ports via Nmap SYN scans
3. **Web vulnerability scanning** on HTTP/HTTPS (and port 8080) using Nikto
4. **Markdown report generation** with neatly formatted tables and capped findings

---

## 🎯 Features

* **Easy to use**: `./main.py --target example.com`
* **Flexible discovery**: Accepts single hosts, domains, or CIDR networks
* **Parallel scanning**: Fast SYN scans across multiple ports
* **Capped vuln output**: Shows up to 20 Nikto findings per port, with count of additional results
* **Clean reports**: Generates `reports/report_<target>.md` with sections:

  * Hosts Discovered
  * Service & Version Scan
  * Web Vulnerability Scan

---

## 🚀 Quick Start

1. **Clone the repo**

   ```bash
   git clone https://github.com/yourusername/AutoRecon.git
   cd AutoRecon
   ```

2. **Set up Python environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   sudo apt update && sudo apt install nmap nikto
   ```

3. **Run AutoRecon**

   ```bash
   chmod +x main.py
   ./main.py --target testphp.vulnweb.com
   ```

4. **View the report**

   ```bash
   less reports/report_testphp.vulnweb.com.md
   ```

---

## 📄 Sample Report

![Sample Report Screenshot](docs/sample_report.png)

---

## ⚙️ Configuration

* **Port List**: Modify `modules/scan.py` `PORT_LIST` constant
* **Timeouts**: Adjust `timeout` in `modules/vulnscan.py`
* **Max Findings**: Change `max_display` default in `web_vuln_scan`

---

## 🛠️ Roadmap & Next Steps

* [ ] GitHub Actions scheduled scans & auto‑commit reports
* [ ] Docker container for one‑step deployment
* [ ] HTML/PDF report generation via Pandoc & Jinja2 templates
* [ ] Plugin architecture for custom scanners
* [ ] Integration of Nmap vuln scripts and OWASP ZAP

---

## 📚 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

*Built by a recent M.S. Cybersecurity graduate from UMD.*
