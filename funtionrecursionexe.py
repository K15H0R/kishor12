def reverse_string(s):
    
    if len(s) <= 1:
        return s
    else:

        return reverse_string(s[1:])+s[0]

a=str(input("enter a word:"))
    
print(reverse_string(a))