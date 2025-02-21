try:
    students = open('students.txt', encoding='utf8')
except:
    print('There is no such of file. Try to use another name or replace this file to this directory.')

average_scores = open('averages.txt', 'w')
student = students.readline()
scores = []
while student:
    student = student.replace(',', '')
    student = student.split()
    name = student[0]
    name = name[:-1]
    line = f'{name} {round((int(student[1]) + int(student[2]) + int(student[3])) / (len(student) - 1), 2)}\n'
    average_scores.write(line)
    student = students.readline()

students.close()
average_scores.close()