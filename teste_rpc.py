from rpc import OperacoesMatematicas

RPC_SERVER = "127.0.0.1"
RPC_PORT = 5050

op = OperacoesMatematicas(RPC_SERVER, RPC_PORT)

soma = op.soma(2, 3)
produto = op.produto(2, 3)
fatorial = op.fatorial(4)

print(soma) # Exibe 5
print(produto) # Exibe 6
print(fatorial) # Exibe 24