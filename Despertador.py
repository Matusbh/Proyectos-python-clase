from tkinter import *
import datetime 
import time 
from threading import Thread
from tkinter import messagebox 
import pygame

# Creacion de ventana principal
root = Tk()
root.title("Despertador de Python")
root.geometry("300x400")
root.config(bg="LightGreen")
root.resizable(0, 0)

# Inicializar pygame para manejar audio
pygame.mixer.init()

# Funcion de solo poder ingresar numeros
def SoloNum(texto):
    """
    Valida si el texto ingresado es un número.
    Retorna True si es un número, de lo contrario False.
    """
    return texto.isdigit()  # Devuelve True si es número o False si es otra cosa

# Registrar la validación de SoloNum para las entradas
validacion = root.register(SoloNum)

# Funcion para detener alarma
def Detener_alarma():
    """
    Detiene la reproducción del sonido de la alarma
    y deshabilita el botón 'Detener alarma'.
    """
    pygame.mixer.music.stop()  # Detiene la reproducción del sonido
    messagebox.showinfo("Alarma detenida", "La alarma ha sido detenida")  # Mensaje al usuario
    boton_detener.config(state=DISABLED)  # Deshabilita el botón

# Funcion para verificar la correcta hora de la alarma
def Verificar_alarma(hora_alarma, minutos_alarma, ampm_alarma):
    """
    Comprueba constantemente si la hora actual coincide con la hora configurada.
    Si coinciden, reproduce el sonido de la alarma y habilita el botón 'Detener alarma'.
    """
    while True:
        # Obtenemos la hora actual
        ahora = datetime.datetime.now()
        hora_actual = ahora.hour  # Hora actual en formato 24 horas
        minutos_actuales = ahora.minute  # Minutos actuales
        ampm_actual = "AM" if hora_actual < 12 else "PM"  # Determinar si es AM o PM

        # Convertir hora a formato 12 horas
        hora_actual = hora_actual % 12 if hora_actual != 12 else 12

        # Comparar hora actual con la hora configurada de la alarma
        if (int(hora_alarma) == hora_actual and 
            int(minutos_alarma) == minutos_actuales and
            ampm_alarma == ampm_actual):
            try:
                # Intentamos cargar y reproducir el sonido
                pygame.mixer.music.load("alarma.mp3")
                pygame.mixer.music.play()
                messagebox.showinfo("Alarma", "¡Es hora de levantarse!")
                boton_detener.config(state=NORMAL)  # Habilitar el botón para detener la alarma

                # Esperar mientras el sonido se reproduce
                while pygame.mixer.music.get_busy():
                    pass
                boton_detener.config(state=DISABLED)  # Deshabilitar el botón cuando el sonido termine
            except pygame.error as e:
                # En caso de error al cargar el sonido
                messagebox.showerror("Error", f"No se pudo cargar el archivo de audio: {e}")
            break

        time.sleep(1)  # Esperar un segundo antes de volver a verificar

# Funcion para configurar la alarma
def Configurar_alarma():
    """
    Valida los datos ingresados por el usuario, configura la alarma
    y lanza un hilo para verificar la hora.
    """
    # Obtener valores de las entradas y el menú
    hora = entrada_hora.get()
    mins = entrada_mins.get()
    ampm = opcion_ampm.get()

    # Validar que las entradas no estén vacías
    if not hora or not mins:
        messagebox.showerror("Error", "Debes configurar una hora para activar la alarma.")
        return

    # Validar que la hora sea válida (1-12)
    if not (1 <= int(hora) <= 12):
        messagebox.showerror("Error", "Por favor ingresa una hora válida (1-12).")
        return

    # Validar que los minutos sean válidos (0-59)
    if not (0 <= int(mins) <= 59):
        messagebox.showerror("Error", "Por favor ingresa minutos válidos (0-59).")
        return

    # Si las validaciones pasan, configurar la alarma
    messagebox.showinfo("Alarma configurada", f"Alarma configurada para {hora}:{mins} {ampm}")
    # Crear un hilo para verificar la alarma sin bloquear la interfaz gráfica
    alarma_thread = Thread(target=Verificar_alarma, args=(hora, mins, ampm))
    alarma_thread.start()

# Igresamos las dos entradas y las descripciones
# Etiqueta de pregunta principal
pregunta = Label(root, text="¿A qué hora quieres que se active la alarma?", font=("Calibri", 12), bg="LightGreen")
pregunta.pack(pady=10)

# Etiqueta y entrada para la hora
Label(root, text="Ingresa la hora", font=("Calibri", 12), bg="LightGreen").pack(pady=10)
entrada_hora = Entry(root, justify=CENTER, validate="key", validatecommand=(validacion, "%S"))
entrada_hora.pack(pady=5)

# Etiqueta y entrada para los minutos
Label(root, text="Ingresa los minutos", font=("Calibri", 12), bg="LightGreen").pack(pady=10)
entrada_mins = Entry(root, justify=CENTER, validate="key", validatecommand=(validacion, "%S"))
entrada_mins.pack(pady=5)

# Crear un StringVar para almacenar las opciones del menú desplegable
opcion_ampm = StringVar(root)
opcion_ampm.set("AM")  # Valor predeterminado
# Menú desplegable para seleccionar AM o PM
menu_ampm = OptionMenu(root, opcion_ampm, "AM", "PM")
menu_ampm.pack(pady=5)

# Botón para activar la alarma
Button(root, text="Activar alarma", font=("Calibri", 12, "bold"), bg="Green", fg="black", command=Configurar_alarma).pack(pady=10)

# Botón para detener la alarma
boton_detener = Button(root, text="Detener alarma", font=("Calibri", 12, "bold"), bg="Green", fg="black", command=Detener_alarma)
boton_detener.pack(pady=10)
boton_detener.config(state=DISABLED)  # Inicialmente deshabilitado

# Ejecutar la ventana principal
root.mainloop()
