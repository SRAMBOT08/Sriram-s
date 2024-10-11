from tkinter import * 
from tkinter import messagebox
from PIL import ImageTk, Image
import logdb1
global additem
def addi():
    def adddb():
        date = en1.get()
        hsn = en2.get()
        product = en3.get()
        size = en4.get()
        quantity = en5.get()
        gsm = en6.get()
        if date and hsn and product and size and quantity and gsm:
            logdb1.addnew(date,hsn,product,size,quantity,gsm)
            messagebox.showinfo("Success","Product added successfully")
        else:
            messagebox.showwarning("Input Error","All fields are required")

    a4=Toplevel()
    a4.geometry('800x800')
    a4.configure(bg='skyblue')
    a4.title("Add New Product")   
    #-------------------------------for text label-----------------------------------------------
    l1=Label(a4,text="ADD NEW PRODUCT",font=("impact",20),bg='skyblue',fg='royalblue')
    l1.place(x=350,y=20)
    l2=Label(a4,text='DATE :',font=('',15),bg='skyblue',fg='royalblue')
    l2.place(x=270,y=90)
    l3=Label(a4,text='HSN CODE :',font=('',15),bg='skyblue',fg='royalblue')
    l3.place(x=270,y=130)
    l4=Label(a4,text='PRODUCT :',font=('',15),bg='skyblue',fg='royalblue')
    l4.place(x=270,y=170)
    l5=Label(a4,text='SIZE :',font=('',15),bg='skyblue',fg='royalblue')
    l5.place(x=270,y=210)
    l6=Label(a4,text='QUANTITY :',font=('',15),bg='skyblue',fg='royalblue')
    l6.place(x=270,y=250)
    l7=Label(a4,text='GSM :',font=('',15),bg='skyblue',fg='royalblue')
    l7.place(x=270,y=290)
    #--------------------------------entry textbox------------------------------------------------
    en1=Entry(a4,text='')
    en1.place(x=400,y=95)
    en2=Entry(a4,text='')
    en2.place(x=400,y=135)
    en3=Entry(a4,text='')
    en3.place(x=400,y=175)
    en4=Entry(a4,text='')
    en4.place(x=400,y=215)
    en5=Entry(a4,text='')
    en5.place(x=400,y=255)
    en6=Entry(a4,text='')
    en6.place(x=400,y=295)
    #------------------------------Button---------------------------------------------------------
    bu1=Button(a4,text='ADD PRODUCT',font=('',15),bg='teal',fg='white',height=1,command=adddb)
    bu1.place(x=340,y=370)
    
    

