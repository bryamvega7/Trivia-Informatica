import random
import time
#Constantes de Colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

#Bienvenida a la trivia
print (BLUE+"      ***Bienvenido a mi trivia sobre Informática***"+RESET)
time.sleep(1)
print(WHITE+"Aquí podrás poner a prueba tus conocimientos! Estas listo?"+RESET)
nombrePersona = input(GREEN+"\nIngresa tu nombre: "+RESET).upper()

#Pantalla de Carga
cargandoTemp=CYAN+"\nCargando...\n>"+RESET

for cargando in range(5,0,-1):
  print(cargandoTemp,cargando)
  cargandoTemp=CYAN+">"+RESET
  time.sleep(1)
  
#Bienvenida al jugador
print (WHITE+"\nBienvenido ", nombrePersona,", Ahora te daremos unas instrucciones sobre el uso de esta trivia."+RESET)
time.sleep(1)
# Instrucciones
print (RED+"\n*Instrucciones:* \n")
time.sleep(1)
print ("1. Por cada respuesta que este correcta o incorrecta los puntos seran aleatorios.")
print ("2. Escribe la letra de la respuesta que consideres correcta.")
print ("3. Presiona 'Enter' para verificar si tu respuesta es correcta."+RESET)
time.sleep(3)

print (WHITE+"\nSi entendió las instrucciones y desea continuar escriba 'si', si no desea continuar escriba 'no'."+RESET)
continuar = input(GREEN+"Respuesta: "+RESET).lower()

#Verificacion de intrucciones
while continuar not in ("si","no","SI","NO","Si","No"):
  continuar = input(YELLOW+"Debes responder si o no. Ingresa nuevamente tu respuesta: "+RESET).lower()

