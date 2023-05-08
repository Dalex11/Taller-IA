import tkinter as tk
from Recorrido import tiempo_total, expandidos, matriz
from PIL import Image, ImageTk
import time

#Guardar en una variable las matrices de los nodos en la lista expandidos
nodo_actual = expandidos[len(expandidos)-1]
caminos = []
caminos_final = []
while nodo_actual.padre is not None:
    nodo_actual = nodo_actual.padre
    caminos.append(nodo_actual.estado)
caminos.insert(0,expandidos[len(expandidos)-1].estado) 
caminos_final = caminos[::-1] #Arreglo que contiene los estados válidos desde la raíz hasta el final   

ventana = tk.Tk()

# Obtener el ancho y la altura de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
altura_pantalla = ventana.winfo_screenheight()

# Calcular la posición x e y de la ventana para centrarla
x = int((ancho_pantalla - 1150) / 2)  # ancho de la ventana es 800
y = int((altura_pantalla - 700) / 2)  # altura de la ventana es 600

# Configurar la posición de la ventana
ventana.geometry(f"1150x700+{x}+{y}")

# Tamaño de cada celda
cell_width = 50
cell_height = 50

# Crear el canvas y dibujar el cuadrado 
canvas = tk.Canvas(ventana, width=cell_width*10, height=cell_height*10) #Ancho del widget canvas
canvas.place(x=60, y=60, width=cell_width*10, height=cell_height*10) #Agregar canvas a la ventana
cuadrado_matriz = canvas.create_rectangle(0,0,cell_width*10,cell_height*10)
canvas.itemconfig(cuadrado_matriz, outline="black", width=7)

# Dibujar la cuadrícula
for i in range(10):
    canvas.create_line(i*cell_width, 0, i*cell_width, cell_height*10) #Dibuja líneas verticales
    canvas.create_line(0, i*cell_height, cell_width*10, i*cell_height) #Dibuja líneas horizontales

imagen = None
canvas.imagenes = []

# Dibujar el contenido de cada celda
def dibujarImagen (url,etiqueta,x,y,width,height):
    imagen = Image.open(url)
    imagen = imagen.resize((x,y))
    imagen = ImageTk.PhotoImage(imagen)
    canvas.create_image(width, height, anchor=tk.NW, image=imagen, tag=etiqueta)
    canvas.imagenes.append(imagen)

# Variable global para guardar la referencia de la imagen
imagenT = None

def mostrarReporte():
    global imagenT
    
    cost = expandidos[len(expandidos)-1].costo
    cost_string = str(cost)
    cuadro_info = tk.Canvas(ventana, width=400, height=400)
    cuadro_info.place(x=580, y=50, width=600, height=600)
    cuadro_info.create_rectangle(50, 100, 500, 400, fill='white')
    cuadro_info.create_text(250, 160, text='El costo minimo de la solución es: ' + cost_string, width=400, font=("Arial", 15))
    cuadro_info.create_text(250, 190, text='Cantidad de nodos expandidos: ' + str(len(expandidos)) + ' nodos', width=400, font=("Arial", 15))
    cuadro_info.create_text(250, 220, text='Tiempo de cómputo: ' + str(round(tiempo_total, 3)) + ' segundos', width=400, font=("Arial", 15))
    imagen = Image.open("../imagenes/muñeca.png")
    imagen = imagen.resize((150, 150))
    imagenT = ImageTk.PhotoImage(imagen)
    cuadro_info.create_image(270, 300, image=imagenT)

#Función que muestra la matriz dada en la ventana
def verMatriz (matriz,url,etiqueta):
     # borramos todo lo dibujado anteriormente
     canvas.delete(etiqueta)
     for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor == '1':
                dibujarImagen(url[0],etiqueta,45,45,j*cell_width, i*cell_height)
            if valor == '2':
                dibujarImagen(url[1],etiqueta,45,45,j*cell_width, i*cell_height)
            if valor == '3':
                dibujarImagen(url[2],etiqueta,45,45,j*cell_width, i*cell_height)
            if valor == '4':
                dibujarImagen(url[3],etiqueta,45,45,j*cell_width, i*cell_height)
            if valor == '5':
                dibujarImagen(url[4],etiqueta,45,45,j*cell_width, i*cell_height)
            if valor == '6':
                dibujarImagen(url[5],etiqueta,45,45,j*cell_width, i*cell_height)
            if valor == '7':
                dibujarImagen(url[6],etiqueta,45,45,j*cell_width, i*cell_height) 
            if valor == '8':
                dibujarImagen(url[7],etiqueta,45,45,j*cell_width, i*cell_height)       

# 2.  Mostrar el estado inicial  
#Función que mostrará la matriz incial
def verMatrizInical():
    verMatriz(matriz, ["../imagenes/muro.png","../imagenes/gokú.png","../imagenes/freezer.png","../imagenes/cell.png","../imagenes/semilla.png","../imagenes/esfera.png"],'imagen')

verMatrizInical()

#Función que permitirá visualizar la animación
def animacion ():
    for matriz in caminos_final[1:]:
        verMatriz(matriz,["../imagenes/muro.png","../imagenes/gokú.png","../imagenes/freezer.png","../imagenes/cell.png","../imagenes/semilla.png","../imagenes/esfera.png"],'imagen')
        time.sleep(0.1)
        ventana.update()
    mostrarReporte()    

#Agregar botones a la ventana y ejecutar función a darles click
btn = tk.Button(ventana, text='Empezar', command = animacion, bg='black', fg='white', font=("Arial", 12))         
btn.place(x=135,y=590, width=150, height=50)
btn2 = tk.Button(ventana, text='Volver', command = verMatrizInical, bg='black', fg='white', font=("Arial", 12))         
btn2.place(x=310,y=590, width=150, height=50)

ventana.mainloop()







