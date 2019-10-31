import tkinter as tk
import time

## class for admin land page
class main:
    def __init__(self,root):
        self.root = root
        canvas = tk.Canvas(root,bg = '#eee')
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
        contentFrame = tk.Frame(canvas,bg = '#eee')
        contentFrame.pack(side = 'right',fill = 'both',expand = 'true')
        self.contentFrame = contentFrame

        #content canvas
        contentCanvas = tk.Canvas(self.contentFrame, bg='#fff')
        contentCanvas.place(relheight=1, relwidth=1)
        self.contentCanvas = contentCanvas
        
        # self.dashboard()
        self.playgrounds()

    def dashboard(self):
        print('dashboard active')
        self.contentCanvas.destroy()
        contentCanvas = tk.Canvas(self.contentFrame, bg='#fff')
        contentCanvas.place(relheight=1, relwidth=1)
        self.contentCanvas = contentCanvas
        # label = tk.Label(self.contentCanvas,text = 'Dashboard', font = ('Consolas',20))
        # label.place(relwidth=0.5, relheight=0.4,rely=0.3, relx=0.5, anchor='n')

        #frame for adding graph
        frame1 = tk.Frame(contentCanvas, bg='red')
        frame1.place(relwidth=0.8, relheight=0.4, relx=0.1, y = 50)

    def transactions(self):
        print('transaction active')
        self.contentCanvas.destroy()
        contentCanvas = tk.Canvas(self.contentFrame, bg='#fff')
        contentCanvas.place(relheight=1, relwidth=1)
        self.contentCanvas = contentCanvas
        label = tk.Label(self.contentCanvas,text = 'Transaction', font = ('Consolas',20))
        label.place(relwidth = 0.5,relheight = 0.4,rely = 0.3,relx = 0.5,anchor = 'n')

    def playgrounds(self):
        print('playground active')
        self.contentCanvas.destroy()
        contentCanvas = tk.Canvas(self.contentFrame, bg='#fff')
        contentCanvas.place(relheight=1, relwidth=1)
        self.contentCanvas = contentCanvas
        # label = tk.Label(self.contentCanvas, text='PLAYGROUNGS',font=('Consolas', 20))
        # label.place(relwidth=0.5, relheight=0.4,rely=0.3, relx=0.5, anchor='n')
        heading = tk.Label(contentCanvas,text = ' PLAYGROUND LIST',
            font = ('Consolas', 20), fg = 'brown',bg = '#fff',anchor = 'w')
        # heading.place(height = 20,y = 50)
        heading.pack(fill = 'x',pady = 30)
        contentCanvas.create_line(15 ,70, 400, 70, width = '3',fill="#888")
        listFrame = tk.Canvas(contentCanvas,bg = '#fff')
        listFrame.pack(side = 'left',expand = 1 ,fill = 'both')

        for i in range(20):
            box = tk.Frame(listFrame,bg = '#eee')
            box.pack(fill = 'x',expand = 1,padx = 10, pady = 10,ipady = 10)
            imageBox = tk.Frame(box,bg = 'pink',width = 200)
            imageBox.pack(side = 'left', fill = 'y')

        # for i in range(500):
        #     label = tk.Label(listFrame,text = f'text {i}',bg = 'red')
        #     label.pack(fill = 'x',pady = 20)
        
        scrollbar = tk.Scrollbar(contentCanvas,orient = 'vertical',command = listFrame.yview)
        scrollbar.pack(side = 'right' , fill = 'y')
        listFrame.config(yscrollcommand = scrollbar.set)
        
root = tk.Tk()
root.geometry('1400x1000+200+20')
root.title('OnlinePlaygroundBookingSystem')
# root.overrideredirect(True)
#for quitting
quit = tk.Button(root, bg='#FF3625', cursor='hand2',
                    text='X', command=root.quit)
quit.place(relx = 1,anchor = 'ne',width = 70,height = 45)
# titleBar = tk.
o = main(root)

print('hello')
root.mainloop()

# root = Tk()
# def move_window(event):
#     root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

# root.overrideredirect(True) # turns off title bar, geometry
# root.geometry('400x100+200+200') # set new geometry

# # make a frame for the title bar
# title_bar = Frame(root, bg='white', relief='raised', bd=2)

# # put a close button on the title bar
# close_button = Button(title_bar, text='X', command=root.destroy)

# # a canvas for the main area of the window
# window = Canvas(root, bg='black')

# # pack the widgets
# title_bar.pack(expand=1, fill=X)
# close_button.pack(side=RIGHT)
# window.pack(expand=1, fill=BOTH)

# # bind title bar motion to the move window function
# title_bar.bind('<B1-Motion>', move_window)

# root.mainloop()
