from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import logdb1
def details():
    username = e11.get()
    password = e22.get()
    if not username or not password:
        messagebox.showerror("Error","All fields are required!")
        return
    else:
        logdb1.registeruser(username,password)
        messagebox.showinfo("Registration Status","Registration Successful")
def main1():
    global e11,e22,e2,e4,e5,e6,Tk
    a1=Toplevel()
    a1.geometry('800x800')
    a1.configure(bg='skyblue')
    a1.title("New User")   
    l2=Label(a1,text="USER NAME :",font=("",15),bg='skyblue',fg='black')
    l2.place(x=250,y=340)
    l22=Label(a1,text="PASSWORD :",font=("",15),bg='skyblue',fg='black')
    l22.place(x=250,y=370)
    b2=Button(a1,text="REGISTER",font=("Impact",12),bg='teal',fg='white',command=details)
    b2.place(x=340,y=425)
    e11=Entry(a1,text="")
    e11.place(x=390,y=345)
    e22=Entry(a1,text="*")
    e22.place(x=390,y=375)


