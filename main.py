#Number guesing game ( with Tkinter )

from tkinter import *
from tkinter import font,messagebox
import random as r
import time

tk = Tk();
chance=10
tk.geometry("800x800")
tk.title("Number Guesingg game")

def check() :
    global chance
    chance=chance-1
    input_number = int(entry.get())
    if chance==0 :
        output.config(text="Out of chnaces Better luck next time")
        messagebox.showwarning("Out Of chances","No more Chances to play")
        time.sleep(3)
        tk.destroy()
    elif not (random_number == input_number) :
        if chance < 3 :
            messagebox.showwarning("Warning",f"You have only {chance} chances")
        head_data.config(text=f"You have {chance} chances to find the number")
    else :
        output.config(text="Its amazing you are right")

underlined_font = font.Font(family="times of india", size=25, underline=1)
Label(tk,text="Number Guessing Game", font=underlined_font,fg="blue").pack(pady=5)

#need to suggest color
head_data=Label(tk,text=f"You have {chance} chances to find the number",font=("Arial",16))
head_data.pack(pady=6,padx=8)

random_number = r.randint(1,1000)
range_random_number = r.randint(1,50)
print(random_number)
random_number_text= Label(tk,text=f"Range to find a number {random_number-range_random_number} and {random_number+(100-range_random_number)}",font=("arial",16))
random_number_text.pack(padx=10,pady=10)

Label(tk,text="Enter your number : ",font=('Helvetica', 14)).pack()

my_var=IntVar
entry=Entry(tk,width=30,textvariable=my_var,borderwidth=3,font=('Helvetica', 14))
entry.pack()

Button(tk,text="Check",font=("Arial",13),command=check).pack(pady=10)

output=Label(tk,text="",font=("Arial",16))
output.pack(padx=10,pady=10)
tk.mainloop()