if continuar == "si":
  intentos = 0
  iniciarTrivia = True
  #Intentos que se haran la trivia
  while iniciarTrivia == True:
    print(YELLOW+"\nEste es tu intento numero: ",intentos,"!\n"+RESET)
    intentos += 1
    puntaje = random.randint(0,10)
    
    time.sleep(1)
    print(BLUE+"\nBien!, Empecemos con la trivia ",nombrePersona,"!\n"+RESET)
    print (GREEN+"Comenzaras con un puntaje de: "+RESET, puntaje)
    time.sleep(1)
    
    # Pregunta 1
    print (CYAN+"\n>PREGUNTA 1: ¿Que sistema operativo tiene como mascota a un pingüino?")
    time.sleep(3)
    print ("a) Windows")
    time.sleep(1)
    print ("b) Linux")
    time.sleep(1)
    print ("c) Mac OS")
    time.sleep(1)
    print ("d) Solaris"+RESET)
    time.sleep(1)
    respuesta_1 = input(GREEN+"\nTu respuesta: "+RESET).lower()
    while respuesta_1 not in ("a","b","c","d","A","B","C","D"):
      respuesta_1 = input(YELLOW+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET).lower()
    if respuesta_1 == 'b':
      print (MAGENTA+"La respuesta es correcta!"+RESET)
      puntaje+=random.randint(10,20)
    else:
      print (MAGENTA+"La respuesta es incorrecta!"+RESET)
      puntaje-=random.randint(0,10)
    time.sleep(1)
    print (RED+"Tu puntaje actual es de: "+RESET, puntaje)
      
    # Pregunta 2
    print (CYAN+"\n>PREGUNTA 2: ¿Cuantos megabytes(MB) exactos hay un gigabyte(GB)?")
    time.sleep(3)
    print ("a) 1024MB")
    time.sleep(1)
    print ("b) 1136MB")
    time.sleep(1)
    print ("c) 1000MB")
    time.sleep(1)
    print ("d) 1036MB"+RESET)
    
    respuesta_2 = input(GREEN+"\nTu respuesta: "+RESET).lower()
    while respuesta_2 not in ("a","b","c","d","x","A","B","C","D","X"):
      respuesta_2 = input(YELLOW+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET).lower()
    if respuesta_2 == 'a':
      print (MAGENTA+"La respuesta es correcta!"+RESET)
      puntaje+=random.randint(10,20)
    #Respuesta Secreta
    elif respuesta_2 == 'x':
      print (RED+"Felicidades! Encontraste la respuesta Secreta!"+RESET)
      puntaje+=random.randint(100,300)
    else:
      print (MAGENTA+"La respuesta es incorrecta!"+RESET)
      puntaje-=random.randint(0,10)
    time.sleep(1)
    print (RED+"Tu puntaje actual es de: "+RESET, puntaje)
  
    # Pregunta 3
    print (CYAN+"\n>PREGUNTA 3: ¿Como se llama el sistema de numeración que usan las computadoras basados en unos y ceros?")
    time.sleep(4)
    print ("a) Binario")
    time.sleep(1)
    print ("b) Hexadecimal")
    time.sleep(1)
    print ("c) Decimal")
    time.sleep(1)
    print ("d) Octal"+RESET)
    time.sleep(1)
    respuesta_3 = input(GREEN+"\nTu respuesta: "+RESET).lower()
    while respuesta_3 not in ("a","b","c","d","A","B","C","D"):
      respuesta_3 = input(YELLOW+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET).lower()
    if respuesta_3 == 'a':
      print (MAGENTA+"La respuesta es correcta!"+RESET)
      puntaje+=random.randint(10,20)
    else:
      print (MAGENTA+"La respuesta es incorrecta!"+RESET)
      puntaje-=random.randint(0,10)
    time.sleep(1)
    print (RED+"Tu puntaje actual es de: "+RESET, puntaje)
  
    # Pregunta 4
    print (CYAN+"\n>PREGUNTA 4: ¿Que hacemos para proteger el contenido de un archivo en un lenguaje cifrado?")
    time.sleep(3)
    print ("a) Descifrar")
    time.sleep(1)
    print ("b) Comprimir")
    time.sleep(1)
    print ("c) Encriptar")
    time.sleep(1)
    print ("d) Formatear"+RESET)
    time.sleep(1)
    respuesta_4 = input(GREEN+"\nTu respuesta: "+RESET).lower()
    while respuesta_4 not in ("a","b","c","d","A","B","C","D"):
      respuesta_4 = input(YELLOW+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET).lower()
    if respuesta_4 == 'c':
      print (MAGENTA+"La respuesta es correcta!"+RESET)
      puntaje+=random.randint(10,20)
    else:
      print (MAGENTA+"La respuesta es incorrecta!"+RESET)
      puntaje-=random.randint(0,10)
    time.sleep(1)
    print (RED+"Tu puntaje actual es de: "+RESET, puntaje)
  
    # Pregunta 5
    print (CYAN+"\n>PREGUNTA 5: ¿Que nombre recibe la distribución mas común de un teclado?")
    time.sleep(3)
    print ("a) QWERTY")
    time.sleep(1)
    print ("b) AZERTY")
    time.sleep(1)
    print ("c) Colemak")
    time.sleep(1)
    print ("d) Dvorak"+RESET)
    time.sleep(1)
    respuesta_5 = input(GREEN+"\nTu respuesta: "+RESET).lower()
    while respuesta_5 not in ("a","b","c","d","A","B","C","D"):
      respuesta_5 = input(YELLOW+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET).lower()
    if respuesta_5 == 'a':
      print (MAGENTA+"La respuesta es correcta!"+RESET)
      puntaje+=random.randint(10,20)
    else:
      print (MAGENTA+"La respuesta es incorrecta!"+RESET)
      puntaje-=random.randint(0,10)
    time.sleep(1)
    print(RED+"\n> Has terminado la trivia ",nombrePersona,", tu puntaje total es: ",puntaje,"!"+RESET)
    time.sleep(1)
    print ("\n\nComo evento final, tienes la opcion de usar tu suerte para cambiar tu puntaje total")
    time.sleep(1)
    print ("WARNING: Igual que tu puntaje puede duplicarse tambien puede dividirse")
    time.sleep(1)
    #Ruleta de la suerte
    suerte = input(GREEN+"Deseas usar tu suerte? (si/no): "+RESET).lower()
    
    while suerte not in ("si","no","SI","NO","Si","No"):
      suerte = input(YELLOW+"Debes responder si o no. Ingresa nuevamente tu respuesta: "+RESET)
  
    if suerte == "si":
      numAzar = random.randint(0,1)
      if numAzar == 0:
        puntaje = puntaje / 2
        time.sleep(1)
        print(CYAN+"\n> Usaste toda tu suerte, pero no fue suficiente y tu puntaje se dividió ",nombrePersona,", tu puntaje total es: ",puntaje)
      elif numAzar ==1:
        puntaje = puntaje * 2
        time.sleep(1)
        print("\n> Usaste toda tu suerte y lograste duplicarlo ",nombrePersona,", tu puntaje total es: ",puntaje)
    elif suerte == "no":
      time.sleep(1)
      print("\n> Decidiste no usar tu suerte ",nombrePersona,", tu puntaje total es: "+RESET,puntaje)
  
    #Puntajes Finales
    if puntaje <= 50:
      time.sleep(1)
      print (MAGENTA+"Tienes que esforzarte mas, inténtalo de nuevo!")
    if puntaje >= 50 and puntaje <= 100:
      time.sleep(1)
      print ("Excelente, manejas el tema!")
    if puntaje > 100:
      time.sleep(1)
      print ("Excelente, en el camino encontraste respuestas secretas"+RESET) 
      
    #Intentar otra vez trivia
    print("\n¿Deseas intentar la trivia nuevamente?")
    repetirTrivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
    
    if repetirTrivia != "si": 
      print("\nEspero {nombre} que lo hayas pasado bien, hasta pronto!")
      iniciarTrivia = False  
    
  
else:
  print(GREEN+"\n>",nombrePersona, " Lamentamos que no quieras continuar, puedes volver a intentar esta trivia en cualquier momento."+RESET)

