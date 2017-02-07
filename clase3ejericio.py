import pygame,random

from pygame.locals import *

xpant = 300
ypant = 300
pygame.init()
screen = pygame.display.set_mode((xpant,ypant))
clock=pygame.time.Clock()
particulas = list ()
N = 40
    
X = 0
Y = 1       


clock.tick(20)

for p in range (N):
    part = [random.randint(0,xpant),random.randint(0,ypant)]
    particulas.append(part)

fuera = False
while not fuera:
    screen.fill((150, 150, 150))
    for event in pygame.event.get():
        if event.type == QUIT:
            fuera = True
            break
        
    for i in range(N): 
        for j in range (len(part)):
            part= particulas[i]
            part[j] = part[j] + random.randint(-1, 1)
        print(part)
        pygame.draw.circle(screen, (0,0,0), (particulas[i]), 3)
    pygame.display.flip()
   
pygame.quit()

