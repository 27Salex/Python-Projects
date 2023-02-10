import random
def start:
    Print("Welcome To Rock Paper Scisors!")
    choice = input("r:Rock, p:Paper or s:Scisors?")
    rivalChoice = (random.randrange(1,3)) 
    """
    1 Rock
    2 Paper
    3 Scisors
    """
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