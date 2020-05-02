reply = False
numlist = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
while reply == False:
    position = int(input("Choose your next postion: (1-9)"))
    if numlist[position] != " ":
        print("This position is occupied! Please input again!")
    else:
        reply = True
