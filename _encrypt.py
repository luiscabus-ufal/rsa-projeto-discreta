# coding=utf-8
from os import system, name, path
from _dict import *

def mdc(dividendo, divisor):
	if divisor == 0:
		return dividendo
	else:
		return mdc(divisor, dividendo % divisor)



def define_encryption(p = 17, q = 41):
	n = int(p) * int(q)
	totiente = (p - 1) * (q - 1)

	# encontrar um número "e" co-primo de totiente, maior que 1 e menor que totiente
	# ou seja, MDC(e, totiente)=1
	# chave publica (n, e)

	i = 0
	for x in xrange(3, totiente):
		if (mdc(totiente, x) == 1):
			i = i + 1
		if (i > 4): #pára depois de encontrar o décimo co-primo
			break
	e = x

	global chave_n
	global chave_e
	chave_n = n
	chave_e = e



def encrypt_this_char(original_char, n, e):
	# c = m ^ e mod n
	return (dicionario.index(original_char)+1) ** e % n


def encrypt_screen():

	global chave_n 
	global chave_e

	file_name = raw_input('Qual o nome do seu arquivo a ser encriptado?\n')
	print ('')
	print ('humm.. ' + boldit(file_name) + '... ok...')
	print ('')

	if not (path.exists(file_name)):
		print ('Não achei o arquivo '+ boldit(file_name, 'RED') +'.\n')
		exit()
	
	primo1 = raw_input('Insira o primeiro número primo para gerar uma chave: (ex. 17).\n')
	primo2 = raw_input('Insira o segundo número primo para gerar uma chave: (ex. 41).\n')

	try:
		val = int(primo1)
		val2 = int(primo2)
		define_encryption(int(primo1), int(primo2))
	except ValueError:
		print("Você precisava digitar números primos válidos, mas vamos usar 17 e 41.")
		define_encryption()
	
	file_source = open(file_name, "r")
	file_destination = file_source.name + '.crypt'
	file_destination = open(file_destination, "w")

	file_content = file_source.read()
	for char in file_content:
		# ord(char) # valor ascii do char 
		# dicionario.index(char) # valor dict do char 
		encrypted_char = encrypt_this_char(char, chave_n, chave_e)
		file_destination.write(str(encrypted_char) + ' ')

	print ('\nPronto, seu arquivo encriptado foi gerado e salvo com o nome ' + boldit(str(file_destination.name), 'RED') + '.\n')

	print ('Anote a chaves pública (n, e) '+boldit('(' +str(chave_n)+','+str(chave_e)+').')+'\n')

	file_source.close()
	file_destination.close()