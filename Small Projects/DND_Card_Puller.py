import random
import sys

again = True

while again:

    num = ["ACE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE","TEN","KING","JACK","QUEEN"]
    cards = ["SPADES","CLUBS","HEARTS","DIAMONDS"]
    spades = ["1","2","3","4","5","6","7","8"]
    spade_races = {
        "1": "MASKED",
        "2": "ASTRAL",
        "3": "SLAKE",
        "4": "WILLOW",
        "5": "TEMPIST",
        "6": "VIXEN",
        "7": "TALON",
        "8": "GERALD"
    }

    random.shuffle(num)
    random.shuffle(cards)
    random.shuffle(spades)

    num = num[0]
    cards = cards[0]
    spades = spades[0]
    spades = spade_races[spades]
    
    if cards == "SPADES":
        print("\nYour card is the " + num + " OF " + cards + " and the race is " + spades + ".\n")
    else:
        print("\nYour card is the " + num + " OF " + cards + ".\n") 

    again = input("\nWould you like to pick another card?\n\nY for Yes,\nN for No\n")

    if again.lower() == "y":
        continue
    else:
        print("\nCya!")
        break
sys.exit()