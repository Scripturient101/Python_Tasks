#Python program to find the IP Address of the system
import socket    
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)     
print( IPAddr)
