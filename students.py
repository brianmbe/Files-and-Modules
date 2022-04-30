from csv import writer

students = ['name', 'age', 'places']

with open('students.csv', 'w', newline="") as file:
    writer = writer(file)
    writer.writerow(students)

