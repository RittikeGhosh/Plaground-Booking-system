from tkinter import *
from numpy import *
from pandas import *
import sqlite3
from PIL import Image, ImageTk
import fieldDetails as fd
import filter1


def city(s,e,win):
    def back():
        top.destroy()
        filter1.filter(email)
    win.destroy()
    email=e
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
    def call(e):
        widget = e.widget.winfo_children()[0].cget("text")
        print(widget)
        fd.call_description(email,widget)
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
        img = Image.open(result[i-1][7])
        img = img.resize((width,height))
        photoImg =  ImageTk.PhotoImage(img)
        b = Label(frame,image=photoImg,width=200)
        b.Image=photoImg
        b.pack(pady=5)
        l3=Label(frame,text="Price : ₹"+str(result[i-1][8]))
        l3.pack(side=LEFT)
        l4=Label(frame,text="SPORTS : "+str(result[i-1][6]))
        l4.pack(side=RIGHT,pady=5)
        button=Button(frame,text="Book")
        button.bind('<Button-1>',lambda e : call(e))
        label=Label(button,text=int(result[i-1][0]))
        button.pack(side=BOTTOM,pady=10,padx=100)
    back = Button(top,text = 'Back',command = back,bg = 'orange', fg = '#fff',font = (' ',16))
    back.place(relx = 0, rely = 0, anchor = 'nw',width = 100, height = 50)
    top.mainloop()
    base.commit()
    base.close()

def sports(s,e,win):
    def back():
        top.destroy()
        filter1.filter(email)
    win.destroy()
    email=e
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
    def call(e):
        widget = e.widget.winfo_children()[0].cget("text")
        print(widget)
        fd.call_description(email,widget)
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
        img = Image.open(result[i-1][7])
        img = img.resize((width,height))
        photoImg =  ImageTk.PhotoImage(img)
        b = Label(frame,image=photoImg,width=200)
        b.image = photoImg
        b.pack(pady=5)
        l3=Label(frame,text="Price : ₹"+str(result[i-1][8]))
        l3.pack(side=LEFT)
        l4=Label(frame,text="CITY : "+str(result[i-1][3]))
        l4.pack(side=RIGHT,pady=5)
        button=Button(frame,text="Book")
        button.bind('<Button-1>',lambda e : call(e))
        label=Label(button,text=int(result[i-1][0]))
        button.pack(side=BOTTOM,pady=10,padx=100)
    back = Button(top,text = 'Back',command = back,bg = 'orange', fg = '#fff',font = (' ',16))
    back.place(relx = 0, rely = 0, anchor = 'nw',width = 100, height = 50)

    top.mainloop()
    base.commit()
    base.close()
