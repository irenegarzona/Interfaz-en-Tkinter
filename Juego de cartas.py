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
from Tkinter import *
import time

def window():
    window = Toplevel()
    window.title('Ventana B')
    window.minsize(300,200)
    
ventana=Tk()
ventana.title('Memoria')
ventana.minsize(600,400)
ventana.resizable(width=True, height=True)
ventana.geometry('400x400+500+150')

