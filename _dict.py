def boldit(texto, cor = ""):
	if (cor == 'PURPLE'):
		cor = '\033[95m'
	elif (cor == 'CYAN'):
		cor = '\033[96m'
	elif (cor == 'DARKCYAN'):
		cor = '\033[36m'
	elif (cor == 'BLUE'):
		cor = '\033[94m'
	elif (cor == 'GREEN'):
		cor = '\033[92m'
	elif (cor == 'YELLOW'):
		cor = '\033[93m'
	elif (cor == 'RED'):
		cor = '\033[91m'
	elif (cor == 'BOLD'):
		cor = '\033[1m'
	elif (cor == 'UNDERLINE'):
		cor = '\033[4m'
	else:
		cor = ""
	return '\033[1m' + cor + texto + '\033[0m'

dicionario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]