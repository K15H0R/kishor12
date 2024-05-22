num_students = int(input("Enter the number of students: "))
num_subjects = int(input("Enter the number of subjects: "))

for student in range(1, num_students + 1):
    total_grade = 0
    print(f"\nStudent {student}:")
    
    for subject in range(1, num_subjects + 1):
        grade = float(input(f"Enter the grade for subject {subject}: "))
        total_grade += grade

    
    average_grade = total_grade / num_subjects
    print(f"Average grade for student {student}: {average_grade}")

