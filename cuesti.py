import tkinter as tk

class KahootQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Kahoot Quiz")
        self.root.geometry("500x400")

        self.questions = [
            {
                "question": "¿Cuál es la capital de Francia?",
                "options": ["Londres", "París", "Madrid", "Roma"],
                "correct_answer": 1
            },
            {
                "question": "¿Cuál es el río más largo del mundo?",
                "options": ["Nilo", "Amazonas", "Mississippi", "Yangtsé"],
                "correct_answer": 0
            },
            # Agrega más preguntas aquí
        ]

        self.current_question = 0
        self.score = 0

        self.create_widgets()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", font=("Arial", 20))
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.root, text="", font=("Arial", 16), command=lambda idx=i: self.check_answer(idx))
            self.option_buttons.append(button)
            button.pack(fill=tk.X, padx=50, pady=10)

        self.next_button = tk.Button(self.root, text="Siguiente pregunta", font=("Arial", 16), command=self.next_question)
        self.next_button.pack(pady=20)

        self.show_question()

    def show_question(self):
        question_info = self.questions[self.current_question]
        self.question_label.config(text=question_info["question"])

        for i in range(4):
            self.option_buttons[i].config(text=question_info["options"][i])

    def check_answer(self, selected_option):
        question_info = self.questions[self.current_question]
        if selected_option == question_info["correct_answer"]:
            self.score += 1

        self.next_question()

    def next_question(self):
        self.current_question += 1

        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.show_final_score()

    def show_final_score(self):
        self.question_label.config(text=f"¡Fin del cuestionario!\nTu puntaje final es: {self.score}/{len(self.questions)}")
        for button in self.option_buttons:
            button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    quiz = KahootQuiz(root)
    root.mainloop()
