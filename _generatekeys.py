# coding=utf-8
from os import system, name, path
from _dict import *

def mdc(dividendo, divisor):
	if divisor == 0:
		return dividendo
	else:
		return mdc(divisor, dividendo % divisor)


def define_public_key(p = 17, q = 41):
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


def define_private_key(p = 17, q = 41, e = 13):
	# what now, general?
	# calcular o inverso multiplicativo modular de "e", que será a chave_d
	n = int(p) * int(q)
	totiente = (p - 1) * (q - 1)

	d = 0

	global chave_n
	global chave_d
	chave_n = n
	chave_d = d



def generate_keys():
	global chave_n 
	global chave_e
	global chave_d

	primo1 = raw_input('Insira o primeiro número primo para gerar as chaves: (ex. 17).\n')
	primo2 = raw_input('Insira o segundo número primo para gerar as chaves: (ex. 41).\n')

	try:
		primo1 = int(primo1)
		primo2 = int(primo2)
		define_public_key(primo1, primo2)
		define_private_key(primo1,primo2,chave_e)
	except ValueError:
		print("Você precisava digitar números primos válidos, mas vamos usar 17 e 41.")
		define_public_key()
		define_private_key()

	print (boldit('\nAnote aí na ordem:\n'))
	print ('Chave pública (n, e): ('+boldit(str(chave_n)+','+str(chave_e))+')\n')
	print ('Chave privada (n, d): ('+boldit(str(chave_n)+','+str(chave_d))+')\n')
	
