# coding=utf-8
from os import system, name, path
from _dict import *


def decrypt_this_char(encrypted_number, n, d):
	# c = m ^ e mod n
	return (dicionario.index(encrypted_number)) ** d % n - 1


def decrypt_screen():

	file_name = raw_input('Qual o nome do arquivo a desencriptar?\n')
	print ('')
	print ('ehhhrrr.. ' + boldit(file_name) + '... tá...')
	print ('')

	if not (path.exists(file_name)):
		print ('Não achei o arquivo '+ boldit(file_name, 'RED') +'.\n')
		exit()
	
	key_1 = raw_input('Insira o primeiro número da chave privada:\n')
	key_2 = raw_input('Insira o segundo número da chave privada:\n')

	try:
		key_1 = int(key_1)
		key_2 = int(key_2)
	except ValueError:
		print("Você precisava digitar chaves válidas.")
		exit()


	# aqui precisa ajudar o usuário a escolher o arquivo, remover o .crypt do nome.. etc
	file_source = open(file_name, "r")
	file_destination = open(file_source.name + '.decrypt', "w") 

	file_content = file_source.read()
	for char in file_content:
		file_destination.write(str(encrypt_this_char(char, key_1, key_2)) + ' ')

	print ('\nPronto, seu arquivo foi desencriptado e salvo com o nome ' + boldit(str(file_destination.name), 'RED') + '.\n')

	file_source.close()
	file_destination.close()