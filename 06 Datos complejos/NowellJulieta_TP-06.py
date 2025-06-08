#EJERCICIO 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}

precios_frutas["Naranja"]=1200
precios_frutas["Manzana"]=1500
precios_frutas["Pera"]=2300

print(precios_frutas)

#EJERCICIO 2
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2000

print(f"{precios_frutas} diccionario punto 2")

#EJERCICIO 3
precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}

lista_frutas = list(precios_frutas.keys())

print("Lista de frutas (solo nombres):")
print(lista_frutas)

#EJERCICIO 4
guia_telefonica={}
for i in range(5):
    clave=input("Ingrese el nombre del contacto: ")
    valor=input("Ingrese el número del contacto: ")
    guia_telefonica[clave]=valor

contacto=input("Qué contacto desea consultar: ")

if contacto in guia_telefonica:
    print(f"El número de {contacto} es {guia_telefonica[contacto]}")
else:
    print(f"El contacto {contacto} no existe en la guía")

#EJERCICIO 5
palabras_unicas= set()
recuento={}
frase = input("Ingrese una frase: ")
palabras= frase.split()

for palabra in palabras:
    palabras_unicas.add(palabra)

for palabra in palabras:
    if palabra in palabras_unicas:
        if palabra in recuento:
            recuento[palabra]+=1
        else:
            recuento[palabra]=1

print(palabras_unicas)
print(recuento)

#EJERCICIO 6
alumnos = {}
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    print(f"Ingresá las 3 notas de {nombre} separadas por espacio:")
    notas = tuple(map(float, input().split()))
    while len(notas) != 3:
        print("Debe ingresar exactamente 3 notas. Intentalo de nuevo:")
        notas = tuple(map(int, input().split()))
    alumnos[nombre] = notas
print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"{nombre}: promedio = {promedio:.2f}")

#EJERCICIO 7
parcial1 = {11, 12, 13, 14, 15}
parcial2 = {14, 15, 16, 17, 18}
ambos = parcial1.intersection(parcial2)
print("Aprobaron ambos parciales:", ambos)
solo_uno = parcial1.symmetric_difference(parcial2)
print("Aprobaron solo uno de los dos:", solo_uno)
al_menos_uno = parcial1.union(parcial2)
print("Aprobaron al menos un parcial:", al_menos_uno)

#EJERCICIO 8
stock_productos = {
        "pan": 30,
        "queso": 15,
        "jamon": 20
    }

while True:
        print("\nOpciones de gestión de stock:")
        print("1. Consultar stock de un producto")
        print("2. Agregar unidades a un producto existente")
        print("3. Agregar un nuevo producto")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            producto = input("Ingrese el nombre del producto a consultar: ").lower()
            if producto in stock_productos:
                print(f"El stock de {producto} es: {stock_productos[producto]} unidades.")
            else:
                print(f"El producto '{producto}' no se encuentra en el stock.")
        elif opcion == '2':
            producto = input("Ingrese el nombre del producto para agregar unidades: ").lower()
            if producto in stock_productos:
                try:
                    unidades = int(input(f"¿Cuántas unidades desea agregar a {producto}?: "))
                    if unidades > 0:
                        stock_productos[producto] += unidades
                        print(f"Se agregaron {unidades} unidades a {producto}. Nuevo stock: {stock_productos[producto]}.")
                    else:
                        print("Por favor, ingrese un número positivo de unidades.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número entero.")
            else:
                print(f"El producto '{producto}' no existe. Use la opción 3 para agregarlo.")
        elif opcion == '3':
            producto = input("Ingrese el nombre del nuevo producto: ").lower()
            if producto not in stock_productos:
                try:
                    unidades = int(input(f"Ingrese el stock inicial para {producto}: "))
                    if unidades >= 0:
                        stock_productos[producto] = unidades
                        print(f"Producto '{producto}' agregado con stock inicial de {unidades}.")
                    else:
                        print("Por favor, ingrese un número de unidades no negativo.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número entero.")
            else:
                print(f"El producto '{producto}' ya existe. Use la opción 2 para agregar unidades.")
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

#EJERCICIO 9
agenda = {
    ("lunes", "10:00"): "Trabajo",
    ("martes", "15:00"): "Gimnasio",
    ("miercoles", "09:00"): "Cafe",
    ("viernes", "18:30"): "Merienda"
}

dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (formato HH:MM): ")
evento = agenda.get((dia, hora))

if evento:
    print(f"El {dia.capitalize()} a las {hora} tenés: {evento}")
else:
    print(f"No hay ningún evento registrado el {dia} a las {hora}.")

#EJERCICIO 10
original = {
    "Argentina": "Buenos Aires",
    "Uruguay": "Montevideo",
    "Italia": "Roma",
    "Inglaterra": "Londres"
}

invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais
    
print(f"Diccionario original: {original}")
print(f"Diccionario invertido: {invertido} ")
