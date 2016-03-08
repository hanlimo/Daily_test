import socket

target_host = "0.0.0.0"
target_port = 7778

while True:
    
    data = raw_input('>')
    if not data:
        break
    
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    client.connect((target_host, target_port))
    
    client.send(data)
    
    response = client.recv(1024)
    
    if not response:
        break
    
    print response
    
    client.close()
  
  
#address = ('127.0.0.1', 31500)  
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
#s.connect(address)  
  
#data = s.recv(512)  
#print 'the data received is',data  
  
#s.send('hihi')  
  
#s.close()  