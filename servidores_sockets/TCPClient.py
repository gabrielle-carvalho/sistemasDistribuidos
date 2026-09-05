# DUPLA: GABRIELLE CARVALHO & CIBELE VALE
import socket
import time

# Função principal do cliente
def start_client():
    server_address = '127.0.0.1'
    server_port = 8000

    # Criação do socket TCP e conexão com o servidor
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((server_address, server_port))
        print("[INFO] Conectado ao servidor.")
        
        print("="*40)
        print("DESAFIO JO-KEN-PO (TCP)")
        print("Regras: Digite 'pedra', 'papel' ou 'tesoura' para jogar.")
        print("Digite 'sair' para encerrar a conexão.")
        print("="*40)

        # Envia 10 mensagens para o servidor (Adaptado para o loop do jogo)
        while True:
            # Recebe a jogada via terminal
            message = input("\nSua jogada: ")
            
            # Condição para sair do jogo
            if message.lower() == 'sair':
                print("Desconectando...")
                break
                
            client_socket.send(message.encode())
            
            # Aguarda resposta do servidor 
            # (Alterado de 40 para 1024 para a resposta do Jokenpo caber inteira)
            data = client_socket.recv(1024).decode()
            print(f"{data}")
            
            # Espera 2 segundos antes de enviar o próximo pedido
            time.sleep(2)

# Início da execução
if __name__ == "__main__":
    start_client()
