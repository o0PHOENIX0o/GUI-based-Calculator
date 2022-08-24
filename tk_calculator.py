from time import sleep
from tkinter import *

# starting the event loop
root = Tk()

root.title("Calculator")
root.geometry("300x580")
root.maxsize(300, 580)


''' background image'''
#photo_1 = PhotoImage(file='img//img3.png')
'''image for back button'''
#back_button_photo = PhotoImage(file='img//img4.png')


# adding the background
canvas = Canvas(root,bg = 'black')
canvas.pack()



# adding a title
title = Label(root, text='Calculator', borderwidth=0, font=(
    "Algerian", 18, "bold"), bg="#00a9d4")
title.place(x=70, y=10)


# adding user instruction
user_instruction = Label(root, text='enter your question', bg="#0D0D0D", fg='white',
                font=("comicsms", 15, "bold"), borderwidth=4, relief=RIDGE, padx=52)
user_instruction.place(x=0, y=80)

# creating a string variable to store input from user
question = StringVar()


# taking user input
value = Entry(root, textvariable=question,font="comicsasms, 15", bg="#0D0D0D",
             fg="white", border=3, relief=SUNKEN)
value.place(x=40, y=125)


# creating a frame for buttons
frame_1 = Label(root, bg="#33363D", padx=145, pady=177,
                borderwidth=5, relief=RIDGE)
frame_1.place(x=0, y=200)


# function to identify which button is pressed
def which_button(sym):
    TEXT = question.get()
    c = len(TEXT) + 1
    if sym == "=":
        equal = Buttons("")
        equal.solve()
    elif sym == 'back':
        Label(root,text = '\t\t\t\t\t',bg = 'black',fg = 'red',font="comicsms 10 bold").place(x = 5, y = 165)
        value.delete(first=c-2, last=c+1)
    elif sym == 'C':
        Label(root,text = '\t\t\t\t\t',bg = 'black',fg = 'red',font="comicsms 10 bold").place(x = 5, y = 165)
    else:
        Label(root,text = '\t\t\t\t\t',bg = 'black',fg = 'red',font="comicsms 10 bold").place(x = 5, y = 165)
        value.insert(c, sym)


# class to create the buttons on the window
class Buttons:

    # instence variables
    def __init__(self,string):
        string = string.split()
        length = len(string)
        self.image = ''
        self.padx = 15
        self.pady = 10
        if length == 3:
            self.text = string[0]
            self.x = int(string[1])
            self.y = int(string[2])
        elif length == 4:
            self.text = string[0]
            self.x = int(string[1])
            self.y = int(string[2])
            self.image = string[3]
        elif length == 5:
            self.text = string[0]
            self.x = int(string[1])
            self.y = int(string[2])
            self.padx = int(string[3])
            self.pady = int(string[4])
        else:
            self.text = None
            self.x = None
            self.y = None
            self.padx = None
            self.pady = None


    # number buttons
    def button_num(self):
        button = Button(root, text=self.text, image=self.image, font="comicsms 10 bold", bg="black", fg='white', borderwidth=4,
                        padx=self.padx, pady=self.pady, command=lambda m=self.text: which_button(m))
        button.place(x=self.x, y=self.y)

    # operator button
    def button_options(self):
        button = Button(root, text=self.text, font="comicsms 11 bold", bg="black", fg='green', borderwidth=4,
                        padx=self.padx, pady=self.pady, command=lambda m=self.text: which_button(m))
        button.place(x=self.x, y=self.y)

    #solution
    @staticmethod
    def solve():
        try:
            que = question.get()
            que = que.replace("x", "*")
            que = que.replace("÷", "/")
            ans = eval(que)
            value.delete(first=0, last=len(que))
            value.insert(0, ans)
        except Exception as e:
            Label(root,text = 'INVALID INPUT',width=10,padx =100,bg = 'black',fg = 'red',font="comicsms 10 bold").place(x = 5, y = 165)

#instantiation (creating class object)
button_2 = Buttons("2 95 440")
button_1 = Buttons("1 25 440")
button_3 = Buttons("3 165 440")
button_4 = Buttons("4 25 370")
button_5 = Buttons("5 95 370")
button_6 = Buttons("6 165 370")
button_7 = Buttons("7 25 300")
button_8 = Buttons("8 95 300")
button_9 = Buttons("9 165 300")
button_0 = Buttons("0 95 510")
button_double_zeros = Buttons("00 25 510")
button_add = Buttons("+ 235 440")
button_sub = Buttons("- 235 370")
button_mul = Buttons("x 235 300") 
button_div = Buttons("÷ 235 230")
button_dot = Buttons(" . 165 510")
button_clear = Buttons("C 20 230")
button_back = Buttons(f"back 160 230")
button_equal = Buttons("= 235 510")
button_bracketopen = Buttons(" ( 90 230 5 10")
button_bracketclose = Buttons(" ) 125 230 5 10")

button_1.button_num()
button_2.button_num()
button_3.button_num()
button_4.button_num()
button_5.button_num()
button_6.button_num()
button_7.button_num()
button_8.button_num()
button_9.button_num()
button_0.button_num()
button_dot.button_num()
button_add.button_options()
button_sub.button_options()
button_mul.button_options()
button_div.button_options()
button_equal.button_options()
button_back.button_options()
button_double_zeros.button_num()
button_clear.button_options()
button_bracketopen.button_options()
button_bracketclose.button_options()

# ending the event loop
root.mainloop()
