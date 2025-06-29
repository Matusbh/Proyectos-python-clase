##########FALTAN COMENTARIOS
# Importamos mdulos 
from tkinter import *
import random

# Inicializar la ventana 
window = Tk()
# Titulo
window.title("ROCK, PAPER, SISSORS GAME")
# Pixeles
window.geometry("500x500")
# Color
window.configure(bg='#8d8b55') 
# Reajustable



# Cargamos imagenes para nosotros elegir por eso las hacemos pequeñas
# Imagen para cuando la mano esta estatica
Imagen_principio = PhotoImage(file="Piedra1.PNG")
# Añadimos la imagen de la piedra y la redimensionamos a un atercera parte de la imagen 
Jugador_piedra = PhotoImage(file="Piedra1.PNG")
Jugador_piedra_dimen = Jugador_piedra.subsample(3, 3)

#Asi con las otras dos posibilidades
Jugador_papel = PhotoImage(file="papel.PNG")
Jugador_papel_dimen = Jugador_papel.subsample(3, 3)

Jugador_tijera = PhotoImage(file="tijera.PNG")
Jugador_tijera_dimen = Jugador_tijera.subsample(3, 3)

# Para hacer ver lo que elejimos nosotros y el ordenador las cargamos nuevamente sin redimensionar 
Piedra_computer = PhotoImage(file="Piedra1.PNG")
Papel_computer = PhotoImage(file="papel.PNG")
Tijera_computer = PhotoImage(file="tijera.PNG")
#Creacion de funciones para las opciones 

def Piedra():
    global opcion_jugador
    opcion_jugador=1
    Imagen_Jugador.configure(image=Jugador_piedra)
    Matching()

def Papel():
    global opcion_jugador
    opcion_jugador=2
    Imagen_Jugador.configure(image=Jugador_papel)
    Matching()

def Tijera():
    global opcion_jugador
    opcion_jugador=3
    Imagen_Jugador.configure(image=Jugador_tijera)
    Matching()

# Configurar las elecciones del ordenador y cual es el mensaje a imprimir dependiendo del resultado 
def Ordenador_Piedra():
    if opcion_jugador == 1:
        Label_Status.config(text="Empate")
    elif opcion_jugador == 2:
        Label_Status.config(text="Ganó el Alejandra")
    elif opcion_jugador == 3:
        Label_Status.config(text="Ganó el ordenador")
    
def Ordenador_Papel():
    if opcion_jugador == 1:
        Label_Status.config(text="Ganó el ordenador")
    elif opcion_jugador == 2:
        Label_Status.config(text="Empate")
    elif opcion_jugador == 3:
        Label_Status.config(text="Ganó el Alejandra")

def Ordenador_Tijera():
    if opcion_jugador == 1:
        Label_Status.config(text="Ganó el Alejandra")
    elif opcion_jugador == 2:
        Label_Status.config(text="Ganó el ordenador")
    elif opcion_jugador == 3:
        Label_Status.config(text="Empate")

    

# Aqui nos dice que dependiendo de la eleccion se ponga una imagen u otra
def Matching():
    # elije un numero del 1 al 3 aleatorio
    eleccion_ordenador = random.randint(1, 3)
    # dependienmdo de las elecciones se llama una funcion u otra 
    if eleccion_ordenador == 1:
        Imagen_ordenador.configure(image=Piedra_computer)
        Ordenador_Piedra()
    elif eleccion_ordenador == 2:
        Imagen_ordenador.configure(image=Papel_computer)
        Ordenador_Papel()
    elif eleccion_ordenador == 3:
        Imagen_ordenador.configure(image=Tijera_computer)
        Ordenador_Tijera()


# Añadimos las imagenes iniciales donde queremos, añadimos botones y texto 
Imagen_Jugador = Label(window, image= Imagen_principio)
Imagen_ordenador = Label(window, image= Imagen_principio)

# Colocamos el texto del jugadir 
Label_Jugador = Label(window, text="Alejandra")
# Donde lo queremos
Label_Jugador.grid(row=1, column=1)
# Modificamos color del Texto y de la fuente y la fuente en si
Label_Jugador.config(bg="#8d8b55", fg="black", font=('Times New Roman', 18, 'bold'))

# Texto de ordenador 
Label_Ordenador = Label(window, text="Ordenador")
Label_Ordenador.grid(row=1, column=3)
Label_Ordenador.config(bg="#8d8b55", fg="black", font=('Times New Roman', 18, 'bold'))

# Configuracion de texto de quien gano
# Aparece vacio ya que todavia no hay resultado 
Label_Status = Label(window, text="", font=('Times New Roman', 12))
Label_Status.config(fg="black", font=('Times New Roman', 20, 'bold', 'italic'))

#Colocar la imagen del jugador en donde queremos y le damos margenes por el eje x e y
# Hacemos coincidir los enunciados de texto de jugador y ordenador con las imagenes 
Imagen_Jugador.grid(row=2, column=1, padx=30, pady=20)
Imagen_ordenador.grid(row=2, column=3, padx=30, pady=20)
# Añadimos el texto de quien gana 
Label_Status.grid(row=3, column=2)

# Añadimos un boton con la imagen respectiva
Piedra_boton = Button(window, image= Jugador_piedra_dimen, command= Piedra)
Papel_boton = Button(window, image= Jugador_papel_dimen, command=Papel)
Papel_tijera = Button(window, image= Jugador_tijera_dimen, command=Tijera)
# Añadimos un boton para para 
Boton_Salir = Button(window, text="Quit", bg="red", fg="white", font=('Times New Roman', 25, 'bold'), command=window.quit)

# Añadimos donde queremos los botones
Piedra_boton.grid(row=4, column=1, pady=30)
Papel_boton.grid(row=4, column=2, pady=30)
Papel_tijera.grid(row=4, column=3, pady=30)
Boton_Salir.grid(row=5, column=2)


window.mainloop()
