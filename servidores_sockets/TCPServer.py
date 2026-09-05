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
        try:
            while True:
                #recebe a mensagem do cliente
                data = self.client_socket.recv(40).decode()
                if not data:
                    break
                print(f"Recebido: {data}")
                
                jogadaCliente = data.lower().strip()
                opcoes_validas = ['pedra', 'papel', 'tesoura']
                
                if jogadaCliente not in opcoes_validas:
                    response = "Erro: Jogada inválida! Digite apenas: pedra, papel ou tesoura."
                else:
                    jogada_servidor = random.choice(opcoes_validas)
                    
                    if jogadaCliente == jogada_servidor: #jogadas iguais gera empate
                        resultado = "EMPATAMOS! "
                    elif (jogadaCliente == 'pedra' and jogada_servidor == 'tesoura') or \
                         (jogadaCliente == 'papel' and jogada_servidor == 'pedra') or \
                         (jogadaCliente == 'tesoura' and jogada_servidor == 'papel'):
                        resultado = "VOCÊ VENCEU! " #
                    else:
                        resultado = "NÃO FOI DESSA VEZ! Gabrielle e Cibele levam o troféu!!"
                        
                    response = f"\n- Você jogou: {jogadaCliente.upper()}\n- Eu joguei: {jogada_servidor.upper()}\n>>> {resultado}"

                #resposta enviada de volta ao cliente
                self.client_socket.send(response.encode())
        except Exception as e:
            print(f"[ERRO] {e}")
        finally:
            self.client_socket.close()
            print(f"[INFO] Conexão com {self.address} encerrada.")

#função principal do servidor
def start_server():
    server_port = 8000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', server_port))
    server_socket.listen()

    opcoes_validas = ['pedra', 'papel', 'tesoura']
    print("="*40)
    print("👾 SERVIDOR JO-KEN-PO TCP LIGADO 👾")
    print(f"Aguardando um desafiante na porta {server_port} ...")
    print("="*40)
    #loop principal para aceitar conexões de clientes
    while True:
        client_socket, addr = server_socket.accept()
        thread = ClientThread(client_socket, addr)
        thread.start()

if __name__ == "__main__": #inicio execução
    start_server()
