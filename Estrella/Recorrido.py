import os, sys
current_dir = os.path.dirname(os.path.abspath('../Funciones/funciones.py'))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from Funciones.funciones import leerArchivo, calcularDuracion, calcularDistanciaManhattan
from Funciones.ClaseNodo import Nodo

# 1.  Leer archivo .txt
matriz = leerArchivo("..\Matrices_de_prueba\prueba_CC_1.txt")

# Aplicación del algoritmo
#Recorrer la matriz por costo

#Variables necesarias
cola = [] #Guadará los nodos hijos
expandidos = [] #Guadará los nodos expandidos

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
 
        #Sacar el nodo con menor costo y almacenarlo en la variable padre_expandido    
        padre_expandido = cola.pop(cola.index(min(cola, key=lambda x: x.get_valor_heuristica_mas_costo())))

        #Verificar si es meta
        if padre_expandido.esMeta(padre_expandido.estado) == True:
            #Añada el nodo meta a la lista expandidos y salgase del while
            expandidos.append(padre_expandido)  
            return
            
        #Crear hijos    
        for nueva_matriz, operador, semillas, pos_enemigo in padre_expandido.moverElemento():    
            #Cree el nodo hijo
            hijo = Nodo(nueva_matriz, padre_expandido, operador)
            #Modificar el enemigo
            hijo.set_enemigo(pos_enemigo)
            #Modificar estado de semilla
            hijo.set_semilla(semillas)
            #llamar el método modificarCosto para que modifique el costo del nodo
            hijo.modificarCosto()
            #Calcular heurística
            valor_heuristica = calcularDistanciaManhattan(nueva_matriz)
            #llamar el método para que modifique el valor del atributo.
            hijo.set_valor_heuristica(valor_heuristica)
            #Llamar método modificarValorHeuristicaMasCosto para sumar el costo + el valor de la heurística
            hijo.modificarValorHeuristicaMasCosto()

            #Si es la raíz o si el estado del hijo y el estado del abuelo son diferentes, entonces 
            if (padre_expandido.get_costo() == 0 or hijo.get_estado() != padre_expandido.get_padre().get_estado()):
                #Agreguelo al final de la cola
                cola.append(hijo)

        #Agregar padre a la lista de nodos espandidos
        expandidos.append(padre_expandido)    
    print('No se puedo encontrar todas las esferas')

#Guardar tiempo en la variable 
tiempo_total = calcularDuracion(recorrerMatriz)