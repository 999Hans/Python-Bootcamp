print("Welcome to Tic Tac Toe!")
player1 = input("Player 1: Do you want to be X or O?")
print("Player 1 will go first")
ready = input("Are you ready to play? Enter Yes or No.")

numlist = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]


def dashboard():
    print(numlist[7] + "|" + numlist[8] + "|" + numlist[9])
    print("-----")
    print(numlist[4] + "|" + numlist[5] + "|" + numlist[6])
    print("-----")
    print(numlist[1] + "|" + numlist[2] + "|" + numlist[3])


if player1 == "X":
    player2 = "O"
    rule = ["#", "X", "O", "X", "O", "X", "O", "X", "O", "X"]
elif player1 == "O":
    player2 = "X"
    rule = ["#", "O", "X", "O", "X", "O", "X", "O", "X", "O"]

if ready == "Yes":
    dashboard()


for i in range(1, 10):
    reply = False
    while reply == False:
        position = int(input("Choose your next postion: (1-9)"))
        if numlist[position] != " ":
            print("This position is occupied! Please input again!")
        else:
            reply = True
    numlist[position] = rule[i]
    dashboard()
    # if (numlist[1] == numlist[2] == numlist[3]) or (numlist[4] == numlist[5] == numlist[6]) or(numlist[7] == numlist[8] == numlist[9]):
    if (numlist[1] == numlist[2] == numlist[3]) and numlist[1] != " ":
        if player1 == numlist[1]:
            print("Player1 Win!")
        elif player2 == numlist[1]:
            print("Player2 Win!")
        break

    if (numlist[4] == numlist[5] == numlist[6]) and numlist[4] != " ":
        if player1 == numlist[4]:
            print("Player1 Win!")
        elif player2 == numlist[4]:
            print("Player2 Win!")
        break

    if (numlist[7] == numlist[8] == numlist[9]) and numlist[7] != " ":
        if player1 == numlist[7]:
            print("Player1 Win!")
        elif player2 == numlist[7]:
            print("Player2 Win!")
        break

    if (numlist[1] == numlist[4] == numlist[7]) and numlist[1] != " ":
        if player1 == numlist[1]:
            print("Player1 Win!")
        elif player2 == numlist[1]:
            print("Player2 Win!")
        break

    if (numlist[2] == numlist[5] == numlist[8]) and numlist[2] != " ":
        if player1 == numlist[2]:
            print("Player1 Win!")
        elif player2 == numlist[2]:
            print("Player2 Win!")
        break

    if (numlist[3] == numlist[6] == numlist[9]) and numlist[3] != " ":
        if player1 == numlist[3]:
            print("Player1 Win!")
        elif player2 == numlist[3]:
            print("Player2 Win!")
        break

    if (numlist[1] == numlist[5] == numlist[9]) and numlist[1] != " ":
        if player1 == numlist[1]:
            print("Player1 Win!")
        elif player2 == numlist[1]:
            print("Player2 Win!")
        break

    if (numlist[3] == numlist[5] == numlist[7]) and numlist[3] != " ":
        if player1 == numlist[3]:
            print("Player1 Win!")
        elif player2 == numlist[3]:
            print("Player2 Win!")
        break
    if i == 9:
        print("Draw!")
