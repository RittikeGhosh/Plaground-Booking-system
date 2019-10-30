import tkinter as tk
import time

## class for admin land page
class main:
    def __init__(self,root):
        self.root = root
        canvas = tk.Canvas(root,bg = '#eee')
        canvas.place(relwidth = 1,relheight = 1)
        self.canvas = canvas

        #navbar for the admin page 
        navbar = tk.Frame(canvas, bg='#E08F7E')
        navbar.place(rely = 1,relheight = 1,width = 200,anchor = 'sw')
        self.navbar = navbar

        #navbar elements
        link1 = tk.Button(navbar, text='DASHBOARD', font=('Gabriola', 16, 'bold'), bd='2', relief='ridge', cursor='hand2')
        link1.place(y = 100,relwidth = 0.9,anchor = 'n',relx = 0.5,height = 40)
        # link1.pack(fill = 'x')
        link2 = tk.Button(navbar, text='TRANSACTIONS', font=('Gabriola', 16,'bold'), bd='2', relief='ridge', cursor='hand2')
        link2.place(y = 160,relwidth = 0.9,anchor = 'n',relx = 0.5,height = 40)
        # link2.pack(fill = 'x')
        link3 = tk.Button(navbar, text='PLAYGROUNDS', font=('Gabriola', 16, 'bold'), bd='2', relief='ridge', cursor='hand2')
        link3.place(y=220, relwidth=0.9, anchor='n',relx = 0.5, height = 50)
        # link3.pack(fill = 'x')

        #for the title...]
        topHeading = tk.Label(canvas, text='Online Playground Booking System(ADMIN PORTAL)', font=(
            'Ink Free', 25, 'bold'), fg='#4E0689')
        # topHeading.pack(side = 'top',fill = 'x')
        topHeading.place(relwidth = 1, height = 50)

        # clear button
        clearButton = tk.Button(root, text='Clear Window',bg='violet', command=self.clearWin)
        clearButton.pack(side='bottom')

    def clearWin(self):
        print('all clear')
        winWidth = self.canvas.winfo_width()
        sub = 1/winWidth
        i = winWidth
        while(i >= 0):
            i = i/1.1 - 1
            self.canvas.place(x=i, anchor='ne')
            self.root.update()
            time.sleep(sub)
        self.canvas.place(relx=-1)
        self.root.update()
        time.sleep(1.5)


