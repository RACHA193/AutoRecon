# modules/report.py

import os

def generate_report(target, hosts, scan_results, vuln_results):
    os.makedirs("reports", exist_ok=True)
    safe = target.replace("/", "_")
    path = f"reports/report_{safe}.md"

    md = [f"# PenTest Report for **{target}**\n"]
    md += ["## 1) Hosts Discovered", ""] + [f"- {h}" for h in hosts] + [""]

    md += ["## 2) Service & Version Scan", ""]
    for h in hosts:
        md.append(f"### {h}")
        info = scan_results.get(h)
        if not info:
            md.append("_No data_\n")
            continue

        md.append("| Port/Proto | Service | Version |")
        md.append("|------------|---------|---------|")
        for p in info.all_protocols():
            for port, m in info[p].items():
                if m["state"]=="open":
                    md.append(f"| {port}/{p} | {m.get('name','—')} | {m.get('version','—')} |")
        md.append("")

    md += ["## 3) Web Vulnerability Scan", ""]
    for h in hosts:
        md.append(f"### {h}")
        vulns = vuln_results.get(h, {})
        if not vulns:
            md.append("_No HTTP(S) ports open or scan skipped_\n")
            continue

        for port, data in vulns.items():
            md.append(f"#### Port {port}")
            entries = data["entries"]
            more    = data["more"]

            if not entries and more==0:
                md.append("_No findings_\n")
                continue

            for e in entries:
                md.append(f"- {e}")
            if more>0:
                md.append(f"- …and **{more} more** findings not shown")
            md.append("")

    with open(path, "w") as f:
        f.write("\n".join(md))

    print(f"[+] Report written to {path}")
