import socket
import logging

def authenticate(username, password):
    with open('credentials.txt', 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(':')
            if username == stored_username and password == stored_password:
                return True
    return False

def start_server(hostname, port):
    while True:
        try:
            sock = socket.socket()
            sock.bind((hostname, port))
            break
        except OSError as e:
            if e.errno == 98:  # Address already in use
                print(f"Порт {port} уже занят. Попробуйте другой порт.")
                port = int(input("Введите номер порта: "))
            else:
                raise
    sock.listen(0)
    logging.info(f"Сервер запущен на порте {port}")
    print(f"Сервер запущен на порте {port}")

    while True:
        try:
            conn, addr = sock.accept()
            logging.info(f"Подключение клиента: {addr}")
            print(f"Подключение клиента: {addr}")

            authenticated = False

            while not authenticated:
                try:
                    data = conn.recv(1024)
                    if not data:
                        break
                    credentials = data.decode()
                    username, password = credentials.split(':')

                    authenticated = authenticate(username, password)

                    if authenticated:
                        conn.send(b"Authenticated")
                        logging.info(f"Пользователь {username} аутентифицирован")
                        print(f"Пользователь {username} аутентифицирован")
                    else:
                        conn.send(b"NotAuthenticated")
                        logging.info(f"Пользователь {username} не аутентифицирован")
                        print(f"Пользователь {username} не аутентифицирован")

                except socket.timeout:
                    logging.info("Время ожидания аутентификации истекло")
                    print("Время ожидания аутентификации истекло")
                    break

            if authenticated:
                msg = ''
                while True:
                    try:
                        data = conn.recv(1024)
                        if not data:
                            break
                        logging.info(f"Прием данных от клиента: {data.decode()}")
                        print(f"Прием данных от клиента: {data.decode()}")
                        msg += data.decode()
                        conn.send(data)
                        logging.info(f"Отправка данных клиенту: {data.decode()}")
                        print(f"Отправка данных клиенту: {data.decode()}")
                    except (socket.timeout, ConnectionAbortedError):
                        logging.info("Соединение с клиентом разорвано")
                        print("Соединение с клиентом разорвано")
                        break
                logging.info("Отключение клиента")
                print("Отключение клиента")
                conn.close()

        except KeyboardInterrupt:
            logging.info("Остановка сервера")
            print("Остановка сервера")
            break

    sock.close()

if __name__ == "__main__":
    logging.basicConfig(filename="server.log", level=logging.INFO, format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    hostname = input("Введите имя хоста (по умолчанию: localhost): ") or "localhost"
    port = int(input("Введите номер порта (по умолчанию: 9092): ") or 9092)

    start_server(hostname, port)
