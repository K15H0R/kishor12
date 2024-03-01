a=str(input("what's your name?:"))
print("hello",a)
b=str(input("are you student?:"))
print("woah okay ",a)

c=float(input("what's your age"))
if c<=12:
    print("hello",a,"you're eligible for discount")
elif c>=13 and b=="yes" :
    print("hello",a,"you're eligible for discount")
elif c>=13 :
    print("hello",a,"you're not eligible for discount")
else:
    print("hahaha are you alien")