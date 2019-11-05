from tkinter import *
from numpy import *
from pandas import *
import sqlite3
from PIL import Image, ImageTk
def city(s):
    j=1
    k=0
    base=sqlite3.connect("playgrounds.db")
    ab=str('select * from playgrounds where location="%s"'%s)
    a=base.execute(ab)
    result=a.fetchall()
    l=len(result)
    print(l)
    top=Toplevel()
    top.geometry()
    l1=Label(top,text=s+ " Playgrounds",justify=CENTER,font=("Brush Script MT",20))
    l1.grid(row=0,column=1,sticky="ns")
    for i in range(1,(l+1)):
        frame = Frame(top, bg="cyan",highlightbackground="green",highlightthickness=5,width=700,height=700)
        frame.grid(row=j,column=k,padx=20,pady=20)
        k=k+1
        if(i%3==0):
            j=j+1
            k=0
        l2=Label(frame,text=result[i-1][1],width=33)
        l2.pack(padx=20)
        width = 200
        height = 70
        img = Image.open(str(result[i-1][7])+".png")
        img = img.resize((width,height))
        photoImg =  ImageTk.PhotoImage(img)
        b = Label(frame,image=photoImg,width=100)
        b.pack(pady=5)
        l3=Label(frame,text="Price : ₹"+str(result[i-1][8]))
        l3.pack(side=LEFT)
        button=Button(frame,text="Book")
        button.pack(side=BOTTOM,pady=10,padx=100)
    top.mainloop()
    base.commit()
    base.close()
def sports(s):
    j=1
    k=0
    base=sqlite3.connect("playgrounds.db")
    ab=str('select * from playgrounds where sports="%s"'%s)
    a=base.execute(ab)
    result=a.fetchall()
    l=len(result)
    print(l)
    top=Toplevel()
    top.geometry()
    l1=Label(top,text=s+ " Playgrounds",justify=CENTER,font=("Brush Script MT",20))
    l1.grid(row=0,column=1,sticky="ns")
    for i in range(1,(l+1)):
        frame = Frame(top, bg="cyan",highlightbackground="green",highlightthickness=5,width=700,height=700)
        frame.grid(row=j,column=k,padx=20,pady=20)
        k=k+1
        if(i%3==0):
            j=j+1
            k=0
        l2=Label(frame,text=result[i-1][1],width=33)
        l2.pack(padx=20)
        width = 200
        height = 70
        img = Image.open(str(result[i-1][7])+".png")
        img = img.resize((width,height))
        photoImg =  ImageTk.PhotoImage(img)
        b = Label(frame,image=photoImg,width=100)
        b.pack(pady=5)
        l3=Label(frame,text="Price : ₹"+str(result[i-1][8]))
        l3.pack(side=LEFT)
        button=Button(frame,text="Book")
        button.pack(side=BOTTOM,pady=10,padx=100)
    top.mainloop()
    base.commit()
    base.close()
