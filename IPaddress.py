#Python program to find the IP Address of the system
import socket  
                  #gethostname() -- return the current hostname
hostname = socket.gethostname()    
                  #gethostbyname() -- map a hostname to its IP number
IPAddr = socket.gethostbyname(hostname)     
print( IPAddr)
