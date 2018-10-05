# coding=utf-8
from os import system, name, path
from _dict import *

def define_decryption(p = 17, q = 41):

	global chave_n
	global chave_d
	chave_n = n
	chave_d = e


def decrypt_screen():

	global chave_n 
	global chave_d

	file_name = raw_input('Qual o nome do arquivo a desencriptar?\n')
	print ('')
	print ('ehhhrrr.. ' + boldit(file_name) + '... tá...')
	print ('')

	if not (path.exists(file_name)):
		print ('Não achei o arquivo '+ boldit(file_name, 'RED') +'.\n')
		exit()
	
	key_n = raw_input('Insira o N, primeiro número da sua chave privada (n, d)).\n')
	key_d = raw_input('Insira o D, segundo número da sua chave privada (n, d)).\n')

	try:
		val = int(key_n)
		val2 = int(key_d)
		# define_decryption(int(primo1), int(primo2))
	except ValueError:
		print("Você precisava digitar inteiros válidos.")
		# define_decryption()
		print("Não deu para desencriptar sem a chave privada.")