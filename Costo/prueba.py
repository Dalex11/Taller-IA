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
        self.pos_valor_enemigo = (0,0,'0')
        self.semilla = 0

    #Métodos getters
    def get_padre(self):
        return self.padre
    
    def get_estado(self):
        return self.estado
    
    def get_pos_valor_enemigo(self):
        return self.pos_valor_enemigo[2]
    
    def get_costo(self):
        return self.costo
    
    def get_semilla(self):
        return self.semilla
    
    #Métodos setters
    def set_pos_valor_enemigo(self, valor):
        self.pos_valor_enemigo = valor

    def set_costo(self, valor):
        self.costo = self.costo + valor

    def set_semilla(self, valor):
        self.semilla = self.semilla + valor

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
        posicion_enemigo = self.pos_valor_enemigo

        # Intentar realizar cada movimiento válido
        for row, column, operador in [(0, 1, "derecha"), (0, -1, "izquierda"), (-1, 0, "subir"), (1, 0, "bajar")]:
            # Verificar si el movimiento es válido
            if self.verificarExistencia(fila + row, columna + column) and matriz[fila + row][columna + column] != '1':
                #copiar matriz original
                matriz_aux = copy.deepcopy(matriz)

                #Vaya pasando el estado de la semilla durante toda la rama
                if (self.get_padre() != None):
                    self.set_semilla( self.get_padre().get_semilla() )

                #Si es una semilla
                if(matriz_aux[fila + row][columna + column] == '5'):
                    #Almacénela en el padre
                    self.set_semilla(1)
                    # Actualizar la matriz con el movimiento
                    matriz_aux[fila + row][columna + column] = '2'
                    matriz_aux[fila][columna] = '0'

                #Si el elemento es un freezer o un cell
                if matriz_aux[fila + row][columna + column] == '3' or matriz_aux[fila + row][columna + column] == '4':
                    #Si no hay semillas
                    if self.get_semilla() <= 0 :
                        #Guardar enemigo
                        #enemigo = matriz_aux[fila + row][columna + column]
                        posicion_enemigo = (fila + row, columna + column, matriz_aux[fila + row][columna + column])
                        # Actualizar la matriz con el movimiento
                        matriz_aux[fila + row][columna + column] = '2'
                        matriz_aux[fila][columna] = '0'
                    else:
                        self.set_semilla(-1)
                        posicion_enemigo = (fila + row, columna + column, '0')
                        # Actualizar la matriz con el movimiento
                        matriz_aux[fila + row][columna + column] = '2'
                        matriz_aux[fila][columna] = '0'

                #Si el padre tiene algún enemigo, entonces reemplacelo       
                if ( self.pos_valor_enemigo[2] != '0' ):
                     matriz_aux[fila + row][columna + column] = '2'
                     matriz_aux[fila][columna] = self.pos_valor_enemigo[2]
                     print('---', self.pos_valor_enemigo[2])
                
                else:
                    matriz_aux[fila + row][columna + column] = '2'
                    matriz_aux[fila][columna] = '0'
                    
                # Agregar la actualización al arreglo    
                movimientos.append((matriz_aux, operador,posicion_enemigo))

        # Devolver el arreglo de movimientos válidos
        return movimientos
        
    def modificarCosto (self):
        if (self.padre != None):
            if self.padre.get_pos_valor_enemigo() == '3':
                self.costo = self.padre.costo + 4
            elif self.padre.get_pos_valor_enemigo() == '4':
                self.costo = self.padre.costo + 7
            else:
                self.costo = self.padre.costo + 1

    # Método meta
    def esMeta (self, matriz):
        #Si la matriz no contiene esferas, es meta
        return ubicarElemento(matriz,'6') == -1
                 
#______________________________________________________________________

from ClaseCosto import Nodo, matriz
import time

# Aplicación del algoritmo
#Recorrer la matriz por costo

#Variables necesarias
cola = [] #Guadará los nodos hijos
expandidos = [] #Guadará los nodos expandidos

def hallarPosicionNodoMenorCosto(colaN):
    nodo = min(colaN, key=lambda x: x.get_costo())
    posicion = colaN.index(nodo)
    return posicion

#Función recorrer matriz
def recorrerMatriz ():
    #Definir padre inicial
    padre = Nodo(matriz,None,None)
    #Agregar padre a la cola
    cola.append(padre)
    #Variable que contendrá el primer elemeto de la cola, es decir el padre
    padre_expandido = 0

    #Ejecute mientras la cola este llena
    while len(cola) != 0:
 
        #Sacar el nodo con menor costo    
        padre_expandido = cola.pop(hallarPosicionNodoMenorCosto(cola))

        #Verificar si es meta
        if padre_expandido.esMeta(padre_expandido.estado) == True:
            #Añada el nodo meta a la lista expandidos y salgase del while
            expandidos.append(padre_expandido)  
            return
            
        #Crear hijos    
        for nueva_matriz, operador, pos_enemigo in padre_expandido.moverElemento():    
            #Cree el nodo hijo
            hijo = Nodo(nueva_matriz, padre_expandido, operador)
            #llamar el método modificarCosto para que modifique el costo del nodo
            hijo.modificarCosto()
            #Modificar el enemigo
            hijo.set_pos_valor_enemigo(pos_enemigo)

            #Si es la raíz o si el estado del hijo y el estado del abuelo son diferentes, entonces 
            if (padre_expandido.costo == 0 or hijo.get_estado() != padre_expandido.get_padre().get_estado()):
                #Agreguelo al final de la cola
                cola.append(hijo)

        #Agregar padre a la lista de nodos espandidos
        expandidos.append(padre_expandido)    
    print('No se puedo encontrar todas las esferas')

#Función calcular tiempo de implementación de la función recorrerMatriz
def calcularDuracion ():
    #Hora inicio
    inicio = time.time()
    recorrerMatriz()
    #Hora finalización
    fin = time.time() 
    #Diferencia entre tiempos para ver el tiempo gastado
    return fin - inicio

#Guardar tiempo en la variable 
tiempo_total = calcularDuracion()
