from tkinter import *



def btnClick(number):
    global operator
    operator += str(number)
    text_input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_input.set(operator)

def btnEqual():
    global operator
    sum = str(eval(operator))
    text_input.set(sum)


window = Tk()
window.title("Calculator")
operator = ""
text_input = StringVar()

#Entry
number_entry = Entry(window, width=48, bd=10, textvariable=text_input, font=("Arial", 10, "bold"), insertwidth=4)
number_entry.grid(column=0, row=0, columnspan=5)

#Button 1,2,3,+
button_1 = Button(window, text="1", font=("Arial", 10, "bold"), width=9, height=4, bd=4, command=lambda: btnClick(1))
button_1.grid(column=0, row=1)
button_2 = Button(window, text="2", font=("Arial", 10, "bold"), width=9, height=4, bd=4, command=lambda: btnClick(2))
button_2.grid(column=1, row=1)
button_3 = Button(window, text="3", font=("Arial", 10, "bold"), width=9, height=4, bd=4, command=lambda: btnClick(3))
button_3.grid(column=2, row=1)
button_plus = Button(window, text="+", font=("Arial", 10, "bold"), width=9, height=4, bd=4, bg="#DCD7C9",
                     command=lambda: btnClick("+"))
button_plus.grid(column=3, row=1)

#button 4,5,6,-
button_4 = Button(window, text="4", font=("Arial", 10, "bold"), width=9, height=4, bd=4, command=lambda: btnClick(4))
button_4.grid(column=0, row=2)
button_5 = Button(window, text="5", font=("Arial", 10, "bold"), width=9, height=4, bd=4, command=lambda: btnClick(5))
button_5.grid(column=1, row=2)
button_6 = Button(window, text="6", font=("Arial", 10, "bold"), width=9, height=4, bd=4, command=lambda: btnClick(6))
button_6.grid(column=2, row=2)
button_minus = Button(window, text="-", font=("Arial", 10, "bold"), width=9, height=4, bd=4,
                      bg="#DCD7C9", command=lambda: btnClick("-"))
button_minus.grid(column=3, row=2)

#button 7,8,9,*
button_7 = Button(window, text="4", font=("Arial", 10, "bold"), width=9, height=4, bd=4, command=lambda: btnClick(7))
button_7.grid(column=0, row=3)
button_8 = Button(window, text="5", font=("Arial", 10, "bold"), width=9, height=4, bd=4, command=lambda: btnClick(8))
button_8.grid(column=1, row=3)
button_9 = Button(window, text="6", font=("Arial", 10, "bold"), width=9, height=4, bd=4, command=lambda: btnClick(9))
button_9.grid(column=2, row=3)
button_kali = Button(window, text="-", font=("Arial", 10, "bold"), width=9, height=4, bd=4,
                     bg="#DCD7C9", command=lambda: btnClick("*"))
button_kali.grid(column=3, row=3)

#button 0,.,=,/
button_0 = Button(window, text="0", font=("Arial", 10, "bold"), width=9, height=4, bd=4, command=lambda: btnClick(0))
button_0.grid(column=0, row=4)
button_clear = Button(window, text="Clear", font=("Arial", 10, "bold"), width=9, height=4, bd=4,
                      bg="#DCD7C9", command=btnClear)
button_clear.grid(column=1, row=4)
button_equal = Button(window, text="=", font=("Arial", 10, "bold"), width=9, height=4, bd=4,
                      bg="#FFED00", command=btnEqual)
button_equal.grid(column=2, row=4)
button_bagi = Button(window, text="/", font=("Arial", 10, "bold"), width=9, height=4, bd=4,
                     bg="#DCD7C9", command=lambda: btnClick("/"))
button_bagi.grid(column=3, row=4)



window.mainloop()