import tkinter as tk

class CuestionarioApp:
    def __init__(self, root):
        self.root = root
        self.pregunta_actual = 0
        self.respuestas_correctas = 0
        
        # Preguntas y respuestas en forma de imágenes
        self.preguntas = ['pregunta1.png', 'pregunta2.png', 'pregunta3.png']
        self.respuestas = [['respuesta1_1.png', 'respuesta1_2.png', 'respuesta1_3.png'],
                           ['respuesta2_1.png', 'respuesta2_2.png', 'respuesta2_3.png'],
                           ['respuesta3_1.png', 'respuesta3_2.png', 'respuesta3_3.png']]
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        self.pregunta_label = tk.Label(self.root, text="Pregunta:")
        self.pregunta_label.pack()
        
        self.pregunta_imagen = tk.PhotoImage(file=self.preguntas[self.pregunta_actual])
        self.pregunta_label = tk.Label(self.root, image=self.pregunta_imagen)
        self.pregunta_label.pack()
        
        self.respuestas_frame = tk.Frame(self.root)
        self.respuestas_frame.pack()
        
        for i in range(len(self.respuestas[self.pregunta_actual])):
            respuesta_imagen = tk.PhotoImage(file=self.respuestas[self.pregunta_actual][i])
            respuesta_boton = tk.Button(self.respuestas_frame, image=respuesta_imagen, command=lambda idx=i: self.verificar_respuesta(idx))
            respuesta_boton.pack(side=tk.LEFT)
        
        self.resultado_label = tk.Label(self.root, text="")
        self.resultado_label.pack()
    
    def verificar_respuesta(self, idx):
        respuesta_correcta = 0  # Índice de la respuesta correcta en la lista de respuestas
        
        if idx == respuesta_correcta:
            self.respuestas_correctas += 1
            self.resultado_label.config(text="¡Respuesta correcta!", fg="green")
        else:
            self.resultado_label.config(text="Respuesta incorrecta", fg="red")
        
        # Cambiar a la siguiente pregunta (si hay más preguntas)
        self.pregunta_actual += 1
        if self.pregunta_actual < len(self.preguntas):
            self.actualizar_pregunta()
        else:
            self.mostrar_resultados()
    
    def actualizar_pregunta(self):
        self.pregunta_imagen = tk.PhotoImage(file=self.preguntas[self.pregunta_actual])
        self.pregunta_label.config(image=self.pregunta_imagen)
        
        for widget in self.respuestas_frame.winfo_children():
            widget.destroy()
        
        for i in range(len(self.respuestas[self.pregunta_actual])):
            respuesta_imagen = tk.PhotoImage(file=self.respuestas[self.pregunta_actual][i])
            respuesta_boton = tk.Button(self.respuestas_frame, image=respuesta_imagen, command=lambda idx=i: self.verificar_respuesta(idx))
            respuesta_boton.pack(side=tk.LEFT)
        
        self.resultado_label.config(text="")
    
    def mostrar_resultados(self):
        self.pregunta_label.destroy()
        self.respuestas_frame.destroy()
        self.resultado_label.destroy()
        
        resultado_final = f"¡Has respondido {self.respuestas_correctas} preguntas correctamente de {len(self.preguntas)}!"
        resultado_label = tk.Label(self.root, text=resultado_final, font=("Arial", 16))
        resultado_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Cuestionario para niños")
    app = CuestionarioApp(root)
    root.mainloop()
