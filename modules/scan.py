for h in hosts:
    print(f"[+] Scanning services on {h}")
    try:
        # Attempt a SYN scan (requires root privileges locally)
        nm.scan(h, PORT_LIST, arguments='-sS -Pn -T4')
        scanned = nm.all_hosts()
        if scanned:
            results[h] = nm[scanned[0]]
        else:
            results[h] = None
    except nmap.PortScannerError as e:
        print(f"[!] SYN scan failed ({e}); retrying with TCP connect scan")
        try:
            nm.scan(h, PORT_LIST, arguments='-sT -Pn -T4')
            scanned = nm.all_hosts()
            if scanned:
                results[h] = nm[scanned[0]]
            else:
                results[h] = None
        except Exception as e2:
            print(f"[!] Connect scan failed too ({e2})")
            results[h] = None
    except Exception as e:
        print(f"[!] Unexpected error scanning {h}: {e}")
        results[h] = None

return results
