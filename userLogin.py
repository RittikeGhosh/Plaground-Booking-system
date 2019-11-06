import Search_feature as sf
import sqlite3
import adminLogin as al
from tkinter import *
from tkinter import messagebox
import mail 
#details=[[1,"resham","9304619889","20","jamshedpur","resham.chaney1099@gmail.com","abc"],[2,"harsha","7209534724","24","jamshedpur","harshachaney95@gmail.com","xyz"]]

details = []
c = 2
window = Tk()
window.title("log in/sign up")
window.geometry("600x400")


def signup():
    reg = Toplevel(window)
    reg.title("sign up")
    reg.geometry("1000x1000")
    frame = Frame(reg, width=600, height=600, bg="pink", padx=100, pady=50)
    frame.pack()

    def verify():  # called on clicking register button
        f1 = f2 = f3 = f4 = f5 = f35 = 0
        l = []
        tag1 = Message(frame, text="", bg="pink", width=100)
        tag1.grid(row=4, column=2)
        tag2 = Message(frame, text="", bg="pink", width=100)
        tag2.grid(row=6, column=2)
        tag3 = Message(frame, text="", bg="pink", width=100)
        tag3.grid(row=8, column=2)
        tag35 = Message(frame, text="", bg="pink", width=100)
        tag35.grid(row=10, column=2)
        tag4 = Message(frame, text="", bg="pink", width=100)
        tag4.grid(row=12, column=2)
        tag5 = Message(frame, text="", bg="pink", width=100)
        tag5.grid(row=15, column=2)

        #name
        s = en1.get()
        if (s.isalpha() or " " in s):
            f1 = 1
        else:
             tag1.config(text="Invalid name")
        #phone no
        if (en2.get().isdigit() and len(en2.get()) == 10):
            f2 = 1
        else:
            tag2.config(text="Invalid phone number")
        #age
        if (not (en3.get().isdigit())):
            tag3.config(text="Invalid age")
        elif int(en3.get()) > 120:
            tag3.config(text="Invalid age")
        else:
            f3 = 1
        #city
        if en4.get().isalpha():
            f35 = 1
        else:
             tag35.config(text="Invalid city")
        #email id
        s = en5.get()
        if("@" in en5.get() and "." in en5.get()):
            if(s[0] != "@" and s[0] != "." and s[len(s)-1] != "@" and s[len(s)-1] != "." and " " not in s):
                if((s.find("@")+1) != s.find(".") or (s.find(".")+1) != s.find("@")):
                    f4 = 1
                else:
                    tag4.config(text="Invalid email id")
            else:
                tag4.config(text="Invalid email id")
        else:
            tag4.config(text="Invalid email id")
        #password cofirmation
        if(en6.get() == "" or en7.get() == ""):
            tag5.config(text="Enter both the fields")
        elif(en6.get() == en7.get()):
            f5 = 1
        else:
            tag5.config(text="Password does not match")

        #to remove the labels if the value is corrected
        if(f1 == 1):
            print("entered")
            tag1.config(text="                 ", bg="pink")
        if(f2 == 1):
            tag2.config(text="                             ", bg="pink")
        if(f3 == 1):
            tag3.config(text="                             ", bg="pink")
        if(f35 == 1):
            tag35.config(text="                             ", bg="pink")
        if(f4 == 1):
            tag4.config(text="                             ", bg="pink")
        if(f5 == 1):
            tag5.config(text="                             ", bg="pink")

        # if all the fiels are correct send otp verification to admin
        if f1 == 1 and f2 == 1 and f3 == 1 and f35 == 1 and f4 == 1 and f5 == 1:
            # n = str(123456)  # arbitrary value for checking the working
            n= mail.sendMail(en5.get()) #admin function call
            print("in the email confirmation")
            email = Toplevel(reg)  # email confirmation window
            email.title("email confirmation")
            email.geometry("800x500")
            frame1 = Frame(email, height=400, width=800,
                           bg="grey", padx=50, pady=50)
            frame1.pack()
            m = Message(
                frame1, text="You have recieved a confirmation mail. Please enter the OTP below to confirm the email id.", width=600)
            m.grid(row=1, columnspan=4, column=1)
            sp1 = Label(frame, bg="grey")
            sp1.grid(row=2)

            def success():  # when signup is successful it is added to the list which could further be updated in the database
                if(entry.get() == n):
                    global c
                    c = c+1
                    database = sqlite3.connect("playgrounds.db")
                    #l.append(c)
                    l.append(en1.get())
                    l.append(en2.get())
                    l.append(en3.get())
                    l.append(en4.get())
                    l.append(en5.get())
                    l.append(en6.get())
                    print(l)
                    details.append(l)
                    print(details)
                    database.execute(
                        "insert into user_details values (?,?,?,?,?,?)", l)
                    database.commit()
                    database.close()
                    messagebox.showinfo(
                        "Information", "Congratualtions! You have successfully resgistered....!!!")
            label = Label(frame1, text="Enter the OTP : ")
            label.grid(row=3, column=3)
            otp = StringVar()
            entry = Entry(frame1, textvariable=otp)
            entry.grid(row=3, column=4)
            sp1 = Label(frame, bg="yellow")
            sp1.grid(row=4)
            submit = Button(frame1, text="submit", bg="green",
                            fg="white", command=success)
            submit.grid(row=5, columnspan=4, column=4)

    head = Label(frame, text="SIGN UP", bg="pink")
    head.config(font=("Times new roman", 44))
    head.grid(row=1, columnspan=2, column=1)
    sp1 = Label(frame, text="   ", bg="pink")
    sp1.grid(row=2)

    lab1 = Label(frame, text="Full Name : ", bg="pink", justify=RIGHT)
    name = StringVar()
    en1 = Entry(frame, textvariable=name)
    lab1.grid(row=3, column=1)
    en1.grid(row=3, column=2)

    lab2 = Label(frame, text="Phone Number : ", bg="pink", justify=RIGHT)
    phone = StringVar()
    en2 = Entry(frame, textvariable=phone)
    lab2.grid(row=5, column=1)
    en2.grid(row=5, column=2)

    lab3 = Label(frame, text="Age : ", bg="pink", justify=RIGHT)
    age = StringVar()
    en3 = Entry(frame, textvariable=age)
    lab3.grid(row=7, column=1)
    en3.grid(row=7, column=2)

    lab4 = Label(frame, text="City : ", bg="pink", justify=RIGHT)
    city = StringVar()
    en4 = Entry(frame, textvariable=city)
    lab4.grid(row=9, column=1)
    en4.grid(row=9, column=2)

    lab5 = Label(frame, text="Email Id : ", bg="pink", justify=RIGHT)
    email = StringVar()
    en5 = Entry(frame, textvariable=email)
    lab5.grid(row=11, column=1)
    en5.grid(row=11, column=2)

    lab6 = Label(frame, text="Password : ", bg="pink", justify=RIGHT)
    password = StringVar()
    en6 = Entry(frame, textvariable=password, show="*")
    lab6.grid(row=13, column=1)
    en6.grid(row=13, column=2)

    lab7 = Label(frame, text="Confirm Password : ", bg="pink", justify=RIGHT)
    confirm = StringVar()
    en7 = Entry(frame, textvariable=confirm, show="*")
    lab7.grid(row=14, column=1)
    en7.grid(row=14, column=2)

    sp1 = Label(frame, bg="pink")
    sp1.grid(row=16)

    register = Button(frame, text="RESGISTER", bg="red",
                      fg="white", command=verify)
    register.grid(row=17, columnspan=2, column=1)

    #reg.mainloop()


