import tkinter as tk
import time
import adminLandPage as alp
from PIL import Image, ImageTk


class main:
    def __init__(self,mainRoot):
        self.cred = {'admin':'admin'}
        root = tk.Toplevel(mainRoot)
        root.geometry('1400x800+250+50')
        root.title('Admin Login')
        self.root = root

        #canvas as super window
        canvas = tk.Canvas(root, bd='0',bg = 'blue')
        canvas.place(relheight=1, relwidth=1)
        self.canvas = canvas

        # placing a background image
        image = Image.open('./images/stadium.jpg')
        background_image = ImageTk.PhotoImage(image)
        background_label = tk.Label(canvas, image=background_image)
        background_label.image = background_image
        background_label.place(relheight= 1, relwidth = 1)

        # to arrage the widgets  #0a9ead
        # shadowFrame = tk.Frame(canvas, bg='#888', height='200', width='300')
        # shadowFrame.place(relx=0.505, rely=0.305,width=300, height=300, anchor='n')
        frame = tk.Frame(canvas, bg='#fff', height='200', width='300',relief='sunken',bd = 5)
        frame.place(relx=0.5, rely=0.3, width=300, height=300, anchor='n')
        # self.shadowFrame = shadowFrame
        self.frame = frame

        #frame heading  #1f4191
        labelHead = tk.Label(frame, text='ADMIN', bg='#1f4191', fg="#fff", font=("Courier", 24))
        labelHead.pack(fill='x')
        self.labelHead = labelHead

        #label of fails
        failLabel = tk.Label(frame, text='Enter Your Credentials',bg ='#fff')
        failLabel.config(font=("Courier", 12,'bold'))
        failLabel.pack(fill='x')
        self.failLabel = failLabel

        # placing text box and label for username
        adminUserName = tk.Entry(frame, bg="#ffffff", justify='center')
        adminPassword = tk.Entry(frame, bg="#ffffff", justify='center', show='*')
        self.adminUserName = adminUserName
        self.adminPassword = adminPassword
        
        adminUserName.config(font=("Courier", 18))
        adminUserName.insert(0, 'Username')
        # adminUserName.bind('<ButtonRelease>',self.clear)
        adminUserName.bind('<Return>', lambda event: self.loginFunc())
        adminUserName.bind('<FocusIn>',self.clear)
        adminUserName.place(relx=0.05, rely=0.3, relwidth=0.9, height=40)

        adminPassword.config(font=("Courier", 18))
        adminPassword.insert(0, 'Password')
        # adminPassword.bind('<ButtonRelease>', self.clear)
        adminPassword.bind('<Return>', lambda event: self.loginFunc())
        adminPassword.bind('<FocusIn>',self.clear)
        adminPassword.place(relx=0.05, rely=0.5, relwidth=0.9, height=40)

        # button for login   #ff1900
        loginButton = tk.Button(frame, text='LOGIN', cursor='hand2',width='50', bg='#ff1900', fg='#fff', command=self.loginFunc)
        loginButton.config(font=("Courier", 16))
        loginButton.place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.1)

    # Function for login verification ...
    def loginFunc(self):
        username = self.adminUserName.get()
        password = self.adminPassword.get()

        # print('data is :', username, ' ', password)
        if(username == '' or password == ''):
            # print('Empty field')
            self.failLabel.config(text='Fields cannot be empty', fg='red')
        else:
            # if(username == 'admin' and password == 'admin'):
            if(username in self.cred.keys() and self.cred[username] == password):
                print('SUccefully Logged in')
                self.failLabel.config(text='Successfully Logged in ...',fg='green')
                # time.sleep()
                self.clearWin()
            else:
                print('Invalid credential')
                self.failLabel.config(text='Wrong Credentials !', fg='red')
                self.adminUserName.delete(0, len(username))
                self.adminPassword.delete(0, len(password))

    # to clear the fields before user input
    def clear(self,event):
        # print('....',event.type)
        event.widget.delete(0, len(event.widget.get()))
        event.widget.config(bd=5)

    #function to clear the window
    def clearWin(self):
        self.root.update()
        time.sleep(0.8)
        # print('all clear')
        winWidth = self.canvas.winfo_width()
        dur = 1
        sub = dur/winWidth
        i = winWidth
        while(i >= 0):
            i = i/1.1 - 1
            self.canvas.place(x=i, anchor='ne')
            self.root.update()
            time.sleep(sub)
        self.canvas.place(relx=-1)
        alp.main(self.root)

