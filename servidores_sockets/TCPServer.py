# DUPLA: GABRIELLE CARVALHO & CIBELE VALE
import socket
import threading
import random

#classe que representa uma thread para lidar com cada cliente
class ClientThread(threading.Thread):
    def __init__(self, client_socket, address):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.address = address
        
        

    def run(self):
        print(f"NOVA CONEXÃO: Cliente {self.address} conectado.")
        try:
            while True: #recebe a mensagem do cliente
                data = self.client_socket.recv(1024).decode() # ate 1024 bytes

                if not data: # sai do loop se o cliente desconectar    
                    break
                
                jogadaCliente = data.lower().strip() # converte input para maiscula e remove espaços em branco
                opcoes_validas = ['pedra', 'papel', 'tesoura']

                print(f"[{self.address}] Jogada recebida: '{jogadaCliente}'")
                
                if jogadaCliente not in opcoes_validas:
                    response = "Erro: Jogada inválida! Digite apenas: pedra, papel ou tesoura."
                else:
                    jogada_servidor = random.choice(opcoes_validas)
                    
                    if jogadaCliente == jogada_servidor: #jogadas iguais gera empate
                        resultado = "EMPATAMOS! "
                    elif (jogadaCliente == 'pedra' and jogada_servidor == 'tesoura') or \
                         (jogadaCliente == 'papel' and jogada_servidor == 'pedra') or \
                         (jogadaCliente == 'tesoura' and jogada_servidor == 'papel'):
                        resultado = "VOCÊ VENCEU! " # o cliente venceu
                    else:
                        resultado = "VOCÊ VENCEU!! " # o servidor venceu
                        
                    response = f"\n- Você jogou: {jogadaCliente.upper()}\n- Eu joguei: {jogada_servidor.upper()}\n>>> {resultado}"

                #resposta enviada de volta ao cliente
                self.client_socket.send(response.encode())
        except Exception as e:
            print(f"ERRO: Exceção na conexão com {self.address}: {e}")
        finally:
            self.client_socket.close()
            print(f"INFO: Conexão com {self.address} encerrada.")

#função principal do servidor
def start_server():
    server_host = '127.0.0.1' #localhost
    server_port = 8000 # porta do servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # cria socket TCP (AF_INET = IPv4, SOCK_STREAM = TCP)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # permite reutilizar o endereço

    server_socket.bind(('localhost', server_port))
    server_socket.listen()

    print("="*40)
    print("👾 SERVIDOR JO-KEN-PO TCP LIGADO ({server_host}:{server_port}) 👾")
    print(f"Aguardando um desafiante na porta {server_port} ...")
    print("="*40)
    #loop principal para aceitar conexões de clientes
    while True:
        client_socket, addr = server_socket.accept() # aceita conexoes
        thread = ClientThread(client_socket, addr) # cria thread
        thread.start() # inicia nova thread para o cliente

if __name__ == "__main__": #inicio execução
    start_server()
