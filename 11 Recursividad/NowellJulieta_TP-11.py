#EJERCICIO 1
num = int(input("Ingrese un número: "))

def factorial(num):
    if num == 0 or num ==1:
      return 1
    else: 
      return num * factorial(num - 1) 

if num > 1:
   print(f"Factoriales del 1 al {num}: ")
   for i in range(1, num + 1):
      print(f"{i}! = {factorial(i)}")

#EJERCICIO 2
def secuencia_fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return secuencia_fibonacci(posicion-1)+secuencia_fibonacci(posicion-2)
                                
print("-- Visualizador de la secuencia de Fibonacci (0 1 1 2 3 5 8 13 21 34 ...) --")
posicion_usuario = int(input("Ingrese la posicion de la secuencia: "))

for i in range(0, posicion_usuario + 1):
    print(f"Posicion: {i}, Valor de Fibonacci: {secuencia_fibonacci(i)}")

#EJERCICIO 3 
def potencia(b, e):
    if b == 1 or e == 0:
        return 1
    else:
        return b * potencia(b, e-1)
    
b = int(input("Ingrese la base: "))
e = int(input("Ingrese el exponente: "))

if e < 0:
    print("El exponente debe ser un numero entero no negativo: ")
else:
    resultado = potencia(b, e)
    print(f"{b} elevado a la exponente {e} es: {resultado}")

#EJERCICIO 4
def conversor(num):
    if num == 0:
        return ""
    elif num < 0:
        return "Invalido"
    else:
        return conversor(num//2) + str(num%2)

num=int(input("Ingrese un numero: "))

if num<0:
    print("Ingrese un positivo")
else:
    binario=conversor(num)
    print(f"El numero {num} en binario es {binario}")

#EJERCICIO 5
def es_palindromo(palabra):
    if len(palabra) == 0 or len(palabra) == 1:
        return True
    if palabra[0] == palabra[-1]:
        palabra = palabra[1:-1] 
        return es_palindromo(palabra)
    return False
        
palabra_usuario = input("Ingrese una palabra para saber si es un palindromo: ")

if es_palindromo(palabra_usuario):
    print(f"'{palabra_usuario}' es un palindromo.")

else:
   print(f"'{palabra_usuario}' NO es un palindromo.") 

#EJERCICIO 6
def suma_digitos(n):
    if n < 10: 
        return n
    else:
        return n % 10 + suma_digitos(n//10) 

print(suma_digitos(1234))
print(suma_digitos(9))
print(suma_digitos(305))

#EJERCICIO 7
bloque = int(input("Ingresa la cantidad de bloques: "))
def contar_bloques(bloque):
    if bloque == 1:
       return 1
    else:
        return bloque + contar_bloques(bloque - 1)

print(contar_bloques(bloque))

#EJERCICIO 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

numero = int(input("Ingresar numero: "))
digito = int(input("Ingresar digito: "))

print(contar_digito(numero, digito))
