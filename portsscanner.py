#socket to communicate with other network to TCP/UDP

import socket
import termcolor 

Ports_services ={20: "FTP Data",21: "FTP Control",22: "SSH",23: "Telnet",
25: "SMTP",53: "DNS",80: "HTTP",443: "HTTPS",3306: "MySQL",
5432: "PostgreSQL",8080: "HTTP Proxy"}


def get_port_services(port):
	servicename = Ports_services.get(port, socket.getservbyport(port, 'tcp'))
	return termcolor.colored(servicename, 'yellow')


def scan(target, port):
	print('\n' + ' Starting Scan For ' +str(target))
	for port in range(1,ports):
		scan_port(target, port)
    

def scan_port(ipaddress, port):
	try:
		sock = socket.socket() #call socket  function
		sock.settimeout(2) #set a time out for connection
		sock.connect((ipaddress, port)) #connection

		service_name =get_port_services(port)
		print(f"[+]Port {port} Is Open: {service_name} ")
		sock.close()
	except:
		pass


#Main
targets = input("[*] Enter Targets To Scan(split with ,): ")
ports = int(input("[*] Enter How Many Port You Need To Scan: "))

if ',' in targets: #muliple ip check
	print("[*] Scanning Multiple Targets")
	for ipadd in targets.split(','):
		scan(ipadd.strip(' '),ports)
    
else: #single ip
	scan(targets, ports)

