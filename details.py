from tkinter import *
from tkinter.font import BOLD
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime





class details:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1300x563+230+220")


        #-------tittle------------------------
        lbl_title=Label(self.root,text="Room Booking Details",font=("times new roman",20,"bold"),bg="black",fg="gold",bd="4",relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1300,height=50)


        #-----------logo------------
        img2=Image.open(r"C:\Users\thebalanar\Desktop\DBMS\Images\logo.jpg")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)


        #--------label frame--------------
        label_frame_left=LabelFrame(self.root,bd=5,relief=RIDGE,text="Room Details",padx=2,font=("times new roman",14,"bold"))
        label_frame_left.place(x=5,y=50,width=426,height=500)

        #-------------------------label and entry---------------
        #Floor
        label_floor=Label(label_frame_left,padx=2,pady=6,text="Floor: ",font=("arial",14,"bold"))
        label_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()

        text_floor=ttk.Entry(label_frame_left,textvariable=self.var_floor,width=26,font=("arial",12,"bold"))
        text_floor.grid(row=0,column=1)

        #Room no
        label_roomNo=Label(label_frame_left,padx=2,pady=6,text="Room no: ",font=("arial",14,"bold"))
        label_roomNo.grid(row=1,column=0,sticky=W)

        self.var_roomNo=StringVar()

        text_roomNo=ttk.Entry(label_frame_left,textvariable=self.var_roomNo,width=26,font=("arial",12,"bold"))
        text_roomNo.grid(row=1,column=1)


        #RoomType
        label_room_type=Label(label_frame_left,padx=2,pady=6,text="Room type: ",font=("arial",14,"bold"))
        label_room_type.grid(row=2,column=0,sticky=W)
        
        self.var_roomType=StringVar()

        text_room_type=ttk.Entry(label_frame_left,textvariable=self.var_roomType,width=26,font=("arial",12,"bold"))
        text_room_type.grid(row=2,column=1)



        #-------------Buttons----------

        btn_frame=Frame(label_frame_left,bd=4,relief=RIDGE)
        btn_frame.place(x=5,y=415,width=400,height=50)
        
        btn_add=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        btn_add.grid(row=0,column=0,padx=8.5,pady=5)
        
        btn_update=Button(btn_frame,text="Update",font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        btn_update.grid(row=0,column=1,padx=8.25)
        
        btn_delete=Button(btn_frame,text="Delete",font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        btn_delete.grid(row=0,column=2,padx=8.25)

        btn_reset=Button(btn_frame,text="Reset",font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        btn_reset.grid(row=0,column=3,padx=8.25)



        #-------Table frame Search system----------
        label_frame_middle=LabelFrame(self.root,bd=5,relief=RIDGE,text="View and Search Room Details",padx=2,font=("times new roman",14,"bold"))
        label_frame_middle.place(x=435,y=50,width=855,height=500)

        

        scroll_x=ttk.Scrollbar(label_frame_middle,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(label_frame_middle,orient=VERTICAL)



        self.room_table=ttk.Treeview(label_frame_middle,column=("floor","roomNo","roomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomNo",text="Room No")
        self.room_table.heading("roomType",text="Room Type")

        self.room_table["show"]="headings"
        
        self.room_table.column("floor",width=100)
        self.room_table.column("roomNo",width=100)
        self.room_table.column("roomType",width=100)

        self.room_table.pack(fill=BOTH,expand=1)


    #add data
    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomNo=="" or self.var_roomType=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotelmanagementsystem")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                            self.var_floor.get(),
                                                                            self.var_roomNo.get(),
                                                                            self.var_roomType.get()                                                         
                                                                            ))

                conn.commit()
                #self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)



        




















if __name__=="__main__":
    root=Tk()
    obj=details(root)
    root.mainloop()