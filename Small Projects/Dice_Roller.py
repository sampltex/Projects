import sys
import random

top1 = "┌─────────┐"
mid1 = "│         │"
mid2 = "│    ●    |"
mid3 = "│       ● │"
mid4=  "│ ●       │"
mid5 = "│ ●     ● │"
bot =  "└─────────┘"

def rolled1():
    print(f"{top1}\n{mid1}\n{mid2}\n{mid1}\n{bot}")

def rolled2():
    print(f"{top1}\n{mid3}\n{mid1}\n{mid4}\n{bot}")

def rolled3():
    print(f"{top1}\n{mid3}\n{mid2}\n{mid4}\n{bot}")

def rolled4():
    print(f"{top1}\n{mid5}\n{mid1}\n{mid5}\n{bot}")

def rolled5():
    print(f"{top1}\n{mid5}\n{mid2}\n{mid5}\n{bot}")

def rolled6():
    print(f"{top1}\n{mid5}\n{mid5}\n{mid5}\n{bot}")

def roll():
    while True:
        amount = input("\nHow many dice would you like to roll?\n1 or 2,\n")
        if amount not in ["1", "2"]:
            continue
        else:
            break

    if amount == "1":
        dice1 = random.choice("123456")
        print(f"\nYou rolled the number {dice1}!\n")
        match dice1:
            case "1":
                rolled1()
            case "2":
                rolled2()
            case "3":
                rolled3()
            case "4":
                rolled4()
            case "5":
                rolled5()
            case "6":
                rolled6()

        while True:
            again = input("Would you like to roll again?\n\nY for yes,\nN for no\n")
            if again.lower() not in ["y", "n"]:
                continue
            else:
                break
        
        if again == "y":
            roll()
        else:
            sys.exit("\nCya!")
    else:
        dice1 = random.choice("123456")
        dice2 = random.choice("123456")
        dicesum = int(dice1) +  int(dice2)
        print(f"\nYou rolled {dice1} and {dice2} or {dicesum}!")
        match dice1:
            case "1":
                rolled1()
            case "2":
                rolled2()
            case "3":
                rolled3()
            case "4":
                rolled4()
            case "5":
                rolled5()
            case "6":
                rolled6()
        match dice2:
            case "1":
                rolled1()
            case "2":
                rolled2()
            case "3":
                rolled3()
            case "4":
                rolled4()
            case "5":
                rolled5()
            case "6":
                rolled6()

        while True:
            again = input("Would you like to roll again?\n\nY for yes,\nN for no\n")
            if again.lower() not in ["y", "n"]:
                continue
            else:
                break
        
        if again == "y":
            roll()
        else:
            sys.exit("\nCya!")

if __name__ == "__main__":
    roll()