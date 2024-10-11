from tkinter import *
from PIL import ImageTk,Image
import loglog
import logreg1
def dlog():
    loglog.main2()
def dreg():
    logreg1.main1()
a=Tk()
a.geometry('800x800')
a.configure(bg='skyblue')
a.title("User Login")
# LOGIN button
b1=Button(a,text="LOGIN",font=("impact",15),bg='teal',fg='white',command=dlog)
b1.place(x=275,y=350)
# SIGNUP button
b2=Button(a,text="SIGNUP",font=("impact",15),bg='teal',fg='white',command=dreg)
b2.place(x=380,y=350)
a.mainloop()
 
