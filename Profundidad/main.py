from ClaseNodo import Nodo
from  ClaseNodo import matriz
import time

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
    pila.append(padre)
    #Variable que contendrá el primer elemeto de la pila, es decir el padre
    padre_expandido = 0
    
    #Ejecute mientras la pila este llena
    while len(pila) != 0:
        #Sacar padre de la pila
        padre_expandido = pila.pop()

        #Verificar si es meta
        if padre_expandido.esMeta(padre_expandido.estado) == True:
            #Añada el nodo meta a la lista expandidos y salgase del while
            expandidos.append(padre_expandido)
            return

        #Crear hijos
        for nueva_matriz, operador in padre_expandido.moverElemento(padre_expandido.estado)[::-1]:
            #Cree el nodo hijo
            hijo = Nodo(nueva_matriz, padre_expandido, operador)
            #llamar el método profundidad para que modifique el valor del atributo.
            hijo.modificarProfundidad()
            
            #Si es la raíz o si el estado del hijo y el estado del abuelo son diferentes, entonces
            if padre_expandido.profundidad == 0 or hijo.get_estado() != padre_expandido.get_padre().get_estado():
                #Agreguelo al inicio de la pila
                pila.append(hijo)
        
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

recorrerMatriz()


