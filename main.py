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
#for linea in matriz_final:
 #   print(linea)

#función para sacar el area total de los cuadrados de manera fuerza bruta
#def area_fuerza_bruta(matriz):
 #   pass


#función para sacar el area de forma recursiba

#def area_recursiba(matriz):
 #   pass

# pintar matriz con los cuados pintados
for linea in matriz_final:
    print(linea)

    # función para sacar el area total de los cuadrados de manera fuerza bruta






def area_rectangulo(xu, yu, xd, yd):
    return (xd - xu) * (yu - yd)

def interseccion(r1, r2):
    x_overlap = max(0, min(r1[2], r2[2]) - max(r1[0], r2[0]))
    y_overlap = max(0, min(r1[1], r2[1]) - max(r1[3], r2[3]))
    return x_overlap * y_overlap

def area_total(rectangulos):
    total = 0
    for r in rectangulos:
        total += area_rectangulo(r[0], r[1], r[2], r[3])

    for i in range(len(rectangulos)):
        for j in range(i+1, len(rectangulos)):
            total -= interseccion(rectangulos[i], rectangulos[j])

    return total


def area_dividir_y_vencer(rectangulos):
    if len(rectangulos) == 1:
        r = rectangulos[0]
        return area_rectangulo(r[0], r[1], r[2], r[3])

    mitad = len(rectangulos) // 2
    izquierda = rectangulos[:mitad]
    derecha = rectangulos[mitad:]

    area_izq = area_dividir_y_vencer(izquierda)
    area_der = area_dividir_y_vencer(derecha)

    intersecciones = 0
    for r1 in izquierda:
        for r2 in derecha:
            intersecciones += interseccion(r1, r2)

    return area_izq + area_der - intersecciones

def area_total_provided(rectangles):
    return area_total(rectangles)

def area_divide_and_conquer_provided(rectangles):
    return area_dividir_y_vencer(rectangles)

if __name__ == "__main__":
    # Calcular y mostrar el área utilizando ambos métodos
    area_bruta_provided = area_total_provided(lista_cuadrados)
    area_divide_conquer_provided = area_divide_and_conquer_provided(lista_cuadrados)

    print(f"Área total (provided algorithms) utilizando fuerza bruta: {area_bruta_provided}")
    print(f"Área total (provided algorithms) utilizando dividir y vencer: {area_divide_conquer_provided}")
