import tkinter as tk
from tkinter import StringVar, filedialog
import shutil
import os

ventana = tk.Tk()

ancho_pantalla = ventana.winfo_screenwidth()
altura_pantalla = ventana.winfo_screenheight()

x = int((ancho_pantalla - 500) / 2)
y = int((altura_pantalla - 400) / 2)

# Configurar la posición de la ventana
ventana.geometry(f"500x300+{x}+{y}")

select_var = StringVar(ventana)

def seleccionar_archivo():
    archivo = filedialog.askopenfilename(title="Seleccionar matriz")
    if archivo:
        confirmar_sobrescritura(archivo)

def confirmar_sobrescritura(archivo):
    confirmar = tk.messagebox.askyesno("Confirmar sobrescritura", f"¿Deseas sobrescribir la matriz?")
    if confirmar:
        shutil.copy2(archivo, "./matriz.txt")
        tk.messagebox.showinfo("Sobrescritura exitosa", f"La matriz ha sido sobrescrita.")

def on_select_change(event):
    selected_option = select_var.get()
    comando = "cd ./" + selected_option + "/ && python main.py"
    
    if selected_option:
        continuar(comando)

def continuar(comando):
    ventana.destroy()
    os.system(comando)

cuadro_info = tk.Canvas(ventana, width=400, height=50)
cuadro_info.place(x=50, y=5, width=400, height=500)
cuadro_info.create_text(200, 50, text='Proyecto 1: Goku Smart', width=400, font=("Arial-Black", 30))

btn_seleccionar = tk.Button(ventana, text="Seleccionar matriz", command=seleccionar_archivo)
btn_seleccionar.place(x=175, y=100, width=150, height=50)

select_options = ['Amplitud', 'Costo', 'Profundidad', 'Avara', 'Estrella']
select_menu = tk.OptionMenu(ventana, select_var, *select_options, command=on_select_change)
select_menu.place(x=175, y=200, width=150, height=50)

ventana.mainloop()