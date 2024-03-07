booklist=[]
authorset=set()
bookdict={}
booklist.append("python programming")
authorset.add("John smith")
bookdict["python programming"]="John smith"
booklist.append("Data structure and algorithms")
authorset.add("Jane Doe")
bookdict["Data structure and algorithms"]="Jane Doe"
booklist.append("Machine learning basics")
authorset.add("Alice Johnson")
bookdict["Machine learning basics"]="Alice Johnson"

searchtitle=input("enter the title of the book:")
if searchtitle in booklist:
    print(f"book found!author: {bookdict[searchtitle]}")
else:
    print("book not found!!!")
print("list of books")
for b in booklist:
    print(b)
removetitle=input("enter the title of the book to remove or skip:")
if removetitle in booklist:
    removeauthor=bookdict[removetitle]
    booklist.remove(removetitle)
    authorset.remove(removeauthor)
    del bookdict[removetitle]
    print("book removed successfully!")
    print("books available:",booklist)
else:
    print("book not found")
    