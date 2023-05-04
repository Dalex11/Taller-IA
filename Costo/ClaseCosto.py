import copy
import numpy as np

# 1.  Leer archivo .txt
with open("Prueba1.txt", 'r') as f:
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

    # def set_costo(self, valor):
    #     self.costo = self.costo + valor

    def set_semilla(self, valor):
        self.semilla = valor

    #Método que modifica el valor de una semilla
    # def modificarSemilla (self, valor):
    #     self.semilla = self.semilla + valor

    #Método que verifica si la fila y la columna del nodo existen en la matriz
    def verificarExistencia (self, fila, columna):
        return fila > -1 and fila < len(matriz[0]) and columna > -1 and columna < len(matriz)
    
    #Método para mover elemento
    def moverElemento(self):
        matriz = self.estado
        # Ubicar a gokú y sus coordenadas
        elemento = ubicarElemento(matriz, '2')
        fila = elemento[0]
        columna = elemento[1]

        # Variable necesaria
        movimientos = []
        enemigo = '0'
        semillas = 0

        #Vaya pasando el estado de la semilla del abuelo al padre
        # if (self.get_padre() != None):
        #     self.set_semilla( self.get_padre().get_semilla() )

        # Intentar realizar cada movimiento válido
        for row, column, operador in [(0, 1, "derecha"), (0, -1, "izquierda"), (-1, 0, "subir"), (1, 0, "bajar")]:

            # Verificar si el movimiento es válido
            if self.verificarExistencia(fila + row, columna + column) and matriz[fila + row][columna + column] != '1':

                #copiar matriz original
                matriz_aux = copy.deepcopy(matriz)

                #Si es una semilla
                if(matriz_aux[fila + row][columna + column] == '5'):
                    #Almacéne la semilla en el hijo, semilla del padre mas uno.
                    semillas = self.get_semilla()+1
                    # Actualizar la matriz con el movimiento
                    matriz_aux[fila + row][columna + column] = '2'
                    matriz_aux[fila][columna] = '0'

                #Si el elemento es un freezer o un cell
                elif matriz_aux[fila + row][columna + column] == '3' or matriz_aux[fila + row][columna + column] == '4':

                    #Si no hay semillas
                    if self.get_semilla() <= 0 :
                        #Valor del enemigo
                        enemigo = matriz_aux[fila + row][columna + column]
                        #Guarda estado de semilla en hijo
                        semillas = self.get_semilla()
                        # Actualizar la matriz con el movimiento
                        matriz_aux[fila + row][columna + column] = '2'
                        matriz_aux[fila][columna] = '0'
                    else:
                        #Disminuir semilla puesto que se debe usar y guarda estado de semilla en hijo
                        semillas = self.get_semilla()-1
                        #Guardar valor del enemigo
                        enemigo = '0'
                        # Actualizar la matriz con el movimiento
                        matriz_aux[fila + row][columna + column] = '2'
                        matriz_aux[fila][columna] = '0'

                #Si el padre tiene algún enemigo, entonces reemplacelo       
                else :
                    #Haya semilla o no, guarde el estado en el hijo
                    matriz_aux[fila + row][columna + column] = '2'
                    matriz_aux[fila][columna] = self.get_enemigo()  
                    enemigo = '0' 
                    semillas = self.semilla
                   
                # Agregar la actualización al arreglo    
                movimientos.append((matriz_aux, operador,semillas, enemigo))

        # Devolver el arreglo de movimientos válidos
        return movimientos
        
    def modificarCosto (self):
        #if (self.padre != None):
        if self.get_enemigo() == '3':
            self.costo = self.padre.costo + 4
        elif self.get_enemigo() == '4':
            self.costo = self.padre.costo + 7
        else:
            self.costo = self.padre.costo + 1

    # Método meta
    def esMeta (self, matriz):
        #Si la matriz no contiene esferas, es meta
        return ubicarElemento(matriz,'6') == -1
                 
