from tkinter import *

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.user_answers = [IntVar(value=-1) for _ in questions]

    def check_results(self):
        count = 0
        for i, q in enumerate(self.questions):
            if self.user_answers[i].get() == q['correct_index']:
                count += 1
        return count
