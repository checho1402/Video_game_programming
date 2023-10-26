import pygame
from pygame.locals import *
import copy
import time 
import random
import math

#Inicializar
pygame.init()

#Mapas
mapa1=[
"azzzzzzzzxzzzzzzzxzzzzzza",
"z        z       z      z",
"z        z       z      z",
"z        z       z      z",
"z  zzzx      xzzza      z",
"z     z      z          z",
"z     z      z          z",
"z     zzzza  z    z     z",
"z     z   z  z    z     z",
"xzz   azzzx  xzzzzx     z",
"z                       z",
"z                       z",
"z                      pz",
"azzzzzzzzzzzzzzzzzzzzzzza",
]
mapa2=[
"lcccccccccccccccccccccccb",
"c        c              c",
"c        c              c",
"c        c              c",
"bcccc    bccc   lcccb   c",
"c               c   c   c",
"c               c   c   c",
"c   ccccl       c   c   c",
"c       c           c   c",
"c       c           c   c",
"bccc    ccc  c      bcccl",
"c       c    c          c",
"c       c p  c          c",
"bcccccccccccccccccccccccl",
]
mapa3=[
"c p l p l p l p l p l o  ",
"b eee  m          m eeeeb",
"  eee               eeee ",
"t eee  c l p lo      eeet",
"  eee  n        n    nee ",
"b      n   aoa  n       b",
"         w    n    iee   ",
"t      t      n    eee  t",
" ee    w  nna d t  eee   ",
"bee                     b",
"teeee   p l p l     eeeet",
"weeee        m      eede ",
" eeee               eeee ",
"ap l p l p l p l p l p   ",
]

#Funciones
def construir_mapa(superficie,mapa):
    puertas =[]
    x = 0
    y = 0
    if mapa == mapa1:
        limites = []
        arbusto = []
        arbol = []
        for linea in mapa:
            for baldosa in linea:
                if baldosa == "x":
                    limites.append([baldosa_muro , pygame.Rect(x,y,50,50)])
                elif baldosa == "z":
                    arbusto.append([baldosa_arbusto , pygame.Rect(x,y,50,50)])
                elif baldosa == "a":
                    arbol.append([baldosa_arbol , pygame.Rect(x,y,50,50)])
                elif baldosa == "p":
                    puertas.append([baldosa_puerta , pygame.Rect(x,y,50,50)])
                x += 50
            x = 0
            y += 50
        return limites,arbusto,arbol,puertas
    if mapa == mapa2:
        cajas = []
        paleta = []
        barril = []
        for linea in mapa:
            for baldosa in linea:
                if baldosa == "c":
                    cajas.append([baldosa_cajas , pygame.Rect(x,y,50,50)])
                elif baldosa == "l":
                    paleta.append([baldosa_paleta , pygame.Rect(x,y,50,50)])
                elif baldosa == "b":
                    barril.append([baldosa_barril , pygame.Rect(x,y,50,50)])
                elif baldosa == "p":
                    puertas.append([baldosa_puerta , pygame.Rect(x,y,50,50)])
                x += 50
            x = 0
            y += 50
        return cajas,paleta,barril,puertas
    if mapa == mapa3:
        arbol_auxiliar = []
        piedras = []
        piedras_izquierda = []
        piedras_arriba = []
        piedras_abajo = []
        piedras_sueltas = []
        costado1 = []
        costado2 = []
        costado3 = []
        costado4 = []
        circulo = []
        armas = []
        transparente = []
        transparente2 = []
        for linea in mapa:
            for baldosa in linea:
                if baldosa == "a":
                    arbol_auxiliar.append([baldosa_arbol_auxiliar , pygame.Rect(x,y,50,50)])
                elif baldosa == "p":
                    piedras.append([baldosa_piedras , pygame.Rect(x,y,130,40)])
                elif baldosa == "l":
                    piedras_izquierda.append([baldosa_piedras_izquierda , pygame.Rect(x,y,130,40)])
                elif baldosa == "t":
                    piedras_arriba.append([baldosa_piedras_arriba , pygame.Rect(x,y,40,130)])
                elif baldosa == "b":
                    piedras_abajo.append([baldosa_piedras_abajo , pygame.Rect(x,y,40,130)])
                if baldosa == "s":
                    piedras_sueltas.append([baldosa_piedras_sueltas , pygame.Rect(x,y,50,50)])
                if baldosa == "c":
                    costado1.append([baldosa_costados , pygame.Rect(x,y,130,40)])
                if baldosa == "o":
                    costado2.append([baldosa_costados2 , pygame.Rect(x,y,140,40)])
                if baldosa == "w":
                    costado3.append([baldosa_costados3 , pygame.Rect(x,y,40,140)])
                if baldosa == "d":
                    costado4.append([baldosa_costados4 , pygame.Rect(x,y,50,50)])
                if baldosa == "i":
                    circulo.append([baldosa_circulo , pygame.Rect(x,y,50,50)])
                if baldosa == "m":
                    armas.append([baldosa_armas , pygame.Rect(x,y,50,50)])
                if baldosa == "n":
                    transparente.append([baldosa_transparente , pygame.Rect(x,y,30,35)])
                if baldosa == "e":
                    transparente2.append([baldosa_transparente , pygame.Rect(x,y,50,50)])
                x += 50
            x = 0
            y += 50

        return arbol_auxiliar,piedras,piedras_izquierda,piedras_abajo,piedras_arriba,piedras_sueltas,circulo,armas,costado1,costado2,costado3,costado4,transparente,transparente2
