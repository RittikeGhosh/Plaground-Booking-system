import adminLogin as al 
import tkinter as tk

#initializing a window of dimention 1000x800
root = tk.Tk()
root.geometry('1000x800+400+50')
root.title('OnlinePlaygroundBookingSystem')

o = al.main(root)
# o = adminLogin()

# # clear button
# clearButton = tk.Button(root, text='Clear Window',bg='violet', command=o.clearWin)
# clearButton.pack(side='bottom')

print('hello')
root.mainloop()
