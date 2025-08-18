from tkinter import Tk
from quiz import Quiz
from quiz_app import QuizApp

if __name__ == "__main__":
    data = [
    {
        'question': "Where in Canada is one of the world's largest institutes for the study of quantum technologies located?",
        'options': ["Vancouver", "Waterloo", "Calgary", "Montreal"],
        'correct_index': 1},
    {
        'question': "Which renewable energy source does Canada use the most?",
        'options': ["Solar power", "Wind power", "Hydro power", "Geothermal power"],
        'correct_index': 2},
    {
        'question': "What medical discovery was made in Canada?",
        'options': ["The invention of penicillin", "The discovery of insulin", "The creation of the polio vaccine", "The development of the MRI scanner"],
        'correct_index': 1},
    {
        'question': "Which famous IT company was founded in Canada?",
        'options': ["Shopify", "Microsoft", "Tesla", "Amazon"],
        'correct_index': 0},
    {
        'question': "Which invention was created in Canada?",
        'options': ["Robotic vacuum cleaner", "Robotic arm for space missions", "Personal computer", "GPS technology"],
        'correct_index': 1},
    ]

    root = Tk()
    quiz = Quiz(data)
    app = QuizApp(root, quiz)

    root.mainloop()