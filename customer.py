from msilib.schema import ComboBox
from textwrap import fill
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox





class customer_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1300x563+230+220")

        #----------variable----------
        self.var_ref=StringVar()
        x=random.randint(1000,99999)
        self.var_ref.set(str(x))
        
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_mobile=StringVar()
        self.var_nationality=StringVar()
        self.var_idproof=StringVar()
        self.var_idnumber=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_postal=StringVar()



        #-------tittle------------------------
        lbl_title=Label(self.root,text="Add Customer Details",font=("times new roman",20,"bold"),bg="black",fg="gold",bd="4",relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1300,height=50)


        #-----------logo------------
        img2=Image.open(r"C:\Users\thebalanar\Desktop\DBMS\Images\logo.jpg")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)


        #--------label frame--------------
        label_frame_left=LabelFrame(self.root,bd=5,relief=RIDGE,text="Customer Details",padx=2,font=("times new roman",14,"bold"))
        label_frame_left.place(x=5,y=50,width=426,height=500)

        #-------------------------label and entry---------------
        #--------cust ref----
        lbl_cust_ref=Label(label_frame_left,padx=2,pady=6,text="Customer Ref: ",font=("arial",14,"bold"))
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_cust_ref=ttk.Entry(label_frame_left,textvariable=self.var_ref,state="readonly",width=26,font=("arial",12,"bold"))
        entry_cust_ref.grid(row=0,column=1)


        #-----cust name----
        lbl_cust_name=Label(label_frame_left,padx=2,pady=6,text="Customer Name: ",font=("arial",14,"bold"))
        lbl_cust_name.grid(row=1,column=0,sticky=W)

        entry_cust_name=ttk.Entry(label_frame_left,textvariable=self.var_name,width=26,font=("arial",12,"bold"))
        entry_cust_name.grid(row=1,column=1)


        #-----gendercombobox----
        lbl_gender=Label(label_frame_left,padx=2,pady=6,text="Gender: ",font=("arial",14,"bold"))
        lbl_gender.grid(row=2,column=0,sticky=W)

        combo_gender=ttk.Combobox(label_frame_left,textvariable=self.var_gender,font=("arial",12,"bold"),width=24,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=2,column=1)



        #-----mobile number----
        lbl_mobile=Label(label_frame_left,padx=2,pady=6,text="Mobile: ",font=("arial",14,"bold"))
        lbl_mobile.grid(row=3,column=0,sticky=W)

        entry_mobile=ttk.Entry(label_frame_left,textvariable=self.var_mobile,width=26,font=("arial",12,"bold"))
        entry_mobile.grid(row=3,column=1)


    

        #-----nationality  combobox----
        lbl_nationality=Label(label_frame_left,padx=2,pady=6,text="Nationality: ",font=("arial",14,"bold"))
        lbl_nationality.grid(row=4,column=0,sticky=W)

        combo_nationality=ttk.Combobox(label_frame_left,textvariable=self.var_nationality,font=("arial",12,"bold"),width=24,state="readonly")
        combo_nationality["value"]=("Nepali","SAARC","Asia","European","American","Australian")
        combo_nationality.current(0)
        combo_nationality.grid(row=4,column=1)


        #-----idproof type combobox----
        lbl_id_proof=Label(label_frame_left,padx=2,pady=6,text="Id Proof Type: ",font=("arial",14,"bold"))
        lbl_id_proof.grid(row=5,column=0,sticky=W)

        combo_id_proof=ttk.Combobox(label_frame_left,textvariable=self.var_idproof,font=("arial",12,"bold"),width=24,state="readonly")
        combo_id_proof["value"]=("Citizenship","Driving liscence","Passport")
        combo_id_proof.current(0)
        combo_id_proof.grid(row=5,column=1)


        #-----id number----
        lbl_id_number=Label(label_frame_left,padx=2,pady=6,text="Id Number: ",font=("arial",14,"bold"))
        lbl_id_number.grid(row=6,column=0,sticky=W)

        entry_id_number=ttk.Entry(label_frame_left,textvariable=self.var_idnumber,width=26,font=("arial",12,"bold"))
        entry_id_number.grid(row=6,column=1)

        #-----email----
        lbl_email=Label(label_frame_left,padx=2,pady=6,text="Email: ",font=("arial",14,"bold"))
        lbl_email.grid(row=7,column=0,sticky=W)

        entry_email=ttk.Entry(label_frame_left,width=26,textvariable=self.var_email,font=("arial",12,"bold"))
        entry_email.grid(row=7,column=1)       



        #-----address----
        lbl_address=Label(label_frame_left,padx=2,pady=6,text="Address: ",font=("arial",14,"bold"))
        lbl_address.grid(row=8,column=0,sticky=W)

        entry_address=ttk.Entry(label_frame_left,width=26,textvariable=self.var_address,font=("arial",12,"bold"))
        entry_address.grid(row=8,column=1)

        #-----postalcode----
        lbl_postal_code=Label(label_frame_left,padx=2,pady=6,text="Postal Code: ",font=("arial",14,"bold"))
        lbl_postal_code.grid(row=9,column=0,sticky=W)

        entry_postal_code=ttk.Entry(label_frame_left,width=26,textvariable=self.var_postal,font=("arial",12,"bold"))
        entry_postal_code.grid(row=9,column=1)


 




        #--------------------------Buttons------------------
        btn_frame=Frame(label_frame_left,bd=4,relief=RIDGE)
        btn_frame.place(x=5,y=415,width=400,height=50)

        btn_add=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        btn_add.grid(row=0,column=0,padx=8.5,pady=5)

        btn_update=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        btn_update.grid(row=0,column=1,padx=8.25)

        btn_delete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        btn_delete.grid(row=0,column=2,padx=8.25)

        btn_reset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        btn_reset.grid(row=0,column=3,padx=8.25)



        #-------Table frame Search system----------
        label_frame_middle=LabelFrame(self.root,bd=5,relief=RIDGE,text="View and Search Details",padx=2,font=("times new roman",14,"bold"))
        label_frame_middle.place(x=435,y=50,width=855,height=500)

        lbl_search_by=Label(label_frame_middle,text="Search By: ",font=("arial",14,"bold"),bg="black",fg="gold")
        lbl_search_by.grid(row=0,column=0,sticky=W,padx=5)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(label_frame_middle,textvariable=self.search_var,font=("arial",12,"bold"),width=15,state="readonly")
        combo_search["value"]=("Ref","Mobile","Name")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=10)


        self.txt_search=StringVar()
        entry_search=ttk.Entry(label_frame_middle,textvariable=self.txt_search,width=30,font=("arial",12,"bold"))
        entry_search.grid(row=0,column=2,padx=10)

        btn_search=Button(label_frame_middle,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_search.grid(row=0,column=3,padx=10)

        btn_show_all=Button(label_frame_middle,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_show_all.grid(row=0,column=4,padx=10)

        #------show data table-----
        label_detail_frame=LabelFrame(label_frame_middle,bd=2.5,relief=RIDGE,padx=2,font=("times new roman",14,"bold"))
        label_detail_frame.place(x=10,y=55,width=825,height=400)

        scroll_x=ttk.Scrollbar(label_detail_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(label_detail_frame,orient=VERTICAL)


        #ref no, custname,gender,mobileno,nationality,idproof,id no,email,address,postalcode

        self.cust_details_table=ttk.Treeview(label_detail_frame,column=("ref","name","gender","mobile","nationality","idproof","idnumber","email" ,"address","postal"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading("ref",text="Refrence No")
        self.cust_details_table.heading("name",text="Name")
        self.cust_details_table.heading("gender",text="Gender")
        self.cust_details_table.heading("mobile",text="Mobile")        
        self.cust_details_table.heading("nationality",text="Nationality")
        self.cust_details_table.heading("idproof",text="Id Proof")
        self.cust_details_table.heading("idnumber",text="Id Proof No")
        self.cust_details_table.heading("email",text="Email")
        self.cust_details_table.heading("address",text="Address")     
        self.cust_details_table.heading("postal",text="PostalCode")

        self.cust_details_table["show"]="headings"
        
        self.cust_details_table.column("ref",width=100)
        self.cust_details_table.column("name",width=100)
        self.cust_details_table.column("gender",width=100)
        self.cust_details_table.column("mobile",width=100)
        self.cust_details_table.column("nationality",width=100)
        self.cust_details_table.column("idproof",width=100)
        self.cust_details_table.column("idnumber",width=100)
        self.cust_details_table.column("email",width=100)
        self.cust_details_table.column("address",width=100)
        self.cust_details_table.column("postal",width=100)        

        
        self.cust_details_table.pack(fill=BOTH,expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_address.get()=="" or self.var_idnumber=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotelmanagementsystem")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_ref.get(),
                                                                            self.var_name.get(),
                                                                            self.var_gender.get(),
                                                                            self.var_mobile.get(),
                                                                            self.var_nationality.get(),
                                                                            self.var_idproof.get(),
                                                                            self.var_idnumber.get(),
                                                                            self.var_email.get(),
                                                                            self.var_address.get(),
                                                                            self.var_postal.get()                                                               
                                                                            ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotelmanagementsystem")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
        
        conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.cust_details_table.focus()
        content=self.cust_details_table.item(cursor_row)
        row=content["values"]
        
        self.var_ref.set(row[0]),
        self.var_name.set(row[1]),
        self.var_gender.set(row[2]),
        self.var_mobile.set(row[3]),
        self.var_nationality.set(row[4]),
        self.var_idproof.set(row[5]),
        self.var_idnumber.set(row[6]),
        self.var_email.set(row[7]),
        self.var_address.set(row[8]),
        self.var_postal.set(row[9])



    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please Enter mobile number",parent=self.root)

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotelmanagementsystem")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set name=%s,gender=%s,mobile=%s,nationality=%s,idproof=%s,idnumber=%s,email=%s,address=%s,postal=%s where ref=%s",(
                                                                            self.var_name.get(),
                                                                            self.var_gender.get(),
                                                                            self.var_mobile.get(),
                                                                            self.var_nationality.get(),
                                                                            self.var_idproof.get(),
                                                                            self.var_idnumber.get(),
                                                                            self.var_email.get(),
                                                                            self.var_address.get(),
                                                                            self.var_postal.get(),
                                                                            self.var_ref.get()                                                              
                                                                            ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated",parent=self.root)



    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want to delete this entry",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotelmanagementsystem")
            my_cursor=conn.cursor()
            #----method2----
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)

        else:
            if not delete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        
        #self.var_ref.set(""),
        self.var_name.set(""),
        #self.var_gender.set(""),
        self.var_mobile.set(""),
        #self.var_nationality.set(""),
        #self.var_idproof.set(""),
        self.var_idnumber.set(""),
        self.var_email.set(""),
        self.var_address.set(""),
        self.var_postal.set("")


        x=random.randint(1000,99999)
        self.var_ref.set(str(x))

        

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotelmanagementsystem")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)

            conn.commit()
        conn.close()


        






if __name__=="__main__":
    root=Tk()
    obj=customer_window(root)
    root.mainloop()