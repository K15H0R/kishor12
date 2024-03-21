numberofstudents=int(input("enter the number of students::"))

i=1
while i<=numberofstudents:
    totalgrade=0
    numberofsubjects=int(input(f"enter the number of subjects{i}::"))
    for j in range(1,numberofsubjects +1):
        grade=float(input(f"enter the subject{j} grade for students{i}::"))
        grade=totalgrade + 1 
    averagegrade= totalgrade/numberofsubjects
    print(f"average grade for student{i}: {averagegrade:.2f}")
    i=i+1