from concurrent.futures import thread
from http import client
from socket import *
from threading import Thread


class chatClient:
    def __init__(self):
        self.ipaddr = '127.0.0.1'
        self.port = 8004

    def setting(self):
        self.clientSock = socket(AF_INET, SOCK_STREAM)
        self.clientSock.connect((f'{self.ipaddr}', self.port))
        print(f'{self.port}번 포트로 접속 완료')

    def receive(self):
        recvData = self.clientSock.recv(1024)
        if not recvData:
            return
        return recvData.decode('utf-8')

    def send(self, msg):
        self.clientSock.send(msg.encode('utf-8'))

class ReceiveThread(Thread):
    def __init__(self, client : chatClient):
        super().__init__()
        self.daemon = True
        self.client = client

    def run(self):
        while True:
            self.client.receive()


if __name__ == "__main__":
    test = chatClient()
    test.setting()
    th1 = ReceiveThread(client=test)
    th1.start()
    while True:
        test.send()