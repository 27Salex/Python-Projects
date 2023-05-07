import os

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "
        ]

def clearCMD():
    if os.name == "nt":
        os.system("cls")
        os.system("MODE CON cols=42 lines=15")
        os.system("COLOR 0C")
        os.system("title Tic Tac Toe!")
    else: 
        os.system("clear")
        os.system("resize -s 15 42")
        os.system("tput setaf 1")
        os.system("tput setab 0")
        os.system("tput bold")
        os.system("echo -en '\033]2;Tic Tac Toe!\a'")
        
def showBoard():
    print("   |   |")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("___|___|___")
    print("   |   |")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("___|___|___")
    print("   |   |")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("   |   |")

turn = "O"

def nextTurn():
    global turn
    tempTurn = turn
    clearCMD()
    print("Turn of ", tempTurn)
    showBoard()
    cell = int(input("Select an empty cell:   "))
    if (cell >= 0 and cell <= 8) and (board[cell] != "X" and board[cell] != "O"):
        if turn == "X":
            turn = "O"
            board[cell] = "X"
            checkWin()
        elif turn == "O":
            turn = "X" 
            board[cell] = "O"
            checkWin()
    else:
        nextTurn()
    
def checkWin():
    
    if board[0] == board[1] and board[0] == board[2] and board[0] != " ":
        clearCMD()
        print("winner is", board[0])
        showBoard()
    elif board[0] == board[3] and board[0] == board[6] and board[0] != " ":
        clearCMD()
        print("winner is", board[0])
        showBoard()
    elif board[0] == board[4] and board[0] == board[8] and board[0] != " ":
        clearCMD()
        print("winner is", board[0])
        showBoard()
    elif board[2] == board[5] and board[2] == board[8] and board[2] != " ":
        clearCMD()
        print("winner is", board[2])
        showBoard()
    elif board[2] == board[4] and board[2] == board[6] and board[2] != " ":
        clearCMD()
        print("winner is", board[2])
        showBoard()
    elif board[1] == board[4] and board[1] == board[7] and board[1] != " ":
        clearCMD()
        print("winner is", board[1])
        showBoard()
    elif board[3] == board[4] and board[3] == board[5] and board[3] != " ":
        clearCMD()
        print("winner is", board[3])
        showBoard()
    elif board[6] == board[7] and board[6] == board[8] and board[6] != " ":
        clearCMD()
        print("winner is", board[3])
        showBoard()
    else:
        nextTurn()
        
def start():
    clearCMD()
    print("Welcome to CMD Tic Tac Toe!")
    menu = str(input("Type help for information or Play:   "))
    if menu == "help" or menu == "Help":
        print("   |   |")
        print(" 0 | 1 | 2 ")
        print("___|___|___")
        print("   |   |")
        print(" 3 | 4 | 5 ")
        print("___|___|___")
        print("   |   |")
        print(" 6 | 7 | 8 ")
        print("   |   |")
    elif menu == "play" or menu == "Play":
        nextTurn()
    else:
        print('ERROR')
        
start()