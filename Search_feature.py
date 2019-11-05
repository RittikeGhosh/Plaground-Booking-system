import tkinter as tk
from PIL import Image, ImageTk
import functions.database_operations as dbo
import fieldDetails as fd
# import filter as fil


def search_page(email):
    # on search button press event
    def on_buttonpress(db_file, value):
        value = value.strip().lower()
        connection = dbo.db_connection(db_file)
        search_list = dbo.select_from_playground(connection)

        # get data from search_list
        if value == '':
            for item in search_list:
                data = item[1]
        else:
            data = []
            for item in search_list:
                if value in item[1].lower():
                    data.append(item[1])
        x = len(data)
        listbox_update(data)
        # # tk.messagebox.showinfo(x)
        # print(x)


    # Show search result when Enter key is pressed
    def Enter_pressed(event):
        on_buttonpress('./db/playgrounds.db', search_box.get())

    # updating the listbox
    def listbox_update(data):
        # delete previous data
        listbox.delete(0, 'end')

        # sorting data 
        #data = sorted(data, key=str.lower)

        # put new data
        for item in data:
            listbox.insert('end', item)

    def on_select(event):
        # display element selected on list
        # print('(event) previous:', event.widget.get('active'))
        # print('(event)  current:', event.widget.get(event.widget.curselection()))
        # print('---')
        connection = dbo.db_connection('./db/playgrounds.db')
        s = event.widget.get(event.widget.curselection())
        print(s)
        select_item = dbo.retrive_f_id(connection, s)
        print(select_item)
        # fd.call_description(email, select_item)

        
    root = tk.Toplevel()
    root.title('Online Playground Booking System')

    canvas = tk.Canvas(root, height=700, width=800)
    canvas.pack()

    # placing a background image
    image = Image.open('./images/bg.jpg')
    background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(root, image=background_image)
    background_label.image = image
    background_label.place(relheight=1, relwidth=1)

    # Search frame consisting of search box and search button
    search_frame = tk.Frame(root, bg='#80bd35', bd=5)
    search_frame.place(relx=0.5, rely=0.1, relwidth=0.75,
                    relheight=0.08, anchor='n')

    search_box = tk.Entry(search_frame, font=40)
    search_box.place(relwidth=0.47, relheight=1)
    search_box.bind('<Return>', Enter_pressed)

    search_button = tk.Button(search_frame, text='SEARCH', font=40,
                            command=lambda: on_buttonpress('./db/playgrounds.db', search_box.get()))
    search_button.place(relx=0.49, relheight=1, relwidth=0.245)

    search_button = tk.Button(search_frame, text='FILTER', font=40,
                            command=lambda: on_buttonpress('./db/playgrounds.db', search_box.get()))
    # search_button = tk.Button(search_frame, text='FILTER', font=40,
    #                         command=lambda: fil.filter(uid))
    search_button.place(relx=0.755, relheight=1, relwidth=0.245)

    # Frame for showing the search results
    search_result_frame = tk.Frame(root, bg='#80bd35', bd=5)
    search_result_frame.place(
        relx=0.5, rely=0.25, relwidth=0.75, relheight=0.65, anchor='n')

    listbox = tk.Listbox(search_result_frame)
    listbox.place(relwidth=1, relheight=1)
    listbox.bind('<<ListboxSelect>>', on_select)

    # root.mainloop()
