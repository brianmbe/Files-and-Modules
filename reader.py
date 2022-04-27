from csv import reader

with open('students.csv') as read:
    file_reader = reader(read)
    for row in file_reader:
        print(row)
