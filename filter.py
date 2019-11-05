from tkinter import *
import project as py
from numpy import *
from pandas import *
import sqlite3
from PIL import Image, ImageTk
s="Jalandhar"
def filter():
    top=Tk()
    top.geometry("1000x1000")
    l1=Label(top,text="WELCOME TO ONLINE PLAYGOUND BOOKING SYSTEM",justify=CENTER,font=("High Tower Text",20))
    l1.place(relx=0.23,rely=0.1)
    C = Canvas(top,width=1500)
    line=C.create_line(0,4,1500,4, fill="orange")
    C.place(rely=0.15)
    l2=Label(top,text="PLAYGROUNDS IN CITIES : SELECT ANY ONE TO SEE",justify=LEFT)
    l2.place(rely=0.2,relx=0.05)
    B1 =Button(top, text ="JALANDHAR",cursor = "heart",bd="6",command=lambda:py.city("Jalandhar"))
    B2 =Button(top, text ="DELHI",cursor = "heart",bd="6",command=lambda:py.city("Delhi"))
    B3 =Button(top, text ="MUMBAI",cursor = "heart" ,bd="6",command=lambda:py.city("Mumbai"))
    B1.place(relx=0.1,rely=0.25)
    B2.place(relx=0.2,rely=0.25)
    B3.place(relx=0.3,rely=0.25)
    l2=Label(top,text="PLAYGROUNDS OF DIFFERENT SPORTS: SELECT ANY ONE TO SEE",justify=LEFT)
    l2.place(rely=0.4,relx=0.05)
    B1 =Button(top, text ="Cricket",cursor = "heart",bd="6",command=lambda:py.sports("Cricket"))
    B2 =Button(top, text ="Badminton",cursor = "heart",bd="6",command=lambda:py.sports("Badminton"))
    B3 =Button(top, text ="BasketBall",cursor = "heart" ,bd="6",command=lambda:py.sports("BasketBall"))
    B1.place(relx=0.1,rely=0.45)
    B2.place(relx=0.2,rely=0.45)
    
    B3.place(relx=0.3,rely=0.45)
    top.mainloop()
filter()
