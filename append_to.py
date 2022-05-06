from csv import writer
from files import student_data


def appending():
    with open('students.csv', 'a', newline="") as file:
        write_to = writer(file)

        for row in student_data():
            write_to.writerow(row)


appending()
