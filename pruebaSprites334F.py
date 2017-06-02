"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
"""
 
import pygame, random
  
# Definimos algunos colores
Negro = (0, 0, 0)
ColPiel = (245,245,200)
Rojo = (255, 0, 0)
Azul = (0, 0, 255)
Rosa = (255,105,185)
xpos = 0
ypos = 0

# Establecemos el largo y alto de la pantalla
size = (xmax, ymax) = (1000, 600)

class Bacteria(pygame.sprite.Sprite):  
    """
    Esta clase representa la Celula/Bacteria.        
    Deriva de la clase "Sprite" en Pygame
    """
     
    def __init__(self, color, width, height):
        """Constructor. Le pasa el color a la celula/bacteria,
        así como la posición de x,y """
        # Llama a la clase constructor padre (Sprite)
        super().__init__()
 
        # Crea una imagen del bloque y lo rellena de color.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
  
        # Extraemos el objeto rectángulo que posee las dimensiones
        # de la imagen. Estableciendo los valores para rect.x and rect.y
        # actualizamos la posición de este objeto.
        self.rect = self.image.get_rect()
 
        # Variables de instancia que controlan los bordes
        # donde rebotamos
        self.limite_izquierdo = 0
        self.limite_derecho = 0
        self.limite_superior = 0
        self.limite_inferior = 0
 
        # Variables de instancia que controlan nuestras
        # velocidades y dirección actuales
        self.cambio_x = 0
        self.cambio_y = 0
        self.fija = False
            
    # Llamada para cada fotograma.
    def update(self):
        if not self.fija:
            self.rect.x += self.cambio_x
            self.rect.y += self.cambio_y
         
            if self.rect.right >= self.limite_derecho or self.rect.left <= self.limite_izquierdo:
                self.cambio_x *= -1
 
            if self.rect.bottom >= self.limite_inferior or self.rect.top <= self.limite_superior:
                self.cambio_y *= -1

    def colorea(self, color):
        self.image.fill(color)
        
#Iniciamos Pygame
pygame.init()
  
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Simulación: Celulas y Bacterias")

  
# Esta es una lista de 'sprites.' Cada bloque en el programa es 
# añadido a esta lista. La lista es gestionada por la clase llamada  'Group.'
bacterias = pygame.sprite.Group()
  
# This is a list of every sprite. All bloques and the protagonista bloque as well.
celulas_y_bacterias = pygame.sprite.Group()
celulas = pygame.sprite.Group()
cel_enfermas = pygame.sprite.Group()

for i in range(250):
    #  Esto representa un bloque
    bacteria = Bacteria(Azul, 20, 15)
  
    # Establece una ubicación aleatoria para la celula
    bacteria.rect.x = random.randrange(xmax)
    bacteria.rect.y = random.randrange(ymax)
    bacteria.cambio_x = 0
    while bacteria.cambio_x == 0:
        bacteria.cambio_x = random.randrange(-3,4)
    bacteria.cambio_y = 0
    while bacteria.cambio_y == 0:
        bacteria.cambio_y = random.randrange(-3,4)
    bacteria.limite_izquierdo = 0
    bacteria.limite_superior = 0
    bacteria.limite_derecho = xmax
    bacteria.limite_inferior = ymax
     
    #Añade el bloque a la lista de objetos
    bacterias.add(bacteria)
    celulas_y_bacterias.add(bacteria)
      
# Crea el conjunto de celulas de color rosa

for ypos in range(10, ymax, 50):
    for xpos in range(10, xmax, 100):
        # Esto representa una celula
        celula = Bacteria(Rosa, 50, 25)

        # Establece una ubicación para la celula
        celula.rect.x = xpos
        celula.rect.y = ypos

        # Añadimos la  celula a la lista de celulas
        celulas.add(celula)
        celulas_y_bacterias.add(celula)

contador = dict()

for ypos in range(10, ymax, 50):
    xpos = random.randrange(10, xmax, 100)
    for xx in range(10, xmax, 100):
        cel_enferma = Bacteria(Negro, 50, 25)
        contador[cel_enferma] = 0
        cel_enferma.rect.x = xpos
        cel_enferma.rect.y = ypos

        cel_enfermas.add(cel_enferma)
        celulas_y_bacterias.add(cel_enferma)

#Iteramos hasta que el usuario haga click sobre el botón de salir.
hecho = False
conteo = 0  
# Lo usamos para gestionar cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()

  
# --------  Lazo Principal del Programa  -----------
while not hecho:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            hecho = True
  
    # Limpiamos la pantalla
    screen.fill(ColPiel)
     
    # Llamamos al método update() para cada sprite en la lista
    celulas_y_bacterias.update()
    for cel_enferma in cel_enfermas:
        # Observamos si una celula enferma ha colisionado con bacterias
        colisionesByC = pygame.sprite.spritecollide(cel_enferma, bacterias, False)  
        #Comprobamos la lista de colisiones
        for bacteria in colisionesByC:
            contador[cel_enferma] += 1
            bacteria.colorea((100, 100, 100))
            bacteria.fija = True
 
        cel_enferma.colorea((min(0.5 * contador[cel_enferma], 255), 105, 185))
    conteo += 1

    # Dibujamos todos los sprites
    celulas_y_bacterias.draw(screen)
      
    # Limitamos a 60 fotogramas por segundo
    reloj.tick(60)
  
    #Avanzamos y actualizamos la pantalla con todo lo que hemos dibujado.
    pygame.display.flip()

print(" ".join([str(x) for x in contador.values()]))  
print(conteo)
pygame.quit()
