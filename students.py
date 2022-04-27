from csv import writer
students = ['name', 'age', 'places']
student_data = [
    ['Jack', 23, 'Zombo'],
    ['Sophie', 22, 'Paidha'],
    ['John', 24, 'Kiira'],
    ['Jane', 30, 'Eldoret'],
    ['Brian', 23, 'Arikpa'],
    ['James', 22, 'KLa'],
    ['John R', 24, 'Jina'],
    ['Patrick', 30, 'Naivasha']
]
with open('students.csv', 'w') as file:
    writer = writer(file)
    writer.writerow(students)
    writer.writerows(student_data)
