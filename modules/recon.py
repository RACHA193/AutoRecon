# modules/recon.py

import nmap

def discover_hosts(target):
    """
    If target is a single host (IP or domain), returns [target].
    If target is a CIDR/network, does a ping sweep and returns alive hosts.
    """
    nm = nmap.PortScanner()

    # Simple heuristic: if it contains '/', treat as network
    if '/' in target:
        print(f"[+] Performing ping sweep on network {target}")
        nm.scan(hosts=target, arguments='-sn -n')
        hosts = nm.all_hosts()
        print(f"[+] Hosts up: {hosts}")
        return hosts
    else:
        print(f"[+] Single‑host target: {target}")
        return [target]
