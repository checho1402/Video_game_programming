#Grupo 7 - Mom's Odissey
#Nombre: Sergio Ramos
#Grupo: CCOMP1-1.2
import pygame, math 
from pygame import mixer 
pygame.init() 
#Creación de mapas
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
"         w y  n    iee   ",
"t      t      n    eee  t",
" ee    w  nna d t  eee   ",
"bee                     b",
"teeee   p l p l     eeeet",
"weeee        m      eede ",
" eeee               eeee ",
"ap l p l p l p l p l p   ",
]
#Funciones
def crear_matriz_vacia(filas,columnas): 
    Espiral = []
    for i in range(filas):
        Espiral.append([""*filas]*columnas)#Se llena la matriz con espacios
    return Espiral
def espiral(matriz,ini,fin):
    if (ini == fin):
        matriz[ini][fin]="f"#se usara para crear el rectangulo fin
        return matriz
    for i in range(ini-1, fin):#Permite dar un espacio 
        matriz[ini][i]="x"
    for i in range(ini, fin):
        matriz[i][fin]="x"
    for i in range(fin,ini,-1):
        matriz[fin][i]="x"
    for i in range(fin,ini+1,-1):#Espacio vertical
        matriz[i][ini]="x"
    espiral(matriz,ini+2,fin-2)
#Los mapas se iteran y según la letra se elige una textura/límite.
def construir_mapa(superficie,mapa):
    puertas =[]
    x = 0
    y = 0
    if mapa == mapa1:#listas vacias donde se guarda el objeto
        limites = []
        arbusto = []
        arbol = []
        for linea in mapa:
            for baldosa in linea:
                if baldosa == "x":
                    limites.append([baldosa_muro , pygame.Rect(x,y,50,50)]) #Se junta la imagen con el objeto rect
                elif baldosa == "z":
                    arbusto.append([baldosa_arbusto , pygame.Rect(x,y,50,50)])
                elif baldosa == "a":
                    arbol.append([baldosa_arbol , pygame.Rect(x,y,50,50)])
                elif baldosa == "p":
                    puertas.append([baldosa_puerta , pygame.Rect(x,y,50,50)])
                x += 50#Permite separar cada objeto iterado en x
            x = 0
            y += 50#Permite separar cada objeto iterado en y
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
                    piedras.append([baldosa_piedras , pygame.Rect(x,y,130,40)])#Diferentes dimensiones del rect
                elif baldosa == "l":
                    piedras_izquierda.append([baldosa_piedras_izquierda , pygame.Rect(x,y,130,40)])
                elif baldosa == "t":
                    piedras_arriba.append([baldosa_piedras_arriba , pygame.Rect(x,y,40,130)])
                elif baldosa == "b":
                    piedras_abajo.append([baldosa_piedras_abajo , pygame.Rect(x,y,40,130)])
                if baldosa == "c":
                    costado1.append([baldosa_costados , pygame.Rect(x,y,130,40)])#al ser costados una imagen el rect tiene que variar
                if baldosa == "o":
                    costado2.append([baldosa_costados2 , pygame.Rect(x,y,140,40)])
                if baldosa == "w":
                    costado3.append([baldosa_costados3 , pygame.Rect(x,y,40,140)])
                if baldosa == "d":
                    costado4.append([baldosa_costados4 , pygame.Rect(x,y,50,50)])#Se mostrara la imagen pero el rect no al no formar parte de la imagen
                if baldosa == "i":
                    circulo.append([baldosa_circulo , pygame.Rect(x,y,50,50)])
                if baldosa == "m":
                    armas.append([baldosa_armas , pygame.Rect(x,y,50,50)])
                if baldosa == "n":
                    transparente.append([baldosa_transparente , pygame.Rect(x,y,30,35)])
                if baldosa == "e":
                    transparente2.append([baldosa_transparente , pygame.Rect(x,y,50,50)])
                elif baldosa == "y":
                    puertas.append([baldosa_puerta , pygame.Rect(x,y,50,50)])
                x += 50
            x = 0
            y += 50
        return arbol_auxiliar,piedras,piedras_izquierda,piedras_abajo,piedras_arriba,circulo,armas,costado1,costado2,costado3,costado4,transparente,transparente2,puertas
    if mapa == mapa4:
        ladrillos = []
        final = []
        for linea in mapa:
            for baldosa in linea:
                if baldosa == "x":
                    ladrillos.append([baldosa_bloquetas, pygame.Rect(x,y,100,50)])
                if baldosa == "f":
                    final.append([baldosa_transparente, pygame.Rect(x,y,100,50)])
                x += 100
            x = 0
            y += 50
        return ladrillos,final
