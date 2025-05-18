#!/usr/bin/env python3
import argparse

from modules.recon    import discover_hosts
from modules.scan     import service_scan
from modules.vulnscan import web_vuln_scan
from modules.report   import generate_report

def main():
    p = argparse.ArgumentParser(description="AutoRecon — Quick Active Recon + Report")
    p.add_argument("--target", required=True,
                   help="IP, domain, or CIDR network to scan")
    args = p.parse_args()

    # 1) Host discovery
    hosts = discover_hosts(args.target)

    # 2) Service/version scan
    scan_data = service_scan(hosts)

    # 3) Web vulnerability scan
    vuln_data = {}
    for host, info in scan_data.items():
        vuln_data[host] = web_vuln_scan(host, info)

    # 4) Report
    generate_report(args.target, hosts, scan_data, vuln_data)

if __name__ == "__main__":
    main()
