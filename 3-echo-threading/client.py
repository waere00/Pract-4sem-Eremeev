import socket
import logging
import getpass

def connect_to_server(hostname, port):
    sock = socket.socket()
    sock.setblocking(1)
    sock.connect((hostname, port))
    logging.info("Соединение с сервером")
    print("Соединение с сервером")

    username = input("Введите имя пользователя: ")
    password = getpass.getpass("Введите пароль: ")

    credentials = f"{username}:{password}"
    sock.send(credentials.encode())
    logging.info("Отправка данных серверу: " + credentials)
    print("Отправка данных серверу: " + credentials)

    response = sock.recv(1024)
    if response == b"Authenticated":
        logging.info("Пользователь аутентифицирован")
        print("Пользователь аутентифицирован")
        while True:
            message = input("Введите сообщение для отправки серверу (или введите 'exit' для выхода): ")
            sock.send(message.encode())
            if message == "exit":
                break
            data = sock.recv(1024)
            logging.info("Прием данных от сервера: " + data.decode())
            print("Прием данных от сервера: " + data.decode())
    else:
        logging.info("Пользователь не аутентифицирован")
        print("Пользователь не аутентифицирован")

    sock.close()
    logging.info("Разрыв соединения с сервером")
    print("Разрыв соединения с сервером")

if __name__ == "__main__":
    logging.basicConfig(filename="client.log", level=logging.INFO, format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    hostname = input("Введите имя хоста (по умолчанию: localhost): ") or "localhost"
    port = int(input("Введите номер порта (по умолчанию: 9092): ") or 9092)

    connect_to_server(hostname, port)
