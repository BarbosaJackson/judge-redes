import os

def write_template(filename, ext):
	template = open('utils/template' + ext, "r")
	string_question = ''
	for line in template:
		string_question += line
	template.close()
	question = open(filename + ext, "w")
	question.write(string_question)
	question.close()

def create(filename, ext):
	os.system('touch ' + filename + ext)
	write_template(filename, ext)
	os.system('touch ' + filename + '_judge_out')
	os.system('touch ' + filename + '_inp')