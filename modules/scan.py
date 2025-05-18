for h in hosts:
    print(f"[+] Scanning services on {h}")
    try:
        # Try SYN scan first (requires root)
        nm.scan(h, PORT_LIST, arguments='-sS -Pn -T4')
        scanned = nm.all_hosts()
        if scanned:
            results[h] = nm[scanned[0]]
        else:
            results[h] = None
    except nmap.PortScannerError:
        print("    ! SYN scan failed (no root). Falling back to TCP connect scan")
        try:
            nm.scan(h, PORT_LIST, arguments='-sT -Pn -T4')
            scanned = nm.all_hosts()
            if scanned:
                results[h] = nm[scanned[0]]
            else:
                results[h] = None
        except Exception as e:
            print(f"    ! Connect scan failed on {h}: {e}")
            results[h] = None
    except Exception as e:
        print(f"    ! Unexpected error on {h}: {e}")
        results[h] = None

return results
