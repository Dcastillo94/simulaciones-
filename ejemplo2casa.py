permitidos = [-4,-3,-2,-1,0,1,2,3,4,]
particulas = []
n=[]
for valor in range (-4,5):
	particulas.append(valor)

	
particulas
[-4, -3, -2, -1, 0, 1, 2, 3, 4]
from random import choice
choice (permitidos)
-4
for particulas in range(7):
	coord = [choice (permitidos)for x in range (2)]
	n.append(coord)
	print(n)

from math import sqrt
for coord in n:
    lon = sqrt(sum([x**2 for x in coord]))
    print(lon)

from matplotlib.pylab import hist, show
hist(lon,7, (0,6))
show()
