import sys

again = True

while again:

    check = input("\nPlease enter a word...\n\n")

    check = check.lower()

    print("\n--------------------------\n")

    check = list(check)

    if check[0:] == check[::-1]:
        print("This is a palindrome!")
    else:
        print("This is a not palindrome!")

    again = input("\nWould you like to check another word?\n\nY for Yes,\nN for No\n")

    if again.lower() == "y":
        continue
    else:
        print("\nCya!\n")
        break
sys.exit()