def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    else:
        return 'F'


name = input("Enter your name: ").title()
fathers_name = input("Enter your father's name: ").title()
roll_number = input("Enter your roll number: ")

subjects = {}
total_marks = 0
max_marks_per_subject = 100

for i in range(1, 6):
    subject_name = input(f"Enter the name of subject {i}: ")
    marks = int(input(f"Enter marks obtained in {subject_name}: "))
    subjects[subject_name] = marks
    total_marks += marks

total_possible_marks = max_marks_per_subject * 5
percentage = (total_marks / total_possible_marks) * 100
grade = calculate_grade(percentage)

print("\n---- Student Report ----")
print(f"Name: {name}")
print(f"Father's Name: {fathers_name}")
print(f"Roll Number: {roll_number}")
print("\nSubjects and Marks:")
for subject, marks in subjects.items():
    print(f"  {subject}: {marks} / {max_marks_per_subject}")

print("\n---- Summary ----")
print(f"Total Marks Obtained: {total_marks} / {total_possible_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
