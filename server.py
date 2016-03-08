import socket
import threading   
import time

bind_ip = "0.0.0.0"
bind_port = 7778
TARG = (bind_ip, bind_port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print "Listen on:%s:%d" % (bind_ip, bind_port)

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print "Recieve from:(%s, %d)" % TARG
    self_sock_addr = client_socket.getsockname()
    print "address is:(%s,%d)" % self_sock_addr
    client_socket.send("ACK!")
    client_socket.close()
            
while True:
    client, addr = server.accept()
    print "[*]Accept from:%s:%d" % (addr[0], addr[1])
    client_handler = threading.Thread(target=handle_client, 
                                     args=(client,))
    client_handler.start()

            
#import socket  
      
#address = ('127.0.0.1', 31500)  
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # s = socket.socket()  
#s.bind(address)  
#s.listen(5)  
      
#ss, addr = s.accept()  
#print 'got connected from',addr  
      
#ss.send('byebye')  
#ra = ss.recv(512)  
#print ra  
      
#ss.close()  
#s.close()