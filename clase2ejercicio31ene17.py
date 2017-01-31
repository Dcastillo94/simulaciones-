from random import randint, choice
n = 30
repeticion = 1000
posicion = randint (0, n)

for paso in range (repeticion):
	print('_'*(posicion - 1)+ 'o'+ '_'*(n - posicion))
	posicion += choice ([1,-1])
	if posicion > n:
		posicion -= n
	elif posicion < 0:
		posicion += n
