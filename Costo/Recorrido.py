from ClaseCosto import Nodo, matriz
import time

# Aplicación del algoritmo
#Recorrer la matriz por costo

#Variables necesarias
cola = [] #Guadará los nodos hijos
expandidos = [] #Guadará los nodos expandidos

#Función que arroja la posición del nodo con menor costo
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
 
        #Sacar el nodo con menor costo y almacenarlo en la variable padre_expandido    
        padre_expandido = cola.pop(hallarPosicionNodoMenorCosto(cola))

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
