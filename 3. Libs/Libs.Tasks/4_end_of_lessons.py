import random

print("Let's find when the lesson will be done.")
while True:
    odd_lesson_count = 0
    even_lesson_count = 0
    lesson_duration = 45
    odd_break_duration = 5
    even_dreak_duration = 15
    lesson = int(input("Enter the number of lesson from 1 to 10: ")) #random.randint(1, 10)
    for l in range(1, lesson):
        if l % 2 == 0:
            even_lesson_count += 1
        else:
            odd_lesson_count += 1
    duration = lesson_duration * lesson + even_lesson_count * even_dreak_duration + odd_lesson_count * odd_break_duration
    hours = duration // 60 + 9
    minutes = duration % 60
    print(f"Lesson {lesson} will be done at {hours:02}:{minutes:02}")
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break