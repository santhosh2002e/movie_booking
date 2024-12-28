from tkinter import *

window = Tk()
window.title('Simple Calculator')

# Icon
window.iconbitmap("C:/Users/ELUMALAI REVATHI/AppData/Local/Programs/Python/Python311/Lib/tkinter/icon.ico")

# Entry field
e = Entry(width=35, borderwidth=5, fg='blue', bg='white')
e.grid(row=0, column=0, columnspan=4)

# Button click function
def button_click(number):
    current = e.get()
    print()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

# Button clear function
def button_clear():
    e.delete(0, END)

def buttonAdd():
    global fnum,math
    math=1
    first_number=e.get()
    fnum=int(first_number)
    e.delete(0,END)  

def buttonSub():
    global fnum,math
    math=2
    first_number=e.get()
    fnum=int(first_number)
    e.delete(0,END)  

def buttonMul():
    global fnum,math
    math=3
    first_number=e.get()
    fnum=int(first_number)
    e.delete(0,END)  

def buttonDiv():
    global fnum,math
    math=4
    first_number=e.get()
    fnum=int(first_number)
    e.delete(0,END)  

def buttonEqual():
    second_number=e.get()
    snum=int(second_number)
    e.delete(0,END)
    if math==1:
        e.insert(0,fnum+snum)
    elif math==2:
        e.insert(0,fnum-snum)
    elif math==3:
        e.insert(0,fnum*snum)
    else:
        e.insert(0,fnum/snum)
        

# Number buttons
button_1 = Button(text='1', padx=40, pady=20, command=lambda: button_click(1), fg='black', bg='gray').grid(row=1, column=0)
button_2 = Button(text='2', padx=40, pady=20, command=lambda: button_click(2), fg='black', bg='gray').grid(row=1, column=1)
button_3 = Button(text='3', padx=40, pady=20, command=lambda: button_click(3), fg='black', bg='gray').grid(row=1, column=2)

button_4 = Button(text='4', padx=40, pady=20, command=lambda: button_click(4), fg='black', bg='gray').grid(row=2, column=0)
button_5 = Button(text='5', padx=40, pady=20, command=lambda: button_click(5), fg='black', bg='gray').grid(row=2, column=1)
button_6 = Button(text='6', padx=40, pady=20, command=lambda: button_click(6), fg='black', bg='gray').grid(row=2, column=2)

button_7 = Button(text='7', padx=40, pady=20, command=lambda: button_click(7), fg='black', bg='gray').grid(row=3, column=0)
button_8 = Button(text='8', padx=40, pady=20, command=lambda: button_click(8), fg='black', bg='gray').grid(row=3, column=1)
button_9 = Button(text='9', padx=40, pady=20, command=lambda: button_click(9), fg='black', bg='gray').grid(row=3, column=2)
button_0 = Button(text='0', padx=40, pady=20, command=lambda: button_click(0), fg='black', bg='gray').grid(row=4, column=0)

# Operator buttons
button_add = Button(text='+', padx=39, pady=20, command=buttonAdd, fg='black', bg='gray').grid(row=1, column=3)
button_sub = Button(text='-', padx=40, pady=20, command=buttonSub, fg='black', bg='gray').grid(row=2, column=3)
button_mul = Button(text='*', padx=40, pady=20, command=buttonMul, fg='black', bg='gray').grid(row=3, column=3)

button_div = Button(text='/', padx=41, pady=20, command=buttonDiv, fg='black', bg='gray').grid(row=4, column=3)
button_equal = Button(text='=', padx=87, pady=20, command=buttonEqual, fg='green', bg='white').grid(row=4, column=1, columnspan=2)
button_clear = Button(text='CLEAR', padx=169, pady=25, command=button_clear, fg='red', bg='white').grid(row=5, column=0, columnspan=4)

window.mainloop()
