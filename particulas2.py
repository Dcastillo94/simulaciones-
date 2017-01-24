permitidos = [-4,-3,-2,-1,0,1,2,3,4,]
particulas = []
for valor in range (-4,5):
	particulas.append(valor)

	
particulas
[-4, -3, -2, -1, 0, 1, 2, 3, 4]
n=[]
from random import choice
choice (permitidos)
0
for particulas in range(7):
	coord = [choice (permitidos)for x in range (2)]
	n.append(coord)
print (n)
