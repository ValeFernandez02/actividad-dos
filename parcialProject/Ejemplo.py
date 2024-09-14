# Conversión de tipos de datos
x = int(input("Ingresa un número entero: "))
y = float(x)
print(f"El número en formato decimal es: {y}")

## Enteros a Decimales
x = 10
y = float(x)
print(y)  # Output: 10.0

## Decimales a Enteros
a = 3.14
b = int(a)
print(b)  # Output: 3

## Cadenas a Enteros
s1 = "42"
c = int(s1)
print(c)  # Output: 42

## Cadenas a Decimales
s2 = "3.14"
d = float(s2)
print(d)  # Output: 3.14

#Multilíneas de cadenas.
text = "¡Hola, mundo!"
length = len(text)
print(length)  # Output: 12

#Funcion Len
text = "¡Hola, mundo!"
length = len(text)
print(length)  # Output: 12

#Subcadenas
message = "¡Bienvenido a Python!"

# Obtener los primeros n caracteres
first_5 = message[:5]
print(first_5)

# Obtener los caracteres de en medio
middle_chars = message[5:11]
print(middle_chars)

# Obtener los últimos n caracteres
last_6 = message[-6:]
print(last_6)

#Función upper().
# Convierte todos los caracteres de una cadena a mayúsculas
text = "¡Hola!"
uppercase_text = text.upper()
print(uppercase_text)

#Función lower()
#Convierte todos los caracteres de una cadena a minúsculas
text = "¡HOLA!"
lowercase_text = text.lower()
print(lowercase_text)

#Función strip()
#Elimina los espacios en blanco al inicio y al final de una cadena
text = "   ¡Hola, mundo!   "
stripped_text = text.strip()
print(stripped_text)

#Función replace()
#Reemplaza todas las ocurrencias de una subcadena por otra

text = "Me gusta Python. Aprendo Python."
new_text = text.replace("Python", "Java")
print(new_text)

#Función split()
#Divide una cadena en una lista de subcadenas.
text = "Hola,mundo,¿cómo,estás?"
words = text.split(",")
print(words)

## Formato de cadenas F-String
name = input("Ingresa tu nombre: ")
age = int(input("Ingresa tu edad: "))
message = f"Hola, mi nombre es {name} y tengo {age} años."
print(message)