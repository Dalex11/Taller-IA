import copy

# 1.  Leer archivo .txt
with open("Prueba_Amplitud.txt", 'r') as f:
    matriz_string = f.read()

matriz = []
#Convertir el string a una matriz
for linea in matriz_string.split('\n'):
    matriz.append(linea.split(' '))
      

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
    def __init__(self, estado, padre,operador):
        self.estado = estado
        self.padre = padre
        self.operador = operador
        self.profundidad = 0

    #Métodos getters
    def get_padre(self):
        return self.padre
    
    def get_estado(self):
        return self.estado
    
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
                 
