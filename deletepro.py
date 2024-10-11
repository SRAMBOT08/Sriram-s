from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import logdb1
global delete
def delete():
    def deletep():
        hsn = en1.get()
        # Call the delete function from the database module
        logdb1.deleteproduct(hsn)
        messagebox.showinfo("Success","Product deleted successfully!")
        a5.destroy()

    a5=Toplevel()
    a5.geometry('800x800')
    a5.configure(bg='skyblue')
    a5.title("Delete Product")    
    #-------------------------------for logo image----------------------------------------------
    #-------------------------------for text label-----------------------------------------------
    l1=Label(a5,text="DELETE PRODUCT",font=("impact",20),bg='skyblue',fg='royalblue')
    l1.place(x=300,y=40)
    l2=Label(a5,text='HSN CODE :',font=('',15),bg='skyblue',fg='royalblue')
    l2.place(x=270,y=130)
    l3=Label(a5,text='PRODUCT :',font=('',15),bg='skyblue',fg='royalblue')
    l3.place(x=270,y=170)
    l4=Label(a5,text='SIZE :',font=('',15),bg='skyblue',fg='royalblue')
    l4.place(x=270,y=210)
    l5=Label(a5,text='GSM :',font=('',15),bg='skyblue',fg='royalblue')
    l5.place(x=270,y=250)
    #--------------------------------entry textbox------------------------------------------------
    en1=Entry(a5,text='')
    en1.place(x=400,y=135)
    en2=Entry(a5,text='')
    en2.place(x=400,y=175)
    en3=Entry(a5,text='')
    en3.place(x=400,y=215)
    en4=Entry(a5,text='')
    en4.place(x=400,y=255)
    #------------------------------Button---------------------------------------------------------
    bu1=Button(a5,text='DELETE PRODUCT',font=('',15),bg='teal',fg='white',height=1,command=deletep)
    bu1.place(x=300,y=290)
    
    

