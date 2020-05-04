import random
self = {"AceSpade": (1, 11), "2Spade": 2, "3Spade": 3, "4Spade": 4, "5Spade": 5, "6Spade": 6, "7Spade": 7, "8Spade": 8, "9Spade": 9, "10Spade": 10, "JackSpade": 10, "QueenSpade": 10, "KingSpade": 10, "AceDia": (1, 11), "2Dia": 2, "3Dia": 3, "4Dia": 4, "5Dia": 5, "6Dia": 6, "7Dia": 7, "8Dia": 8, "9Dia": 9, "10Dia": 10, "JackDia": 10, "QueenDia": 10, "KingDia": 10, "AceClover": (
    1, 11), "2Clover": 2, "3Clover": 3, "4Clover": 4, "5Clover": 5, "6Clover": 6, "7Clover": 7, "8Clover": 8, "9Clover": 9, "10Clover": 10, "JackClover": 10, "QueenClover": 10, "KingClover": 10, "AceHeart": (1, 11), "2Heart": 2, "3Heart": 3, "4Heart": 4, "5Heart": 5, "6Heart": 6, "7Heart": 7, "8Heart": 8, "9Heart": 9, "10Heart": 10, "JackHeart": 10, "QueenHeart": 10, "KingHeart": 10}

decklist = list(self.keys())

random.shuffle(decklist)

selfshuffle = {}

for i in decklist:
    selfshuffle[i] = self[i]
