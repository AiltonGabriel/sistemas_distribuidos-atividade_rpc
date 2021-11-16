import socket
import json

class OperacoesMatematicas:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    # Abre a conexão com o servidor.
    def __open_connection(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.ip, self.port))

    # Fecha a conexão com o servidor.
    def __close_connection(self):
        self.sock.close()

    # Envia a operação para o servidor, recebe o resultado e o retorna.
    def __realizar_operacao(self, operacao):
        try:
            self.__open_connection()
            self.sock.sendall(json.dumps(operacao).encode())

            result = self.sock.recv(1024).decode()

            self.__close_connection()
        except:
            result = None
        return result

    def soma(self, x, y):
        operacao = {}
        operacao['operacao'] = 'soma'
        operacao['x'] = x
        operacao['y'] = y
        return self.__realizar_operacao(operacao)
    
    def produto(self, x, y):
        operacao = {}
        operacao['operacao'] = 'produto'
        operacao['x'] = x
        operacao['y'] = y
        return self.__realizar_operacao(operacao)
    
    def fatorial(self, x):
        operacao = {}
        operacao['operacao'] = 'fatorial'
        operacao['x'] = x
        return self.__realizar_operacao(operacao)
    