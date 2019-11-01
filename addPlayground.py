import tkinter as tk

class main:
    def __init__(self,root):
        # root.configure(state = tk.disabled)
        self.root = root
        top = tk.Toplevel(root)
        top.minsize(height=650, width=550)
        canvas = tk.Canvas(top,bg = '#fff')
        canvas.pack(fill = 'both',expand = 1)
        label = tk.Label(canvas, text='ADD FIELD DETAILS', 
                         font=('Georgia', 24), fg='#FF3625', bg='#fff', pady=20)
        label.pack(fill = 'x')
        
        #frame for the field id
        frame=tk.Frame(canvas,bg='blue')
        frame.pack(fill='x',padx=10,pady=10,ipady=20)
        label = tk.Label(frame,bg="#fff",text='PLAYGROUND ID :',anchor='w',font=(' ',12))
        label.place(height=30, relwidth=0.4, rely=0.5, relx=0, anchor='w')
        fieldId = tk.Label(frame,font=(' ',11),text='id')
        fieldId.place(height=30,relwidth = 0.6,rely=0.5,relx=1,anchor ='e')

        name = tk.StringVar()
        name.set('hello')
        #frame for the field name
        frame=tk.Frame(canvas,bg='#fff')
        frame.pack(fill='x',padx=10,pady=10,ipady=20)
        label = tk.Label(frame,bg="#fff",text='PLAYGROUND NAME :',anchor='w',font=(' ',12,'bold'))
        label.place(height=30, relwidth=0.4, rely=0.5, relx=0, anchor='w')
        fieldName = tk.Entry(frame,font=(' ',11),relief='ridge',bd=2,textvariable=name)
        fieldName.place(height=30,relwidth = 0.6,rely=0.5,relx=1,anchor ='e')
        self.fieldName = fieldName

        #frame for the field name
        frame=tk.Frame(canvas,bg='#fff')
        frame.pack(fill='x',padx=10,pady=10,ipady=20)
        label = tk.Label(frame,bg="#fff",text='SPORT :',anchor='w',font=(' ',12,'bold'))
        label.place(height=30, relwidth=0.4, rely=0.5, relx=0, anchor='w')
        fieldSport = tk.Entry(frame,font=(' ',11),relief='ridge',bd=2)
        fieldSport.place(height=30,relwidth = 0.6,rely=0.5,relx=1,anchor ='e')
        self.fieldSport = fieldSport
        #frame for the dimension
        frame=tk.Frame(canvas,bg='#fff')
        frame.pack(fill='x',padx=10,pady=10,ipady=20)
        label = tk.Label(frame,bg="#fff",text='DIMENSION :',anchor='w',font=(' ',12,'bold'))
        label.place(height=30, relwidth=0.4, rely=0.5, relx=0, anchor='w')
        fieldDimension = tk.Entry(frame,font=(' ',11),relief='ridge',bd=2)
        fieldDimension.place(height=30,relwidth = 0.6,rely=0.5,relx=1,anchor ='e')
        self.fieldDimension = fieldDimension
        #frame for the loaction
        frame=tk.Frame(canvas,bg='#fff')
        frame.pack(fill='x',padx=10,pady=10,ipady=20)
        label = tk.Label(frame, bg="#fff", text='LOCATION :', anchor='w',font=(' ', 12, 'bold'))
        label.place(height=30, relwidth=0.4, rely=0.5, relx=0, anchor='w')
        fieldLocation = tk.Entry(frame,font=(' ',11),relief='ridge',bd=2)
        fieldLocation.place(height=30,relwidth = 0.6,rely=0.5,relx=1,anchor ='e')
        self.fieldLocation = fieldLocation
        #frame for the capacity
        frame=tk.Frame(canvas,bg='#fff')
        frame.pack(fill='x',padx=10,pady=10,ipady=20)
        label = tk.Label(frame,bg="#fff",text='CAPACITY :',anchor='w',font=(' ',12,'bold'))
        label.place(height=30, relwidth=0.4, rely=0.5, relx=0, anchor='w')
        fieldCapacity = tk.Entry(frame,font=(' ',11),relief='ridge',bd=2)
        fieldCapacity.place(height=30,relwidth = 0.6,rely=0.5,relx=1,anchor ='e')
        self.fieldCapacity = fieldCapacity
        #frame for the Cost
        frame=tk.Frame(canvas,bg='#fff')
        frame.pack(fill='x',padx=10,pady=10,ipady=20)
        label = tk.Label(frame,bg="#fff",text='COST :',anchor='w',font=(' ',12,'bold'))
        label.place(height=30, relwidth=0.4, rely=0.5, relx=0, anchor='w')
        fieldCost = tk.Entry(frame,font=(' ',11),relief='ridge',bd=2)
        fieldCost.place(height=30,relwidth = 0.6,rely=0.5,relx=1,anchor ='e')
        self.fieldCost = fieldCost
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
                           text='Save', cursor='hand2', bg='#000',fg='#fff',command=self.get)
        submit.place(height=40,relwidth = 0.4,relx=0.5,rely=1,anchor ='s')
        # submit.pack(side ='bottom')

    def get(self):
        print(self.fieldName.get())
        print(self.fieldCost.get())
        print(self.fieldCapacity.get())
        print(self.fieldDimension.get())
        print(self.fieldLocation.get())
        print(self.adminPass.get())
