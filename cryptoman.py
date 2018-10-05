# coding=utf-8

# +----+ +----+ +    + +----+ +--+-+ +----+    +     + +---+ +-   +
# |      |    | |+  +| |    |    |   |    |    +-- --+ |   | | +  |
# |      +--+-+  --+-  +----+    |   |    |    |  +  | +---+ |  + |
# |      |  |      |   |         |   |    |    |     | |   | |   |+
# +----+ +  +-+    +   +         +   +----+    +     + +   + +   ++
#
# By Luís Alberto Cabús, Nicolas Leão, Matheus Artur Bugman Costa e Fábio Palmeira

# import things from other files
from _art import *
from _encrypt import *
from _decrypt import *

# import only system from os (and path for later)
from os import system, name, path

# define our clear function 
def clear(): 
	if name == 'nt': # for windows 
		_ = system('cls') 
	else: # for mac and linux(here, os.name is 'posix') 
		_ = system('clear')



# public variables but whyyyyyyy 
chave_n = ''
chave_e = ''
chave_d = ''



def main():
	clear()
	print (program_name)
	print ('Oi, este é o programa ' + boldit('CRYPTO_MAN'))
	print ('Este programa é feito para você, que é mega um encriptador.')
	print ('O que você deseja fazer nesta sessão?\n')
	print boldit('1. gerar uma chave\n')
	print boldit('2. encriptar\n')
	print boldit('3. desencriptar\n')
	print boldit('4. quero arte!\n')

	user_option = raw_input("Entre sua opção:\n")

	try:
		val = int(user_option)
		user_option = int(user_option)
	except ValueError:
		print("Você precisa digitar um número inteiro, conforme as opções oferecidas.")
		exit()




	if (user_option == 1):
		clear()
		print (program_name)
		print ('#tama')


	if (user_option == 2):
		clear()
		print (program_name)
		# Chave pública (n, e)
		encrypt_screen()


	if (user_option == 3):
		clear()
		print (program_name)
		# Chave privada (n, d)
		decrypt_screen()






	if (user_option == 4):
		clear()
		print (program_name)
		print ("")
		print (program_art1)
		print ("")
		print (program_art2)


main()