# coding=utf-8
from os import system, name, path
from _dict import *


def encrypt_this_char(original_char, n, e):
	# c = m ^ e mod n
	return (dicionario.index(original_char)+1) ** e % n


def encrypt_screen():

	file_name = raw_input('Qual o nome do seu arquivo a ser encriptado?\n')
	print ('')
	print ('humm.. ' + boldit(file_name) + '... ok...')
	print ('')

	if not (path.exists(file_name)):
		print ('Não achei o arquivo '+ boldit(file_name, 'RED') +'.\n')
		exit()
	
	key_1 = raw_input('Insira o primeiro número da chave pública:\n')
	key_2 = raw_input('Insira o segundo número da chave pública:\n')

	try:
		key_1 = int(key_1)
		key_2 = int(key_2)
	except ValueError:
		print("Você precisava digitar chaves válidas.")
		exit()

	
	file_source = open(file_name, "r")
	file_destination = open(file_source.name + '.crypt', "w")

	file_content = file_source.read()
	for char in file_content:
		file_destination.write(str(encrypt_this_char(char, key_1, key_2)) + ' ')

	print ('\nPronto, seu arquivo encriptado foi gerado e salvo com o nome ' + boldit(str(file_destination.name), 'RED') + '.\n')

	file_source.close()
	file_destination.close()