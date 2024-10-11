from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import logdb1
import stockmanagement
def verify():
    username=e11.get()
    password=e22.get()
    if not username or not password:
        messagebox.showerror("Error","All fields are required!")
        return
    else:
        if logdb1.verifyuser(username, password):
            messagebox.showinfo("Login Status","Login Successful")
            stockmanagement.pg1()
        else:
            messagebox.askyesno("Login Status","Invalid Input --- DO YOU WANT TO RETRY")
def main2():
    global e11,e22,logophotoo
    a3=Toplevel()  # Use Toplevel to create a new window
    a3.geometry('800x800')
    a3.configure(bg='skyblue')
    a3.title("Login")   
    l2 = Label(a3,text="USER NAME :",font=("", 15), bg='skyblue',fg='black')
    l2.place(x=250,y=340)
    l3 = Label(a3,text="PASSWORD :",font=("", 15), bg='skyblue',fg='black')
    l3.place(x=250,y=370)
    e11 = Entry(a3)
    e11.place(x=390,y=350)
    e22 = Entry(a3,show="*")
    e22.place(x=390,y=380)
    b1 = Button(a3,text="LOGIN",font=("impact", 15),bg='teal',fg='white',command=verify)
    b1.place(x=350,y=425)
