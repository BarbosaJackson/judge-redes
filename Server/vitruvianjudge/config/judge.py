import os

COLOR = {
	'RED': '\033[31m', 
	'GREEN': '\033[32m',
	'BLUE': '\033[33m',
	'BLACK': '\033[30m',
	'WHITE':'\033[37m',
	'BOLD': '\033[1m',
	'WHITE_BACKGROUND': '\033[47m',
	'ORIGINAL_COLOR': '\033[0;0m'
}

def insert_spaces(current_text):
	maxN = 80
	final_text = current_text
	pos = len(current_text)
	while(pos <= maxN):
		final_text += ' '
		pos += 1
	final_text += '|' + COLOR['ORIGINAL_COLOR']
	return final_text

def clean(filename, ext):
	os.system('rm ' + filename)
	os.system('rm ' + filename + '_user_out')
	os.system('rm ' + filename + '.' + ext)

def compare_tests(filename, ext):
	ans = COLOR['BOLD'] + COLOR['WHITE_BACKGROUND']
	text = insert_spaces(ans + COLOR['BLACK'] + "| FILE: " + filename + '.' + ext) + '\n'
	suite_a = get_suite_test(filename + '_user_out')
	suite_b = get_suite_test(filename + '_judge_out')
	for i in range(len(suite_a)):		
		if(suite_a[i] == suite_b[i]):
			text += insert_spaces(ans + COLOR['GREEN'] + '| Case #' + str(i + 1) + ': ACCEPTED') + '\n'
		else:
			text += insert_spaces(ans + COLOR['RED'] + '| Case #' + str(i + 1) + ': WRONG ANSWER') + '\n'
	return text

def compile_file(filename, ext):
	os.system('g++ ' + filename + '.' + ext + ' -o ' + filename + ' -lm')

def get_suite_test(filename):
	suite_test = []
	outputs = open(filename)
	for output in outputs:
		suite_test.append(output)
	return suite_test

def run_test_case(filename, ext):
	os.system('./' + filename + ' < ' + filename + '_inp' + ' > ' + filename + '_user_out')