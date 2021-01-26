import sys
from config.judge import *

def main():
	command = sys.argv[1]
	filename = sys.argv[2]
	ext = "." + sys.argv[3]
	if(command == 'run'):
		compile_arq(filename, ext)
		run_test_case(filename, ext)
	elif(command == 'create'):
		create(filename, ext)
	else:
		print("comando nao reconhecido")
main()