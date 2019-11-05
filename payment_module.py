import tkinter as tk
from PIL import Image, ImageTk
import random
import mail


def payment(p):
    # p = 10000
    root = tk.Toplevel()
    root.title('Online Playground Booking System')

    canvas = tk.Canvas(root, height = 700, width = 800)
    canvas.pack()

    # placing a background image
    image = Image.open('./images/bg.jpg')
    background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(root, image = background_image)
    background_label.place(relheight = 1, relwidth = 1)

    # frame for payment interface
    payment_frame = tk.Frame(root, bg = '#ffffff')
    payment_frame.place(relx = 0.5, rely = 0.2, relwidth = 0.50, relheight = 0.60, anchor = 'n')

    price_label = tk.Label(payment_frame, text = (f'Rs {p}'), font = ("Courier", 18))
    price_label.place(relx = 0.5, rely = 0.1, relwidth = 1, relheight = 0.20, anchor = 'n')

    # Amount entry
    price_entry_label = tk.Label(payment_frame, text = 'Enter Amount:', font=("Courier", 10), bg = '#ffffff')
    price_entry_label.place(relx = 0.20, rely = 0.425, anchor = 'nw')

    price_entry_box = tk.Entry(payment_frame, font = 40, highlightcolor = '#80bd35')
    price_entry_box.place(relx = 0.5, rely = 0.5, relwidth = 0.60, relheight = 0.08, anchor = 'n')

    # Password entry
    password_entry_label = tk.Label(payment_frame, text = 'Enter Password:', font=("Courier", 10), bg = '#ffffff')
    password_entry_label.place(relx = 0.20, rely = 0.625, anchor = 'nw')

    password_entry_box = tk.Entry(payment_frame, font = 40, highlightcolor = '#80bd35', show = '*')
    password_entry_box.place(relx = 0.5, rely = 0.7, relwidth = 0.60, relheight = 0.08, anchor = 'n')

    # Pay button
    pay_button = tk.Button(payment_frame, text = 'PAY', font = 40, bg = '#80bd35', fg = '#ffffff')
    pay_button.place(relx = 0.5, rely = 0.9, relwidth = 1, relheight = 0.1, anchor = 'n')

    # root.mainloop()