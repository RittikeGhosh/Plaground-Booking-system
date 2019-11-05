from tkinter import *
import sqlite3




def call_description(email, uid):
    window = Toplevel()
    window.title("view details")

    amenities = ["artificial turf",
                "boundary netting", "changing room", "washrooms"]

    canvas1 = Canvas(window)
    yscrollbar = Scrollbar(window, orient="vertical", command=canvas1.yview)

    frame_can = Frame(canvas1)

    database = sqlite3.connect("playgrounds.db")
    em = database.execute("select * from playgrounds")
    x = em.fetchall()
    for i in x:
        if(i[0] == uid):
            frame = Frame(frame_can, height=100, width=800, padx=10, pady=10)
            frame.pack()
            head = Label(frame, text=i[1], font=("Times new roman", 20))
            head.grid(row=1)
            # fname = "image_88996_.gif"
            fname = i[7]
            image1 = PhotoImage(file=fname)
            w = image1.width()
            h = image1.height()
            window.geometry("1000x1000")
            canvas = Canvas(frame_can, width=w+20, height=h+20)
            canvas.pack()
            canvas.create_image(0, 0, image=image1, anchor="nw")
            frame2 = Frame(frame_can, height=600, width=800, padx=50, pady=50)
            frame2.pack()
            head2 = Label(frame2, text="Location", font=(
                "Times new roman", 15), width=50, anchor="nw", justify="left")
            #label1=Label(frame2,text="Location :")
            msg1 = Label(frame2, width=100, justify="left",
                            text=i[3], anchor="nw")
            frame3 = Frame(frame2, pady=10)
            head3 = Label(frame3, text="Description", font=(
                "Times new roman", 15), width=50, anchor="nw", justify="left")
            msg2 = Message(frame3, justify="left",
                            relief="raised", text=i[9], anchor="nw")
            head2.grid(row=1, column=1, sticky=W)
            sp1 = Label(frame2)
            sp1.grid(row=2, column=1)

            #label1.grid(row=3,column=1)
            msg1.grid(row=3, column=1, padx=10, pady=10, sticky=W)
            sp1 = Label(frame2)
            sp1.grid(row=4)
            frame3.grid(row=5, column=1, sticky=W+E+N+S)
            head3.pack(side=TOP, fill='both')
            msg2.pack(expand=True, fill='both')
            msg2.bind("<Configure>", lambda e: msg2.configure(width=e.width-10))

            sp1 = Label(frame2)
            sp1.grid(row=6)

            frame35 = Frame(frame2, pady=10)
            frame35.grid(row=7, column=1, sticky=W+E+N+S)
            head35 = Label(frame35, text="Sports", font=(
                "Times new roman", 15), anchor="nw", justify="left")
            head35.grid(row=1, column=1)
            sp1 = Label(frame35)
            sp1.grid(row=2)
            sports = i[6]
            sport = Label(frame35, text=sports, justify="left",
                            font=("Times new roman", 13))
            sport .grid(row=2, column=1)

            sp1 = Label(frame2)
            sp1.grid(row=8)

            frame4 = Frame(frame2, pady=10)
            frame4.grid(row=9, column=1, sticky=W+E+N+S)
            head4 = Label(frame4, text="Amenities", font=(
                "Times new roman", 15), anchor="nw", justify="left")
            head4.grid(row=1, column=1)
            sp1 = Label(frame4)
            sp1.grid(row=2)

            var = []
            t = 0
            col = 3
            for i in range(len(amenities)):
                var.append(IntVar())
                var[i].set(1)
                t = t+1
                C1 = Checkbutton(
                    frame4, text=amenities[i], justify="left", variable=var[i], onvalue=1, offvalue=0)
                if(t % 2 == 0):
                    C1.grid(row=col, column=2)
                else:
                    C1.grid(row=col, column=1)
                if(t % 2 == 0 and t != 0):
                    col = col+1

            sp1 = Label(frame2)
            sp1.grid(row=10)

            frame6 = Frame(frame2, pady=10)
            frame6.grid(row=11, column=1, sticky=W+E+N+S)
            dim = i[2]
            dimensions = Label(frame6, text="Dimensions : %s" %
                                dim, justify="left", font=("Times new roman", 13))
            dimensions .grid(row=1, column=1)

            sp1 = Label(frame2)
            sp1.grid(row=12)

            frame5 = Frame(frame2, pady=10)
            frame5.grid(row=13, column=1, sticky=W+E+N+S)
            cap = i[4]
            perhour = i[8]
            charge = Label(frame5, text="Per Hour Price : %s" %
                            perhour, font=("Times new roman", 13))
            seating = Label(frame5, text="Seating Capacity : %s" %
                            cap, font=("Times new roman", 13))
            charge.pack(side=LEFT)
            seating.pack(side=RIGHT)

            sp1 = Label(frame2)
            sp1.grid(row=14)

            def paymentportal():
                pass

            frame7 = Frame(frame2, pady=10)
            frame7.grid(row=15, column=1, sticky=W+E+N+S)
            book = Button(frame7, text="BOOK", bg="green",
                            fg="white", command=paymentportal)
            book.pack(side=TOP)

            sp1 = Label(frame2)
            sp1.grid(row=16)

            sp1 = Label(frame2)
            sp1.grid(row=17)

            frame.pack()
            canvas.pack()
            frame2.pack()

    canvas1.create_window(0, 0, anchor='nw', window=frame_can)

    canvas1.update_idletasks()

    canvas1.configure(scrollregion=canvas1.bbox('all'),
                        yscrollcommand=yscrollbar.set)

    canvas1.pack(fill='both', expand=True, side='left')
    yscrollbar.pack(fill='y', side='right')

    window.mainloop()

# call_description(3)