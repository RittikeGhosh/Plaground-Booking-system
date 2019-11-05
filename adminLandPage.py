import tkinter as tk
import time
import addPlayground 
from PIL import Image, ImageTk
import sqlite3


## class for admin land page
class main:
    def __init__(self,root):
        self.root = root
        root.title('Admin Page')
        root.geometry('1400x800+250+50')
        canvas = tk.Canvas(root,bg = '#fff')
        canvas.place(relwidth = 1,relheight = 1)
        self.canvas = canvas
        
        #for the title...]
        topHeading = tk.Label(canvas, text='ADMIN PORTAL', font=(
            'Small Fonts', 25, 'bold'), fg='#4E0689', bg='#fff', justify='left')
        topHeading.pack(side = 'top',fill = 'x')

        #navbar for the admin page 
        navbar = tk.Frame(canvas, bg='#C70039', width=200)
        navbar.pack(side = 'left', fill = 'y')
        self.navbar = navbar

        #navbar elements
        link1 = tk.Button(navbar, text='DASHBOARD', font=(' ', 14,), bd='2',
            relief='ridge', cursor='hand2',command = self.dashboard)
        link1.place(y = 100,relwidth = 0.94,anchor = 'n',relx = 0.5,height = 40)
        link2 = tk.Button(navbar, text='TRANSACTIONS', font=(' ', 14), bd='2',
            relief='ridge', cursor='hand2', command = self.transactions)
        link2.place(y = 160,relwidth = 0.94,anchor = 'n',relx = 0.5,height = 40)
        link3 = tk.Button(navbar, text='PLAYGROUNDS', font=(' ', 14), bd='2',
            relief='ridge', cursor='hand2', command = self.playgrounds)
        link3.place(y = 220,relwidth = 0.94, anchor='n',relx = 0.5, height = 50)

        #content frame 
        contentFrame = tk.Frame(canvas,bg = '#fff')
        contentFrame.pack(side = 'right',fill = 'both',expand = 'true')
        self.contentFrame = contentFrame

        #content canvas
        contentCanvas = tk.Canvas(self.contentFrame, bg='#fff')
        contentCanvas.place(relheight=1, relwidth=1)
        self.contentCanvas = contentCanvas
        
        self.dashboard()
    
    #dashboasrd feature coming soon :-)
    def dashboard(self):
        print('dashboard active')
        self.contentCanvas.destroy()
        contentCanvas = tk.Canvas(self.contentFrame, bg='#fff')
        contentCanvas.place(relheight=1, relwidth=1)
        self.contentCanvas = contentCanvas
        label = tk.Label(self.contentCanvas,text = 'Dashboard\nFeature Coming Soon...', font = ('Consolas',20))
        label.place(relwidth=0.5, relheight=0.4,rely=0.3, relx=0.5, anchor='n')

    #dashboasrd feature coming soon :-)
    def transactions(self):
        print('transaction active')
        self.contentCanvas.destroy()
        contentCanvas = tk.Canvas(self.contentFrame, bg='#fff')
        contentCanvas.place(relheight=1, relwidth=1)
        self.contentCanvas = contentCanvas
        label = tk.Label(
            self.contentCanvas, text='Transaction\nFeature Coming Soon...', font=('Consolas', 20))
        label.place(relwidth = 0.5,relheight = 0.4,rely = 0.3,relx = 0.5,anchor = 'n')

    def playgrounds(self):

        #db fetching 
        conn = sqlite3.connect('playgrounds.db')
        a = conn.execute('select * from playgrounds')
        l = a.fetchall()
        # print(l)
        conn.close()

        print('playground active')
        self.contentCanvas.destroy()
        contentCanvas = tk.Canvas(self.contentFrame, bg='#fff')
        contentCanvas.place(relheight=1, relwidth=1)
        self.contentCanvas = contentCanvas

        #heading for the playground page
        heading = tk.Label(contentCanvas,text = ' PLAYGROUND LIST',
            font = ('Consolas', 20), fg = 'brown',bg = '#fff',anchor = 'w')
        heading.pack(fill = 'x',pady = 30)
        #underline for the headline 
        contentCanvas.create_line(15 ,70, 400, 70, width = '3',fill="#888")

        addButton = tk.Button(contentCanvas, text='ADD PLAYGROUND',
            font=('Consolas', 20),height = 1,relief='raise', cursor = 'hand2',
            command=lambda: addPlayground.main(self.root), bg='#8AEC9B', bd=8)
        addButton.pack(fill='x',padx = 400,pady =10)

        frame = tk.Frame(contentCanvas,bg = '#fff')
        frame.pack(side = 'left',fill = 'both', expand = 1)
        canvas = tk.Canvas(frame,bg = '#fff')
        listFrame = tk.Frame(canvas,bg = '#fff')
        yscrollbar = tk.Scrollbar(frame, command = canvas.yview)
        canvas.config(yscrollcommand = yscrollbar.set)
        yscrollbar.pack(side = 'right',fill = 'y')
        canvas.pack(side = 'left',fill = 'both',expand = 1)
        canvas.update()
        canvas.create_window((0,0),window=listFrame, anchor='nw',width = canvas.winfo_width())
        listFrame.bind("<Configure>", lambda event: canvas.config(scrollregion=canvas.bbox("all")))
        
        for i in range(len(l)):
            box = tk.Frame(listFrame,bg = '#eee',bd= 1 ,relief = 'raise')
            idBox = tk.Frame(box,width = 100,bg='pink')
            idBox.pack(side = 'left', fill = 'y')
            label = tk.Label(idBox, text = f'#{l[i][0]}', font=(' ', 15, 'bold'), fg='#fff', bg='#83348B')
            label.place(relheight = 1,relwidth = 1)

            #field details frame
            fieldDetails = tk.Frame(box,bg = '#eee')           
            tk.Label(fieldDetails,text=l[i][1], anchor = 'w',
                font=(' ',14,'italic')).pack(side = 'top', fill='x')
            dtlsContainer = tk.Frame(fieldDetails)
            dtlsContainer.pack(fill = 'x',side = 'top')
            tk.Label(dtlsContainer,text=f'SPORT : {l[i][6]}',
                font=(' ',12)).pack(side = 'left')
            tk.Label(dtlsContainer, text=f'DIMENSION : {l[i][2]}',
                font=(' ', 12)).pack(side='left', padx=20)
            tk.Label(dtlsContainer, text=f'CAPACITY : {l[i][4]}',
                font=(' ', 12)).pack(side='left', padx=20)
            tk.Label(dtlsContainer, text=f'LOCATION : {l[i][3]}',
                font=(' ', 12)).pack(side='left', padx=20)
            tk.Label(fieldDetails,text=f'Rate per day : {l[i][8]}', font=(' ',12)).pack(side ='left')
            #field alteration button
            update = tk.Button(box, text='UPDATE', bg='#000', fg='#fff', font=(' ', 10, 'bold'))
            update.place(relx = 0.99,rely= 0.05,width = 70,height = 40,anchor = 'ne')
            update.bind('<ButtonRelease-1>', lambda e: self.update(e))
            remove = tk.Button(box, text='REMOVE', bg='red', fg='#fff',font=(' ', 10,'bold'))
            remove.place(relx = 0.99,rely =0.95,width = 70,height = 40,anchor = 'se')
            remove.bind('<ButtonRelease-1>',lambda event: self.remove(event))
            fieldDetails.pack(side='left',fill ='x',padx = 20)
            #for storing id 
            id = tk.Label(remove,text = l[i][0])
            id.place(relx = -1)
            box.pack(fill = 'x',expand = 1,padx = 10, pady = 10,ipady = 10)
            id = tk.Label(update,text = l[i][0])
            id.place(relx = -1)
            box.pack(fill = 'x',expand = 1,padx = 30, pady = 10,ipady = 10)

    #update table
    def update(self,e):
        id = e.widget.winfo_children()[0].cget('text')
        # print(id)
        addPlayground.main(self.root, int(id))

    def remove(self,e):
        # print(e.widget.winfo_children()[0].cget('text'))
        passConfirm = tk.Toplevel(self.contentCanvas)
        # top.overrideredirect('true')
        passConfirm.maxsize(300,150)
        passConfirm.transient(self.root)
        self.passConfirm = passConfirm
        passConfirm.geometry('300x150+400+400')
        password = tk.StringVar()
        label = tk.Label(passConfirm,text = 'Enter the password : ',anchor = 'w',font = (' ',14,'italic'))
        label.pack(side = 'top',fill = 'x',padx = 10,pady = 5)
        password= tk.Entry(passConfirm,show = '*',font = (' ',16,'bold'),justify = 'center',textvariable = password)
        password.pack(side = 'top',fill = 'x',padx = 10,pady = 5)
        confirm = tk.Button(passConfirm,text = 'Confirm',font = (' ',14),command = lambda: self.delete(e,password))
        confirm.pack(side = 'top',pady = 10) 
    #delete row from the table 
    def delete(self,e,password):
        id = e.widget.winfo_children()[0].cget('text')
        if(password.get() == 'admin'):

            #db fetching
            conn = sqlite3.connect('playgrounds.db')
            conn.execute(f'delete from playgrounds where f_id = {id}')
            conn.commit()
            conn.close()

            print(f'{password.get()} item with id {id} deleted .')
            self.passConfirm.withdraw()
            self.playgrounds()
        else:
            print('the password is incorrect')

# root = tk.Tk()
# root.geometry('1000x1000+200+20')
# root.title('OnlinePlaygroundBookingSystem')
# o = main(root)
# print('hello')
# root.mainloop()
