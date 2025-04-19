# EJERCICIO 1
for numero in range(101):
    print(numero)

# EJERCICIO 2
numero = abs(int(input("Ingrese un numero entero: ")))
if numero == 0:
    print("El número tiene 1 dígito")
else:
    contador = 0
    while numero > 0:
        numero = numero // 10
        contador += 1
    print(f"El número tiene {contador} dígito(s)")

# EJERCICIO 3
numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
suma = 0
inicio = min(numero1, numero2)
fin = max(numero1, numero2)
for numero in range(inicio + 1 ,fin):
    suma += numero 
print(f"La suma de los números entre {numero1} y {numero2} (excluyéndolos) es: {suma}")

EJERCICIO 4
total = 0
while True:
    numero = int(input("Ingresa un número (Ingresa 0 para terminar): "))
    if numero == 0:
        break 
    total += numero  
print(f"El total acumulado es: {total}")

# EJERCICIO 5
import random
respuesta = random.randint(0, 9)
intentos = 0
while True:
    numero = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1   
    if numero == respuesta:
        print("¡Correcto!")
        break
    else:
        print("Incorrecto, sigue intentando.")
print(f"Necesitaste {intentos} intento/s")

# EJERCICIO 6
print("Los numeros pares del 0 al 100 de manera decreciente son:")
for numero in range (100,-1,-2):
    print(numero)

EJERCICIO 7
numero_usuario = int(input("Ingrese un numero entero positivo: "))
suma = 0
for numero in range(0,numero_usuario+1):
    suma += numero
print(f"La suma de los numeros entre el 0 y {numero_usuario} es: {suma}")

# EJERCICIO 8
par = 0
impar = 0 
positivo = 0
negativo = 0
print("Ingrese 5 numeros enteros ")
for i in range(100):
    num = int(input(f"Numero {i+1}: "))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    if num >= 0:
        positivo += 1
    else:
        negativo += 1
print("\nResultados: ")
print(f"Numeros pares: {par}")
print(f"Numeros impares: {impar}")
print(f"Numeros positivos: {positivo}")
print(f"Numeros negativos: {negativo}")

# EJERCICIO 9
cantidad_numeros = 5
suma_total = 0
numeros_ingresados = 1
print(f"Ingrese {cantidad_numeros} numeros enteros: ")
while numeros_ingresados <= cantidad_numeros:
    numero = int(input(f"Numero {numeros_ingresados}: "))
    suma_total += numero
    numeros_ingresados += 1
if cantidad_numeros > 0 :
    media = suma_total / cantidad_numeros
    print(f"\nLa media es: {media:.2f}")
else:
    print("No se ingresaron numeros para calcular la media")

# EJERCICIO 10
numero = int(input("Ingrese un número entero positivo: "))
numero_invertido = 0
num_original = numero
while numero > 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero = numero // 10
print(f"El número {num_original} invertido es: {numero_invertido}")
