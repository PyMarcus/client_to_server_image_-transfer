import socket
import sys
from threading import Thread
from sys import argv
from colorama import Fore


class Server:
    def __init__(self, host, port):
        self.__host = host
        self.__port = port

    @property
    def host(self):
        return self.__host

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, new_port):
        self.__port = new_port

    @staticmethod
    def info_conn(adress):
        print(Fore.LIGHTBLUE_EX + f"Recebendo conexão de host: {adress} ")

    def run(self):
        tcp_ip = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        home = (self.__host, self.__port)
        tcp_ip.bind(home)  # turn on
        tcp_ip.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # allow reuse ip
        tcp_ip.listen(1)
        print(Fore.BLUE + f"Ouvindo em {self.__host} : {self.__port}")
        print("Para finalizar, ctrl + c")
        while True:
            conn, addr_client = tcp_ip.accept()
            Server.info_conn(addr_client)
            while True:
                received = conn.recv(65535)
                new = received
                with open('download_image.jpg', 'wb') as gg:
                    gg.write(new)
                if len(received) > 0:
                    print(f"cliente diz: {received}")
                print("Imagem salva")
                break


class Client:
    def __init__(self, ip, port):
        self.__ip = ip
        self.__port = port

    @property
    def ip(self):
        return self.__ip

    @property
    def port(self):
        return self.__port

    @ip.setter
    def ip(self, new_ip):
        self.__ip = new_ip

    @port.setter
    def port(self, new_port):
        self.__port = new_port

    @staticmethod
    def conn():
        print(Fore.GREEN + "Conectando ao servidor...")

    def run(self):
        tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv_addr = (self.__ip, self.__port)
        tcp_client.connect(serv_addr)
        Client.conn()
        print("Para finalizar, ctrl + c")
        msg = f"{socket.gethostname()} - conectando...".encode()
        while True:
            # cp_client.send(msg)
            with open('path', 'rb') as f:  # PycharmProjects/webscrapping_js/base.py
                file = f.read()
                tcp_client.sendall(file)
            print("Imagem enviada!")
            break
        sys.exit(1)


class Main:
    """Main class"""
    @classmethod
    def run_serv(cls):
        serv = Server('localhost', 6000)
        thread = Thread(serv.run(), args=())
        thread.start()
        thread.join()

    @classmethod
    def run_client(cls):
        client = Client('localhost', 6000)
        thread = Thread(client.run(),args=())
        thread.start()
        thread.join()


if __name__ == '__main__':
    try:
        if argv[1] == 'server':
            th = Thread(Main.run_serv(), args=())
            th.start()
            th.join()
        elif argv[1] == 'client':
            th = Thread(Main.run_client(), args=())
            th.start()
            th.join()
        else:
            print("Por favor, rode o servidor como: python3 system.py server\nApós isso, rode o cliente: python3 "
                  "system.py client")
    except IndexError:
        print(Fore.RED + "Abra o terminal e: ")
        print("Por favor, rode o servidor como: python3 system.py server\nApós isso, rode o cliente: python3 "
              "system.py client")
