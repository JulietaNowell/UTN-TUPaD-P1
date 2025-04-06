#EJERCICIO 1
edad=int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

#EJERCICIO 2
nota=float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#EJERCICIO 3
numero=int(input("Ingrese un numero par "))
if numero % 2 == 0:
    print("Ha ingresado un numero par")
else: 
    print("Por favor, ingrese un numero par")

#EJERCICIO 4
edad=int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a") 

#EJERCICIO 5
contraseña=input("Introducir una contraseña: ")
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña correcta")

#EJERCICIO 6
import random
from statistics import mode, median, mean
numeros_aleatorios=[random.randint(1, 100) for i in range(50)]
moda=mode(numeros_aleatorios)
mediana=median(numeros_aleatorios)
media=mean(numeros_aleatorios)
if moda < mediana < media:
    sesgo="sesgo positivo o a la derecha"
elif media < mediana < moda:
    sesgo="sesgo negativo o a la izquierda"
else:
    sesgo="sin sesgo"
print(f"Lista generada: {numeros_aleatorios}")
print(f"\nMedia: {media: .2f}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"\nConclusion: {sesgo}")

#EJERCICIO 7
frase=input("Ingrese una palabra o frase: ")
vocales=('a','e','i','o','u')
if frase[-1] in vocales:
    frase += '!'
print(frase)

#EJERCICIO 8
nombre=input("Ingrese su nombre: ")
numero=int(input("Ingrese un numero (1 Mayusculas, 2 Minusculas, 3 Primera letra mayuscula): "))
if numero == 1:
    nombre_opcion = nombre.upper()
elif numero == 2:
    nombre_opcion = nombre.lower()
elif numero == 3:
    nombre_opcion = nombre.title()
print("Nombre: ", nombre_opcion)

#EJERCICIO 9
magnitud=float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    categoria = "Muy leve"
elif 3 <= magnitud < 4:
    categoria = "Leve"
elif 4 <= magnitud < 5:
    categoria = "Moderado"
elif 5 <= magnitud < 6:
    categoria = "Fuerte"
elif 6 <= magnitud < 7:
    categoria = "Muy fuerte"
else:
    categoria = "Extremo"
print("\nLa categoria del terremoto es: ", categoria)  

#EJERCICIO 10
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))
if hemisferio not in ['N', 'S']:
    print("Error: Hemisferio debe ser 'N' o 'S'")
else:
    if mes in (3, 4, 5, 6):
        if (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20) or (mes == 5) or (mes == 4):
            estacion = 'primavera' if hemisferio == 'N' else 'otoño'
        else:
            estacion = 'invierno' if hemisferio == 'N' else 'verano'
    elif mes in (6, 7, 8, 9):
        if (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20) or (mes == 8) or (mes == 7):
            estacion = 'verano' if hemisferio == 'N' else 'invierno'
        else:
            estacion = 'primavera' if hemisferio == 'N' else 'otoño'
    elif mes in (9, 10, 11, 12):
        if (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20) or (mes == 11) or (mes == 10):
            estacion = 'otoño' if hemisferio == 'N' else 'primavera'
        else:
            estacion = 'verano' if hemisferio == 'N' else 'invierno'
    else:  
        if (mes == 12 and dia >= 21) or (mes == 3 and dia <= 20) or (mes == 2) or (mes == 1):
            estacion = 'invierno' if hemisferio == 'N' else 'verano'
        else:
            estacion = 'otoño' if hemisferio == 'N' else 'primavera'
    print(f"Actualmente es {estacion} en el hemisferio {hemisferio}")