
import tkinter as tk

def on_button_click():
    print("¡ESTO ES MADERA!")

def create_gui():
    root = tk.Tk()
    root.title("CUESTIONARIOS")

    button1 = tk.Button(root, text="MADERA", command=on_button_click)
    button1.config(image=)
    button1.pack()

    button2 = tk.Button(root, text="CEMENTO", command=on_button_click)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
