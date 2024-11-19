def distribution(filename):
    with open(filename, 'r') as file:
        grades = file.read().split()

    grade_counts = {
        'A': grades.count('A'),
        'B': grades.count('B'),
        'C': grades.count('C'),
        'D': grades.count('D'),
        'F': grades.count('F')
    }

    for grade, count in grade_counts.items():
        if count > 0:
            print(f"students got {grade} {count}")


x = input("Enter name of file : ")
distribution(x)
