import random
print("Welcome To Rock Paper Scissors!")
choice = input("r Rock, p Paper or s Scissors?").lower()
rivalChoice = random.choice(['r', 'p', 's'])
if choice == "r" and rivalChoice == 's':
    print("You Won!")
elif choice == "r" and rivalChoice == 'p':
    print("You Lose!")
elif choice == "r" and rivalChoice == 'r':
    print("Oops its a Draw")
elif choice == "p" and rivalChoice == 'r':
    print("You Won!")
elif choice == "p" and rivalChoice == 's':
    print("You Lose!")
elif choice == "p" and rivalChoice == 'p':
    print("Oops its a Draw")
elif choice == "s" and rivalChoice == 'p':
    print("You Won!")
elif choice == "s" and rivalChoice == 'r':
    print("You Lose!")
elif choice == "s" and rivalChoice == 's':
    print("Oops its a Draw")
else:
    print("Sorry choose between r, p or s")


"""
import random
def start():
    print("Welcome To Rock Paper Scisors!")
    choice = input("r Rock, p Paper or s Scisors?")
    rivalChoice = (random.randrange(1,3)) 
   
    1 Rock
    2 Paper
    3 Scisors
    
    if choice == "r" and rivalChoice == 3:
        print("You Won!")
    elif choice == "r" and rivalChoice == 2:
        print("You Lose!")
    elif choice == "r" and rivalChoice == 1:
        print("Oops its a Draw")
    elif choice == "p" and rivalChoice == 1:
        print("You Won!")
    elif choice == "p" and rivalChoice == 3:
        print("You Lose!")
    elif choice == "p" and rivalChoice == 2:
        print("Oops its a Draw")
    elif choice == "s" and rivalChoice == 2:
        print("You Won!")
    elif choice == "s" and rivalChoice == 1:
        print("You Lose!")
    elif choice == "s" and rivalChoice == 3:
        print("Oops its a Draw")
    else:
        print("Sorry choose between r, p or s")
        start()
"""