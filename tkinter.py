from tkinter import *

def load_img(name):
    path = os.path.join('imgs',name)
    img = PhotoImage(file = path)
    return img

def derecha():
    contenedor.move('BOLA',50,0)

def winB():
    windowB = Toplevel()
    windowB.title('Ventana B')
    windowB.minsize(300,200)
    
ventana=Tk()
ventana.title('Ejemplo')
ventana.minsize(600,400)
ventana.resizable(width=False, height=False)
ventana.geometry('400x400+500+150')

texto=Label(ventana,text="Hola Mundo")
texto.place(x=50, y=50)


contenedor = Canvas(ventana, width=400, height=400, bg="#7279B6")
contenedor.place(x=0,y=0)
contenedor.create_oval(1,1,160,160,width=0,fill='green', tags='BOLA')

botonA = Button(ventana,width=8,height=2,command=derecha,text="Derecha",bg="#000000",fg="#FFFFFF")
botonA.place(x=100,y=350)

grootIMG = load_img('groot.jpg')
contenedor.create_image(100,200,image=grootIMG, tags='groot')

ventana.mainloop()
