import tkinter as tk

def agregar_evento():
    evento = evento_entry.get()
    fecha = fecha_entry.get()
    hora = hora_entry.get()
    if evento and fecha and hora:
        evento_listbox.insert(tk.END, f"{evento} - {fecha} - {hora}")
        evento_entry.delete(0, tk.END)
        fecha_entry.delete(0, tk.END)
        hora_entry.delete(0, tk.END)

def eliminar_evento():
    seleccionado = evento_listbox.curselection()
    if seleccionado:
        evento_listbox.delete(seleccionado)

# Crear la ventana principal
root = tk.Tk()
root.title("Agenda")
root.geometry("400x300")

# Entradas para el evento, fecha y hora
evento_label = tk.Label(root, text="Evento:")
evento_label.pack(pady=5)

evento_entry = tk.Entry(root)
evento_entry.pack(pady=5)

fecha_label = tk.Label(root, text="Fecha:")
fecha_label.pack(pady=5)

fecha_entry = tk.Entry(root)
fecha_entry.pack(pady=5)

hora_label = tk.Label(root, text="Hora:")
hora_label.pack(pady=5)

hora_entry = tk.Entry(root)
hora_entry.pack(pady=5)

# Botones para agregar y eliminar eventos
agregar_btn = tk.Button(root, text="Agregar Evento", command=agregar_evento)
agregar_btn.pack(pady=10)

eliminar_btn = tk.Button(root, text="Eliminar Evento", command=eliminar_evento)
eliminar_btn.pack(pady=5)

# Lista de eventos
evento_listbox = tk.Listbox(root, width=50)
evento_listbox.pack(pady=20)

# Ejecutar el bucle principal de la aplicación
root.mainloop()