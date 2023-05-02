import copy
import numpy as np

# 1.  Leer archivo .txt
with open("Prueba1.txt", 'r') as f:
    matriz_string = f.read()

matriz = []
#Convertir el string a una matriz
for linea in matriz_string.split('\n'):
    matriz.append(linea.split(' '))

matriz2 = []
#Convertir el string a una matriz
for linea in matriz_string.split('\n'):
    matriz2.append(linea.split(' '))
      

#Ubicar posición del elemento
def ubicarElemento (matriz, elementoabuscar):
    coordenadas = []
    for fila in matriz:
        for elemento in fila:
            if elemento == elementoabuscar:
                coordenadas.append(matriz.index(fila))
                coordenadas.append(fila.index(elemento))
                return coordenadas
    return -1

def ubicarEnemigos (matriz):
    coordenadas = []
    coor = []
    for fila in matriz:
        for elemento in fila:
            if elemento == '3' or elemento == '4':
                coordenadas.append(matriz.index(fila))
                coordenadas.append(fila.index(elemento))
                coor.append(coordenadas)
                coordenadas.pop()

# Clase Nodo
class Nodo:
    #Constructor
    def __init__(self, estado, padre, operador):
        self.estado = estado
        self.padre = padre
        self.operador = operador
        self.costo = 0
        self.enemigo = '0'
        self.semilla = 0

    #Métodos getters
    def get_padre(self):
        return self.padre
    
    def get_estado(self):
        return self.estado
    
    def get_enemigo(self):
        return self.enemigo
    
    def get_costo(self):
        return self.costo
    
    def get_semilla(self):
        return self.semilla
    
    #Métodos setters
    def set_enemigo(self, valor):
        self.enemigo = valor

    def set_costo(self, valor):
        self.costo = self.costo + valor

    def set_semilla(self, valor):
        self.semilla = self.semilla + valor

    #Método que verifica si la fila y la columna del nodo existen en la matriz
    def verificarExistencia (self, fila, columna):
        return fila > -1 and fila < len(matriz[0]) and columna > -1 and columna < len(matriz)
    
    #Método para mover elemento
    def moverElemento(self,matriz):
        # Ubicar a gokú y sus coordenadas
        elemento = ubicarElemento(matriz, '2')
        fila = elemento[0]
        columna = elemento[1]

        # Variable necesaria
        movimientos = []

        # Intentar realizar cada movimiento válido
        for row, column, operador in [(0, 1, "derecha"), (0, -1, "izquierda"), (-1, 0, "subir"), (1, 0, "bajar")]:
            # Verificar si el movimiento es válido
            if self.verificarExistencia(fila + row, columna + column) and matriz[fila + row][columna + column] != '1':
                #copiar matriz original
                matriz_aux = copy.deepcopy(matriz)
                # Actualizar la matriz con el movimiento
                # matriz_aux[fila + row][columna + column] = '2'
                # if matriz2[fila][columna] == '3' or matriz2[fila][columna] == '4':
                #     if self.semilla > 0:
                #         matriz_aux[fila][columna] = '0'
                #         self.semilla -= 1
                #     else:
                #         matriz_aux[fila][columna] = matriz2[fila][columna]
                # elif matriz2[fila + row][columna + column] == '5':
                #     matriz_aux[fila][columna] = '0'
                #     self.semilla += 1
                # else:
                #     matriz_aux[fila][columna] = '0'
                ###########################################################
                # if matriz2[fila][columna] == '3' or matriz2[fila][columna] == '4':
                #     if self.semilla == 0:
                #         matriz_aux[fila][columna] = matriz2[fila][columna]
                #         self.costo +=  3
                #     else:
                #         matriz_aux[fila][columna] = '0'
                #         self.semilla -= 1
                # elif matriz2[fila][columna] == '5':
                #     matriz_aux[fila][columna] = '0'
                #     self.semilla += 1
                # else:
                #     matriz_aux[fila][columna] = '0'
                # matriz_aux[fila + row][columna + column] = '2'
                #############################################################
                if (self.padre != None):
                    matriz_aux[fila][columna] = self.padre.get_enemigo()
                    self.set_semilla(self.padre.get_semilla())
                else:
                    matriz_aux[fila][columna] = '0'
                if matriz_aux[fila + row][columna + column] == '3' or matriz_aux[fila + row][columna + column] == '4':
                    if self.get_semilla() == 0:
                        self.set_enemigo(matriz_aux[fila + row][columna + column])
                    else:
                        self.set_semilla(-1)
                        self.set_enemigo('0')
                elif matriz_aux[fila + row][columna + column] == '5':
                    self.set_semilla(1)
                    self.set_enemigo('0')
                else:
                    self.set_enemigo('0')
                matriz_aux[fila + row][columna + column] = '2'
                # Agregar la actualización al arreglo    
                movimientos.append((matriz_aux, operador))
        # Devolver el arreglo de movimientos válidos
        return movimientos

    #Método que aumenta el costo del nodo
    def modificarCosto (self):
        if (self.padre != None):
            if self.padre.get_enemigo() == '3':
                self.costo = self.padre.costo + 4
            elif self.padre.get_enemigo() == '4':
                self.costo = self.padre.costo + 7
            else:
                self.costo = self.padre.costo + 1

    # Método meta
    def esMeta (self, matriz):
        #Si la matriz no contiene esferas, es meta
        return ubicarElemento(matriz,'6') == -1
                 
