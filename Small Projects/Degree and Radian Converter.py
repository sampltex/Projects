import sys
import math

again = True

while again:

    x = input("\nEnter a radian or degree value you would like to convert...\n\n") # basic input

    if "π" in x:
        x = x.replace("π", "")
        rad = True
    elif "pi" in x:
        x = x.replace("pi", "")
        rad = True
    else:
        rad = False
        if x.lstrip("-").isnumeric():
            pass
        else:
            sys.exit("Hey! wth man!")


    x = list(x) # convert to list

    def simple(var): # gets rid of unwanted characters
        var = var.replace("'", "")
        var = var.replace(",", "")
        var = var.replace("[", "")
        var = var.replace("]", "")
        var = var.replace(" ", "")
        return var

    if rad == True:
        if x[0] != "/": # actual radian to degree converter (includes negative numbers and coefficients not floats)
            temp1 = x.index("/")
            if x[0] == "-":
                x = str(x)
                x = x.replace("-", "")
                x = list(x)
                neg = True
                y = 1
            else:
                neg = False
                y = x[:temp1]
            x = x[temp1:]
            x = str(x)
            y = str(y)
            x = x.replace("/", "")
            x = simple(x)
            y = simple(y)
            x = x.replace("\"", "")
            y = y.replace("\"", "")
            x = int(x)
            y = int(y)
            z = y / x
            z = z * 180
            a = z % 360
            if neg == False:
                if z > 360:
                    print("Your number in degrees is " + str(z) + " or " + str(a))
                else:
                    print("Your number in degrees is " + str(z))
            else:
                if z > 360:
                    print("Your number in degrees is " + "-" + str(z) + " or " + "-" + str(a) + "(oh yea this is wrong btw lol)")
                else:
                    print("Your number in degrees is " + "-" + str(z))
                
        else:
            temp1 = x.index("/")
            y = 1
            x = x[temp1:]
            x = str(x)
            y = str(y)
            x = simple(x)
            x = x.replace("/", "")
            x = x.replace("\"", "")
            y = y.replace("\"", "")
            x = int(x)
            y = int(y)
            z = y / x
            z = z * 180
            print("Your number in degrees in " + str(z))
    else:
        x = str(x)
        x = simple(x)
        z = math.radians(int(x))
        div = 180
        d = math.gcd(int(x),180)
        div = div // d
        x = int(x) // d


        if x == 1:
            print("\nYour number in radians is " + "π" + "/" + str(div) + " or " + str(z) + "radians")
        else:
            print("\nYour number in radians is " + str(x) + "π" + "/" + str(div) + " or " + str(z) + " radians")

    again = input("\nWould you like to convert another value?\n\nY for Yes,\nN for No\n")
    if again.lower() == "y":
        continue
    else:
        print("\nCya!")
        break