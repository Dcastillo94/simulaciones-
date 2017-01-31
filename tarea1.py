permitidos = 40
n=[]
grafica = []
import random
	
for particulas in range(50):
	coord = [random.randrange (-permitidos,permitidos,5)for x in range (3)]
	n.append(coord)
	print(n)

from math import sqrt
for coord in n:
    lon = sqrt(sum([x**2 for x in coord]))
    print(lon)
    grafica.append(lon)

from matplotlib.pylab import hist, show
hist(grafica,50, (0,80))
show()
