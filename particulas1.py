import pygame,random
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
    d = 30
    colal= (random.randint(100,200),random.randint(100,200), random.randint(100,200))

    clock=pygame.time.Clock()

    particulas = []
    for part in range(100):  #Cantidad de partículas
        particulas.append( Particle(d*random.randint(0,xmax//d),d*random.randint(0,ymax//d)) ) #Ajuste de posicion inicial
     
    exitflag = False
    while not exitflag:
        for event in pygame.event.get():
            if event.type == QUIT:
                exitflag = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exitflag = True

        screen.fill(white)
        loc= []
        for p in particulas:
            p.move(d,xmax,ymax)
            ub = (p.x,p.y)
            col = colal
            if ub not in loc:
                loc.append(ub)
            else:
                col = black
            pygame.draw.circle(screen, col, (p.x, p.y), d //2 - 2)

        pygame.display.flip()
        clock.tick(8) #Ajuste del tiempo
    pygame.quit()

if __name__ == "__main__":
    main()
