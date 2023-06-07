import socket
import datetime
import psutil

sock = socket.socket()
port = 8080
while port in [i.laddr.port for i in psutil.net_connections()]:
    port += 1
    print('new port', port)
sock.bind(('', port))
sock.listen(5)
conn, addr = sock.accept()
print('Connection to has been established {}'.format(addr))
data = conn.recv(8192)
msg = data.decode()
print(msg)
nowdate = datetime.datetime.utcnow().strftime(r"%a, %d %b %Y %H:%M:%S GMT")
print(nowdate)
file = open('1.html', 'r')
content = file.read()
content_length = len(content)
resp = f"""HTTP/1.1 200 OK
Date: {nowdate}
Content-length: {content_length}
Server: SelfMadeServer v0.0.1
Content-type: text/html; charset = utf8
Connection: close

{content}"""
log = open('log.txt', 'w')
log.write(resp)
log.close()
conn.send(resp.encode())

conn.close()