from socket import * 
from threading import Thread

class chatServer:
    def __init__(self):
        self.ipaddr = '127.0.0.1'
        self.port = 8004

    def setting(self):
        self.serverSock = socket(AF_INET, SOCK_STREAM)
        self.serverSock.bind((f'{self.ipaddr}', self.port))
        self.serverSock.listen(1)
        print('%d번 포트로 접속 대기중...'%self.port)

    def setupSock(self):
        self.connectionSock, self.addr = self.serverSock.accept()
        print(str(self.addr), '에서 접속되었습니다.')

    def send(self, msg):
        self.connectionSock.send(msg.encode('utf-8'))

    def receive(self):
        recvData = self.connectionSock.recv(1024)
        if not recvData:
            return None
        return recvData.decode('utf-8')

class ReceiveThread(Thread):
    def __init__(self, server : chatServer):
        super().__init__()
        self.daemon = True
        self.server = server

    def run(self):
        while True:
            self.server.receive()

if __name__ == "__main__":
    test = chatServer()
    test.setting()
    test.setupSock()
    th1 = ReceiveThread(server=test)
    th1.start()
    while True:
        test.send()