import tkinter as tk
from tkinter import ttk
import logdb1
def viewpg():
    def viewall():
        for i in tree.get_children():
            tree.delete(i)  # Clear the treeview before displaying new data

        records = logdb1.fetch()  # Fetch all records using the function from db.py
        for row in records:
            tree.insert("", tk.END, values=row)
    def viewone():
        product = e1.get()
        hsn = e2.get()
        if product and hsn:
            for i in tree.get_children():
                tree.delete(i)  # Clear the treeview before displaying new data

            records = logdb1.fetchone(product, hsn)
            for row in records:
                tree.insert("", tk.END, values=row)
    a=tk.Toplevel()
    a.title("View product")
    a.geometry("800x800")
#---------------------#mainframe#----------------------------- #   
    mainframe=tk.Frame(a)
    mainframe.pack(expand=True,fill=tk.BOTH)
#--------------------viewpage frame----------------------------#
    vp=tk.Frame(mainframe,bg='lightgreen')
    vp.grid(row=0,column=0,sticky='nsew')
#--------------------treeview frame----------------------------#
    treeviewframe = tk.Frame(mainframe,bg='lightblue')
    treeviewframe.grid(row=0,column=1,sticky='nsew')
#---------------------frame configuration----------------------#
    mainframe.grid_columnconfigure(0,weight=3)  
    mainframe.grid_columnconfigure(1,weight=7)  
    mainframe.grid_rowconfigure(0,weight=1)
#---------------------tree view column and heading---------------------------------------------------------------------#
    tree=ttk.Treeview(treeviewframe,columns=("s.no","date","hsc code","product","size","qty","Gsm"),show='headings')
    tree.heading("s.no",text="s.no")
    tree.heading("date",text="date")
    tree.heading("hsc code",text="hsc code")
    tree.heading("product",text="product")
    tree.heading("size",text="size")
    tree.heading("qty",text="qty")
    tree.heading("Gsm",text="Gsm")
    tree.column("s.no",width=10)
    tree.column("date",width=40)
    tree.column("hsc code",width=40)
    tree.column("product",width=100)
    tree.column("size",width=40)
    tree.column("qty",width=40)
    tree.column("Gsm",width=40)
    tree.pack(expand=True,fill=tk.BOTH)
#---------------------------vp heading-------------------------------------#
    tk.Label(vp,text="VIEW STOCK",font='Calibri',bg='lightgreen').pack(pady=10)
#---------------------------lable entry and button--------------------------#
    l1=tk.Label(vp,text="PRODUCT",bg='light green',fg='black')
    l1.pack(pady=1)
    e1=tk.Entry(vp)
    e1.pack(pady=2)
    l2=tk.Label(vp,text="HSC CODE",bg='light green',fg='black')
    l2.pack(pady=1)
    e2=tk.Entry(vp)
    e2.pack(pady=2)
    b1=tk.Button(vp,text="View All",bg='sky blue',fg='black',command=viewall)
    b1.pack(pady=5)
    b2=tk.Button(vp,text="view",bg='skyblue',fg='black',command=viewone)
    b2.pack(pady=10)
    a.mainloop()

