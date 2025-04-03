#EJERCICIO 1 
print("Hola mundo")

#EJERCICIO 2
nombre=input("Ingrese su nombre ")
print(f"Hola {nombre}!")

#EJERCICIO 3
nombre=input("Ingrese su nombre ")
apellido=input("Ingrese su apellido ")
edad=input("Ingrese su edad ")
lugar_residencia=input("Ingrese su lugar de residencia ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}")

#EJERCICIO 4 
import math
radio=float(input("Ingrese el radio "))
radio=float(radio)
area=math.pi*(radio**2)
perimetro=radio*2*math.pi
print(f"El area es {area} y el perimetro es {perimetro}")

#EJERCICIO 5
segundos=int(input("Ingrese una cantidad de segundos "))
horas=segundos/3600
print (f"La cantidad de segundos ingresada equivale a {horas} horas")

#EJERCICIO 6
numero = int(input("Ingresa un número para generar su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {numero}:")
resultado1=numero*1
resultado2=numero*2
resultado3=numero*3
resultado4=numero*4
resultado5=numero*5
resultado6=numero*6
resultado7=numero*7
resultado8=numero*8
resultado9=numero*9
resultado10=numero*10
print(f"{numero} x {1} = {resultado1}")
print(f"{numero} x {2} = {resultado2}")
print(f"{numero} x {3} = {resultado3}")
print(f"{numero} x {4} = {resultado4}")
print(f"{numero} x {5} = {resultado5}")
print(f"{numero} x {6} = {resultado6}")
print(f"{numero} x {7} = {resultado7}")
print(f"{numero} x {8} = {resultado8}")
print(f"{numero} x {9} = {resultado9}")
print(f"{numero} x {10} = {resultado10}")

#EJERCICIO 7
numero1 = int(input("Ingresa un primer numero entero: "))
numero2 = int(input("Ingresa un segundo numero entero: ")) 
suma = numero1 + numero2
resta = numero1 - numero2
division = numero1 / numero2
multiplicacion = numero1 * numero2
print (f"La suma es igual a {suma}, la resta es igual a {resta}, la division es igual a {division} y la multiplicacion es igual a {multiplicacion}")

#EJERCICIO 8
altura = float(input("Ingresa su altura: "))
peso = float(input("Ingresa su peso: "))
IMC = peso/(altura**2)
print ("Su Indice de Masa Corporal es ",IMC)

#EJERCICIO 9
celsius = int(input("Ingrese una temperatura en grados celsuis: "))
fahrenheit = 9/5 * celsius + 32
print ("El equivalente en Fahrenheit es ",fahrenheit)

#EJERCICIO 10
numero1 = float(input("Ingresa un primer numero: "))
numero2 = float(input("Ingresa un segundo numero: ")) 
numero3 = float(input("Ingresa un tercer numero: ")) 
promedio = (numero1 + numero2 + numero3)/3
print ("El promedio de los numero es ", promedio)