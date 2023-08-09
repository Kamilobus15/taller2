import os


ruta = os.path.join(os.path.dirname(__file__),'matriz_ejemplo.txt')
maxX = 0
maxY = 0
lista_cuadrados  = [[]]
with open(ruta,'r') as matriz:
    cuadrados = matriz.readlines()

#hacer lista de cordenadas de cuadrados
for cd in cuadrados:
    puntos = cd.split(',',3)
    lista_enteros = [int(caracter) for caracter in puntos]
    lista_cuadrados.append(lista_enteros)
lista_cuadrados.pop(0)
print(lista_cuadrados)


#función para sacar el punto maximo en x
for cd in cuadrados:
    puntos = cd.split(',',3)
    puntosIntX = int(puntos[2])
    puntosIntY = int(puntos[1])
    if maxX < puntosIntX:
        maxX = puntosIntX
    if maxY < puntosIntY:
        maxY = puntosIntY 



#pintamos matriz con cuadrados 
for x in range(maxX-1):
    for y in range(maxY-1):
        
        print('* ', end='')
    print()

#pintar matriz
