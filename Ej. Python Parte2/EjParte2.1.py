import random
lista = []

def encontrarMayor(lista, numeroEncontrado):
    contMayor = 0
    for i in lista:
        if i > numeroEncontrado:
            contMayor+=1
    return contMayor

for i in range (0,10):
    lista.append(random.randint(1, 20))
print (lista)

numeroIngresado = int(input("Ingrese un numero "))
print (f"La cantidad de numero mayores a {numeroIngresado} es: {encontrarMayor (lista, numeroIngresado)}")

def promediar (lista):
    suma = 0
    for i in lista:
        suma += i
        promedio = suma/len(lista) 
    return promedio


for i in range (0,10):
    lista.append(random.randint(1, 20))
print (lista)
print (f"El promedio de la lista de numeros aleatorios es: {promediar(lista)}")

def encontrarMayorMenor(lista):
    Mayor = lista[0]
    Menor = lista[0]
    for i in lista:
        if i > Mayor:
            Mayor = i
        elif i < Menor: 
            Menor = i
    return Mayor, Menor


for i in range (0,10):
    lista.append(random.randint(1, 20))
print (lista)
print(f"El numero mayor y el numero menor son: {encontrarMayorMenor(lista)}")
