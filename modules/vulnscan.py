# modules/vulnscan.py

import subprocess

# Metadata‐only prefixes to strip out
_META_PREFIXES = (
    "+ Target", "+ SSL Info", "+ Start Time", "+ End Time",
    "+ Scan terminated", "+ 1 host", "----"
)

def web_vuln_scan(host, scan_info, timeout=240, max_display=20):
    """
    Runs Nikto on HTTP/HTTPS/8080, extracts up to max_display findings.
    If no '+ ' lines, fall back to raw output lines.
    """
    results = {}
    if not scan_info:
        return results

    for proto in scan_info.all_protocols():
        for port, meta in scan_info[proto].items():
            if meta["state"] != "open" or port not in (80, 443, 8080):
                continue

            # build the correct URL
            if port == 443:
                url = f"https://{host}"
            elif port == 8080:
                url = f"http://{host}:8080"
            else:
                url = f"http://{host}"

            print(f"[+] Nikto scan: {url}  (timeout={timeout}s)")
            cmd = ["nikto", "-h", url, "-maxtime", str(timeout)]
            try:
                proc   = subprocess.run(cmd,
                                         capture_output=True,
                                         text=True,
                                         timeout=timeout+5)
                output = proc.stdout
            except subprocess.TimeoutExpired:
                print(f"[!] Nikto timed out after {timeout}s on {url}")
                output = f"ERROR: Nikto timed out after {timeout}s on {url}\n"

            lines = output.splitlines()
            # 1) pick out '+ ' vulnerability lines (minus metadata)
            findings = [
                l for l in lines
                if l.startswith("+ ")
                and not any(l.startswith(pref) for pref in _META_PREFIXES)
            ]

            # If no clean '+ ' lines, fall back to raw non‑meta lines
            if not findings:
                raw = [
                    l for l in lines
                    if l.strip()
                    and not any(l.startswith(pref) for pref in _META_PREFIXES)
                    and not l.startswith("----")
                ]
                findings = raw

            # Cap display and count the remainder
            display = findings[:max_display]
            more    = max(0, len(findings) - max_display)

            results[port] = {
                "entries": display,
                "more": more
            }

    return results
