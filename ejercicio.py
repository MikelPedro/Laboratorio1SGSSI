
#######################Ejercicio del laboratorio 1 Cifrado I de SGSSI##################

#Introducir mensaje a descifrar:

print("Introduce el mensaje cifrado")
mensaje =  input()

letras = {'A':0,
	  'B':0,
	  'C':0,
	  'D':0,
	  'E':0,
	  'F':0,
	  'G':0,
	  'H':0,
	  'I':0,
	  'J':0,
	  'K':0,
	  'L':0,
	  'M':0,
	  'N':0,
	  'Ñ':0,
	  'O':0,
	  'P':0,
	  'Q':0,
	  'R':0,
	  'S':0,
	  'T':0,
	  'U':0,
	  'V':0,
	  'W':0,
	  'X':0,
	  'Y':0,
	  'Z':0,
	  }
cont = 0

for caracter in mensaje:

    if caracter in letras:
        
         letras[caracter] += 1 # suma uno cada vez que coincida una letra
         cont += 1  

letrasOrd = sorted(letras.items(),key=lambda x: x[1], reverse=True)
print("\n Las frecuencias de las letras en el texto son: \n")
print(letrasOrd)
print("En este texto hay " +  str(cont)  + " letras \n")

#################################CAMBIOS##########################################
# Se van cambiando las letras del mensaje en base a las frecuencias obtenidas o por prueba 

cambio = mensaje.replace("X","e")
cambio = cambio.replace("A","d")
cambio = cambio.replace("E","a")
cambio = cambio.replace("T","l")
cambio = cambio.replace("G","j")
cambio = cambio.replace("Z", "u")
cambio = cambio.replace("C","i")
cambio = cambio.replace("I","o")
cambio = cambio.replace("D","p")
cambio = cambio.replace("R","c")
cambio = cambio.replace("V","y")
cambio = cambio.replace("P","m")
cambio = cambio.replace("J","n")
cambio = cambio.replace("K","r")
cambio = cambio.replace("H","t")
cambio = cambio.replace("S","q")
cambio = cambio.replace("N","s")
cambio = cambio.replace("Q","b")
cambio = cambio.replace("O","f")

print("Texto con los cambios de letras indicados: \n")
print(cambio + "\n")

print("A continuación para cambiar letras modifique el script con $ gedit ejercicio.py y haga los cambios que considere oportunos en la parte indicada como cambios, en esa parte se pueden cambiar las letras de la manera: cambio = cambio.replace(letra a cambiar, letra nueva) o si es la primera vez cambio=mensaje.replace(letra a cambiar, letra nueva) \n ")

