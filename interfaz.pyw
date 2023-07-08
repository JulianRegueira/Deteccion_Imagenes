import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox, filedialog
import os
import main


#--------------------------------------------------------------------------------------------------------------------------------
#FUNCIONES DE LOS BOTONES

def infoCreador():
    messagebox.showinfo("Buscador de Objetos", "Creado por Julian Regueira")

def avisoSalir():
    opciones=messagebox.askquestion("Salir", "¿Deseas salir?")

    if opciones == "yes":
        root.destroy()

    else:
        pass

def abrirImagen():
    global show_img
    filename = filedialog.askopenfilename(initialdir='Objetos/Joyas',
                                          title="Buscar Objeto",
                                          filetypes=(("Imagenes JPG", "*.JPG"), ("Imagenes PNG","*.PNG"), ("Todos los archivos", "*.*")))   
    show_img = ImageTk.PhotoImage(Image.open(filename))
    display_img = Label(image=show_img)
    display_img.config(width="150", height="50")
    display_img.pack()

def run():
    main.main()

#--------------------------------------------------------------------------------------------------------------------------------
#CONFIGURACION GENERAL

#MAIN
root = tk.Tk()

#TITULO MAIN
root.title("Para Maxi")

#ICONO DE LA APP
root.iconbitmap("esq.ico")

#FONDO
root.config(bg="grey")

#TAMAÑO
root.geometry("350x250")
root.resizable(0,0)


#--------------------------------------------------------------------------------------------------------------------------------
#BARRA DE ACCIONES
barraMenu = Menu(root)
root.config(menu=barraMenu)

#Funcionalidad botones 1
Nuevo_Cargar=Menu(barraMenu, tearoff=0)
Nuevo_Cargar.add_command(label="Nuevo item", command=abrirImagen)
Nuevo_Cargar.add_command(label="Cargar item")
Nuevo_Cargar.add_separator()
Nuevo_Cargar.add_command(label="Salir", command=avisoSalir)

#Funcionalidad botones 2
Ayuda=Menu(barraMenu, tearoff=0)
Ayuda.add_command(label="Desarrollo")
Ayuda.add_command(label="Sobre el programa...", command=infoCreador)

#Distribucion MENU, add_cascade hace que aparezcan en la intrerfaz
barraMenu.add_cascade(label="Archivo", menu=Nuevo_Cargar)
barraMenu.add_cascade(label="Ayuda", menu=Ayuda)

#--------------------------------------------------------------------------------------------------------------------------------
#BOTON START

boton = tk.Button(root, text= "Start", width="20", height="2", command=run)
boton.place(x=100, y=180)

#FUNCIONALIDAD DEL BOTON PARA COMENZAR

root.mainloop()