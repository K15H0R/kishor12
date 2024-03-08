Name=[]
grade=set()
age={}
Name.append("kishor kumar ghalley")
grade.add("1")
age["19"]="1"
Name.append("pema wangdi")
grade.add("1")
age["19"]="1"
Name.append("tshering dorji")
grade.add("2")
age["20"]="2"

searchname=input("enter the name of the student:")
if searchname in Name:
    print(f"name found!grade: ")
else:
    print("name not found!!!")
print("list of name")
for b in Name:
    print(b)
removename=input("enter the name of the student to remove or skip:")
if removename in Name:
    removegrade=age[removename]
    Name.remove(removename)
    grade.remove(removegrade)
    del age[removename]
    print("name removed successfully!")
    print("name of student available:",Name)
else:
    print("name not found")
    