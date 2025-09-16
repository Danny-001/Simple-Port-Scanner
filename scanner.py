import sys
import socket
from datetime import datetime

#define target

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # Translate hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python scanner.py <ip>")
    
#add a pretty banner

print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)


try:
    for port in range(1, 65535):  # Scan all ports from 1 to 65535
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
        socket.setdefaulttimeout(1)  # Set a timeout of 1 second
        result = s.connect_ex((target, port))  # Connect to the target on the specified port
        if result == 0:  # If the connection is successful
            print(f"Port {port} is open")
        s.close()  # Close the socket

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to server.")
    sys.exit()

    