def mostrar_bala(x,y,tipo):
    ventana.blit(tipo,(x,y))
def mostrar_puntaje(x):
    puntaje_render = tipo_letra.render("Score: "+str(puntaje), True, (255,255,255))
    ventana.blit(puntaje_render,(x,A-(puntaje_render.get_size()[1])))
def mostrar_fin():
    fin_render = tipo_letra_go.render("GAME OVER", True, (255,255,255))
    x=10
    y=A-(fin_render.get_size()[1])
    ventana.blit(fin_render,(x,y))
def mostrar_nivel():
    nivel_render = tipo_letra.render("Nivel: "+str(nivel), True, (255,255,255))
    x=0
    y=A-(nivel_render.get_size()[1])
    ventana.blit(nivel_render,(x,y))
def d_general(p1,p2,distancia): # retorna un booleano, evalua la distancia de 2 puntos (x,y)
    return math.sqrt(math.pow(p1.x-p2.x,2) + math.pow(p2.y-p2.y,2)) <= distancia
def d_y(p1,p2,distancia_y): #evalua la distancia en cuanto al eje (y)
    if p1.y - p2.y <= distancia_y or p1.y - p2.y >= -distancia_y:
        return True
    else:
        return False
            
#Tipos de letra
tipo_letra_go = pygame.font.Font('freesansbold.ttf', 46)
tipo_letra = pygame.font.Font('freesansbold.ttf', 28)
letra_p_i_L = 10
letra_p_i_A = 10

#Medidas
L=1280
A=720
#ventana
ventana = pygame.display.set_mode((L,A))
reloj = pygame.time.Clock()

#score
puntaje=0
nivel=1

#imagenes para el fondo
fondo_juego = pygame.image.load("imagenes_juego/fondo1.jpg").convert()
fondo_juego2 = pygame.image.load("imagenes_juego/fondo5.jpg").convert()
fondo_juego3 = pygame.image.load("imagenes_juego/fondo10.jpg").convert()

baldosa_muro = pygame.image.load("imagenes_juego/arbusto_imagen.png").convert_alpha()
baldosa_arbusto = pygame.image.load("imagenes_juego/arbusto_alto_imagen.png").convert_alpha()
baldosa_arbol = pygame.image.load("imagenes_juego/arbol2_imagen.png").convert_alpha()
baldosa_puerta = pygame.image.load("imagenes_juego/portal.png").convert_alpha()

