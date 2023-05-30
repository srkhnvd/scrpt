import nmap

def nmap_scan(target_ip):
    scanner = nmap.PortScanner()
    scanner.scan(target_ip, arguments='-Pn -sV')

    for host in scanner.all_hosts():
        if scanner[host].state() == 'up':
            print(f"Host: {host}")
            for port in scanner[host]['tcp']:
                print(f"Port: {port} \tState: {scanner[host]['tcp'][port]['state']}")
                print(f"Service: {scanner[host]['tcp'][port]['name']}")

# main part
print("Enter IP address")
n=input()
target_ip = n

nmap_scan(target_ip)

