
import socket

hostname = socket.gethostname()
print("YOUR ARE  WORKING ON:"+socket.gethostbyname(hostname))
print("YOUR IP :"+socket.gethostbyname(hostname))

url=input("ENTER THE URL TO SCAN>>")
print("the ip is:"+url+"is",socket.gethostbyname(url))


import socket

def check_port(host,port):
    try:
        socket.create_connection((host,port),timeougoot=1)
        return port
    except socket.error:
        pass

target_host =input("enter the target_url>>")
print("the ip is:"+target_host+"is",socket.gethostbyname(target_host))
start_port = 1
end_port = 1000

open_port = [port for port in range(start_port,end_port + 1)
             if check_port(target_host,port)]

print("open ports:", open_port)

