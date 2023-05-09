import time

#___________________________________________________________________________________________________

# 1.  Leer archivo .txt
def leerArchivo (url):
    with open(url, 'r') as f:
        matriz_string = f.read()

    matriz = []
    #Convertir el string a una matriz
    for linea in matriz_string.split('\n'):
        matriz.append(linea.split(' '))

    return matriz    

#___________________________________________________________________________________________________

def revisarNodoRepetido(posibleEstado, nodoPadre):
    if nodoPadre.get_padre() == None: # el nodo no tiene padre (es la raíz)
        return True # el estado del hijo es diferente a todos los ancestros
    elif posibleEstado == nodoPadre.get_padre().get_estado(): # el estado del hijo es igual al del padre
        return False # el estado del hijo es igual a uno de sus ancestros
    else:
        return revisarNodoRepetido(posibleEstado, nodoPadre.get_padre()) # recursivamente revisa al siguiente ancestro
    
#___________________________________________________________________________________________________

#Ubicar posición del elemento
def ubicarElemento (matriz, elementoabuscar):
    coordenadas = []
    for fila in matriz:
        for elemento in fila:
            if elemento == elementoabuscar:
                coordenadas.append(matriz.index(fila))
                coordenadas.append(fila.index(elemento))
    if not coordenadas:
        return -1
    return coordenadas

#___________________________________________________________________________________________________

#Función que calcula la distancia manhattan desde gokú hasta la esfera más cerca + la distancia manhattan entre las esferas.     
def calcularDistanciaManhattan(matriz):
    # Coordenadas gokú    
    coordenadas_goku = ubicarElemento(matriz, '2')
    # Coordenadas esferas
    coordenadas_esferas = ubicarElemento(matriz,'6')
    
    if coordenadas_goku == -1 or coordenadas_esferas == -1:
        return 0
    
    # Calcular distancia de Goku a cada esfera
    #Variable que contendrá las distancia manhattan desde goku hasta las esferas
    distancias = []
    for i in range(0, len(coordenadas_esferas), 2):
        #Variable que sumará la distancia entre goku y la esfera encontrada
        distancia = abs(coordenadas_esferas[i] - coordenadas_goku[0]) + abs(coordenadas_esferas[i+1] - coordenadas_goku[1])
        #Guarda dicha distancia en el arreglo
        distancias.append(distancia)
    
    # Calcular distancia total
    #Si solo hay una distancia (porque solo hay una esfera)
    if len(distancias) == 1:
        #Distancia total es igual a la distancia entre gokú y la única esfera que hay
        distancia_total = distancias[0]
    else:
        for i in range(0, len(coordenadas_esferas) -2, 2):
            #La distancia entre las esferas simere se calculará igual
            distancia_entre_esferas = abs(coordenadas_esferas[i] - coordenadas_esferas[i + 2]) + abs(coordenadas_esferas[i + 1] - coordenadas_esferas[i + 3])
        # tome la distancia menor (esfera más cerca) y súmele las distancia entre esferas
        distancia_total = min(distancias) + distancia_entre_esferas

    #Devuelva la distancia total    
    return distancia_total

#___________________________________________________________________________________________________

#Función calcular tiempo de implementación de la función recorrerMatriz
def calcularDuracion (funcion):
    #Hora inicio
    inicio = time.time()
    funcion()
    #Hora finalización
    fin = time.time() 
    #Diferencia entre tiempos para ver el tiempo gastado
    return fin - inicio


