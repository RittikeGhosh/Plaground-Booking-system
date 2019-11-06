import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3 as sl
import random
import mail

x = 1

def payment(email, p):
    # p = 10000
    def payment_validation():
        global x
        if(x <= 3):
            conn = sl.connect("playgrounds.db")
            if(price_entry_box.get() != str(p)):
                messagebox.showinfo("Information", "Please enter correct price....!!!")
            else:
                cur = conn.cursor()
                cur.execute(f"SELECT password FROM user_details WHERE email = '{email}'")
                password = cur.fetchall()
                conn.close()
                print(password)
                if(password[0][0] == password_entry_box.get()):
                    for widget in payment_frame.winfo_children():
                        widget.destroy()
                    s = tk.Label(payment_frame, text = 'SUCCESSFUL PAYMENT', font = ("Courier", 18))
                    s.place(relx = 0.5, rely = 0.1, relwidth = 1, relheight = 0.20, anchor = 'n')
                    tx = random.randint(1000000000, 10000000000)
                    s = tk.Label(payment_frame, text = f'Tx ID: {tx}', font = ("Courier", 14))
                    s.place(relx = 0.5, rely = 0.40, relwidth = 1, relheight = 0.16, anchor = 'n')
                    mail.sendMail(email, True)
            x += 1
        else:
            for widget in payment_frame.winfo_children():
                widget.destroy()
            s = tk.Label(payment_frame, text = 'PAYMENT FAILED', font = ("Courier", 18))
            s.place(relx = 0.5, rely = 0.1, relwidth = 1, relheight = 0.20, anchor = 'n')

    # root = tk.Toplevel()
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
    pay_button = tk.Button(payment_frame, text = 'PAY', font = 40, bg = '#80bd35', fg = '#ffffff', command = payment_validation)
    pay_button.place(relx = 0.5, rely = 0.9, relwidth = 1, relheight = 0.1, anchor = 'n')

    # root.mainloop()

# payment('tanu25.behera@gmail.com', 1000)