baldosa_cajas = pygame.image.load("imagenes_juego/caja.png").convert_alpha()
baldosa_paleta = pygame.image.load("imagenes_juego/paleta.png").convert_alpha()
baldosa_barril = pygame.image.load("imagenes_juego/barril.png").convert_alpha()

baldosa_arbol_auxiliar = pygame.image.load("imagenes_juego/arbol_mapa3.png").convert_alpha()
baldosa_piedras = pygame.image.load("imagenes_juego/piedras.png").convert_alpha()
baldosa_piedras_izquierda = pygame.image.load("imagenes_juego/piedras_izquierda.png").convert_alpha()
baldosa_piedras_arriba = pygame.image.load("imagenes_juego/piedras_arriba.png").convert_alpha()
baldosa_piedras_abajo = pygame.image.load("imagenes_juego/piedras_abajo.png").convert_alpha()
baldosa_piedras_sueltas = pygame.image.load("imagenes_juego/piedras_sueltas.png").convert_alpha()
baldosa_costados = pygame.image.load("imagenes_juego/costados.png").convert_alpha()
baldosa_costados2 = pygame.image.load("imagenes_juego/costados2.png").convert_alpha()
baldosa_costados3 = pygame.image.load("imagenes_juego/costados3.png").convert_alpha()
baldosa_costados4 = pygame.image.load("imagenes_juego/costados4.png").convert_alpha()
baldosa_circulo = pygame.image.load("imagenes_juego/circulo.png").convert_alpha()
baldosa_armas = pygame.image.load("imagenes_juego/armas.png").convert_alpha()
baldosa_transparente = pygame.image.load("imagenes_juego/transparente.png").convert_alpha()
casa1 = pygame.image.load("imagenes_juego/casa1.png").convert_alpha()
casa2 = pygame.image.load("imagenes_juego/casa2.png").convert_alpha()
casa3 = pygame.image.load("imagenes_juego/casa3.png").convert_alpha()
casa4 = pygame.image.load("imagenes_juego/casa4.png").convert_alpha()

#personaje
personaje_imagen = pygame.image.load("imagenes_juego/mama_derecha.png")
orientación="derecha"
personaje_rectangulo = personaje_imagen.get_rect()
personaje_rectangulo.x=50
personaje_rectangulo.y=50
personaje_vel_x = 0
personaje_vel_y = 0
personaje_tamaño= (personaje_imagen.get_size()[0],personaje_imagen.get_size()[1])

#Villano
villano_imagen = pygame.image.load("imagenes_juego/villano.png")
villano_rectangulo = villano_imagen.get_rect()
villano_tamaño = (villano_imagen.get_size()[0],villano_imagen.get_size()[1])
villano_rectangulo.x = 400 #coordenadas iniciales
villano_rectangulo.y = 300

villano_x = [[400 ,50, L- 120],[50, L - 320, L - 700],[300, 605, 650],[230, 605,770]]
villano_y = [[300, A-115 , 50],[A - 460,A - 265, A - 460],[50, A-165, 300],[A-120, 115, 470]]
pos = 0

#bala_villano
'''bala_villano = pygame.image.load("imagenes_juego/bala_villano.png")
bala_tamaño_v = (bala_villano.get_size()[0],bala_villano.get_size()[1])
x_temp_v = 0
y_temp_v = 0
bala_status_v = "Espera" 
velocidad_v = 10 
velocidad2_v = 0 
contador_rebotes_v = 0'''


#Valores balas
'''
El sistema de disparo consiste en que la bala se encuentra compartiendo la posición del personaje en todo momento, oculta por
el sprite, este es el estado "Espera". En cuanto se dispara, se libera de las coordenadas del jugador y asume unas propias. 
(x_temp y y_temp). Este es el estado "Fuego" Cuando rebota un número determinado de veces, desaparece y vuelve a "Espera".
'''
bala=pygame.image.load("imagenes_juego/bala_2.png")
bala_derecha=pygame.image.load("imagenes_juego/bala2_derecha.png")
bala_izquierda=pygame.image.load("imagenes_juego/bala2_izquierda.png")
bala_abajo=pygame.image.load("imagenes_juego/bala2_abajo.png")
bala_size=(bala.get_size()[0],bala.get_size()[1])
x_temp=0#Estas variables se convertirán en las coordenadas de la bala al dispararse.
y_temp=0
bala_status="Espera"#La bala se encuentra sin disparar y lista
velocidad=10 # velocidad inicial de la bala.(horizontal)
velocidad2=0#velocidad inicial vertical. Es 0 para que el primer tiro sea recto.
contador_rebotes=0#Cuenta el número de rebotes antes de desaparecer.

