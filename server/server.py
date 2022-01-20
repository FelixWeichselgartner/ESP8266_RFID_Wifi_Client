import socketserver
from datetime import datetime

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))

        data_str = str(self.data, 'utf-8')

        print(data_str)

        if ('uid: ' in data_str):
            uid_str = data_str[5:-1]
            now = datetime.now()
            print(f'{uid_str} tag was recognized at {now}')
            self.request.sendall(bytes(uid_str + " ok\n", 'utf-8'))
        else:
            self.request.sendall(b'wrong data error.\n')

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
