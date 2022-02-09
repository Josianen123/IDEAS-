import tkinter as tk


calculation = ''

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,'end')
    text_result.insert(1.0,calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0,'end')
        text_result.insert(1.0, calculation)
    except:
        clear_Field()
        text_result.insert(1.0,'Error')
        


def clear_Field():
    global calculation
    calculation = ''
    text_result.delete(1.0,'end')

    

root = tk.Tk()
root.title('Josiane\'s Calculator')
root.geometry('400x400')

text_result= tk.Text(root, height=2, width=30, font=('Times New Roman',25))
text_result.grid(columnspan=10)

button1 = tk.Button(root, text='1', command=lambda:add_to_calculation(1), width=7,font=('Times New Roman',20))
button1.grid(row=2,column=1)

button2 = tk.Button(root, text='2', command=lambda:add_to_calculation(2), width=7,font=('Times New Roman',15))
button2.grid(row=2,column=2)

button3 = tk.Button(root, text='3', command=lambda:add_to_calculation(3), width=7,font=('Times New Roman',15))
button3.grid(row=2,column=3)

button4 = tk.Button(root, text='4', command=lambda:add_to_calculation(4), width=7,font=('Times New Roman',15))
button4.grid(row=3,column=1)

button5 = tk.Button(root, text='5', command=lambda:add_to_calculation(5), width=7,font=('Times New Roman',15))
button5.grid(row=3,column=2)

button6 = tk.Button(root, text='6', command=lambda:add_to_calculation(6), width=7,font=('Times New Roman',15))
button6.grid(row=3,column=3)

button7 = tk.Button(root, text='7', command=lambda:add_to_calculation(7), width=7,font=('Times New Roman',15))
button7.grid(row=4,column=1)

button8 = tk.Button(root, text='8', command=lambda:add_to_calculation(8), width=7,font=('Times New Roman',15))
button8.grid(row=4,column=2)

button9 = tk.Button(root, text='9', command=lambda:add_to_calculation(9), width=7,font=('Times New Roman',15))
button9.grid(row=4,column=3)

buttonPlus = tk.Button(root, text='+', command=lambda:add_to_calculation('+'), width=7,font=('Times New Roman',15))
buttonPlus.grid(row=2,column=4)

buttonDivide = tk.Button(root, text='/', command=lambda:add_to_calculation('/'), width=7,font=('Times New Roman',15))
buttonDivide.grid(row=3, column=4)

buttonTimes = tk.Button(root, text='x', command=lambda:add_to_calculation('*'), width=7,font=('Times New Roman',15))
buttonTimes.grid(row=4,column=4)

buttonMinus = tk.Button(root, text='-', command=lambda:add_to_calculation('-'), width=7,font=('Times New Roman',15))
buttonMinus.grid(row=5,column=4)

button5 = tk.Button(root, text='.', command=lambda:add_to_calculation('.'), width=7,font=('Times New Roman',15))
button5.grid(row=5,column=1)

button0 = tk.Button(root, text='0', command=lambda:add_to_calculation(0), width=7,font=('Times New Roman',15))
button0.grid(row=5,column=2)

buttonEqual = tk.Button(root, text='=', command=evaluate_calculation, width=7,font=('Times New Roman',15))
buttonEqual.grid(row=5,column=3)


root.mainloop()


#JKN