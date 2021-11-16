import socket
import threading
import time
import json

RPC_PORT = 5050

# Inicia o servido. Recebe as conexões e inicia uma thread para tratar cada uma delas.
def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', RPC_PORT))
    sock.listen(1)
    while True:
        conn, addr = sock.accept()
        threading.Thread(target=connection, args=(conn, addr)).start()

# Função que trata as conexões.
def connection(conn, addr):
    try:
        # Recebendo as informações da operação.
        operacao = recv_operacao(conn)
        print('Connection from {}: {}'.format(addr, operacao))

        # Verifica qual operação foi solicitada e calcula o resultado.
        if operacao['operacao'] == 'soma':
            result = operacao['x'] + operacao['y']
        elif operacao['operacao'] == 'produto':
            result = operacao['x'] * operacao['y']
        elif operacao['operacao'] == 'fatorial':
            result = fatorial(operacao['x'])
            
        # Envia o resultado para o cliente.
        conn.sendall(str(result).encode())
    except:
        pass
    conn.close()

# Recebendo o dicionário com as informações da operação.
def recv_operacao(conn):
    msg = json.loads(conn.recv(1024).decode())
    return msg

# Função para calcular o fatorial de um número.
def fatorial(x):
    if x == 0:
        return 1
    return x * fatorial(x - 1)

def main():
    try:
        # Iniciando uma thread deamon para executar o servidor, para que assim seja possível encerrar o programa como CTRL+C.
        th = threading.Thread(target=server)
        th.daemon = True
        th.start()

        # Loop para que a thread principal não encerre, encerrando assim posteriormente a thread deamon do servidor.
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()