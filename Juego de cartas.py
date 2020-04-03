#############################################################################
#
#   Instituto Tecnológico de Costa Rica
#
#   Área Academica de Ingeniería en Computadores
#
#   Curso: Taller de Programación
#
#   Programa: Python
#
#   Autor: Irene Garzona Moya
#
#   Versión: 3.8.1
#
#   Profesor:X
#
#   Tarea Corta: Interfaz gráfica en Tkinter
#
#############################################################################
from tkinter import *
import time
    
ventana=Tk()
ventana.title('Memoria'
ventana.minsize(600,400)
ventana.resizable(width=False, height=False)
ventana.geometry('400x400+500+150')


contenedor = Canvas(ventana, width=600, height = 400, bg="#FFBED2")
contenedor.place(x=0,y=0)

magic_card = PhotoImage(file=magiccard.jpg)
              
window.mainloop()
