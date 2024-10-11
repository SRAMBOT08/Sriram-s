from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import updateitem
import additem
import deletepro
import viewpage
#-------------------------------------------------- page naviation ----------------------------------
def ve():
    viewpage.viewpg()
def add():
    additem.addi()
def upt():
    updateitem.upro()
def dele():
    deletepro.delete()
#--------------------------------------------------------------------------------------------------
#------------------------------------------------- main fun of this page --------------------------
def pg1():
    a0=Toplevel()
    a0.geometry('800x800')
    a0.configure(bg='skyblue')
    a0.title("Stock Management")        
    #-------------------------------for logo image----------------------------------------------
    #------------------------------label--------------------------------------------------------
    l1=Label(a0,text="STOCK MANAGEMENT",font=("impact",20),bg='skyblue',fg='teal')
    l1.place(x=310,y=210)
    #--------------------------------buttons----------------------------------------------------
    bu1=Button(a0,text="VIEW PRODUCT",font=("impact",15),bg='teal',fg='white',command=ve)
    bu1.place(x=360,y=270)
    bu1=Button(a0,text="UPDATE PRODUCT",font=("impact",15),bg='teal',fg='white',command=upt)
    bu1.place(x=348,y=330)
    bu1=Button(a0,text="ADD NEW PRODUCT",font=("impact",15),bg='teal',fg='white',command=add)
    bu1.place(x=340,y=390)
    bu1=Button(a0,text="DELETE PRODUCT",font=("impact",15),bg='teal',fg='white',command=dele)
    bu1.place(x=350,y=450)
#---------------------------------------------------------------------------------------------------
