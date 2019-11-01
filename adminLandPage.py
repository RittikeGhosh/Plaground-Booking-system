import tkinter as tk
import time
import addPlayground 

## class for admin land page
class main:
    def __init__(self,root):
        self.root = root
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
        
        # self.dashboard()
        self.playgrounds()
        
    def dashboard(self):
        print('dashboard active')
        self.contentCanvas.destroy()
        contentCanvas = tk.Canvas(self.contentFrame, bg='#fff')
        contentCanvas.place(relheight=1, relwidth=1)
        self.contentCanvas = contentCanvas
        label = tk.Label(self.contentCanvas,text = 'Dashboard', font = ('Consolas',20))
        label.place(relwidth=0.5, relheight=0.4,rely=0.3, relx=0.5, anchor='n')

        #frame for adding graph
        # frame1 = tk.Frame(contentCanvas, bg='red')
        # frame1.place(relwidth=0.8, relheight=0.4, relx=0.1, y = 50)

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

        #heading for the playground page
        heading = tk.Label(contentCanvas,text = ' PLAYGROUND LIST',
            font = ('Consolas', 20), fg = 'brown',bg = '#fff',anchor = 'w')
        heading.pack(fill = 'x',pady = 30)
        #underline for the headline 
        contentCanvas.create_line(15 ,70, 400, 70, width = '3',fill="#888")

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

        addButton = tk.Button(listFrame, text='ADD PLAYGROUND',
            font=('Consolas', 20),height = 2,relief='raise', cursor = 'hand2',
            command=lambda: addPlayground.main(self.root), bg='#75E5EE')
        # label.place(relwidth=0.5, relheight=0.4,rely=0.3, relx=0.5, anchor='n')
        addButton.pack(fill='x', expand=1, padx=200, pady=10)
        
        for i in range(10):
            box = tk.Frame(listFrame,bg = '#eee')
            box.pack(fill = 'x',expand = 1,padx = 10, pady = 10,ipady = 50)
            imageBox = tk.Frame(box,bg = 'pink',width = 200)
            imageBox.pack(side = 'left', fill = 'y')

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
