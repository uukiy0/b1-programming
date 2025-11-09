
# Defining a list of risky ports (21, 23, 3389)
devices = [ ("192.168.1.10", [22, 80, 443]),
           ("192.168.1.11", [21, 22, 80]),
            ("192.168.1.12", [23,80, 3389])]

risky_ports = [21, 23, 3389]

print("Scanning network devices...")

risk_count = 0

#Nested for loop, going through the devices the IP address is named ip and the the ports named: open_ports
for ip, open_ports in devices:
    #Loop through every open port
    for port in open_ports:
        #inside the same for loop check for risky ports that were listed
        for risky_port in risky_ports:
#if its equal to a risky one print a warning and count risk
            if port== risky_port:
                print("WARNING " + ip + " has a risky port" +str(port) +" open")
                risk_count = risk_count + 1

print("Scan complete: " + str(risk_count) + " security risks")

    

