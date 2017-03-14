import pygame,random
from math import sqrt, fabs
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
    d = 24
    tam = d //2 - 2
    umbral = 4 * tam
    n0 = 10 #particulas al inicio 
    nmeta = 100 #canridad de particulas al final del programa 

    clock=pygame.time.Clock()

    colores = []
    particulas = []
    for part in range(n0):  #Cantidad de partículas inciales con colores al azar 
        particulas.append( Particle(d*random.randint(0,xmax//d),d*random.randint(0,ymax//d)) )#Ajuste de posicion inicial
        colores.append ((random.randint(50,250),random.randint(50,250), random.randint(50,250)))
     
    exitflag = False
    n = n0
    while n < nmeta and not exitflag: #si el numero de particulas es menor a 100 no finaliza el programa, finaliza al completar las 100 particulas
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
            (r, g, b) = colores[pos]
            for otropos in range(pos + 1, n):
                otro = particulas[otropos]
                (tr, tg, tb) = colores[otropos]
                distancia = sqrt((p.x - otro.x)**2 + (p.y - otro.y)**2)
                if distancia < umbral:
                    f = (umbral - distancia) / umbral
                    dr = int(round(f * (colores[pos][0] - colores[otropos][0]) / 2))#numeros entereros en colores (int(round
                    dg = int(round(f * (colores[pos][1] - colores[otropos][1]) / 2))
                    db = int(round(f * (colores[pos][2] - colores[otropos][2]) / 2))
                    colores[pos] = (max(min(255, r - dr), 0), max(min(255, g - dg), 0), max(min(255, b - db), 0))#no puede haber menor a 0 ni mayor a 255
                    colores[otropos] = (min(255, max(tr + dr, 0)), min(255, max(tg + dg, 0)), min(255, max(tb + db, 0)))
            pygame.draw.circle(screen, colores[pos], (p.x, p.y), tam)
        pygame.display.flip()
        clock.tick(8) #Ajuste del tiempo
        if random.random() < 0.1: #random.random es para elegir al azar cuando aapreceran las particulas
          particulas.append( Particle(d*random.randint(0,xmax//d),d*random.randint(0,ymax//d)) )#Ajuste de posicion inicial
          colores.append ((random.randint(50,250),random.randint(50,250), random.randint(50,250)))#una ves que corre el programa ya imprime las nuevas particulas
          n += 1

    pygame.quit()

if __name__ == "__main__":
    main()
