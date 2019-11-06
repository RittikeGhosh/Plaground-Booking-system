import tkinter as tk
from PIL import Image, ImageTk
import sqlite3


class main:
    def __init__(self,root,id = -1):
        self.id = id
        self.root = root
        top = tk.Toplevel(root)
        top.transient(root)
        top.minsize(height=650, width=850)
        self.top = top
        canvas = tk.Canvas(top,bg = '#fff')
        canvas.pack(fill = 'both',expand = 1)
        label = tk.Label(canvas, text='ADD FIELD DETAILS', 
                         font=('Georgia', 24), fg='#FF3625', bg='#fff', pady=20)
        label.pack(fill = 'x')

        #Frame foe the  image
        frame=tk.Frame(canvas,bg='#fff',height = 200)
        frame.pack(fill='x',padx=10,pady=10,ipady=20)
        image = tk.Label(frame,text = 'THE IMAGE WILL APPEAR HERE ',
            bg = '#eee',relief = 'raise',font = (' ',16),fg = '#000')
        image.place(relwidth = 1,relheight = 1)
        self.image = image
        #frame for the field id
        frame=tk.Frame(canvas,bg='blue')
        frame.pack(fill='x',padx=10,pady=10,ipady=20)
        label = tk.Label(frame,bg="#fff",text='PLAYGROUND ID :',anchor='w',font=(' ',12))
        label.place(height=30, relwidth=0.4, rely=0.5, relx=0, anchor='w')
        fieldId = tk.Label(frame,font=(' ',11),text= 'ID' )
        fieldId.place(height=30,relwidth = 0.6,rely=0.5,relx=1,anchor ='e')
        self.fieldId = fieldId
        #frame for the field name
        frame=tk.Frame(canvas,bg='#fff')
        frame.pack(fill='x',padx=10,pady=10,ipady=20)
        label = tk.Label(frame,bg="#fff",text='PLAYGROUND NAME :',anchor='w',font=(' ',12,'bold'))
        label.place(height=30, relwidth=0.4, rely=0.5, relx=0, anchor='w')
        fieldName = tk.Entry(frame,font=(' ',11),relief='ridge',bd=2)
        fieldName.place(height=30,relwidth = 0.6,rely=0.5,relx=1,anchor ='e')
        self.fieldName = fieldName
       	#frame for the field image
        frame = tk.Frame(canvas, bg='#fff')
        frame.pack(fill='x', padx=10, pady=10, ipady=20)
        label = tk.Label(frame, bg="#fff", text='IMAGE PATH :',
                         anchor='w', font=(' ', 12, 'bold'))
        label.place(height=30, relwidth=0.15, rely=0.5, relx=0, anchor='w')
        imageLoc = tk.Entry(frame, font=(' ', 11), relief='ridge', bd=2)
        imageLoc.place(height=30, relwidth=0.349,
                       rely=0.5, relx=0.15, anchor='w')
        imageLoc.bind('<Return>', self.updateImage)
        label = tk.Label(frame, bg="#fff", text='SPORT :',
                         anchor='w', font=(' ', 12, 'bold'))
        label.place(height=30, relwidth=0.15, rely=0.5, relx=0.5, anchor='w')
        fieldSport = tk.Entry(frame, font=(' ', 11), relief='ridge', bd=2)
        fieldSport.place(height=30, relwidth=0.349,
                         rely=0.5, relx=0.65, anchor='w')
        self.fieldSport = fieldSport
        self.imageLoc = imageLoc
        #frame for the field sport

        #frame for the field sport
        frame = tk.Frame(canvas, bg='#fff')
        frame.pack(fill='x', padx=10, pady=10, ipady=20)
        label = tk.Label(frame, bg="#fff", text='LOCATION :',
                         anchor='w', font=(' ', 12, 'bold'))
        label.place(height=30, relwidth=0.15, rely=0.5, relx=0, anchor='w')
        fieldLocation = tk.Entry(frame, font=(' ', 11), relief='ridge', bd=2)
        fieldLocation.place(height=30, relwidth=0.349,
                            rely=0.5, relx=0.15, anchor='w')
        label = tk.Label(frame, bg="#fff", text='DIMENSION :',
                         anchor='w', font=(' ', 12, 'bold'))
        label.place(height=30, relwidth=0.15, rely=0.5, relx=0.5, anchor='w')
        fieldDimension = tk.Entry(frame, font=(' ', 11), relief='ridge', bd=2)
        fieldDimension.place(height=30, relwidth=0.349,
                             rely=0.5, relx=0.65, anchor='w')
        self.fieldLocation = fieldLocation
        self.fieldDimension = fieldDimension
        #frame for the dimension

        #frame for the Cost
        frame = tk.Frame(canvas, bg='#fff')
        frame.pack(fill='x', padx=10, pady=10, ipady=20)
        label = tk.Label(frame, bg="#fff", text='COST :',
                         anchor='w', font=(' ', 12, 'bold'))
        label.place(height=30, relwidth=0.15, rely=0.5, relx=0, anchor='w')
        fieldCost = tk.Entry(frame, font=(' ', 11), relief='ridge', bd=2)
        fieldCost.place(height=30, relwidth=0.349,
                        rely=0.5, relx=0.15, anchor='w')
        label = tk.Label(frame, bg="#fff", text='CAPACITY :',
                         anchor='w', font=(' ', 12, 'bold'))
        label.place(height=30, relwidth=0.15, rely=0.5, relx=0.5, anchor='w')
        fieldCapacity = tk.Entry(frame, font=(' ', 11), relief='ridge', bd=2)
        fieldCapacity.place(height=30, relwidth=0.349,
                            rely=0.5, relx=0.65, anchor='w')
        self.fieldCost = fieldCost
        self.fieldCapacity = fieldCapacity
        #frame for the capacity
        # #frame for the field image
        # frame=tk.Frame(canvas,bg='#fff')
        # frame.pack(fill='x',padx=10,pady=10,ipady=20)
        # label = tk.Label(frame,bg="#fff",text='IMAGE PATH :',anchor='w',font=(' ',12,'bold'))
        # label.place(height=30, relwidth=0.4, rely=0.5, relx=0, anchor='w')
        # imageLoc = tk.Entry(frame,font=(' ',11),relief='ridge',bd=2)
        # imageLoc.place(height=30,relwidth = 0.6,rely=0.5,relx=1,anchor ='e')
        # imageLoc.bind('<Return>',self.updateImage)
        # self.imageLoc = imageLoc
        # #frame for the field sport
        # frame=tk.Frame(canvas,bg='#fff')
        # frame.pack(fill='x',padx=10,pady=10,ipady=20)
        # label = tk.Label(frame,bg="#fff",text='SPORT :',anchor='w',font=(' ',12,'bold'))
        # label.place(height=30, relwidth=0.4, rely=0.5, relx=0, anchor='w')
        # fieldSport = tk.Entry(frame,font=(' ',11),relief='ridge',bd=2)
        # fieldSport.place(height=30,relwidth = 0.6,rely=0.5,relx=1,anchor ='e')
        # self.fieldSport = fieldSport
        # #frame for the dimension
        # frame=tk.Frame(canvas,bg='#fff')
        # frame.pack(fill='x',padx=10,pady=10,ipady=20)
        # label = tk.Label(frame,bg="#fff",text='DIMENSION :',anchor='w',font=(' ',12,'bold'))
        # label.place(height=30, relwidth=0.4, rely=0.5, relx=0, anchor='w')
        # fieldDimension = tk.Entry(frame,font=(' ',11),relief='ridge',bd=2)
        # fieldDimension.place(height=30,relwidth = 0.6,rely=0.5,relx=1,anchor ='e')
        # self.fieldDimension = fieldDimension
        # #frame for the loaction
        # frame=tk.Frame(canvas,bg='#fff')
        # frame.pack(fill='x',padx=10,pady=10,ipady=20)
        # label = tk.Label(frame, bg="#fff", text='LOCATION :', anchor='w',font=(' ', 12, 'bold'))
        # label.place(height=30, relwidth=0.4, rely=0.5, relx=0, anchor='w')
        # fieldLocation = tk.Entry(frame,font=(' ',11),relief='ridge',bd=2)
        # fieldLocation.place(height=30,relwidth = 0.6,rely=0.5,relx=1,anchor ='e')
        # self.fieldLocation = fieldLocation
        # #frame for the capacity
        # frame=tk.Frame(canvas,bg='#fff')
        # frame.pack(fill='x',padx=10,pady=10,ipady=20)
        # label = tk.Label(frame,bg="#fff",text='CAPACITY :',anchor='w',font=(' ',12,'bold'))
        # label.place(height=30, relwidth=0.4, rely=0.5, relx=0, anchor='w')
        # fieldCapacity = tk.Entry(frame,font=(' ',11),relief='ridge',bd=2)
        # fieldCapacity.place(height=30,relwidth = 0.6,rely=0.5,relx=1,anchor ='e')
        # self.fieldCapacity = fieldCapacity
        # #frame for the Cost
        # frame=tk.Frame(canvas,bg='#fff')
        # frame.pack(fill='x',padx=10,pady=10,ipady=20)
        # label = tk.Label(frame,bg="#fff",text='COST :',anchor='w',font=(' ',12,'bold'))
        # label.place(height=30, relwidth=0.4, rely=0.5, relx=0, anchor='w')
        # fieldCost = tk.Entry(frame,font=(' ',11),relief='ridge',bd=2)
        # fieldCost.place(height=30,relwidth = 0.6,rely=0.5,relx=1,anchor ='e')
        # self.fieldCost = fieldCost
        #frame for the FIeld description
        frame = tk.Frame(canvas, bg='#fff')
        frame.pack(fill='x', padx=10, pady=10, ipady=20)
        fieldDesc = tk.Entry(frame, font=(' ', 11), relief='ridge', bd=2)
        fieldDesc.place(height=30, relwidth=1, rely=0.5, relx=1, anchor='e')
        self.fieldDesc = fieldDesc
        #frame for the password
        frame=tk.Frame(canvas,bg='#fff')
        frame.pack(fill='x',padx=10,pady=10,ipady=20)
        label = tk.Label(frame,bg="#fff",text='PASSWORD :',anchor='w',font=(' ',12,'bold'))
        label.place(height=30, relwidth=0.4, rely=0.5, relx=0, anchor='w')
        adminPass = tk.Entry(frame, font=(' ', 11), relief='ridge', bd=2, show='*')
        adminPass.place(height=30,relwidth = 0.6,rely=0.5,relx=1,anchor ='e')
        self.adminPass = adminPass
        #button for the submit 
        frame=tk.Frame(canvas,bg='#fff')
        frame.pack(fill='x',padx=10,pady=15,ipady=20)
        submit = tk.Button(frame, font=(' ', 14), relief='ridge',
                           text='Save', cursor='hand2', bg='#000',fg='#fff',command=self.save)
        submit.place(height=40,relwidth = 0.4,relx=0.5,rely=1,anchor ='s')

        #when called for updation
        if(id > 0):
            # self.fieldId.config(text = id)
            conn = sqlite3.connect('playgrounds.db')
            query = f'select * from playgrounds where f_id = {id};'
            a = conn.execute(query)
            l = a.fetchall()
            # print(l)
            conn.close()
            print(id)
            # self.top.quit()
            self.fieldId.config(text= f'#{id}')
            self.fieldName.insert(0,str(l[0][1]))
            self.fieldDimension.insert(0,str(l[0][2]))
            self.fieldLocation.insert(0,str(l[0][3]))
            self.fieldCapacity.insert(0,str(l[0][4]))
            self.fieldSport.insert(0,str(l[0][6]))
            self.imageLoc.insert(0,str(l[0][7]))
            self.fieldCost.insert(0,str(l[0][8]))
            self.fieldDesc.insert(0,str(l[0][9]))
            widget = self.image
            try:
                path = str(l[0][7])
                image = Image.open(path)
                background_image = ImageTk.PhotoImage(image)
                widget.config(text='', image=background_image)
                widget.image = background_image
                print('Image Updated', path)
            except:
                widget.config(text='Wrong Path or Format\nImage Will Appear here', image='')
                print('wrong path')
    
    #for the image update
    def updateImage(self,e):
        widget = self.image
        try:
            path = e.widget.get()
            image = Image.open(path)
            background_image = ImageTk.PhotoImage(image)
            widget.config(text='', image=background_image)
            widget.image = background_image
            print('Image Updated', path)
        except:
            widget.config(text = 'Wrong Path or Format\nImage Will Appear here',image = '')
            print('wrong path')

    def save(self):
        fieldName = self.fieldName.get()
        fieldDimension = self.fieldDimension.get()
        fieldLocation = self.fieldLocation.get()
        fieldCapacity = self.fieldCapacity.get()
        fieldSport = self.fieldSport.get()
        imageLoc  = self.imageLoc.get()
        fieldCost = self.fieldCost.get()
        fieldDesc = self.fieldDesc.get()
        password = self.adminPass.get()
        l = [(fieldName,fieldDimension,fieldLocation,fieldCapacity,fieldSport,imageLoc,fieldCost,fieldDesc)]
        print(l,password)
        
        #admin password verification 
        if(password == 'admin'):
            if self.id == -1 :
                try:
                    conn = sqlite3.connect('playgrounds.db')
                    conn.executemany(
                        'Insert into playgrounds(f_name,dimension,location,capacity,sports,image,price,description) values (?,?,?,?,?,?,?,?)', l)
                    print('inserted')
                    conn.commit()
                    conn.close()
                    self.top.withdraw()

                except:
                    print('error insert')
            else:
                # try:
                conn = sqlite3.connect('playgrounds.db')
                # query = f'update playgrounds set f_name = {fieldName},dimension = {fieldDimension},location = {fieldLocation},capacity = {fieldCapacity},sports = {fieldSport},image = {imageLoc},price = {fieldCost},description = {fieldDesc} where f_id = {self.id};'
                query = "update playgrounds set f_name = '" + fieldName + "',dimension = '" + fieldDimension + "', location = '" + fieldLocation  + "',capacity ='" + fieldCapacity + "',sports = '" + fieldSport + "',image = '" + imageLoc + "',price = '" + fieldCost + "',description ='" + fieldDesc + "' where f_id = " + str(self.id)
                print(query)

                conn.execute(query)
                print('updated')
                conn.commit()
                conn.close()
                self.top.withdraw()
                # except:
                    # print('error update')

        else:
            print('The password is incorrect')

# root = tk.Tk()
# # root.geometry('1000x1000+200+20')
# root.title('OnlinePlaygroundBookingSystem')
# o = main(root)
# print('hello')
# root.mainloop()
