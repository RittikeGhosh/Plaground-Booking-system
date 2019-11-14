from tkinter import *
import project1 as py
from numpy import *
from pandas import *
import sqlite3
from PIL import Image, ImageTk
def filter(es):
    # if(win):
    #     win.destroy()
    j=0
    k=0
    m=0
    email=es
    count=0
    B1=list()
    B2=list()
    base=sqlite3.connect("playgrounds.db")
    a=str('select distinct(location) from playgrounds')
    b=str('select distinct(sports) from playgrounds')
    a1=base.execute(a)
    b1=base.execute(b)
    r1=a1.fetchall()
    r2=b1.fetchall()
    le1=len(r1)
    le2=len(r2)
    print(r1)
    # top=Tk()
    top = Toplevel()
    top.geometry("1000x800")
    l1=Label(top,text="WELCOME TO ONLINE PLAYGOUND BOOKING SYSTEM",justify=CENTER,font=("High Tower Text",20))
    l1.place(relx=0.23,rely=0.1)
    C = Canvas(top,width=1500)
    line=C.create_line(0,4,1500,4, fill="orange")
    C.place(rely=0.15)
    l2=Label(top,text="PLAYGROUNDS IN CITIES : SELECT ANY ONE TO SEE",justify=LEFT)
    l2.place(rely=0.2,relx=0.05)
    def sendCity(e):
        widget = e.widget.winfo_children()[0].cget('text')
        py.city(widget,email,top)        
    def sendSport(e):
        widget = e.widget.winfo_children()[0].cget('text')
        py.sports(widget,email,top)

    for i in range(le1):
        b2 =  Button(top, text =r1[i][0],cursor = "heart",bd="6")
        b2.bind('<Button-1>',lambda e : sendCity(e))
        B1.append(b2)
        label = Label(B1[i],text = r1[i][0])
        label.place()
        B1[-1].place(relx=0.3+(j/5),rely=0.25)
        j=j+1
    l2=Label(top,text="PLAYGROUNDS OF DIFFERENT SPORTS: SELECT ANY ONE TO SEE",justify=LEFT)
    l2.place(rely=0.4,relx=0.05)
    for i in range(le2):
        b1 =  Button(top, text =r2[i][0],cursor = "heart",bd="6")
        b1.bind('<Button-1>',lambda e : sendSport(e))
        B2.append(b1)
        label = Label(B2[i],text = r2[i][0])
        label.place()
        B2[-1].place(relx=0.1+(k/5),rely=0.45+m)
        k=k+1
        if(k%3==0):
            k=0
            m=0.08+count
            count=count+0.08
    # top.mainloop()
