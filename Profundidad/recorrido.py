import os, sys
current_dir = os.path.dirname(os.path.abspath('../Funciones/funciones.py'))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from Funciones.funciones import leerArchivo, revisarNodoRepetido, calcularDuracion
from Funciones.ClaseNodo import Nodo

# 1.  Leer archivo .txt
matriz = leerArchivo("..\Matrices_de_prueba\prueba_SC_1.txt")

# Aplicación del algoritmo
#Recorrer la matriz por amplitud

#Variables necesarias
pila = [] #Guardará los nodos hijos
expandidos = [] #Guardará los nodos expandidos

#Función recorrer matriz
def recorrerMatriz():
    #Definir padre inicial
    padre = Nodo(matriz, None, None)
    #Agregar padre a la pila
    pila.insert(0,padre)
    #Variable que contendrá el primer elemeto de la pila, es decir el padre
    padre_expandido = 0
    
    #Ejecute mientras la pila este llena
    while len(pila) != 0:
        #Sacar padre de la pila
        padre_expandido = pila.pop(0)

        #Verificar si es meta
        if padre_expandido.esMeta(padre_expandido.estado) == True:
            #Añada el nodo meta a la lista expandidos y salgase del while
            expandidos.append(padre_expandido)
            return

        #Crear hijos
        for nueva_matriz, operador, semillas, enemigo in padre_expandido.moverElemento():
            #Cree el nodo hijo
            hijo = Nodo(nueva_matriz, padre_expandido, operador)
            #llamar el método profundidad para que modifique el valor del atributo.
            hijo.modificarProfundidad()
            
            #Si el padre es la raiz o el hijo no ha existido en la rama, entonces 
            if (padre_expandido.profundidad == 0 or revisarNodoRepetido(hijo.get_estado(), padre_expandido)):
                #Agreguélo al principio de la pila
                pila.insert(0,hijo)
        
        #Agregar padre a la lista de nodos expandidos
        expandidos.append(padre_expandido)
    print('No se puedo encontrar todas las esferas')

#Guardar tiempo en la variable 
tiempo_total = calcularDuracion(recorrerMatriz)