def login():
    f = 0
    database = sqlite3.connect("playgrounds.db")
    if(e1.get() == ""):
        messagebox.showinfo("Information", "Please enter username....!!!")
    else:
        em = database.execute("select * from user_details")
        x = em.fetchall()
        for i in x:
            if i[4] == e1.get():
                if(e2.get() == ""):
                    messagebox.showwarning(
                        "Warning", "Please enter password....!!!")
                elif(e2.get() == i[5]):
                    messagebox.showinfo(
                        "Information", "You have successfully logged in....!!!")
                    sf.search_page(e1.get())
                else:
                    messagebox.showwarning(
                        "Warning", "You have entered the wrong password or this username does not exist!!!")
    database.commit()
    database.close()
    #for i in details:
    #if(e1.get()==i[5]):
    #f=1
    #if(e2.get()==""):
    #messagebox.showwarning("Warning","Please enter password....!!!")
    #elif(e2.get()==i[6]):
    #messagebox.showinfo("Information","You have successfully logged in....!!!")
    #sf.search_page(e1.get())
    #else:
    #messagebox.showwarning("Warning","You have entered the wrong password....!!!")
#if(f==0):
    #messagebox.showinfo("Information","This username does not exist!You need to Sign up....!!!")


def adminlogin():  # called on clickin the admin login button. To be edited by the admin page creator
    al.main(window)


frame = Frame(window, width=600, height=600, bg="yellow", padx=100, pady=50)
frame.pack()

head = Label(frame, text="LOG IN", bg="yellow")
admin = Button(frame, bg="black", fg="white", text="ADMIN LOGIN",
               anchor="e", command=adminlogin)
admin.grid(row=10, column=3)
head.config(font=("Times new roman", 44))

sp1 = Label(frame, bg="yellow")
sp1.grid(row=3)

lb1 = Label(frame, text="User Name : ", bg="yellow")
username = StringVar()
e1 = Entry(frame, textvariable=username)
head.grid(row=2, columnspan=2, column=1)
lb1.grid(row=4, column=1)
e1.grid(row=4, column=2)

lb2 = Label(frame, text="Password : ", bg="yellow")
password = StringVar()
e2 = Entry(frame, textvariable=password, show="*")
lb2.grid(row=5, column=1)
e2.grid(row=5, column=2)

sp1 = Label(frame, bg="yellow")
sp1.grid(row=6)

log = Button(frame, bg="green", fg="white", text="LOG IN", command=login)
log.grid(row=7, columnspan=2, column=1)

sp1 = Label(frame, bg="yellow")
sp1.grid(row=8)
sp1 = Label(frame, bg="yellow")
sp1.grid(row=9)

#lb3=Label(frame,text="                New user ? ",bg="yellow",anchor="e")
sign = Button(frame, bg="black", fg="white",
              text="SIGN UP", anchor="w", command=signup)
#lb3.grid(row=9,column=3)
sign.grid(row=10, column=4)

window.mainloop()
