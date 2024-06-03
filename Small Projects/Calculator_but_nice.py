from tkinter import *

root = Tk()
root.title("Simple Calculator") # .title() names the program at the top like discord in the top left

screen = Entry(root, width=30, borderwidth=5)
screen.grid(row=0,column=0, columnspan=4, padx=10, pady=10)
# columnspan tells the column how wide to be, so if there are 3 other columns under it
# then column span will make screen span 3 columns
# screen.insert(0, "Enter Your Name")
# the reason the first argument is 0 is 

warning = Label(root, text="DIVIDE BY \nMULTIPLES")

def buttonclick(num):
    current = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(current) + str(num))

def button_clear():
    screen.delete(0, END)

def button_add():
    first_num = screen.get()
    global f_num
    f_num = int(first_num)
    screen.delete(0, END)
    global operator
    operator = "add"

def button_sub():
    first_num = screen.get()
    global f_num
    f_num = int(first_num)
    screen.delete(0, END)
    global operator
    operator = "sub"

def button_multi():
    first_num = screen.get()
    global f_num
    f_num = int(first_num)
    screen.delete(0, END)
    global operator
    operator = "multi"

def button_div():
    first_num = screen.get()
    global f_num
    f_num = int(first_num)
    screen.delete(0, END)
    global operator
    operator = "div"

def button_equal():
    second_number = int(screen.get())
    screen.delete(0, END)
    if operator == "add":
        screen.insert(0, f_num + second_number)
    elif operator == "sub":
        screen.insert(0, f_num - second_number)
    elif operator == "multi":
        screen.insert(0, f_num * second_number)
    elif operator == "div":
        screen.insert(0, f_num // second_number)

# Define all the buttons

button1 = Button(root, text="1", padx=30, pady=18, command=lambda: buttonclick(1)) # you need to use a lambda since you cant actually input arguments in tkinter
button2 = Button(root, text="2", padx=30, pady=18, command=lambda: buttonclick(2))
button3 = Button(root, text="3", padx=30, pady=18, command=lambda: buttonclick(3))
button4 = Button(root, text="4", padx=30, pady=18, command=lambda: buttonclick(4))
button5 = Button(root, text="5", padx=30, pady=18, command=lambda: buttonclick(5))
button6 = Button(root, text="6", padx=30, pady=18, command=lambda: buttonclick(6))
button7 = Button(root, text="7", padx=30, pady=18, command=lambda: buttonclick(7))
button8 = Button(root, text="8", padx=30, pady=18, command=lambda: buttonclick(8))
button9 = Button(root, text="9", padx=30, pady=18, command=lambda: buttonclick(9))
button0 = Button(root, text="0", padx=30, pady=18, command=lambda: buttonclick(0))

buttonadd = Button(root, text="+", padx=30, pady=18, command=button_add)
buttonequal = Button(root, text="=", padx=30, pady=18, command=button_equal)
buttonclear = Button(root, text="Clear", padx=20, pady=18, command=button_clear) # you only need the lambda if you want to pass something into it

buttonsubtract = Button(root, text="-", padx=30, pady=18, command=button_sub)
buttonmultiply = Button(root, text="*", padx=30, pady=18, command=button_multi)
buttonadivide = Button(root, text="/", padx=30, pady=18, command=button_div)

# Put the buttons on the screen

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
buttonclear.grid(row=4, column=2)
buttonadd.grid(row=1, column=4)
buttonequal.grid(row=4, column=1)

buttonsubtract.grid(row=2, column=4)
buttonmultiply.grid(row=3, column=4)
buttonadivide.grid(row=4, column=4)

warning.grid(row=0, column=4)

root.mainloop()