# modules/scan.py

import nmap

# Comma‑separated list of ports to scan
PORT_LIST = "21,22,25,53,80,443,8080,3306"

def service_scan(hosts):
    """
    For each host in `hosts`, attempt:
      1) a SYN scan (-sS)
      2) on failure (no root), a TCP connect scan (-sT)
    Returns: dict mapping host -> nmap scan result or None.
    """
    nm = nmap.PortScanner()
    results = {}

    for h in hosts:
        print(f"[+] Scanning services on {h}")
        try:
            # Try SYN scan first
            nm.scan(h, PORT_LIST, arguments='-sS -Pn -T4')
        except nmap.PortScannerError:
            # Fallback to connect scan if SYN requires root
            print("[!] SYN scan failed (missing privileges?), retrying with -sT")
            nm.scan(h, PORT_LIST, arguments='-sT -Pn -T4')

        scanned = nm.all_hosts()
        if scanned:
            # Use the first returned host (usually the IP)
            real = scanned[0]
            results[h] = nm[real]
        else:
            results[h] = None

    return results
