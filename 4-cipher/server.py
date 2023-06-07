import socket
import pickle
import os

HOST = '127.0.0.1'
PORT = 8080
KEYS_FILE = 'keys.txt'

# Функция для генерации новой пары ключей и их сохранения в файл
def generate_keys():
    p, g, a = 7, 5, 3
    A = g ** a % p
    keys = (p, g, A)
    with open(KEYS_FILE, 'wb') as file:
        pickle.dump(keys, file)

# Функция для загрузки ключей из файла
def load_keys():
    with open(KEYS_FILE, 'rb') as file:
        keys = pickle.load(file)
    return keys

# Проверяем, существуют ли ключи на диске
if not os.path.exists(KEYS_FILE):
    generate_keys()

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()

# Загружаем ключи из файла
p, g, A = load_keys()

# Принимаем открытый ключ клиента
client_public_key = conn.recv(1024)
client_public_key = pickle.loads(client_public_key)

# Отправляем свой открытый ключ клиенту
conn.send(pickle.dumps(A))

msg = conn.recv(1024)
msg = pickle.loads(msg)

# Расшифровываем сообщение с использованием общего секретного ключа
decrypted_msg = ''
for char in msg:
    decrypted_char = chr(ord(char) - A)
    decrypted_msg += decrypted_char

print(decrypted_msg)

conn.close()
