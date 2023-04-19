import copy
import time
import pygame

# Variables
matriz = []
tamaño_ventana = 50

# Leer archivo .txt
with open('Prueba1.txt', 'r') as f:
    matriz_string = f.read()

# Convertir el string a una matriz
for linea in matriz_string.split('\n'):
    matriz.append([int(valor) for valor in linea.split(' ')])

# Mostrar la matriz
pygame.init()
ventana = pygame.display.set_mode((len(matriz[0])*tamaño_ventana, len(matriz)*tamaño_ventana))
pygame.display.set_caption('Matriz')

img_suelo = pygame.image.load('.\imagenes\suelo.jpg')
img_pared = pygame.image.load('.\imagenes\pared.jpg')
img_goku = pygame.image.load('.\imagenes\goku.jpg')
img_freezer = pygame.image.load('./imagenes/freezer.jpg')
img_cell = pygame.image.load('.\imagenes\cell.jpg')
img_semilla = pygame.image.load('.\imagenes\semilla.jpg')
img_esfera = pygame.image.load('.\imagenes\esfera.jpg')


for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == 0:
            ventana.blit(img_suelo, (j*tamaño_ventana, i*tamaño_ventana))
        elif matriz[i][j] == 1:
            ventana.blit(img_pared, (j*tamaño_ventana, i*tamaño_ventana))
        elif matriz[i][j] == 2:
            ventana.blit(img_goku, (j*tamaño_ventana, i*tamaño_ventana))
        elif matriz[i][j] == 3:
            ventana.blit(img_freezer, (j*tamaño_ventana, i*tamaño_ventana))
        elif matriz[i][j] == 4:
            ventana.blit(img_cell, (j*tamaño_ventana, i*tamaño_ventana))
        elif matriz[i][j] == 5:
            ventana.blit(img_semilla, (j*tamaño_ventana, i*tamaño_ventana))
        elif matriz[i][j] == 6:
            ventana.blit(img_esfera, (j*tamaño_ventana, i*tamaño_ventana))

# Actualizar la ventana
pygame.display.update()

# Esperar a que el usuario cierre la ventana
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

# 3.  Se aplicará búsqueda por amplitud

# 4.  Aplicación del algoritmo

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

# Clase Nodo
class Nodo:
    #Constructor
    def __init__(self, estado, padre, operador):
        self.estado = estado
        self.padre = padre
        self.operador = operador
        self.profundidad = 0

    #Métodos getters
    def get_padre(self):
        return self.padre
    
    def get_estado(self):
        return self.estado
    
    def get_operador(self):
        return self.operador
    
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
                matriz_aux[fila + row][columna + column] = '2'
                matriz_aux[fila][columna] = '0'
                # Agregar la actualización al arreglo    
                movimientos.append((matriz_aux, operador))

        # Devolver el arreglo de movimientos válidos
        return movimientos

    #Método que aumenta la profundidad del nodo
    def modificarProfundidad (self):
        if (self.padre != None):
            self.profundidad = self.padre.profundidad +1    

    # Método meta
    def esMeta (self, matriz):
        #Si la matriz no contiene esferas, es meta
        return ubicarElemento(matriz,'6') == -1
                 


# Función profundidad del árbol

#Recorrer la matriz por amplitud


