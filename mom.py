import pygame, random
from pygame.locals import *
pygame.init()
import math

mapa=[
"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
"x                x               x               x",
"x                x               x               x",
"x                x               x               x",
"x                x               x               x",
"x                x               x               x",
"x                x               x               x",
"x     xxxxxxx             xxxxxxxx               x",
"x           x                    x               x",
"x           x                    x               x",
"x           x                    x               x",
"x           x                    x               x",
"x           x                    x               x",
"x           x                    x               x",
"x           xxxxxxxxxxxxx        x       x       x",
"x           x           x        x       x       x",
"x           x           x        x       x       x",
"x           x           x        x       x       x",
"x           x           x        x       x       x",
"x           x           x        x       x       x",
"x           x           x        x       x       x",
"xxxxxx      xxxxxxxxxxxxx        xxxxxxxxx       x",
"x                                                x",
"x                                                x",
"x                                                x",
"x                                                x",
"x                                                x",
"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
]
mapa2=[
"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
"x                x                               x",
"x                x                               x",
"x                x                               x",
"x                x                               x",
"x                x                               x",
"x                x                               x",
"xxxxxxxx         xxxxxxxx        xxxxxxxxx       x",
"x                                x       x       x",
"x                                x       x       x",
"x                                x       x       x",
"x                                x       x       x",
"x                                x       x       x",
"x                                x       x       x",
"x       xxxxxxxxx       x                x       x",
"x                       x                x       x",
"x                       x                x       x",
"x                       x                x       x",
"x                       x                x       x",
"x                       x                x       x",
"x                       x                x       x",
"xxxxxxxx         xxxxxxxx        x       xxxxxxxxx",
"x                x               x               x",
"x                x               x               x",
"x                x               x               x",
"x                x               x               x",
"x                x               x               x",
"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
]
mapa3=[
"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
"x                                                x",
"x                                                x",
"x                                                x",
"x                                                x",
"x        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx         x",
"x        x                             x         x",
"x        x                             x         x",
"x        x                             x         x",
"x        x                             x         x",
"x        x         xxxxxxxxxxx         x         x",
"x                            x                   x",
"x                            x                   x",
"x                            x                   x",
"x                  x                             x",
"x        x         x                   x         x",
"x        x         x                   x         x",
"x        x         xxxxxxxxxxx         x         x",
"x        x                             x         x",
"x        x                             x         x",
"x        x                             x         x",
"x        x                             x         x",
"x        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx         x",
"x                                                x",
"x                                                x",
"x                                                x",
"x                                                x",
"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
]

#funciones
def dibujar_muro(superficie,rectangulo):
    pygame.draw.rect(superficie,MARRON,rectangulo)
def dibujar_personaje(superficie,rectangulo):
    pygame.draw.rect(superficie,AZUL,rectangulo)
def construir_mapa(mapa):
    muros = []
    x = 0
    y = 0
    for fila in mapa:#los mapas son matrices
        for muro in fila:
            if muro == "x":
                muros.append(pygame.Rect(x,y,25,20)) #Guarda coordenadas y tamaño.
            x += 15.5 #El equivalente a avanzar un "espacio" horizontalmente.
        x = 0
        y += 20 #El equivalente a avanzar un "espacio" verticalmente.
    return muros
def dibujar_mapa(superficie,muros):
    for muro in muros: #muro es un índice cualquiera.
        dibujar_muro(superficie,muro) #Se dibujan los rect para el laberinto.
def mostrar_bala(x,y,tipo):
    ventana.blit(tipo,(x,y))
def mostrar_puntaje(x,y):
    puntaje_render = tipo_letra.render("Score: "+str(puntaje), True, (255,255,255))
    ventana.blit(puntaje_render,(x,y))
def mostrar_nivel():
    nivel_render = tipo_letra.render("Nivel: "+str(nivel), True, (255,255,255))
    x=0
    y=A-(nivel_render.get_size()[1])
    ventana.blit(nivel_render,(x,y))
def mostrar_fin(): #Funcion game over y subir nivel 
    fin_render = tipo_letra_go.render("GAME OVER", True, (255,255,255))
    x=L//2-(fin_render.get_size()[0]//2)
    y=A//2-(fin_render.get_size()[1]//2)
    ventana.blit(fin_render,(x,y))
def see(pun1,pun2,distancia):
    if math.sqrt(math.pow(pun1.x-pun2.x,2) + math.pow(pun1.y-pun2.y,2)) < distancia:
        return True
    else:
        return False

#Valores ventana
L=800
A=600
#colores
NEGRO  = (0,0,0)
AZUL   = (0,0,225)
MARRON = (150,70,10)
color_fondo = (180,55,78)