def limites (x):#Permitira que tanto el enemigo como el personaje se detengan al momento de tocar un objeto o pared de los mapas
    global personaje_rectangulo, habitacion, personaje_vel_x, personaje_vel_y
    for limite in habitacion[x]:
        if personaje_rectangulo.colliderect(limite[1]):# Si colisiona directamente con el rect no con la imagen
            personaje_rectangulo.x -= personaje_vel_x
            personaje_rectangulo.y -= personaje_vel_y
        for i in range(villano_num):
            if villano_rectangulo[i].colliderect(limite[1]):
                if v_izquierda[i] == True:
                    villano_rectangulo[i].x += 1#Se contraresta el movimiento en x
                    v_izquierda[i] = False
                if v_derecha[i] == True:
                    villano_rectangulo[i].x -= 1
                    v_derecha[i] = False
                if v_arriba[i] == True:
                    villano_rectangulo[i].y +=1#Se contraresta el movimiento en y
                    v_arriba[i] = False
                if v_abajo[i] == True:
                    villano_rectangulo[i].y -= 1
                    v_abajo[i] = False
def pantalla_ini(): 
    inicio = tipo_letra_ini.render("Presione L para comenzar ", True, AMARILLO)
    ventana.blit(inicio,(L//2-350,A-200))
    salir = tipo_letra_ini.render("Presione ESC para salir ", True, AMARILLO)
    ventana.blit(salir,(L//2-308,A-120))
    titulo = tipo_letra_titule.render("mom's oddyssey ", True, AMARILLO)
    ventana.blit(titulo,(L//2-300,A-500))
def mostrar_mensaje_final():
    mensaje = tipo_letra.render("felicidades salvaste a luisito",True,(51,198,170))
    ventana.blit(mensaje,(L//2-(mensaje.get_size()[0])//2, A//2-(mensaje.get_size()[1])))
def mostrar_fin():
    fin_render = tipo_letra_titule.render("game over", True, (255,255,255))
    ventana.blit(fin_render,(L//2-(fin_render.get_size()[0]//2),A//2-(fin_render.get_size()[1]//2)))
def mostrar_nivel(nivel):
    nivel_render = tipo_letra_game.render("nivel: "+str(nivel), True, (147,174,164))
    ventana.blit(nivel_render,(0, A-(nivel_render.get_size()[1]) ))
def mostrar_puntaje(puntaje):
    puntaje_render = tipo_letra_game.render("puntaje: "+str(puntaje), True, (147,174,164))
    ventana.blit(puntaje_render,(L-(puntaje_render.get_size()[0]),A-(puntaje_render.get_size()[1])))
def mostrar_vida(life):
    life_render = tipo_letra_game.render("vida: "+str(life), True, (147,174,164))
    ventana.blit(life_render,(L//2-(life_render.get_size()[0])*3, A-(life_render.get_size()[1]) ))
def mostrar_bala(x,y,tipo):
    ventana.blit(tipo,(x,y))#Posicion de la bala
def avistamiento(a,b,distancia):
    return True if(math.sqrt(((b.x - a.x)**2)+((b.y - a.y)**2))) < distancia else False
def lis_villano(villano,villano_num,niv):
    for i in range(villano_num): 
        villano.append(Villano(villano_imagen[i],villano_rectangulo[i],villano_x[niv][i],villano_y[niv][i],villano_bala[i],0,0))
    return villano
class Villano:
    def __init__(self,img,rec,x,y,b,bx,by):
        bx=x#La bala adquiere las posiciones del enemigo
        by=y
        self.imagen=img
        self.recta=rec
        self.recta.x=x
        self.recta.y=y
        self.bala=b
        self.bala_rect=self.bala.get_rect()
        self.bala_rect.x=bx #Valores propios de la bala
        self.bala_rect.y=by
        self.estado="Espera"

#Tipos de letra
tipo_letra_ini = pygame.font.Font('estilo_letra/starjedi/Starjhol.ttf', 43)
tipo_letra_titule = pygame.font.Font('estilo_letra/stjedise/STJEDISE.ttf', 70)
tipo_letra = pygame.font.Font('estilo_letra/stjedise/STJEDISE.ttf', 40)
tipo_letra_game = pygame.font.Font('estilo_letra/starjout/Starjout.ttf', 28)
AMARILLO = (249,231,3)

#score
puntaje=0
nivel=1
life = 3
#Medidas
L=1280
A=720
#ventana
ventana = pygame.display.set_mode((L,A), pygame.FULLSCREEN)#Permite mostrar en toda la pantalla
reloj = pygame.time.Clock()

#musica
pygame.mixer.init()
primer_nivel = mixer.Sound("musica_juego/BoxCat_Games_-_20_-_Battle_Normal.wav")
segundo_nivel= mixer.Sound("musica_juego/Polarsounds_-_Gaming_Mode_Xtreme.wav")
tercer_nivel=mixer.Sound("musica_juego/Daniel Dombrowsky - Deliverance.wav")
cuarto_nivel=mixer.Sound("musica_juego/Musica de la_rosa_de_Guadalupe.wav")

#sonidos
transicion=mixer.Sound("musica_juego/Cambio_nivel.wav")
sonido_disparo = mixer.Sound("musica_juego/Disparo2.wav")
sonido_disparo_malo = mixer.Sound("musica_juego/explosion.wav")
sonido_disparo_villano = mixer.Sound("musica_juego/Disparo2.wav")
rebote_bala=mixer.Sound("musica_juego/Rebote_bala.wav")
muerte_villano=mixer.Sound("musica_juego/Enemigo_muerto2.wav")
game_over=mixer.Sound("musica_juego/Game_over_2.wav")

#imagenes fondo
fondo_inicio = pygame.image.load('Imagenes_juego/inicio.jpg').convert()
fondo_final = pygame.image.load('Imagenes_juego/imagen_final.jpg').convert()
fondo_juego = pygame.image.load("Imagenes_juego/fondo1.jpg").convert()
fondo_juego2 = pygame.image.load("Imagenes_juego/fondo5.jpg").convert()
fondo_juego3 = pygame.image.load("Imagenes_juego/fondo10.jpg").convert()#pixeles y se pueda mostrar en pantalla
fondo_juego4 = pygame.image.load("Imagenes_juego/fondo_final.jpg").convert()
#mapa1
baldosa_muro = pygame.image.load("Imagenes_juego/arbusto_imagen.png").convert_alpha()#pixeles y se pueda mostrar en pantalla para imagenes png
baldosa_arbusto = pygame.image.load("Imagenes_juego/arbusto_alto_imagen.png").convert_alpha()
baldosa_arbol = pygame.image.load("Imagenes_juego/arbol2_imagen.png").convert_alpha()
baldosa_puerta = pygame.image.load("Imagenes_juego/portal.png").convert_alpha()
#mapa2
baldosa_cajas = pygame.image.load("Imagenes_juego/caja.png").convert_alpha()
baldosa_paleta = pygame.image.load("Imagenes_juego/paleta.png").convert_alpha()
baldosa_barril = pygame.image.load("Imagenes_juego/barril.png").convert_alpha()
#mapa3
baldosa_arbol_auxiliar = pygame.image.load("Imagenes_juego/arbol_mapa3.png").convert_alpha()
baldosa_piedras = pygame.image.load("Imagenes_juego/piedras.png").convert_alpha()
baldosa_piedras_izquierda = pygame.image.load("Imagenes_juego/piedras_izquierda.png").convert_alpha()
baldosa_piedras_arriba = pygame.image.load("Imagenes_juego/piedras_arriba.png").convert_alpha()
baldosa_piedras_abajo = pygame.image.load("Imagenes_juego/piedras_abajo.png").convert_alpha()
baldosa_costados = pygame.image.load("Imagenes_juego/costados.png").convert_alpha()
baldosa_costados2 = pygame.image.load("Imagenes_juego/costados2.png").convert_alpha()
baldosa_costados3 = pygame.image.load("Imagenes_juego/costados3.png").convert_alpha()
baldosa_costados4 = pygame.image.load("Imagenes_juego/costados4.png").convert_alpha()
baldosa_circulo = pygame.image.load("Imagenes_juego/circulo.png").convert_alpha()
baldosa_armas = pygame.image.load("Imagenes_juego/armas.png").convert_alpha()
baldosa_transparente = pygame.image.load("Imagenes_juego/transparente.png").convert_alpha()
casa1 = pygame.image.load("Imagenes_juego/casa1.png").convert_alpha()
casa2 = pygame.image.load("Imagenes_juego/casa2.png").convert_alpha()
casa3 = pygame.image.load("Imagenes_juego/casa3.png").convert_alpha()
casa4 = pygame.image.load("Imagenes_juego/casa4.png").convert_alpha()
#mapa4
baldosa_bloquetas = pygame.image.load("Imagenes_juego/bloquetas.png").convert_alpha()
niño = pygame.image.load("Imagenes_juego/niño_solo.png").convert_alpha()
niño_rectangulo = niño.get_rect()#Las dimensiones del niño

#personaje
personaje_imagen = pygame.image.load("Imagenes_juego/mama_derecha.png")
orientación="derecha"#orientación inicial
personaje_rectangulo = personaje_imagen.get_rect()
personaje_rectangulo.x=50#Coordenadas iniciales del personaje
personaje_rectangulo.y=50
personaje_vel_x = 0#Velocidades iniciales del personaje
personaje_vel_y = 0
personaje_tamaño= (personaje_imagen.get_size()[0],personaje_imagen.get_size()[1])#dimensiones del personaje

#Villano
villano_num = 3
villano_arriba = []
villano_abajo = []
villano_derecha = []
villano_izquierda = []
villano_bala = []
v_arriba = []
v_abajo = []
v_derecha = []
v_izquierda = []  
villano_imagen = []
villano_rectangulo = []
villano = []
villano_x = [[400 ,900, L- 520],[50, L - 20, L - 300],[100, 605, 650]]#Posiciones
villano_y = [[300, A-115 , 50],[A - 60,A - 265, A - 60],[50, A-165, 300]]
for i in range(villano_num): 
    villano_arriba.append(pygame.image.load("Imagenes_juego/villano.png"))
    villano_abajo.append(pygame.image.load("Imagenes_juego/villano_abajo.png"))
    villano_derecha.append(pygame.image.load("Imagenes_juego/villano_derecha.png"))
    villano_izquierda.append(pygame.image.load("Imagenes_juego/villano_izquierda.png"))
    villano_bala.append(pygame.image.load("Imagenes_juego/bala_villano.png"))
    v_arriba.append(False)
    v_abajo.append(False)
    v_derecha.append(False)
    v_izquierda.append(False) 
    villano_imagen.append(villano_arriba[i])#Orientación inicial
    villano_rectangulo.append(villano_imagen[i].get_rect())
villano = lis_villano(villano,villano_num,nivel-1)#Objetos villano

#Valores balas
bala=pygame.image.load("Imagenes_juego/bala_2.png")
bala_derecha=pygame.image.load("Imagenes_juego/bala2_derecha.png")
bala_izquierda=pygame.image.load("Imagenes_juego/bala2_izquierda.png")
bala_abajo=pygame.image.load("Imagenes_juego/bala2_abajo.png")#Hasta aquí las imágenes en las 4 direcciones.
x_temp=0#Estas variables se convertirán en las coordenadas de la bala al dispararse.
y_temp=0
bala_status="Espera"#La bala se encuentra sin disparar y lista
velocidad=5 # velocidad inicial de la bala.(horizontal)
velocidad2=0#velocidad inicial vertical. Es 0 para que el primer tiro sea recto.
contador_rebotes=0#Cuenta el número de rebotes antes de desaparecer.

#Datos
mat=crear_matriz_vacia(13,13)#Se crea una matriz llena de ""
espiral(mat,0,len(mat)-1)#Se llama a la función recursiva espiral y se les asigna los valores a mat
mapa4=mat#Ahora se llama mapa4
habitacion1 = construir_mapa(ventana,mapa1)#se asigna el constructor de mapas
habitacion2 = construir_mapa(ventana,mapa2)
habitacion3 = construir_mapa(ventana,mapa3)
habitacion4 = construir_mapa(ventana,mapa4)
habitacion = habitacion1#Habitación inicial

#Bucle principal
perder = False#vidas y game over
correr = True
iniciar_juego = False
encontro_hijo = False#Pantalla final
while correr:
    reloj.tick(120)#La velocidad a la que se ejecuta el juego
    #Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            correr = False
        if evento.type == pygame.KEYDOWN:
            if evento.key==pygame.K_ESCAPE:
                correr = False
            if iniciar_juego == True and perder == False:
            #disparar bala           
                if evento.key==pygame.K_SPACE:       
                    if bala_status=="Espera":
                        sonido_disparo.play()
                        x_temp=personaje_rectangulo.x+(personaje_tamaño[0]//4)#Cuadrar la bala
                        y_temp=personaje_rectangulo.y+10                
                        bala_status="Fuego"
                        orientación2=orientación #No permite que la bala cambie de direccion según la madre
                    
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
                    
        elif evento.type==pygame.KEYDOWN:
            if evento.key==pygame.K_l:
                iniciar_juego = True 

    #mov del jugador
    personaje_rectangulo.x += personaje_vel_x
    personaje_rectangulo.y += personaje_vel_y
   #Límites del jugado, bordes

    if personaje_rectangulo.x < 0:
        personaje_rectangulo.x = 0

    #Orientación del jugador
    if orientación == "arriba":
        personaje_imagen = pygame.image.load('Imagenes_juego/mama_arriba.png')#cambio de imagen por orientación
    elif orientación == "abajo":
        personaje_imagen = pygame.image.load("Imagenes_juego/mama_abajo.png")
    elif orientación == "derecha":
        personaje_imagen = pygame.image.load("Imagenes_juego/mama_derecha.png")
    elif orientación == "izquierda":
        personaje_imagen = pygame.image.load("Imagenes_juego/mama_izquierda.png")
    
    #Dibujos fondo
    if perder==False:
        if habitacion == habitacion1:#condicionales por habitación
            fondo = ventana.blit(fondo_juego,(0,0))#Se le asiga un fondo
            limites(0) #funcion limites linea 176
            limites(1)
            limites(2)
            #musica
            if pygame.mixer.get_busy()==False:
                primer_nivel.play()#la musica del primer nivel
            for puerta in habitacion[3]:#El portal cambiara de mapa
                if personaje_rectangulo.colliderect(puerta[1]) and puntaje == 10:#Avanza de nivel solo si eliminó al villano
                    transicion.play()#Sonido de transición
                    habitacion = habitacion2#cambio de mapa
                    personaje_rectangulo.x ,personaje_rectangulo.y = 50,50#nuevas coordenadas para el personaje


        if habitacion == habitacion2:
            nivel=2
            fondo = ventana.blit(fondo_juego2,(0,0))        
            limites(0)
            limites(1)
            limites(2)
            primer_nivel.stop()
            if pygame.mixer.get_busy()==False:
                segundo_nivel.play()
            for puerta in habitacion[3] :
                if personaje_rectangulo.colliderect(puerta[1]) and puntaje == 20:
                    transicion.play()
                    habitacion = habitacion3
                    personaje_rectangulo.x ,personaje_rectangulo.y = 50,50

        if habitacion == habitacion3:
            nivel=3
            fondo = ventana.blit(fondo_juego3,(0,0))
            ventana.blit(casa1,(100,30))
            ventana.blit(casa2,(50,420))
            ventana.blit(casa3,(1000,50))
            ventana.blit(casa4,(1000,500))
            for i in range(13):
                if i!=10:
                    limites(i)
            segundo_nivel.stop()
            if pygame.mixer.get_busy()==False:
                tercer_nivel.play()
            for puerta in habitacion[13]:
                if personaje_rectangulo.colliderect(puerta[1]) and puntaje == 30:
                    transicion.play()
                    habitacion = habitacion4
                    personaje_rectangulo.x ,personaje_rectangulo.y = 50,50

        if habitacion == habitacion4:
            nivel=4
            fondo = ventana.blit(fondo_juego4,(0,0))   
            niño_rectangulo=niño.get_rect()  
            niño_rectangulo.x = L//2-(niño.get_size()[0]//2)
            niño_rectangulo.y = A//2-(niño.get_size()[1]//2)
            ventana.blit(niño,niño_rectangulo)#El niño no es un objeto rect
            limites(0)
            tercer_nivel.stop()
            if pygame.mixer.get_busy()==False:
                cuarto_nivel.play()
            if personaje_rectangulo.colliderect(niño_rectangulo):
                iniciar_juego = False
                encontro_hijo = True

        for elemento in habitacion:
            for baldosa in elemento:
                ventana.blit(baldosa[0],baldosa[1])

        #Trayectoria disparo
        if bala_status=="Fuego":  
            if orientación2 == "arriba":
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
            
            if  x_temp<=0 or contador_rebotes==10 :#Cuando se llega a un borde o se rebota 10 veces.
                contador_rebotes=0
                bala_status="Espera"

        if bala_status== "Espera":
            velocidad=5# Es importante reiniciar estos valores cada vez.
            velocidad2=0
            mostrar_bala(personaje_rectangulo.x+(personaje_tamaño[0]//4),personaje_rectangulo.y+5,bala)

        #Rebote de las balas
        bala_dimensiones=bala.get_rect(center=(x_temp,y_temp))#Se hallan las coordenadas que va adquiriendo la bala al moverse.
        switch=True #variable usada para el rebote.
        for i in range (0,len(habitacion)):
            for limite in habitacion[i]:
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
                    rebote_bala.play()
        #villano
        Villano_up = []
        Villano_down = []
        Villano_right = []
        Villano_left = []
        niv = nivel
        if habitacion == habitacion4:
            niv = 0
        for i in range (niv):
        #el villano sigue al jugador
            if avistamiento(villano_rectangulo[i], personaje_rectangulo, 300):#Contraresta el movimiento
                if villano_rectangulo[i].x > personaje_rectangulo.x:  
                    villano_rectangulo[i].x -= 1
                    v_izquierda[i] = True
                if villano_rectangulo[i].x < personaje_rectangulo.x: 
                    villano_rectangulo[i].x += 1
                    v_derecha[i] = True
                if villano_rectangulo[i].y > personaje_rectangulo.y: 
                    villano_rectangulo[i].y -= 1
                    v_arriba[i] = True
                if villano_rectangulo[i].y< personaje_rectangulo.y: 
                    villano_rectangulo[i].y += 1
                    v_abajo[i] = True
        #el villano voltea a disparar
            Villano_up.append((villano[i].recta.x-25,villano[i].recta.y-500,75,500))
            Villano_down.append((villano[i].recta.x-25,villano[i].recta.y+50,75,500))
            Villano_right.append((villano[i].recta.x+50,villano[i].recta.y-10,600,75))
            Villano_left.append((villano[i].recta.x-625,villano[i].recta.y-10,600,75))
        #Apuntado enemigo
            villano[i].estado="Espera"
            if villano[i].estado=="Espera":
                if personaje_rectangulo.colliderect(Villano_up[i]):
                    villano[i].imagen=villano_arriba[i]
                    villano[i].estado="Fuego"
                if personaje_rectangulo.colliderect(Villano_down[i]):
                    villano[i].imagen=villano_abajo[i]
                    villano[i].estado="Fuego"
                if personaje_rectangulo.colliderect(Villano_left[i]):
                    villano[i].imagen=villano_izquierda[i]
                    villano[i].estado="Fuego"
                if personaje_rectangulo.colliderect(Villano_right[i]):
                    villano[i].imagen=villano_derecha[i]
                    villano[i].estado="Fuego"
        #disparo enemigo
            if villano[i].estado=="Fuego":
                if villano[i].bala_rect.colliderect(personaje_rectangulo) and life > 0:
                    sonido_disparo_malo.play()
                    personaje_rectangulo.x, personaje_rectangulo.y=50, 50
                    life -= 1
                if life == 0:
                    game_over.play()
                    mostrar_fin()
                    personaje_vel_x, personaje_vel_y = 0, 0
                    perder = True
                if villano[i].imagen==villano_arriba[i]:
                    villano[i].bala_rect.y-=5
                if villano[i].imagen==villano_abajo[i]:
                    villano[i].bala_rect.y+=5
                if villano[i].imagen==villano_derecha[i]:
                    villano[i].bala_rect.x+=5
                if villano[i].imagen==villano_izquierda[i]:
                    villano[i].bala_rect.x-=5
                ventana.blit(villano[i].bala,villano[i].bala_rect)
                sonido_disparo_villano.play()
                for k in range (0,len(habitacion)):
                    for limite in habitacion[k]:
                        if villano[i].bala_rect.colliderect(limite[1]):
                            villano[i].bala_rect.y=villano[i].recta.y
                            villano[i].bala_rect.x=villano[i].recta.x
            	
            if villano[i].estado=="Espera":
                villano[i].bala_rect.y=villano[i].recta.y
                villano[i].bala_rect.x=villano[i].recta.x
                ventana.blit(villano[i].bala,villano[i].recta)
            ventana.blit(villano[i].imagen,villano[i].recta)           
        #sube score   
            if avistamiento(villano[i].recta,bala_dimensiones,40):
                muerte_villano.play()
                villano_rectangulo[i].x=0
                villano_rectangulo[i].y=2000
                bala_status = "Espera"
                puntaje += 10
    #pantalla de inicio
    if iniciar_juego==True:    
        mostrar_nivel(nivel)
        mostrar_puntaje(puntaje)
        mostrar_vida(life)
        ventana.blit(personaje_imagen,personaje_rectangulo)
    elif iniciar_juego==False and encontro_hijo == False:
        ventana.blit(fondo_inicio,(0,0))
        pantalla_ini()
    elif encontro_hijo==True:
        ventana.blit(fondo_final,(0,0))
        mostrar_mensaje_final()
    pygame.display.update()