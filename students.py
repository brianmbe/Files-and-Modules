from csv import writer
from files import students


def main():
    with open('students.csv', 'w', newline="") as file:
        writer_file = writer(file)
        writer_file.writerow(students)


main()
