import tkinter as tk

# Function for login verification ...
def loginFunc(unameObj,passObj,failLabel):
    username = unameObj.get()
    password = passObj.get()

    print('data is :',username,' ',password)
    if(username == '' or password == ''):
        print('Empty field')
        failLabel.config(text='Fields cannot be empty', fg='red')
    else:
        if(username == 'admin' and password == 'admin'):
            print('SUccefully Logged in')
            failLabel.config(text='Successfully Logged in ...',
                            fg='#20b31b')
        else:
            print('Invalid credential')
            failLabel.config(text='Wrong Credentials !', fg='red')
            unameObj.delete(0,len(username))
            passObj.delete(0,len(password))

# to clear the fields before user input
def clear(event):
    print('....')
    event.widget.delete(0,len(event.widget.get()))

#function to clear the window
def clearWin(window):
    print('all clear')
    window.destroy()

# Graphics Development 
def adminLoginGraphics():
    root = tk.Tk()

    # to set the window to a fixed height and width
    root.geometry('1000x800')
    root.title('OnlinePlaygroundBookingSystem')

    canvas = tk.Canvas(root, bd='0', bg='#c7cdff', relief='ridge')
    canvas.place(relheight = 1,relwidth =1)

    #set backgrounf image ###### not working  ################
    # backgroundImage = tk.PhotoImage(file = './images/stadium.jpg')
    # backgroundImageLabel = tk.Label(root,image = backgroundImage)
    # backgroundImageLabel.place(relheight = 1,relwidth=1)
    # background_image = tk.PhotoImage(file = 'stadium2.png')
    # background_label = tk.Label(root, image=background_image)
    # background_label.place(x=0, y=0, relwidth=1, relheight=1)


    # to arrage the widgets
    shadowFrame = tk.Frame(canvas, bg='#888', height='200', width='300')
    shadowFrame.place(relx = 0.505,rely = 0.205,width=300, height=300,anchor = 'n')
    frame = tk.Frame(canvas, bg='#0a9ead', height='200', width='300')
    frame.place(relx = 0.5,rely = 0.2,width=300, height=300,anchor = 'n')

    #frame heading 
    labelHead = tk.Label(frame, text='ADMIN', bg='#1f4191',fg = "#fff")
    labelHead.config(font=("Courier", 24))
    labelHead.pack(fill='x')

    #label of fails
    failLabel = tk.Label(frame,text='Enter Your Credentials')
    failLabel.config(font=("Courier", 12))
    failLabel.pack(fill = 'x')

    # placing text box and label for username 
    adminUserName = tk.Entry(frame,bg ="#ffffff",justify = 'center')
    adminPassword = tk.Entry(frame,bg ="#ffffff", justify = 'center',show ='*')
    
    adminUserName.config(font=("Courier", 18))
    adminUserName.insert(0,'Username')
    adminUserName.bind('<ButtonRelease>',clear)
    adminUserName.bind('<Return>',lambda event : loginFunc(
        adminUserName,adminPassword,failLabel))
    adminUserName.place(relx = 0.05,rely = 0.3,relwidth = 0.9,height = 40)

    adminPassword.config(font=("Courier", 18))
    adminPassword.insert(0,'Password')
    adminPassword.bind('<ButtonRelease>',clear)
    adminPassword.bind('<Return>', lambda event: loginFunc(
        adminUserName, adminPassword, failLabel))
    adminPassword.place(relx = 0.05,rely = 0.5,relwidth = 0.9,height = 40)

    # button for login 
    loginButton = tk.Button(frame, text='LOGIN',cursor='hand2', width='50',
        bg='#ff1900',fg = '#fff',command = lambda: loginFunc(adminUserName,adminPassword,failLabel))
    loginButton.config(font=("Courier", 16))
    loginButton.place(relx = 0.1,rely = 0.8, relwidth=0.8, relheight=0.1)

    #clear button 
    clearButton = tk.Button(root,text = 'Clear Window',bg ='violet',command = lambda:clearWin(canvas))
    clearButton.pack(side = 'bottom')

    #Back to login Page button
    BackToUserLogin = tk.Button(
        root, text='Back to User Login', bg='orange', command=root.quit)
    BackToUserLogin.config(font=('Courier', 13))
    BackToUserLogin.pack(side='top')

    root.mainloop()

adminLoginGraphics()


