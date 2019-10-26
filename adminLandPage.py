import tkinter as tk
import time

## class for admin land page
class main:
    def __init__(self,root):
        self.root = root
        canvas = tk.Canvas(root,bg = 'red')
        canvas.place(relwidth = 1,relheight = 1)
        self.canvas = canvas

        # clear button
        clearButton = tk.Button(root, text='Clear Window',bg='violet', command=self.clearWin)
        clearButton.pack(side='bottom')

    def clearWin(self):
        print('all clear')
        winWidth = self.canvas.winfo_width()
        sub = 1/winWidth
        print(sub)
        i = winWidth
        while(i >= 0):
            i = i/1.1 - 1
            self.canvas.place(x=i, anchor='ne')
            self.root.update()
            time.sleep(sub)
        self.canvas.place(relx=-1)
        self.root.update()
        time.sleep(1.5)
