def sumofdigit(n):
    if n<10: 
        return n
    else:
        lastdigit= n%10
        remainingdigit= n//10
        return lastdigit + sumofdigit(remainingdigit)

print(sumofdigit(123456))