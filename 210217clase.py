import pygame,random
from math import sqrt
from pygame.locals import *
xmax = 850    #ancho de la pantalla
ymax = 600     #alto de la pantalla

class Particle():
    def __init__(self, iniciox, inicioy):

        self.x = iniciox
        self.y = inicioy
        self.sx = iniciox
        self.sy = inicioy

    def move(self,d,mx,my):

        if self.y < 0:

            self.x=self.sx
            self.y=self.sy

        else:
            self.y-=random.randint(-10,10) #Valores permitidos en el eje y
            
        self.x+=random.randint(-10,10) #Valores permitidos en el eje X        

def main():  #declaracion de colores
    pygame.init()
    screen = pygame.display.set_mode((xmax,ymax))
    white = (255,255,255) 
    black = (0,0,0)
    grey = (100,100,100)
    d = 15
    tam = d //2 - 2
    umbral = 2 * tam
    n = 300
    colal= (random.randint(100,200),random.randint(100,200), random.randint(100,200))

    clock=pygame.time.Clock()

    colores = []
    particulas = []
    for part in range(n):  #Cantidad de partículas
        particulas.append( Particle(d*random.randint(0,xmax//d),d*random.randint(0,ymax//d)) )#Ajuste de posicion inicial
        colores.append ((random.randint(50,250),random.randint(50,250), random.randint(50,250)))
     
    exitflag = False
    while not exitflag:
        for event in pygame.event.get():
            if event.type == QUIT:
                exitflag = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exitflag = True

        screen.fill(black)
        for p in particulas:
            p.move(d,xmax,ymax)

        for pos in range(n):
            p = particulas[pos]
            for otropos in range(pos + 1, n):
                otro = particulas[otropos]
                distancia = sqrt((p.x - otro.x)**2 + (p.y - otro.y)**2)
                if distancia < umbral:
                    r = (colores[pos][0] + colores[otropos][0]) // 2
                    g = (colores[pos][1] + colores[otropos][1]) // 2
                    b = (colores[pos][2] + colores[otropos][2]) // 2
                    colores[pos] = colores[otropos] = (r, g, b)
            pygame.draw.circle(screen, colores[pos], (p.x, p.y), tam)

        pygame.display.flip()
        clock.tick(8) #Ajuste del tiempo
    pygame.quit()

if __name__ == "__main__":
    main()
