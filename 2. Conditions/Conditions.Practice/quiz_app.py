from tkinter import *
from tkinter import ttk
from quiz import Quiz

class QuizApp:
    def __init__(self, root, quiz: Quiz):
        self.root = root
        self.quiz = quiz
        self.root.title("Quiz")
        self.root.geometry("450x850")

        self._build_ui()

    def _build_ui(self):
        for i, q in enumerate(self.quiz.questions):
            frame = ttk.Frame(borderwidth=1, relief=SOLID)

            lbl_question = ttk.Label(frame, wraplength=400, justify="left",
                                     anchor="w", text=q['question'])
            lbl_question.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")

            for r in range(2):
                for c in range(2):
                    option_index = r * 2 + c
                    radio = ttk.Radiobutton(
                        frame,
                        text=f"{option_index + 1}. {q['options'][option_index]}",
                        variable=self.quiz.user_answers[i],
                        value=option_index
                    )
                    radio.grid(row=r+1, column=c, sticky="w")

            frame.pack(anchor=NW, fill=X, padx=5, pady=5)

        frame1 = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
        frame1.pack(anchor=SW, fill=X, padx=5, pady=5)

        btn_result = ttk.Button(frame1, text="Result", command=self.show_result)
        btn_result.pack()

        self.lbl_result = ttk.Label(frame1)
        self.lbl_result.pack()

    def show_result(self):
        score = self.quiz.check_results()
        color_map = {
            5: "green",
            4: "light green",
            3: "yellow",
            2: "orange",
            1: "purple",
            0: "red"
        }
        self.lbl_result.config(
            text=f"{score} of {len(self.quiz.questions)}",
            background=color_map.get(score, "white")
        )