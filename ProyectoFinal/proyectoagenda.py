import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

def agregar_evento():
    evento = evento_entry.get()
    fecha = fecha_entry.get()
    if evento and fecha:
        evento_listbox.insert(tk.END, f"{fecha}: {evento}")
        evento_entry.delete(0, tk.END)

def navegar_semana(anterior=False):
    global fecha_actual
    if anterior:
        fecha_actual -= timedelta(days=7)
    else:
        fecha_actual += timedelta(days=7)
    actualizar_vista_semanal()

def actualizar_vista_semanal():
    semana_label.config(text=f"Semana del {fecha_actual.strftime('%d/%m/%Y')} al {fecha_actual + timedelta(days=6)}")
    evento_listbox.delete(0, tk.END)
    for i in range(7):
        fecha = fecha_actual + timedelta(days=i)
        eventos_del_dia = [evento for evento in eventos if evento.startswith(fecha.strftime('%Y-%m-%d'))]
        for evento in eventos_del_dia:
            evento_listbox.insert(tk.END, evento)

# Crear la ventana principal
root = tk.Tk()
root.title("Agenda Semanal")
root.geometry("500x400")

# Variables
fecha_actual = datetime.now().date()
eventos = []

# Etiqueta para la semana actual
semana_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"))
semana_label.pack(pady=10)
actualizar_vista_semanal()

# Botones para navegar la semana
navegar_frame = tk.Frame(root)
navegar_frame.pack()

anterior_btn = tk.Button(navegar_frame, text="<< Anterior", command=lambda: navegar_semana(anterior=True))
anterior_btn.pack(side=tk.LEFT)

siguiente_btn = tk.Button(navegar_frame, text="Siguiente >>", command=lambda: navegar_semana(anterior=False))
siguiente_btn.pack(side=tk.LEFT)

# Entradas para agregar eventos
evento_label = tk.Label(root, text="Evento:")
evento_label.pack(pady=5)

evento_entry = tk.Entry(root)
evento_entry.pack(pady=5)

# Botón para agregar evento
agregar_btn = tk.Button(root, text="Agregar Evento", command=agregar_evento)
agregar_btn.pack(pady=10)

# Lista de eventos
evento_listbox = tk.Listbox(root, width=60)
evento_listbox.pack(pady=20)

# Ejecutar el bucle principal de la aplicación
root.mainloop()