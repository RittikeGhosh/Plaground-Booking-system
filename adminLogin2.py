import tkinter as tk

class adminLogin:
    def __init__(self):

        self.cred = {'admin':'admin'}
        root = tk.Tk()

        # to set the window to a fixed height and width
        root.geometry('1000x800')
        root.title('OnlinePlaygroundBookingSystem')
        self.root = root

        #canvas as super window
        canvas = tk.Canvas(root, bd='0', bg='#c7cdff', relief='ridge')
        canvas.place(relheight=1, relwidth=1)
        self.canvas = canvas

        #set backgrounf image ###### not working  ################
        # backgroundImage = tk.PhotoImage(file = './images/stadium.jpg')
        # backgroundImageLabel = tk.Label(root,image = backgroundImage)
        # backgroundImageLabel.place(relheight = 1,relwidth=1)
        # background_image = tk.PhotoImage(file = 'stadium2.png')
        # background_label = tk.Label(root, image=background_image)
        # background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # to arrage the widgets  #0a9ead
        shadowFrame = tk.Frame(canvas, bg='#888', height='200', width='300')
        shadowFrame.place(relx=0.505, rely=0.205,
                        width=300, height=300, anchor='n')
        frame = tk.Frame(canvas, bg='#fff', height='200', width='300')
        frame.place(relx=0.5, rely=0.2, width=300, height=300, anchor='n')
        self.shadowFrame = shadowFrame
        self.frame = frame

        #frame heading  #1f4191
        labelHead = tk.Label(frame, text='ADMIN', bg='#000', fg="#fff")
        labelHead.config(font=("Courier", 24))
        labelHead.pack(fill='x')
        self.labelHead = labelHead

        #label of fails
        failLabel = tk.Label(frame, text='Enter Your Credentials',bg ='#fff')
        failLabel.config(font=("Courier", 12))
        failLabel.pack(fill='x')
        self.failLabel = failLabel

        # placing text box and label for username
        adminUserName = tk.Entry(frame, bg="#ffffff", justify='center', highlightcolor='blue')
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
        adminPassword.bind('<ButtonRelease>', self.clear)
        adminPassword.bind('<Return>', lambda event: self.loginFunc())
        adminPassword.place(relx=0.05, rely=0.5, relwidth=0.9, height=40)

        # button for login   #ff1900
        loginButton = tk.Button(frame, text='LOGIN', cursor='hand2', width='50',bg='#000', fg='#fff', command= self.loginFunc)
        loginButton.config(font=("Courier", 16))
        loginButton.place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.1)

        # clear button
        clearButton = tk.Button(root, text='Clear Window',bg='violet', command= self.clearWin)
        clearButton.pack(side='bottom')
        self.clearButton = clearButton

        #Back to login Page button
        BackToUserLogin = tk.Button(root, text='Back to User Login',bg='orange', command=root.quit)
        BackToUserLogin.config(font = ('Courier',13))
        BackToUserLogin.pack(side='top')

        #test for momving to new window
        newFrame = tk.Frame(root,bg = 'red')
        self.newFrame = newFrame
        root.mainloop()

    # Function for login verification ...
    def loginFunc(self):
        username = self.adminUserName.get()
        password = self.adminPassword.get()

        print('data is :', username, ' ', password)
        if(username == '' or password == ''):
            print('Empty field')
            self.failLabel.config(text='Fields cannot be empty', fg='red')
        else:
            # if(username == 'admin' and password == 'admin'):
            if(username in self.cred.keys() and self.cred[username] == password):
                print('SUccefully Logged in')
                self.failLabel.config(text='Successfully Logged in ...',
                                      fg='green')
            else:
                print('Invalid credential')
                self.failLabel.config(text='Wrong Credentials !', fg='red')
                self.adminUserName.delete(0, len(username))
                self.adminPassword.delete(0, len(password))

    # to clear the fields before user input
    def clear(self,event):
        print('....',event.type)
        event.widget.delete(0, len(event.widget.get()))
        event.widget.config(bd=5)

    #function to clear the window
    def clearWin(self):
        print('all clear')
        self.canvas.destroy()
        self.newFrame.place(relwidth = 1,relheight = 1)

    # def __del__(self):
    #     print('Destructor called')
    #     self.canvas.destroy()

login = adminLogin()


