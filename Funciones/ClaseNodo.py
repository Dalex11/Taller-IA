import copy
import os, sys
current_dir = os.path.dirname(os.path.abspath('../Funciones/funciones.py'))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from Funciones.funciones import calcularDistanciaManhattan, ubicarElemento
      
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
        self.valor_heuristica_mas_costo = 0
        self.valor_heuristica = 0
        self.profundidad = 0

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
    
    def get_valor_heuristica(self):
        return self.valor_heuristica
    
    def get_valor_heuristica_mas_costo(self):
        return self.valor_heuristica_mas_costo
    
    #Métodos setters
    def set_enemigo(self, valor):
        self.enemigo = valor

    def set_semilla(self, valor):
        self.semilla = valor

    def set_valor_heuristica(self,valor):
        self.valor_heuristica = valor    

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
        valor_heuristica = 0

        # Intentar realizar cada movimiento válido
        for row, column, operador in [(0, 1, "derecha"), (0, -1, "izquierda"), (-1, 0, "subir"), (1, 0, "bajar")]:

            # Verificar si el movimiento es válido
            if fila + row in range(len(matriz)) and columna + column in range(len(matriz[0])) and matriz[fila + row][columna + column] != '1':

                #copiar matriz original
                matriz_aux = copy.deepcopy(matriz)

                #Si es una semilla
                if(matriz_aux[fila + row][columna + column] == '5'):
                    #Almacéne la semilla en el hijo, semilla del padre mas uno.
                    semillas = self.get_semilla()+1
                    #Actualizar la matriz con el movimiento
                    matriz_aux[fila + row][columna + column] = '2'
                    matriz_aux[fila][columna] = self.enemigo
                    #Después de coger una esfera el hijo no tendrá enemigos pendientes 
                    enemigo = '0'
                    #Guardar valor de la heurítica
                    valor_heuristica = calcularDistanciaManhattan(matriz_aux)

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
                        matriz_aux[fila][columna] = self.enemigo #En veremos
                        #Guardar valor de la heurítica
                        valor_heuristica = calcularDistanciaManhattan(matriz_aux)
                    else:
                        #Disminuir semilla puesto que se debe usar y guarda estado de semilla en hijo
                        semillas = self.get_semilla()-1
                        #Guardar valor del enemigo
                        enemigo = '0'
                        # Actualizar la matriz con el movimiento
                        matriz_aux[fila + row][columna + column] = '2'
                        # Cuando hay semilla, el enemigo desaparecerá definitivamente
                        matriz_aux[fila][columna] = '0'
                        #Guardar valor de la heurítica
                        valor_heuristica = calcularDistanciaManhattan(matriz_aux)

                #sino, mueva a gokú y coloque al enemigo cuando sea necesario      
                else :
                    # Actualizar la matriz con el movimiento
                    matriz_aux[fila + row][columna + column] = '2'
                    matriz_aux[fila][columna] = self.get_enemigo()  
                    #El enemigo será cero
                    enemigo = '0' 
                    #Haya semilla o no, guarde el estado en el hijo
                    semillas = self.semilla
                    #Guardar valor de la heurítica
                    valor_heuristica = calcularDistanciaManhattan(matriz_aux)
                   
                # Agregar la actualización al arreglo    
                movimientos.append((matriz_aux, operador,semillas, enemigo,valor_heuristica))

        # Devolver el arreglo de movimientos válidos
        return movimientos
        
    #Método que aumenta la profundidad del nodo
    def modificarProfundidad (self):
        if (self.padre != None):
            self.profundidad = self.padre.profundidad +1    
    
    def modificarCosto (self):
        if self.get_enemigo() == '3':
            self.costo = self.padre.costo + 4
        elif self.get_enemigo() == '4':
            self.costo = self.padre.costo + 7
        else:
            self.costo = self.padre.costo + 1

    def modificarValorHeuristicaMasCosto(self,valor):
        self.valor_heuristica_mas_costo = self.costo + valor  
           

    # Método meta
    def esMeta (self, matriz):
        #Si la matriz no contiene esferas, es meta
        return ubicarElemento(matriz,'6') == -1
                 