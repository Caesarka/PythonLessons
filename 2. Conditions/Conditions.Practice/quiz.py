from tkinter import *
from tkinter import ttk

data = {
    "Where in Canada is one of the world's largest institutes for the study of quantum technologies located?": ["Vancouver", "Waterloo", "Calgary", "Montreal"],
    "Which renewable energy source does Canada use the most?": ["Solar power", "Wind power", "Hydro power", "Geothermal power"],
    "What medical discovery was made in Canada?": ["The invention of penicillin", "The discovery of insulin", "The creation of the polio vaccine", "The development of the MRI scanner"],
    "Which famous IT company was founded in Canada?": ["Shopify", "Microsoft", "Tesla", "Amazon"],
    "Which invention was created in Canada?": ["Robotic vacuum cleaner", "Robotic arm for space missions", "Personal computer", "GPS technology"]
}

questions = list(data.keys())
answers = list(data.values())
user_answers = []

def click_button():
    color_map = {
        5: "green",
        4: "light green",
        3: "yellow",
        2: "orange",
        1: "purple",
        0: "red"
    }

    right_answers = ['1', '2', '1', '0', '3']
    values = [user_answer.get() for user_answer in user_answers]
    count = 0
    for i in range(5):
        if values[i] == right_answers[i]:
            count += 1
            print(f"Value[{i}]: {values[i]}, right answer[{i}]: {right_answers[i]}")
    text = f"{count} of 5"
    color = color_map.get(count)
    lbl_result.config(text=text, background=color)

root = Tk()
root.title("Quiz")
root.geometry("450x850")

for i in range(5):
    frame = ttk.Frame(borderwidth=1, relief=SOLID)
    lbl_question = ttk.Label(frame, wraplength=400, justify="left", anchor="e", text=questions[i], padding=8)
    lbl_question.grid(row=0, column=0, columnspan=2)
    #lbl_question.pack()
    for r in range(2):
        for c in range(2):
            lbl_answer_option = ttk.Label(frame, text=f"{r * 2 + c + 1}. {answers[i][r * 2 + c]}", anchor="center", padding=8)
            lbl_answer_option.grid(row=r+1, column=c)
    user_answer = ttk.Entry(frame)
    user_answer.grid(row=3+i, column=0, columnspan=2, padx=10, pady=8)
    frame.pack(anchor=NW, fill=X, padx=5, pady=5)
    user_answers.append(user_answer)

frame1 = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
frame1.pack(anchor=SW, fill=X, padx=5, pady=5)
btn_result = ttk.Button(frame1, text="Result", command=click_button)
btn_result.pack()
lbl_result = ttk.Label(frame1)
lbl_result.pack()

root.mainloop()