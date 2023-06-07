import socket
import pickle

HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.connect((HOST, PORT))

# Генерируем ключи на клиенте
p, g, a = 7, 5, 3
A = g ** a % p

# Отправляем открытый ключ серверу
sock.send(pickle.dumps(A))

# Получаем открытый ключ сервера
B = pickle.loads(sock.recv(1024))

# Вычисляем общий секретный ключ
s = B ** a % p

# Отправляем зашифрованное сообщение серверу
message = 'Hello, server!'
encrypted_msg = ''
for char in message:
    encrypted_char = chr(ord(char) + s)
    encrypted_msg += encrypted_char

sock.send(pickle.dumps(encrypted_msg))

sock.close()
