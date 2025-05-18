# modules/scan.py

import nmap

# ports to scan (comma‑separated)
PORTS = "21,22,25,53,80,110,143,443,445,3306,3389,8080"

def service_scan(hosts):
    """
    For each host, runs a SYN service/version scan on PORTS.
    Returns a dict: host -> nmap scan info object.
    """
    nm = nmap.PortScanner()
    results = {}

    for h in hosts:
        print(f"[+] Scanning services on {h}")
        nm.scan(h, PORTS, arguments='-sS -Pn -T4')
        # nmap host entries might use IP as key
        live = nm.all_hosts()
        if live:
            results[h] = nm[live[0]]
        else:
            results[h] = None
    return results
