import sys
import random

top1 = "┌─────────┐\n"
mid1 = "│         │\n"
mid2 = "│    ●    |\n"
mid3 = "│       ● │\n"
mid4=  "│ ●       │\n"
mid5 = "│ ●     ● │\n"
bot =  "└─────────┘"

def rolled1():
    print(f"{top1}{mid1}{mid2}{mid1}{bot}")

def rolled2():
    print(f"{top1}{mid3}{mid1}{mid4}{bot}")

def rolled3():
    print(f"{top1}{mid3}{mid2}{mid4}{bot}")

def rolled4():
    print(f"{top1}{mid5}{mid1}{mid5}{bot}")

def rolled5():
    print(f"{top1}{mid5}{mid2}{mid5}{bot}")

def rolled6():
    print(f"{top1}{mid5}{mid5}{mid5}{bot}")

def end():
    while True:
        again = input("Would you like to roll again?\n\nY for yes,\nN for no\n")
        if again.lower() not in ["y", "n"]:
            continue
        else:
            break
            
    if again.lower() == "y":
        roll()
    else:
        sys.exit("\nCya!")

def roll():
    while True:
        dicetype = input("\nWhich dice would you like to roll\n1 = 6 Sided Dice,\n2 = 20 Sided Dice,\n")
        if dicetype not in ["1", "2"]:
            continue
        else:
            break

    if dicetype == "1":

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
            end()

        else:
            dice1 = random.choice("123456")
            dice2 = random.choice("123456")
            dicesum = int(dice1) + int(dice2)
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
        end()

    else:
        print(f"\nYou rolled the number {random.randint(1,20)}!")
        end()
    
if __name__ == "__main__":
    roll()

print(f"You rolled the number {random.randint(1,20)}!")