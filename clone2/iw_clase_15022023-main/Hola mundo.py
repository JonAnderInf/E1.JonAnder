# Muestra tu nombre escribiendolo
nombre = input("Introduce tu nombre: ")
print(nombre)
# Tipo FLOAT mostrar
z=float(5.44)
print(z)
print(str(type(z)))


# Mostrar Ecuación
a = 4
b = 3
print(f"La multiplicación de {a} y {b} es igual a {a * b}")


# CONVERSIÓN de tipos Bool , Int y Float
num1 = 88
num2 = 99.8
test = True

# Mal por que no puede concatenar int con float sin poner str
print ("Tengo" + num1 + "perros y tengo" + num2 + "kilos de pienso y" + test)

# Bien si pones str
print ("Tengo" + str(num1) + "perros y tengo" + str(num2) + "kilos de piensoy" + str(test))


# MÉTODOS DE CADENA DE TEXTO(String)

frase = 'El one piece existe'
frase[0] # devuelve el primer caracter
frase[1] # devuelve el segundo caracter
frase[-1] # devuelve el primer caracter empezando por el final
frase[-2] # # devuelve el segundo caracter empezando por el final

print(frase[0])

# OBTENER UN SUBSTRING
frase = "Chupa chupa"
mi_substring = frase [1:5]
 # devolverá los caracteres desde la posición 1 hasta la 5 (no incluye el 0,5)
print(mi_substring)

frase = "Chupa chupa"
mi_substring = frase [1:]
# devolverá los caracteres desde la posición 1 para adelante (Sin la 0)
print(mi_substring)


frase = "Chupa chupa"
mi_substring = frase [:5]
# devolverá los caracteres desde la posición 5 para atras (Sin el 5)
print(mi_substring)



# MÉTODOS ÚTILES STRING

len(str) # devuelve la longitud del string
frase = "chupa chupa"
print(len(str(frase)))

str.upper() # convierte a mayúsculas
frase = "chupa chupa"
print(str.upper(frase))

str.lower() # convierte a minúsculas
frase = "chupa chupa"
print(str.lower(frase))

str.title() # convierte a mayúsculas la primera letra de cada palabra
frase = "chupa chupa"
print(str.title(frase))

str.count(substring [, inicio, fin]) # devuelve el número de veces que aparece
# el substring en el string. Opcionalmente se puede indicar el inicio y fin.

str.find('d') # devuelve el índice de la primera aparición de 'd'
# (devolverá -1 si no lo encuentra)

substr in str # devuelve True si el string contiene el substring

str.replace(old, new [, count]) # reemplaza 'old' por 'new' un máximo de 'count' vec\
es.

str.isnumeric() # devuelve TRUE si str contiene solamente números sino FALSE
frase = "chupa chupa "
print(str.isnumeric(frase))


#EJERCICIO 1  CODING TIME!!

nombre = "Michael Jordan"
edad = 50
media_punto = float(28.5)
activo = False

print (nombre , edad , media_punto , activo)


#EJERCICIO 2 

nombre = input("Esbribe tu nombre ")
print(nombre)

DNI = input("Esbribe tu DNI ")
print(DNI)

edad = input("Esbribe tu edad ")
print(edad)

print("Mi nombre es" + str(nombre) + "Mi DNI es " + str(DNI) + "y tengo" + str(edad) + "años")


#EJERCICIO 3 SIN LEN()

palabra = input("Escribe la frase")
print(palabra[0],palabra[1],palabra[2],palabra[-3],palabra[-2],palabra[-1])



#EJERCICIO 3 CON LEN()

def obtener_primeros_y_ultimos_caracteres(frase):

  # Obtenemos la longitud del string
  longitud_texto = len(frase)

  # Si el string tiene menos de 6 caracteres, devolvemos el string original
  if longitud_texto < 6:
    return frase

  # Obtenemos los primeros 3 caracteres
  primeros_caracteres = frase[:3]

  # Obtenemos los últimos 3 caracteres
  ultimos_caracteres = frase[longitud_texto-3:]

  # Devolvemos el string compuesto por los primeros 3 caracteres y los últimos 3 caracteres
  return primeros_caracteres + ultimos_caracteres

# Ejemplo de uso
texto = input("Introduce un texto: ")

resultado = obtener_primeros_y_ultimos_caracteres(texto)

print(f"Resultado: {resultado}")


#EJERCICIO 4

def obtener_substring(frase, posicion, longitud):
  # Validamos la posición y la longitud
  if posicion < 0 or posicion >= len(frase):
    raise ValueError("La posición debe ser un valor entre 0 y la longitud de la frase.")
  if longitud < 0:
    raise ValueError("La longitud debe ser un valor positivo.")

  return substring

# Pedimos la frase y los dos números al usuario
frase = input("Escribe una frase: ")
posicion = int(input("Escribe la posición de inicio del substring: "))
longitud = int(input("Escribe la longitud del substring: "))

substring = frase[posicion:posicion+longitud]
print(f"Substring: {substring}")

#Ejercicio 5 ¿A medias preguntar?
#globales y acceso desde dentro funcion y como modificar

def reemplazar_letra(frase, letra_origen, letra_nueva) :
    
  frase_minus = frase.lower()

  num_aparicion = frase_minus.count(letra_origen)
  

  Frase_rempl = frase_minus.replace(letra_origen, letra_nueva)

  return Frase_rempl.capitalize()

frase = input("Escribe una frase :")

letra_origen = input("Escribe una letra para reemplazar :")

letra_nueva = input("Escribe la letra que quieras reemplazar :")

Frase_rempl = reemplazar_letra(frase, letra_origen, letra_nueva)

print(f"Número de apariciones: {num_aparicion}")

print(f"Resultado: {Frase_rempl}")


#EJERCICIO 1 OPERADORES LÓGICOS:

def mostrar_tabla_multiplicar(numero):

  # Validamos el número
  if numero < 1 or numero > 10:
    print(f"NO es valido ,el número debe estar entre 1 y 10.")
    return

  # Mostramos la tabla de multiplicar
  for i in range(1, 11):
    print(f"{i * numero}")
    
# Pedimos el número al usuario
numero = int(input("Introduce un número del 1 al 10: "))
mostrar_tabla_multiplicar(numero)
