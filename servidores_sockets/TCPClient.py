# DUPLA: GABRIELLE CARVALHO & CIBELE VALE

# A escolha do protocolo TCP (Transmission Control Protocol) para a implementação do sistema cliente-servidor de Jo-Ken-Pô 
# se deu graças às garantias essenciais fornecidas pela camada de transporte, garantindo segurança e consistência. 
# Por ser um protocolo orientado à conexão, o TCP estabelece um canal de comunicação bidirecional e dedicado antes 
# de qualquer troca de dados, utilizando o mecanismo de handshake de três vias, garantindo que tanto as requisições quanto
#  os resultados sejam entregues sem perda de pacotes, alterações ou duplicação de dados. 
# Além disso, o TCP oferece controle de fluxo e retransmissão transparente de pacotes em caso de oscilações na rede (jitter),
#  o que previne comportamentos imprevisíveis na interface do usuário e assegura o sequenciamento correto das mensagens. 
# Do ponto de vista da arquitetura do servidor, a utilização do TCP associada ao gerenciamento de threads permite isolar 
# cada conexão aceita em uma execução paralela e independente. Dessa forma, o servidor é capaz de atender múltiplos clientes 
# simultaneamente de forma estável e responsiva, sem bloquear a escuta de novas conexões e garantindo o pleno funcionamento 
# dos requisitos propostos para o sistema. 


import socket
import time

def start_client():
    server_address = '127.0.0.1'
    server_port = 8000

    print("="*40)
    print("DESAFIO JO-KEN-PO (TCP)")
    print("Regras: Digite 'pedra', 'papel' ou 'tesoura' para jogar.")
    print("Digite 'sair' para encerrar a conexão.")
    print("="*40)

    try:

        # Criação do socket TCP e conexão com o servidor
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            print(f"[INFO] Conectando ao servidor {server_address}:{server_port}...")
            client_socket.connect((server_address, server_port))
            print("[INFO] Conectado ao servidor.")
            

            while True:
                # Recebe a jogada via terminal
                message = input("\nSua jogada: ").strip()

                if not message:
                    continue  # Ignora entradas vazias
                
                # Condição para sair do jogo
                if message.lower() == 'sair':
                    print("Desconectando...")
                    break
                    
                client_socket.send(message.encode()) # Envia a string lida para o servidor
                
                data = client_socket.recv(1024).decode() # Recebe a resposta do servidor
                print(f"{data}")
                
                time.sleep(1) # Espera 1 segundo antes de enviar o próximo pedido

    except ConnectionRefusedError:
        print(f"[ERRO] Não foi possível conectar ao servidor {server_address}:{server_port}.")
    except Exception as e:
        print(f"[ERRO] Ocorreu um erro: {e}")

if __name__ == "__main__":
    start_client()
