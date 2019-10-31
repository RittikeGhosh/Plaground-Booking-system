import tkinter as tk
from PIL import Image, ImageTk
import functions.database_operations as dbo

# on search button press event
def on_buttonpress(db_file, value):
    
    value = value.strip().lower()
    connection = dbo.db_connection(db_file)
    search_list = dbo.select_from_playground(connection)

    # get data from search_list
    if value == '':
        data = search_list
    else:
        data = []
        for item in search_list:
            if value in item.lower():
                data.append(item)
    listbox_update(data)

# updating the listbox
def listbox_update(data):
    # delete previous data
    listbox.delete(0, 'end')

    # sorting data 
    #data = sorted(data, key=str.lower)

    # put new data
    for item in data:
        listbox.insert('end', item)
   

root = tk.Tk()
root.title('Online Playground Booking System')

canvas = tk.Canvas(root, height = 700, width = 800)
canvas.pack()

# placing a background image
image = Image.open('./images/bg.jpg')
background_image = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image = background_image)
background_label.place(relheight = 1, relwidth = 1)

# Search frame consisting of search box and search button
search_frame = tk.Frame(root, bg = '#80bd35', bd = 5)
search_frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.08, anchor = 'n')

search_box = tk.Entry(search_frame, font = 40)
search_box.place(relwidth = 0.67, relheight = 1)

search_button = tk.Button(search_frame, text = 'SEARCH', font = 40, command = lambda: on_buttonpress('./db/playgrounds.db', search_box.get()))
search_button.place(relx = 0.69, relheight = 1, relwidth = 0.31)

# Frame for showing the search results
search_result_frame = tk.Frame(root, bg = '#80bd35', bd = 5)
search_result_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.65, anchor = 'n')

listbox = tk.Listbox(search_result_frame)
listbox.place(relwidth = 1, relheight = 1)

root.mainloop()
