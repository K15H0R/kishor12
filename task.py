a=int(input("enter the number which you want multiplication table:"))
b=int(input("enter the number for the limit:"))
for i in range(1,b+1):
    c=a*i
    print(a,"x",i,"=",c)
   
   
count=1
while count<=b:
    f=count*a
    print(a,"x",count,"=",f)
    count=count+1