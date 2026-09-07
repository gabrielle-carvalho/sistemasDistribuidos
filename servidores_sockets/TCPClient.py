# DUPLA: GABRIELLE CARVALHO & CIBELE VALE
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
