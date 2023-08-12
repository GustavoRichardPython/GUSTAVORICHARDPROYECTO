import tkinter as tk
from PIL import Image, ImageTk

def cambiar_fondo():
    # Cargar una nueva imagen para el fondo del botón
    nueva_imagen = Image.open("Fondo.jpg")  # Reemplaza "ruta_de_la_imagen.jpg" con la ruta de tu imagen
    imagen_convertida = ImageTk.PhotoImage(nueva_imagen)
    boton.config(image=imagen_convertida)
    boton.image = imagen_convertida

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cambio de fondo de botón con imagen")

# Cargar una imagen inicial para el botón
imagen_inicial = Image.open("Fondo.jpg")  # Reemplaza "ruta_de_la_imagen_inicial.jpg" con la ruta de tu imagen inicial
imagen_inicial = ImageTk.PhotoImage(imagen_inicial)

# Crear el botón
boton = tk.Button(ventana, image=imagen_inicial, command=cambiar_fondo)
boton.pack(pady=20)

boton2 = tk.Button(ventana, image=imagen_inicial, command=cambiar_fondo)
boton2.pack(pady=50)
# Iniciar el bucle de la aplicación
ventana.mainloop()
