import random
secretnumber= random.randint(1,10)
maxattemp= 3 

def welcomemassage():
    print("\nwelcome to the number guessing game!")
    print(f"you have {maxattemp} attemps to guess the correct number.")

def guessrecursive(attempleft):
    guess= int(input("\nguess the number between 1 to 10"))

    if guess==secretnumber:
        print("congratulation human being! for the first time you have answered correctly hahahah")
    else:
        print(f"wrong guess human now your attemp left is {attempleft-1}")
        if attempleft > 1:
            guessrecursive(attempleft-1)
        else:
            print(f"\nsorry human, you won't be able to guess the number correct :) the correct answer was {secretnumber}")

welcomemassage()
guessrecursive(maxattemp)

print(f"memory address of secret number{secretnumber} is {id(secretnumber)}")