#Datos
habitacion1 = construir_mapa(ventana,mapa1)
habitacion2 = construir_mapa(ventana,mapa2)
habitacion3 = construir_mapa(ventana,mapa3)

habitacion = habitacion1

#Bucle principal
correr = True
while correr:
    reloj.tick(120)
    #Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            correr = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                correr = False

        #disparar bala
            if evento.key == pygame.K_SPACE:
                if bala_status=="Espera":
                    x_temp=personaje_rectangulo.x+(personaje_tamaño[0]//4)
                    y_temp=personaje_rectangulo.y+10 #Se crean copias de la posición del jugador una unica vez, para que la bala no se mueva con la nave al ser disparada.
                    bala_status="Fuego"
                    orientación2=orientación #"orientación 2" solo funcionará cuando la bala recién ha sido disparada
                    #Si se trabaja con "orientación" en la dirección de la bala, esta se moverá con la nave cada vez que apretemos espacio.
            
            #Movimiento personaje.
            if evento.key == pygame.K_d or evento.key == pygame.K_RIGHT:
                orientación="derecha"
                personaje_vel_x = 5
            if evento.key == pygame.K_a or evento.key == pygame.K_LEFT:
                orientación="izquierda"
                personaje_vel_x = -5
            if evento.key == pygame.K_s or evento.key == pygame.K_DOWN:
                orientación="abajo"
                personaje_vel_y = 5
            if evento.key == pygame.K_w or evento.key == pygame.K_UP:
                orientación="arriba"
                personaje_vel_y = -5

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_d or evento.key == pygame.K_RIGHT or evento.key == pygame.K_a or evento.key == pygame.K_LEFT:
                personaje_vel_x = 0
            if evento.key == pygame.K_s or evento.key == pygame.K_DOWN or evento.key == pygame.K_w or evento.key == pygame.K_UP:
                personaje_vel_y = 0
   
    #Lógica
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

    #Dibujos del fondo
    if habitacion == habitacion1:
        fondo = ventana.blit(fondo_juego,(0,0))
        for limite in habitacion[0] and habitacion[1] and habitacion[2]:
            if personaje_rectangulo.colliderect(limite[1]):
                personaje_rectangulo.x -= personaje_vel_x
                personaje_rectangulo.y -= personaje_vel_y
        for limite in habitacion[1]:
            if personaje_rectangulo.colliderect(limite[1]):
                personaje_rectangulo.x -= personaje_vel_x
                personaje_rectangulo.y -= personaje_vel_y
        for limite in habitacion[2]:
            if personaje_rectangulo.colliderect(limite[1]):
                personaje_rectangulo.x -= personaje_vel_x
                personaje_rectangulo.y -= personaje_vel_y
        for puerta in habitacion[3]:
            if personaje_rectangulo.colliderect(puerta[1]):
                if habitacion == habitacion1:
                    habitacion = habitacion2
                    personaje_rectangulo.x = 50
                    personaje_rectangulo.y = 50
                elif habitacion == habitacion2:
                    habitacion = habitacion3
                    personaje_rectangulo.x = 50
                    personaje_rectangulo.y = 50
    elif habitacion == habitacion2:
        fondo = ventana.blit(fondo_juego2,(0,0))
        for limite in habitacion[0]:
            if personaje_rectangulo.colliderect(limite[1]):
                personaje_rectangulo.x -= personaje_vel_x
                personaje_rectangulo.y -= personaje_vel_y
        for limite in habitacion[1]:
            if personaje_rectangulo.colliderect(limite[1]):
                personaje_rectangulo.x -= personaje_vel_x
                personaje_rectangulo.y -= personaje_vel_y
        for limite in habitacion[2]:
            if personaje_rectangulo.colliderect(limite[1]):
                personaje_rectangulo.x -= personaje_vel_x
                personaje_rectangulo.y -= personaje_vel_y
        for puerta in habitacion[3]:
            if personaje_rectangulo.colliderect(puerta[1]):
                if habitacion == habitacion1:
                    habitacion = habitacion2
                    personaje_rectangulo.x = 50
                    personaje_rectangulo.y = 50
                elif habitacion == habitacion2:
                    habitacion = habitacion3
                    personaje_rectangulo.x = 50
                    personaje_rectangulo.y = 50
    elif habitacion == habitacion3:
        fondo = ventana.blit(fondo_juego3,(0,0))
        ventana.blit(casa1,(100,30))
        ventana.blit(casa2,(50,420))
        ventana.blit(casa3,(1000,50))
        ventana.blit(casa4,(1000,500))
        for limite in habitacion[0]:
            if personaje_rectangulo.colliderect(limite[1]):
                personaje_rectangulo.x -= personaje_vel_x
                personaje_rectangulo.y -= personaje_vel_y
        for limite in habitacion[1]:
            if personaje_rectangulo.colliderect(limite[1]):
                personaje_rectangulo.x -= personaje_vel_x
                personaje_rectangulo.y -= personaje_vel_y
        for limite in habitacion[2]:
            if personaje_rectangulo.colliderect(limite[1]):
                personaje_rectangulo.x -= personaje_vel_x
                personaje_rectangulo.y -= personaje_vel_y
        for limite in habitacion[3]:
            if personaje_rectangulo.colliderect(limite[1]):
                personaje_rectangulo.x -= personaje_vel_x
                personaje_rectangulo.y -= personaje_vel_y
        for limite in habitacion[4]:
            if personaje_rectangulo.colliderect(limite[1]):
                personaje_rectangulo.x -= personaje_vel_x
                personaje_rectangulo.y -= personaje_vel_y
        for limite in habitacion[6]:
            if personaje_rectangulo.colliderect(limite[1]):
                personaje_rectangulo.x -= personaje_vel_x
                personaje_rectangulo.y -= personaje_vel_y
        for limite in habitacion[7]:
            if personaje_rectangulo.colliderect(limite[1]):
                personaje_rectangulo.x -= personaje_vel_x
                personaje_rectangulo.y -= personaje_vel_y
        for limite in habitacion[8]:
            if personaje_rectangulo.colliderect(limite[1]):
                personaje_rectangulo.x -= personaje_vel_x
                personaje_rectangulo.y -= personaje_vel_y
        for limite in habitacion[9]:
            if personaje_rectangulo.colliderect(limite[1]):
                personaje_rectangulo.x -= personaje_vel_x
                personaje_rectangulo.y -= personaje_vel_y
        for limite in habitacion[10]:
            if personaje_rectangulo.colliderect(limite[1]):
                personaje_rectangulo.x -= personaje_vel_x
                personaje_rectangulo.y -= personaje_vel_y
        for limite in habitacion[12]:
            if personaje_rectangulo.colliderect(limite[1]):
                personaje_rectangulo.x -= personaje_vel_x
                personaje_rectangulo.y -= personaje_vel_y
        for limite in habitacion[13]:
            if personaje_rectangulo.colliderect(limite[1]):
                personaje_rectangulo.x -= personaje_vel_x
                personaje_rectangulo.y -= personaje_vel_y

    for elemento in habitacion:
        for baldosa in elemento:
            ventana.blit(baldosa[0],baldosa[1])

    #Trayectoria disparo del jugador
    if bala_status=="Fuego":
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
        velocidad=5# Es importante reiniciar estos valores cada vez.
        velocidad2=0
        mostrar_bala(personaje_rectangulo.x+(personaje_tamaño[0]//4),personaje_rectangulo.y+5,bala)#En espera la bala se queda oculta en la nave.

    #Rebote de las balas
    bala_dimensiones=bala.get_rect(center=(x_temp,y_temp))#Se hallan las coordenadas que va adquiriendo la bala al moverse.
    switch=True #variable usada para el rebote.
    for limite in habitacion[1]:
        if bala_dimensiones.colliderect(limite[1]) and bala_status=="Fuego" and switch==True:
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

    #imagenes del villano 
    if d_y(personaje_rectangulo,villano_rectangulo,villano_tamaño[0]*2):
        if villano_rectangulo.x > personaje_rectangulo.x :
            villano_imagen = pygame.image.load("imagenes_juego/villano_izquierda.png")
        if villano_rectangulo.x < personaje_rectangulo.x :
            villano_imagen = pygame.image.load("imagenes_juego/villano_derecha.png")

    if villano_rectangulo.y  > personaje_rectangulo.y:
        villano_imagen = pygame.image.load("imagenes_juego/villano.png")
    if villano_rectangulo.y < personaje_rectangulo.y:
        villano_imagen = pygame.image.load("imagenes_juego/villano_abajo.png")

    #el villano se movera de pos cada 5 seg
    '''tiempo = time.gmtime(time.time())
    if (tiempo.tm_sec) % 5 == 0 :
        for one in range (10000000): # para que solo se haga un cambio
            if one == 0:
                x = random.randint(0,1)
                y = random.randint(0,1)
    villano_x = [(L - (villano_tamaño[0]*2+20)),400]
    villano_y = [(A - (villano_tamaño[1]*2+20)),300]
    villano_rectangulo.x = villano_x[x]
    villano_rectangulo.y = villano_y[y]'''

    #disparo de balas del villano
    '''if #distancia(villano_rectangulo,personaje_rectangulo,A):  
        if bala_status_v == "Espera":                    
            x_temp_v = villano_rectangulo.x + (villano_tamaño[0]//4)
            y_temp_v = villano_rectangulo.y + 10                    
            bala_status_v = "Fuego"

    if bala_status=="Fuego":
        if villano_arriba :
            mostrar_bala(x_temp_v,y_temp_v,bala_villano)
            y_temp-=velocidad
            x_temp-=velocidad2
        elif villano_abajo:
            mostrar_bala(x_temp_v,y_temp_v,bala_villano)
            y_temp+=velocidad
            x_temp+=velocidad2
        elif villano_izquierda:
            mostrar_bala(x_temp_v,y_temp_v,bala_villano)
            x_temp-=velocidad
            y_temp-=velocidad2
        elif villano_derecha:
            mostrar_bala(x_temp_v,y_temp_v,bala_villano)
            x_temp+=velocidad
            y_temp+=velocidad2

    if (y_temp_v<=0 or y_temp_v>= A or x_temp_v<=0 or x_temp_v>= L) or contador_rebotes_v==10:
        contador_rebotes_v=0 
        bala_status_v="Espera"

    if bala_status_v== "Espera":
        velocidad_v=5 
        velocidad2_v=0
        mostrar_bala(villano_rectangulo.x+(villano_tamaño[0]//4),villano_rectangulo.y+5,bala_villano)

    #Rebote de las balas villano
    bala_dimensiones_v=bala_villano.get_rect(center=(x_temp_v,y_temp_v))
    rebote =True 
    for muro in muros:
        if bala_dimensiones_v.colliderect(muro) and bala_status_v=="Fuego" and rebote==True:
            contador_rebotes_v+=1
            if contador_rebotes_v==1:
                velocidad_v*=-1
                velocidad2_v= velocidad_v
            elif contador_rebotes_v%2==0:
                velocidad_v=velocidad_v
                velocidad2_v*=-1
            elif contador_rebotes_v%2==1:
                velocidad_v*=-1
                velocidad2_v=velocidad2_v
            rebote=False '''


    mostrar_nivel()
    mostrar_puntaje(650)
    ventana.blit(villano_imagen,villano_rectangulo)
    ventana.blit(personaje_imagen,personaje_rectangulo)
    pygame.display.update()