#score
tipo_letra_go = pygame.font.Font('freesansbold.ttf', 46)
tipo_letra = pygame.font.Font('freesansbold.ttf', 28)
letra_p_i_L = 10
letra_p_i_A = 10
puntaje = 0
nivel=1

#Valores personaje
orientación = "derecha"
personaje_imagen = pygame.image.load("imagenes_juego/mama_derecha.png")
personaje_rectangulo = personaje_imagen.get_rect()
personaje_rectangulo.x =30
personaje_rectangulo.y= 30
personaje_vel_x = 0
personaje_vel_y = 0
personaje_tamaño= (personaje_imagen.get_size()[0],personaje_imagen.get_size()[1])


#Valores balas
'''
El sistema de disparo consiste en que la bala se encuentra compartiendo la posición del personaje en todo momento, oculta por
el sprite, este es el estado "Espera". En cuanto se dispara, se libera de las coordenadas del jugador y asume unas propias. 
(x_temp y y_temp). Este es el estado "Fuego" Cuando rebota un número determinado de veces, desaparece y vuelve a "Espera".
'''
bala = pygame.image.load("imagenes_juego/bala_2.png")
bala_derecha = pygame.image.load("imagenes_juego/bala2_derecha.png")
bala_izquierda = pygame.image.load("imagenes_juego/bala2_izquierda.png")
bala_abajo = pygame.image.load("imagenes_juego/bala2_abajo.png")
bala_size = (bala.get_size()[0],bala.get_size()[1])

x_temp = 0 #Estas variables se convertirán en las coordenadas de la bala al dispararse.
y_temp = 0
bala_status = "Espera" #La bala se encuentra sin disparar y lista
velocidad = 10 # velocidad inicial de la bala.(horizontal)
velocidad2 = 0 #velocidad inicial vertical. Es 0 para que el primer tiro sea recto.
contador_rebotes = 0#Cuenta el número de rebotes antes de desaparecer.

#Villano
villano_imagen = pygame.image.load("imagenes/marciano4.png")
villano_rectangulo = villano_imagen.get_rect()
villano_tamaño = (villano_imagen.get_size()[0],villano_imagen.get_size()[1])
villano_rectangulo.x = L - (villano_tamaño[0] *2) #coordenadas iniciales
villano_rectangulo.y =  A - (villano_tamaño[1] *2)
villano_vel_x = 0.5
villano_vel_y = 0.5
#ventana
ventana = pygame.display.set_mode((L,A))
muros = construir_mapa(mapa3) #elección mapa

