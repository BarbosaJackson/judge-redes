import socket
import threading
import os
from vitruvianjudge.config import judge
import sys

list_clients = []
cur_id_client = 0

class Client(threading.Thread):
    def __init__(self, socket, address, id, is_connected):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.id = id
        self.is_connected = is_connected
    
    def __str__(self):
        return str(self.id) +  ' ' + str(self.address[0]) + ':' + str(self.address[1])
    
    def run(self):
        while self.is_connected:
            try:
                data = self.socket.recv(2048).decode()
            except:
                print('Client ' + str(self) + ' desconectou')
                self.is_connected = False
                list_clients.remove(self)
                break
            if data != "":
                send_data = ''
                if(data == 'list-quests'):
                    send_data = ' link                                | nome                         | nome arquivo\n'
                    send_data += '---------------------------------------------------------------------------------------\n'
                    send_data += 'https://thehuxley.com/problem/2827  | Mineração                    | mineracao.cpp\n'
                    send_data += 'https://thehuxley.com/problem/2935  | Alberto, o rato              | alberto.cpp\n'
                    send_data += 'https://thehuxley.com/problem/2746  | A entidade e o boneco        | boneco.cpp\n'
                    send_data += 'https://thehuxley.com/problem/144   | Álbum                        | album.cpp\n'
                    send_data += 'https://thehuxley.com/problem/2402  | Avaliação financeira         | avaliacao.cpp\n'
                else:
                    questions = ['mineracao', 'alberto', 'boneco', 'album', 'avaliacao']
                    filename = create_file(data)
                    print(filename + ' recebido do cliente: #ID ' + str(self.id))
                    question_name = ''
                    extension = ''
                    has_question_name = False
                    for letter in filename:
                        if not has_question_name:
                            if letter == '.':
                                has_question_name = True
                            else:
                                question_name += letter
                        else:
                            extension += letter
                    if not question_name in questions:
                        send_data = 'Erro: questão não cadastrada\n'
                    else:
                        judge.compile_file(question_name, extension)
                        judge.run_test_case(question_name, extension)
                        send_data = judge.compare_tests(question_name, extension)
                        judge.clean(question_name, extension)
                for client in list_clients:
                    if client.id == self.id:
                        client.socket.sendall(bytes(send_data, 'UTF-8'))

def create_file(file):
	has_filename = False
	code = ''
	sz = len(file)
	idx = 0
	line = ''
	filename = ''
	while(idx < sz):
		if (file[idx] == '\n'):
			if not has_filename:
				filename = line
				has_filename = True
			else:
				code += line + '\n'
			line = ''
		else:
			line += file[idx]
		idx += 1
	file = open(filename, 'w')
	file.writelines(code)
	file.close()
	return filename

def newClient(socket):
    while True:
        connection, address = socket.accept()
        global cur_id_client
        list_clients.append(Client(connection, address, cur_id_client, True))
        list_clients[len(list_clients) - 1].start()
        print('[ * ] Nova conexão: ' + str(list_clients[len(list_clients) - 1]))
        cur_id_client += 1

def main():
    host = sys.argv[1]
    port = int(sys.argv[2])

    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.bind((host, port))
    connection.listen(5)
    print('[ * ] servidor iniciado esperando conexões')
    print('[ * ] HOST = ', str(host))
    print('[ * ] PORT = ', str(port))
    server = threading.Thread(target = newClient, args = (connection,))
    server.start()
    
main()