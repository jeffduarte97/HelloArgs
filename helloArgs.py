import sys

def helloArgs(arg):
	return ('hello, {}'.format(arg))

while True:
	try:
		if sys.argv[1] != '':
			print(helloArgs(sys.argv[1]))
			break
	except Exception as e:
		print('Ops, não foi passado nenhum parametro ao script, tente novamente.')
		break