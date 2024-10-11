from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import logdb1
def upro():
    def upddb():
        date = en1.get()
        hsn = en2.get()
        product = en3.get()
        size = en4.get()
        quantity = en5.get()
        gsm = en6.get()

        if hsn:
            logdb1.updt(hsn, date=date, product=product, size=size, quantity=quantity, gsm=gsm)
            messagebox.showinfo("Success", "Product updated successfully")
        else:
            messagebox.showwarning("Input Error", "HSN code is required")
    a6=Toplevel()Z
    a6.geometry('800x800')
    a6.configure(bg='skyblue')
    #------------------------------- for logo image -----------------------------------------------
    #------------------------------- for text label -----------------------------------------------
    l1=Label(a6,text="UPDATE PRODUCT",font=("impact",20),bg='skyblue',fg='royalblue')
    l1.place(x=310,y=20)
    l2=Label(a6,text='DATE :',font=('',15),bg='skyblue',fg='royalblue')
    l2.place(x=270,y=90)
    l3=Label(a6,text='HSN CODE :',font=('',15),bg='skyblue',fg='royalblue')
    l3.place(x=270,y=130)
    l4=Label(a6,text='PRODUCT :',font=('',15),bg='skyblue',fg='royalblue')
    l4.place(x=270,y=170)
    l5=Label(a6,text='SIZE :',font=('',15),bg='skyblue',fg='royalblue')
    l5.place(x=270,y=210)
    l6=Label(a6,text='QUANTITY :',font=('',15),bg='skyblue',fg='royalblue')
    l6.place(x=270,y=250)
    l7=Label(a6,text='GSM :',font=('',15),bg='skyblue',fg='royalblue')
    l7.place(x=270,y=290)
    #-------------------------------- entry textbox ------------------------------------------------
    en1=Entry(a6,text='')
    en1.place(x=400,y=95)
    en2=Entry(a6,text='')
    en2.place(x=400,y=135)
    en3=Entry(a6,text='')
    en3.place(x=400,y=175)
    en4=Entry(a6,text='')
    en4.place(x=400,y=215)
    en5=Entry(a6,text='')
    en5.place(x=400,y=255)
    en6=Entry(a6,text='')
    en6.place(x=400,y=295)
    #------------------------------ Button ---------------------------------------------------------
    bu1=Button(a6,text='UPDATE PRODUCT',font=('',15),bg='teal',fg='white',height=1,command=upddb)
    bu1.place(x=310,y=350)

