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
"""for x in range(maxX-1):
    for y in range(maxY-1):
        print('* ', end='')
    print()"""

#pintar matrizcon sus respectivos cuadros 

matriz_final = [['@' for _ in range(maxY + 1)] for _ in range(maxX + 1)]
for cd in lista_cuadrados:
    for x in range(maxY + 1):
        for y in range(maxX + 1):
            valor3 = abs(cd[3]- 6)
            valor1 = abs(cd[1]- 6)
            if valor1  == x   and cd[2] >= y and cd[0] <= y:
                matriz_final[x][y] = '+' 
                print('* ', end='')
            elif valor3 == x and cd[2] >= y and cd[0] <= y:
                print('* ', end='')
                matriz_final[x][y] = '+' 
            elif cd[0] == y and valor3 >= x and valor1 <= x:
                print('* ', end='')
                matriz_final[x][y] = '+'  
            elif cd[2] == y and valor3 >= x and valor1 <= x:
                print('* ', end='')
                matriz_final[x][y] = '+' 
            else:
                print('* ', end='')

        print()

    print()
    print()


#pintar matriz con los cuados pintados 
for linea in matriz_final:
    print(linea)

#función para sacar el area total de los cuadrados de manera fuerza bruta 
def area_fuerza_bruta(matriz):
    pass


#función para sacar el area de forma recursiba 

def area_recursiba(matriz):
    pass