#Bucle principal
reloj = pygame.time.Clock()
correr = True
while correr:
    reloj.tick(120) #Control de fps.
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            correr = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                correr = False
            
            #disparar bala
            if evento.key == pygame.K_SPACE:  
                if bala_status == "Espera":                    
                    x_temp = personaje_rectangulo.x + (personaje_tamaño[0]//4)
                    y_temp = personaje_rectangulo.y + 10 #Se crean copias de la posición del jugador una unica vez, para que la bala no se mueva con la nave al ser disparada.                    
                    bala_status = "Fuego"
                    orientación2 = orientación #"orientación 2" solo funcionará cuando la bala recién ha sido disparada
                    #Si se trabaja con "orientación" en la dirección de la bala, esta se moverá con la nave cada vez que apretemos espacio.
            
            #Movimiento personaje.
            if evento.key == pygame.K_d:
                orientación = "derecha"
                personaje_vel_x = 5
            if evento.key == pygame.K_a:
                orientación = "izquierda"
                personaje_vel_x = -5
            if evento.key == pygame.K_s:
                orientación = "abajo"
                personaje_vel_y = 5
            if evento.key == pygame.K_w:
                orientación = "arriba"
                personaje_vel_y = -5

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_d or  evento.key == pygame.K_a:
                personaje_vel_x = 0
            if evento.key == pygame.K_s or evento.key == pygame.K_w:
                personaje_vel_y = 0
    
    personaje_rectangulo.x += personaje_vel_x
    personaje_rectangulo.y += personaje_vel_y
    
    #Límites del personaje
    if personaje_rectangulo.x > L - personaje_rectangulo.width:
        personaje_rectangulo.x = L - personaje_rectangulo.width
    if personaje_rectangulo.x < 0:
        personaje_rectangulo.x = 0
    if personaje_rectangulo.y > A - personaje_rectangulo.height:
        personaje_rectangulo.y = A - personaje_rectangulo.height
    if personaje_rectangulo.y < 0:
        personaje_rectangulo.y = 0

    #Orientación del personaje.
    if orientación == "arriba":
        personaje_imagen = pygame.image.load("imagenes_juego/mama_arriba.png")
    elif orientación == "abajo":
        personaje_imagen = pygame.image.load("imagenes_juego/mama_abajo.png")
    elif orientación == "derecha":
        personaje_imagen = pygame.image.load("imagenes_juego/mama_derecha.png")
    elif orientación == "izquierda":
        personaje_imagen = pygame.image.load("imagenes_juego/mama_izquierda.png")

    #Colisión con los muros.
    for muro in muros:
        if personaje_rectangulo.colliderect(muro):
            personaje_rectangulo.x -= personaje_vel_x
            personaje_rectangulo.y -= personaje_vel_y
    ventana.fill(color_fondo)

    #Trayectoria disparo
    if bala_status=="Fuego":
       #dependiendo de status el disparo se efectúa con diferentes png de balas (direcciones)
        if orientación2 == "arriba": #movimiento y sprites dependiendo de la orientación al disparar.(velocidad 2 es 0 al inicio)
            mostrar_bala(x_temp,y_temp,bala)
            y_temp-=velocidad
            x_temp-=velocidad2
        elif orientación2 == "abajo":
            mostrar_bala(x_temp,y_temp,bala_abajo)
            y_temp+=velocidad
            x_temp+=velocidad2
        elif orientación2 == "izquierda":
            mostrar_bala(x_temp,y_temp,bala_izquierda)
            x_temp-=velocidad
            y_temp-=velocidad2
        elif orientación2 == "derecha":
            mostrar_bala(x_temp,y_temp,bala_derecha)
            x_temp+=velocidad
            y_temp+=velocidad2
        
        if (y_temp<=0 or y_temp>= A or x_temp<=0 or x_temp>= L) or contador_rebotes==10:#Cuando se llega a un borde o se rebota 10 veces.
            contador_rebotes=0 # se reinician los rebotes.
            bala_status="Espera"

    if bala_status== "Espera":
        velocidad=5 # Es importante reiniciar estos valores cada vez.
        velocidad2=0
        mostrar_bala(personaje_rectangulo.x+(personaje_tamaño[0]//4),personaje_rectangulo.y+5,bala)#En espera la bala se queda oculta en la nave.

    #Rebote de las balas
    bala_dimensiones=bala.get_rect(center=(x_temp,y_temp))#Se hallan las coordenadas que va adquiriendo la bala al moverse.
    switch=True #variable usada para el rebote.
    for muro in muros:
        if bala_dimensiones.colliderect(muro) and bala_status=="Fuego" and switch==True:
            contador_rebotes+=1
            if contador_rebotes==1:# estos if se usan para que los rebotes sean más dinámicos, invirtiendo las velocidades cada 2 rebotes.
                velocidad*=-1
                velocidad2= velocidad#Velocidad 2 deja de ser 0.
            elif contador_rebotes%2==0:
                velocidad=velocidad
                velocidad2*=-1
            elif contador_rebotes%2==1:
                velocidad*=-1
                velocidad2=velocidad2
            switch=False 
    
    #villano
    villano_derecha = False
    villano_izquierda = False
    villano_abajo = False
    villano_arriba = False
    if see(villano_rectangulo,personaje_rectangulo,L):
        if villano_rectangulo.x > personaje_rectangulo.x:
            villano_rectangulo.x -= villano_vel_x
            villano_izquierda = True
        if villano_rectangulo.x < personaje_rectangulo.x:
            villano_rectangulo.x += villano_vel_x
            villano_derecha = True

        if villano_rectangulo.y  > personaje_rectangulo.y:
            villano_rectangulo.y -= villano_vel_y
            villano_arriba= True
        if villano_rectangulo.y < personaje_rectangulo.y:
            villano_rectangulo.y += villano_vel_y
            villano_abajo= True
    #limites del villano "que no toque los muros"
    if villano_rectangulo.x > L - villano_rectangulo.width:
        villano_rectangulo.x = L - villano_rectangulo.width
    if villano_rectangulo.x < 0:
        villano_rectangulo.x = 0
    if villano_rectangulo.y > A - villano_rectangulo.height:
        villano_rectangulo.y = A - villano_rectangulo.height
    if villano_rectangulo.y < 0:
        villano_rectangulo.y = 0

    for muro in muros:
        if villano_rectangulo.colliderect(muro):
            villano_rectangulo.x -= villano_vel_x
            villano_rectangulo.y -= villano_vel_y
    ventana.fill(color_fondo)


    ventana.blit(villano_imagen,villano_rectangulo)

    #dibujar mapa
    dibujar_mapa(ventana,muros)
    #dibujar personaje
    ventana.blit(personaje_imagen,personaje_rectangulo)#Se está colocando el png encima del rectángulo.

    mostrar_nivel()
    mostrar_puntaje(650,560)

    pygame.display.update()