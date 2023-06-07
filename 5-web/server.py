import socket
import time

sock = socket.socket()
try:
    sock.bind(('', 80))
    port = 80
except OSError:
    sock.bind(('', 8080))
    port = 8080
sock.listen(5)
print(f'Сервер запущен и слушает порт {port}')

while True:
    conn, addr = sock.accept()
    print('Соединение установлено с: {}'.format(addr))

    data = conn.recv(8192)
    msg = data.decode()
    print(msg)

    nowdate = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())
    print(nowdate)

    with open('1.html', 'r') as file:
        content = file.read()

    content_length = len(content)

    response = f"""HTTP/1.1 200 OK
Date: {nowdate}
Content-Length: {content_length}
Server: MyNewServer v1.0.0 Release
Content-Type: text/html; charset=utf-8
Connection: keep-alive

{content}"""

    conn.send(response.encode())
    conn.close()
