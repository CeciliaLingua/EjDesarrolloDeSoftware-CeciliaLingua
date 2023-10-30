import random

def generar_lista_de_atletas():
    """
    Esta función genera aleatoriamente los datos de 20 atletas que participaron de una maratón.
    Devuelve una lista de atletas donde cada atleta es un diccionario con los campos:
        - nombre: el nombre del atleta
        - numero: el número con el que participó en la maratón
        - tiempo_llegada: la cantidad de segundos que tardó en llegar
    """
    lista_atletas = []
    nombres = ('Daniel', 'Alejandro', 'Pablo', 'Hugo', 'Álvaro', 'Adrián', 'David', 'Sergio', 'Diego')
    apellidos = ('García', 'Rodríguez', 'González', 'Fernández', 'López', 'Martínez', 'Sanchez', 'Pérez')    
    for i in range(1, 21):
        atleta = {
            "nombre": random.choice(nombres) + " " + random.choice(apellidos),
            "numero": i,
            "tiempo_llegada": random.random() * 120
        }
        lista_atletas.append(atleta)
    return lista_atletas

def imprimir_info_atletas(lista_atletas):
    for atleta in lista_atletas:
        print(f"{atleta['numero']} - {atleta['nombre']}: ({atleta['tiempo_llegada']} segundos)")

def encontrar_ganador(lista_atletas):
    ganador = min(lista_atletas, key=lambda x: x['tiempo_llegada'])
    return ganador['numero']

def obtener_datos_atleta(numero_atleta, lista_atletas):
    for atleta in lista_atletas:
        if atleta['numero'] == numero_atleta:
            return atleta

def encontrar_podio(lista_atletas):
    podio = sorted(lista_atletas, key=lambda x: x['tiempo_llegada'])[:3]
    return [atleta['numero'] for atleta in podio]

lista_atletas = generar_lista_de_atletas()

imprimir_info_atletas(lista_atletas)

numero_ganador = encontrar_ganador(lista_atletas)
print(f"El ganador es el atleta número {numero_ganador}")

podio_ganadores = encontrar_podio(lista_atletas)
print(f"Podio de ganadores: {podio_ganadores}")

numero_competidor = int(input("Ingrese el numero de atleta de un competidor: "))  
datos_competidor = obtener_datos_atleta(numero_competidor, lista_atletas)
print(f"Datos del competidor número {numero_competidor}: {datos_competidor}")