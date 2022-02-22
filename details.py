from tkinter import *
from tkinter.font import BOLD
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox



class details:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1300x563+226+220")
        self.root.resizable(False,False)


        #-------tittle------------------------
        lbl_title=Label(self.root,text="Room Booking Details",font=("times new roman",20,"bold"),bg="#ad4740",fg="white",bd="4",relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1300,height=50)


        


        #--------label frame--------------
        label_frame_left=LabelFrame(self.root,bd=5,relief=RIDGE,text="Room Details",padx=2,font=("times new roman",14,"bold"),fg="#ad4740",bg="white")
        label_frame_left.place(x=5,y=50,width=426,height=500)

        #-------------------------label and entry---------------
        #Floor
        label_floor=Label(label_frame_left,padx=2,pady=6,text="Floor: ",font=("arial",14,"bold"),bg="white",fg="black")
        label_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()

        text_floor=ttk.Entry(label_frame_left,textvariable=self.var_floor,width=26,font=("arial",12,"bold"))
        text_floor.grid(row=0,column=1)

        #Room no
        label_roomNo=Label(label_frame_left,padx=2,pady=6,text="Room no: ",font=("arial",14,"bold"),bg="white",fg="black")
        label_roomNo.grid(row=1,column=0,sticky=W)

        self.var_roomNo=StringVar()

        text_roomNo=ttk.Entry(label_frame_left,textvariable=self.var_roomNo,width=26,font=("arial",12,"bold"))
        text_roomNo.grid(row=1,column=1)


        #RoomType
        label_room_type=Label(label_frame_left,padx=2,pady=6,text="Room type: ",font=("arial",14,"bold"),bg="white",fg="black")
        label_room_type.grid(row=2,column=0,sticky=W)
        
        self.var_roomType=StringVar()

        combo_room_type=ttk.Combobox(label_frame_left,font=("arial",12,"bold"),textvariable=self.var_roomType,width=24,state="readonly")
        combo_room_type["value"]=("Single","Double","Suit","Villa")
        combo_room_type.current(0)
        combo_room_type.grid(row=2,column=1)



        #-------------Buttons----------

        btn_frame=Frame(label_frame_left,bd=4,relief=RIDGE)
        btn_frame.place(x=5,y=415,width=400,height=50)
        
        btn_add=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="#ad4740",fg="white",width=7)
        btn_add.grid(row=0,column=0,padx=8.5,pady=5)
        
        btn_update=Button(btn_frame,text="Update",command=self.update_data,font=("arial",12,"bold"),bg="#ad4740",fg="white",width=7)
        btn_update.grid(row=0,column=1,padx=8.25)
        
        btn_delete=Button(btn_frame,text="Delete",font=("arial",12,"bold"),command=self.delete,bg="#ad4740",fg="white",width=7)
        btn_delete.grid(row=0,column=2,padx=8.25)

        btn_reset=Button(btn_frame,text="Reset",font=("arial",12,"bold"),command=self.reset,bg="#ad4740",fg="white",width=7)
        btn_reset.grid(row=0,column=3,padx=8.25)



        #-------Table frame Search system----------
        label_frame_middle=LabelFrame(self.root,bd=5,relief=RIDGE,text="View and Search Room Details",padx=2,font=("times new roman",14,"bold"),fg="#ad4740",bg="white")
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
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    #get cursor to bind data from db to input section
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_floor.set(row[0])
        self.var_roomNo.set(row[1])
        self.var_roomType.set(row[2])
        



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
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)



    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotelmanagementsystem")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
        
        conn.commit()
        conn.close()


    #update
    def update_data(self):
        if self.var_floor.get()=="" or self.var_roomNo.get()=="" or self.var_roomType.get()=="":
            messagebox.showerror("Error","Please enter all etails",parent=self.root)

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotelmanagementsystem")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set floor=%s,roomType=%s where roomNo=%s",(
                                                                            self.var_floor.get(),
                                                                            self.var_roomType.get(),
                                                                            self.var_roomNo.get()                                                          
                                                                            ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated",parent=self.root)



    #delete
    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want to delete this entry",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotelmanagementsystem")
            my_cursor=conn.cursor()
            #----method2----
            query="delete from details where roomNo=%s"
            value=(self.var_roomNo.get(),)
            my_cursor.execute(query,value)

        else:
            if not delete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()



    #reset
    def reset(self):
        self.var_floor.set("")
        self.var_roomNo.set("")
        self.var_roomType.set("")





















if __name__=="__main__":
    root=Tk()
    obj=details(root)
    root.mainloop()