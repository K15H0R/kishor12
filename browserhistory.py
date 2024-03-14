from queue import LifoQueue
backwardhistory= LifoQueue()
forwardhistory= LifoQueue()
currentpage= None

noofvisit= int(input("enter the no. of URL history:"))
print("enter URLS to visit:")
for i in range(noofvisit):
    url=input("URL:")
    print(f"visiting{url}")
    backwardhistory.put(currentpage)
    print(f"currentpage:{currentpage}")
    while input("do you want to go back?(yes/no):").lower() == "yes":
        if not backwardhistory.empty():
            forwardhistory.put(currentpage)
            currentpage= backwardhistory.get()
            print(f"going back to {currentpage}")
        else:
            print("no previous page available!")
    while input("do you want to go forward?(yes/no):").lower() == "yes":
        if not forwardhistory.empty():
            backwardhistory.put(currentpage)
            currentpage= forwardhistory.get()
            print(f"going forward to {currentpage}")
        else:
            print("no forward page available!")