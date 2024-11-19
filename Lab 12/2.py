import random

students = ["Ali", "Sara", "Imran", "Ayesha", "Usman", "Fatima", "Bilal", "Zara"]

popped_student = students.pop()

new_list = students[:]

scholarship_winners = random.sample(new_list, 2)

print(f"Popped student: {popped_student}")
print(f"Scholarship winners: {scholarship_winners}")
