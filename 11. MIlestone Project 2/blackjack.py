# 한 명의 유저와 한 명의 컴퓨터로 시작
# 유저는 계좌를 가지고 있고, 이 돈 안에서 배팅을 할 수 있음

# 카드 덱이 있고, 셔플을 해야함

# 게임을 시작하면 딜러는 하나의 카드를 오픈하고, 유저는 2장의 카드를 오픈함
# 유저의 선택지는 2가지가 있음
# 1. hit (한 장의 카드를 더 받음)
# 2. Stay (카드를 더 받지 않음)

# 컴퓨터의 턴에는 유저를 이기거나, 21을 넘어갈때까지 카드를 받음

# 추가 규칙
# jack, queen, king = 10
# Ace = 1 or 11


class Deck():
    deck = {"AceSpade": 11, "2Spade": 2, "3Spade": 3, "4Spade": 4, "5Spade": 5, "6Spade": 6, "7Spade": 7, "8Spade": 8, "9Spade": 9, "10Spade": 10, "JackSpade": 10, "QueenSpade": 10, "KingSpade": 10, "AceDia": 11, "2Dia": 2, "3Dia": 3, "4Dia": 4, "5Dia": 5, "6Dia": 6, "7Dia": 7, "8Dia": 8, "9Dia": 9, "10Dia": 10, "JackDia": 10, "QueenDia": 10, "KingDia": 10, "AceClover":
            11, "2Clover": 2, "3Clover": 3, "4Clover": 4, "5Clover": 5, "6Clover": 6, "7Clover": 7, "8Clover": 8, "9Clover": 9, "10Clover": 10, "JackClover": 10, "QueenClover": 10, "KingClover": 10, "AceHeart": 11, "2Heart": 2, "3Heart": 3, "4Heart": 4, "5Heart": 5, "6Heart": 6, "7Heart": 7, "8Heart": 8, "9Heart": 9, "10Heart": 10, "JackHeart": 10, "QueenHeart": 10, "KingHeart": 10}

    def __init__(self):
        pass

    def shuffle(self):
        import random

        decklist = list(self.deck.keys())
        random.shuffle(decklist)
        selfshuffle = {}

        for i in decklist:
            selfshuffle[i] = self.deck[i]

        return selfshuffle


def userscore():
    score = 0
    for i in userdeck:
        score += deck.deck[i]
    if score == 21:
        print("BlackJack!")
        userturn = False
    return score


def dealerscore():
    score = 0
    for i in dealerdeck:
        score += deck.deck[i]
    return score


print("Welcome to Black Jack World!")
userbankaccount = input("\nHow much do you have($)? Please input number only.")

print("Game Start!")
reset = False
while reset == False:
    print("Your balance is $" + userbankaccount)
    userturn = True
    dealerturn = True

    deck = Deck()
    deckshuffle = deck.shuffle()
    deckshufflelist = list(deckshuffle.keys())

    userdeck = [deckshufflelist.pop(0), deckshufflelist.pop(1)]
    dealerdeck = [deckshufflelist.pop(0)]

    print("\nYour card")
    print(userdeck)

    print("\nYour Score is ")
    yourscore = userscore()
    print(yourscore)

    print("\nDealer Card")
    print(dealerdeck)

    print("\nDealer's Score is ")
    dealscore = dealerscore()
    print(dealscore)

    print("\nYour Turn!")
    while userturn == True:
        userchoice = input("\nHit or Stay?")
        if userchoice.lower() == "hit":
            userdeck.append(deckshufflelist.pop(0))

            print("\nYour card")
            print(userdeck)
            yourscore = userscore()
            print(yourscore)
            if yourscore > 21:
                print("You are Bust!")
                dealerturn = False
                break
            elif yourscore == 21:
                break
        elif userchoice.lower() == "stay":
            userturn = False
            print("\nDealer's Turn!")
        else:
            print("Please input again!")

    while dealerturn == True:
        dealerdeck.append(deckshufflelist.pop(0))
        print("\nDealer Card")
        print(dealerdeck)
        dealscore = dealerscore()
        print(dealscore)

        if dealscore <= 21 and dealscore > yourscore:
            print("\nDealer Win!")
            print("You lost betting money")
            dealerturn = False
        elif dealscore > 21:
            print("\nDealer is Bust!")
            print("You Win!")
            dealerturn = False

    question = input("Do you want play again(Yes or No)?")
    if question.lower() == "yes":
        reset = False
    elif question.lower() == "no":
        reset = True
