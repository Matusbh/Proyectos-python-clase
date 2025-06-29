
# Importamos lo necesario
from tkinter import *
from tkinter.messagebox import showerror

#Definicion de la ventana
root = Tk()
root.title("Calculadora Python")
root.geometry("265x500")
root.resizable(0,0)

# Funciones
def añadir_txt(texto, strvar: StringVar):
    strvar.set(f'{strvar.get()}{texto}')

# Función para evaluar la expresión en el display
def Evaluar(Entrada_StringVar):
    try:
        # Reemplazar el símbolo de multiplicación "X" con "*" para que python pueda leer bien la expresion matematica ingresada
        expresion = Entrada_StringVar.get().replace("X", "*")
        # Evaluamos la expresion y la actualizamos en el display
        resultado = eval(expresion)
        Entrada_StringVar.set(resultado)
    except Exception as e:
        # Muestra error si la expresión es inválida
        showerror("Error", "Expresión inválida")

#Borra todo
def Limpiar():
    Entrada_StringVar.set("")

#Borrar ultimo caracter
def Limpiar_uno():
    # para saber que hay escrito
    contenido_actual= Entrada_StringVar.get()
    nuevo_contenido= contenido_actual[:-1]
    Entrada_StringVar.set(nuevo_contenido)

#Vatiables de tipo StringVar
Entrada_StringVar = StringVar(root)

# Metemos el titulo en la ventana
titulo_dentro= Label(root, text="Calculadora de Matus", font=("Bodoni", 15), bg="LightCyan2")
titulo_dentro.pack()
instruciones= Label(root, text="Pulsa doble \'x\' para exponencias", font=("Bodoni", 10), bg="LightCyan2")
instruciones.pack()

# Mostrar lo que escribimos  
pantalla = Entry(root, justify=RIGHT, textvariable=Entrada_StringVar, width=21, font=12, state='disabled')
pantalla.place(x=35, y=70)

# Botones numericos
Button(root, height=2, width=5, text="7", font=9, bg="Cyan", command=lambda: añadir_txt("7", Entrada_StringVar)).place(x=5, y=170)
Button(root, height=2, width=5, text="8", font=9, bg="Cyan", command=lambda: añadir_txt("8", Entrada_StringVar)).place(x=65, y=170)
Button(root, height=2, width=5, text="9", font=9, bg="Cyan", command=lambda: añadir_txt("9", Entrada_StringVar)).place(x=125, y=170)
Button(root, height=2, width=5, text="4", font=9, bg="Cyan", command=lambda: añadir_txt("4", Entrada_StringVar)).place(x=5, y=230)
Button(root, height=2, width=5, text="5", font=9, bg="Cyan", command=lambda: añadir_txt("5", Entrada_StringVar)).place(x=65, y=230)
Button(root, height=2, width=5, text="6", font=9, bg="Cyan", command=lambda: añadir_txt("6", Entrada_StringVar)).place(x=125, y=230)
Button(root, height=2, width=5, text="3", font=9, bg="Cyan", command=lambda: añadir_txt("3", Entrada_StringVar)).place(x=5, y=290)
Button(root, height=2, width=5, text="2", font=9, bg="Cyan", command=lambda: añadir_txt("2", Entrada_StringVar)).place(x=65, y=290)
Button(root, height=2, width=5, text="1", font=9, bg="Cyan", command=lambda: añadir_txt("1", Entrada_StringVar)).place(x=125, y=290)
Button(root, height=2, width=5, text="0", font=9, bg="Cyan", command=lambda: añadir_txt("0", Entrada_StringVar)).place(x=65, y=350)

# Botones de operacion
Button(root, height=2, width=5, text="X", font=9, bg="Cyan", command= lambda: añadir_txt("X", Entrada_StringVar)).place(x=195, y=170)
Button(root, height=2, width=5, text="+", font=9, bg="Cyan", command= lambda: añadir_txt("+", Entrada_StringVar)).place(x=195, y=230)
Button(root, height=2, width=5, text="-", font=9, bg="Cyan", command= lambda: añadir_txt("-", Entrada_StringVar)).place(x=195, y=290)
Button(root, height=2, width=5, text="/", font=9, bg="Cyan", command= lambda: añadir_txt("/", Entrada_StringVar)).place(x=5, y=350)
Button(root, height=2, width=5, text=".", font=9, bg="Cyan", command= lambda: añadir_txt(".", Entrada_StringVar)).place(x=125, y=350)
Button(root, height=2, width=5, text="(", font=9, bg="Cyan", command= lambda: añadir_txt("(", Entrada_StringVar)).place(x=65, y=110)
Button(root, height=2, width=5, text=")", font=9, bg="Cyan", command= lambda: añadir_txt(")", Entrada_StringVar)).place(x=125, y=110)
Button(root, height=2, width=5, text="=", font=9, bg="Cyan", command= lambda: Evaluar(Entrada_StringVar)).place(x=195, y=350)
Button(root, height=2, width=5, text="AC", font=9, bg="Cyan", command= Limpiar).place(x=5, y=110)
Button(root, height=2, width=5, text="C", font=9, bg="Cyan", command= Limpiar_uno).place(x=195, y=110)

root.mainloop()


































