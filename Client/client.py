import socket
import threading
import sys


def file_to_string(filename):
    code = filename + '\n'
    try:
        file = open(filename, 'r')
        lines = file.readlines()
        for line in lines:
            code += line + '\n'
        file.close()
    except FileNotFound:
        code = "FNF"
    return code
    pass

def send_file(connection):
    file_path = input('nome do arquivo: ')
    if file_path =='quit':
        connection.sendall(bytes(file_path, 'UTF-8'))
        return -1
    code = file_to_string(file_path)
    if(code == "FNF"): 
        print("Erro: Arquivo não encontrado, verifique se o arquivo existe")
    else:
        print('enviando arquivo...')
        connection.sendall(bytes(code, 'UTF-8'))
        print('arquivo enviado')
    answer =  connection.recv(2048)
    print(answer.decode())
    return 0


def receive(socket, is_connected):
    while is_connected:
        try:
            send_file(socket)
        except:
            is_connected = False
            break
def main():
    host = sys.argv[1]
    port = int(sys.argv[2])
    print(host, port)

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
    except:
        print("Não foi possivel conectar o servidor")
        input("Aperte qualquer tecla para sair")
        sys.exit(0)

    receiveThread = threading.Thread(target = receive, args = (sock, True))
    receiveThread.start()

main()