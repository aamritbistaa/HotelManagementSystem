from tkinter import *
from tkinter.font import BOLD
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime





class room_booking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1300x563+226+220")

        #--------------Variables----------
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

    


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
        label_frame_left=LabelFrame(self.root,bd=5,relief=RIDGE,text="Room Booking Details",padx=2,font=("times new roman",14,"bold"))
        label_frame_left.place(x=5,y=50,width=426,height=500)

        #-------------------------label and entry---------------
        #contact number
        label_contact=Label(label_frame_left,padx=0,pady=6,text="Contact:",font=("arial",14,"bold"))
        label_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(label_frame_left,width=19,textvariable=self.var_contact,font=("arial",12,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        #fetch data button
        btn_fetch_data=Button(label_frame_left,command=self.fetch_contact,text="Get data",font=("arial",8,"bold"),bg="black",fg="gold",width=7)
        btn_fetch_data.place(x=345,y=6)




        #check in date
        label_check_in_date=Label(label_frame_left,padx=2,pady=6,text="Check in date: ",font=("arial",14,"bold"))
        label_check_in_date.grid(row=1,column=0,sticky=W)

        text_check_in_date=ttk.Entry(label_frame_left,textvariable=self.var_checkin,width=26,font=("arial",12,"bold"))
        text_check_in_date.grid(row=1,column=1)

        #check out date
        label_check_out_date=Label(label_frame_left,padx=2,pady=6,text="Check out date: ",font=("arial",14,"bold"))
        label_check_out_date.grid(row=2,column=0,sticky=W)

        text_check_out_date=ttk.Entry(label_frame_left,textvariable=self.var_checkout,width=26,font=("arial",12,"bold"))
        text_check_out_date.grid(row=2,column=1)

        #room type
        label_room_type=Label(label_frame_left,padx=2,pady=6,text="Room Type: ",font=("arial",14,"bold"))
        label_room_type.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotelmanagementsystem")
        my_cursor=conn.cursor()
        my_cursor.execute("select roomType from details")

        roomtype=my_cursor.fetchall()

        combo_room_type=ttk.Combobox(label_frame_left,font=("arial",12,"bold"),textvariable=self.var_roomtype,width=24,state="readonly")
        combo_room_type["value"]=roomtype
        combo_room_type.current(0)
        combo_room_type.grid(row=3,column=1)

        #available room
        label_available=Label(label_frame_left,padx=2,pady=6,text="Available Room: ",font=("arial",14,"bold"))
        label_available.grid(row=4,column=0,sticky=W)

        # text_available=ttk.Entry(label_frame_left,width=26,textvariable=self.var_roomavailable,font=("arial",12,"bold"))
        # text_available.grid(row=4,column=1)


        my_cursor.execute("select roomNo from details")

        rows=my_cursor.fetchall()


        combo_room_no=ttk.Combobox(label_frame_left,font=("arial",12,"bold"),textvariable=self.var_roomavailable,width=24,state="readonly")
        combo_room_no["value"]=rows
        combo_room_no.current(0)
        combo_room_no.grid(row=4,column=1)
        conn.commit()
        conn.close()  

        #----food-----
        #meal
        label_meal=Label(label_frame_left,padx=2,pady=6,text="Meal: ",font=("arial",14,"bold"))
        label_meal.grid(row=5,column=0,sticky=W)

        text_meal=ttk.Entry(label_frame_left,width=26,textvariable=self.var_meal,font=("arial",12,"bold"))
        text_meal.grid(row=5,column=1)     






        #days
        label_no_of_days=Label(label_frame_left,padx=2,pady=6,text="No of days: ",font=("arial",14,"bold"))
        label_no_of_days.grid(row=6,column=0,sticky=W)

        text_no_of_days=ttk.Entry(label_frame_left,width=26,textvariable=self.var_noofdays,font=("arial",12,"bold"))
        text_no_of_days.grid(row=6,column=1)



        
        
        #paid tax
        label_paid_tax=Label(label_frame_left,padx=2,pady=6,text="Tax: ",font=("arial",14,"bold"))
        label_paid_tax.grid(row=7,column=0,sticky=W)

        text_paid_tax=ttk.Entry(label_frame_left,width=26,textvariable=self.var_paidtax,font=("arial",12,"bold"))
        text_paid_tax.grid(row=7,column=1) 

        #sub total
        label_sub_cost=Label(label_frame_left,padx=2,pady=6,text="Total: ",font=("arial",14,"bold"))
        label_sub_cost.grid(row=8,column=0,sticky=W)

        text_sub_cost=ttk.Entry(label_frame_left,width=26,textvariable=self.var_actualtotal,font=("arial",12,"bold"))
        text_sub_cost.grid(row=8,column=1) 

        #total
        label_total_cost=Label(label_frame_left,padx=2,pady=6,text="Grand Total: ",font=("arial",14,"bold"))
        label_total_cost.grid(row=9,column=0,sticky=W)

        text_total_cost=ttk.Entry(label_frame_left,textvariable=self.var_total,width=26,font=("arial",12,"bold"))
        text_total_cost.grid(row=9,column=1) 


        #-----bill button-------
        btn_bill=Button(label_frame_left,text="Bill",command=self.total,font=("arial",10,"bold"),bg="black",fg="gold",width=5)
        btn_bill.grid(row=10,column=1,padx=0,pady=0,sticky=E)


        #--------------------------Buttons------------------
        btn_frame=Frame(label_frame_left,bd=4,relief=RIDGE)
        btn_frame.place(x=5,y=415,width=400,height=50)
        
        btn_add=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        btn_add.grid(row=0,column=0,padx=8.5,pady=5)
        
        btn_update=Button(btn_frame,text="Update",command=self.update_data,font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        btn_update.grid(row=0,column=1,padx=8.25)
        
        btn_delete=Button(btn_frame,text="Delete",font=("arial",12,"bold"),command=self.delete,bg="black",fg="gold",width=7)
        btn_delete.grid(row=0,column=2,padx=8.25)

        btn_reset=Button(btn_frame,text="Reset",font=("arial",12,"bold"),command=self.reset,bg="black",fg="gold",width=7)
        btn_reset.grid(row=0,column=3,padx=8.25)

        #----------(middle)right side section-------
        #mody frame
        label_frame_top_middle=LabelFrame(self.root,bd=5,relief=RIDGE)
        label_frame_top_middle.place(x=930,y=50,width=358,height=242)
        

        


        #frame
        
            #insert Hotel image for mid section
        img_center_mid=Image.open(r"C:\Users\thebalanar\Desktop\DBMS\Images\singleRoom.webp")
        img_center_mid=img_center_mid.resize((490,235),Image.ANTIALIAS)
        self.photoimg_center_mid=ImageTk.PhotoImage(img_center_mid)

        lblimg=Label(self.root,image=self.photoimg_center_mid,bd=1,relief=RIDGE)
        lblimg.place(x=435,y=60)





        #images
        img3=Image.open(r"C:\Users\thebalanar\Desktop\DBMS\Images\singleRoom.webp")
        img3=img3.resize((172,114),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(label_frame_top_middle,image=self.photoimg3,bd=1,relief=RIDGE)
        lblimg.grid(row=0,column=0)

        img4=Image.open(r"C:\Users\thebalanar\Desktop\DBMS\Images\doubleRoom.webp")
        img4=img4.resize((172,114),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg=Label(label_frame_top_middle,image=self.photoimg4,bd=1,relief=RIDGE)
        lblimg.grid(row=0,column=1)

        img5=Image.open(r"C:\Users\thebalanar\Desktop\DBMS\Images\suit.webp")
        img5=img5.resize((172,114),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg=Label(label_frame_top_middle,image=self.photoimg5,bd=1,relief=RIDGE)
        lblimg.grid(row=1,column=0)

        img6=Image.open(r"C:\Users\thebalanar\Desktop\DBMS\Images\villa.webp")
        img6=img6.resize((172,114),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        lblimg=Label(label_frame_top_middle,image=self.photoimg6,bd=1,relief=RIDGE)
        lblimg.grid(row=1,column=1)
        

        #-------Table frame Search system----------
        label_frame_middle=LabelFrame(self.root,bd=5,relief=RIDGE,text="View and Search Details",padx=2,font=("times new roman",14,"bold"))
        label_frame_middle.place(x=435,y=290,width=855,height=260)

        lbl_search_by=Label(label_frame_middle,text="Search By: ",font=("arial",14,"bold"),bg="black",fg="gold")
        lbl_search_by.grid(row=0,column=0,sticky=W,padx=5)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(label_frame_middle,textvariable=self.search_var,font=("arial",12,"bold"),width=15,state="readonly")
        combo_search["value"]=("Contact","Room")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=10)


        self.txt_search=StringVar()
        entry_search=ttk.Entry(label_frame_middle,textvariable=self.txt_search,width=30,font=("arial",12,"bold"))
        entry_search.grid(row=0,column=2,padx=10)

        btn_search=Button(label_frame_middle,command=self.search,text="Search",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_search.grid(row=0,column=3,padx=10)

        btn_show_all=Button(label_frame_middle,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_show_all.grid(row=0,column=4,padx=10)

        #------show data table-----
        label_detail_frame=LabelFrame(label_frame_middle,bd=0,relief=RIDGE,padx=2,font=("times new roman",14,"bold"))
        label_detail_frame.place(x=5,y=38,width=825,height=190)

        scroll_x=ttk.Scrollbar(label_detail_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(label_detail_frame,orient=VERTICAL)



        self.room_table=ttk.Treeview(label_detail_frame,column=("contact","checkin","checkout","roomtype","roomavailable","meal","noofdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Checkin")
        self.room_table.heading("checkout",text="Checkout")
        self.room_table.heading("roomtype",text="Room Type")        
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noofdays",text="No Of Days")

        self.room_table["show"]="headings"
        
        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noofdays",width=100)

        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    #-------------------------Data fetch----------------
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Invalid contact number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotelmanagementsystem")
            my_cursor=conn.cursor()
            query=("select Name from customer where mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","User not found \nInvalid contact number",parent=self.root)
            else:
                conn.commit()
                conn.close()
                
                #frame
                label_frame_mid=LabelFrame(self.root,bd=5,relief=RIDGE,text="Customer Details",padx=2,font=("times new roman",14,"bold"))
                label_frame_mid.place(x=435,y=50,width=495,height=240)

                #display Name::
                labelname=Label(label_frame_mid,text="Name:",font=("arial",14,"bold"))
                labelname.grid(row=0,column=0,sticky=W)

                lblname=Label(label_frame_mid,text=row,font=("arial",14,"bold"))
                lblname.grid(row=0,column=1,sticky=W)

                #display Gender::
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotelmanagementsystem")
                my_cursor=conn.cursor()
                query=("select Gender from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                labelgender=Label(label_frame_mid,text="Gender:",font=("arial",14,"bold"))
                labelgender.grid(row=1,column=0,sticky=W)

                lblgender=Label(label_frame_mid,text=row,font=("arial",14))
                lblgender.grid(row=1,column=1,sticky=W)

                #display nationality::
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotelmanagementsystem")
                my_cursor=conn.cursor()
                query=("select nationality from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                labelnationality=Label(label_frame_mid,text="nationality:",font=("arial",14,"bold"))
                labelnationality.grid(row=2,column=0,sticky=W)

                lblnationality=Label(label_frame_mid,text=row,font=("arial",14))
                lblnationality.grid(row=2,column=1,sticky=W)


                #display idproof::

                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotelmanagementsystem")
                my_cursor=conn.cursor()
                query=("select idproof from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                labelidproof=Label(label_frame_mid,text="Idproof:",font=("arial",16,"bold"))
                labelidproof.grid(row=3,column=0,sticky=W)

                lblidproof=Label(label_frame_mid,text=row,font=("arial",14))
                lblidproof.grid(row=3,column=1,sticky=W)


                #display idnumber::

                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotelmanagementsystem")
                my_cursor=conn.cursor()
                query=("select idnumber from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                labelidnumber=Label(label_frame_mid,text="Idnumber:",font=("arial",14,"bold"))
                labelidnumber.grid(row=4,column=0,sticky=W)

                lblidnumber=Label(label_frame_mid,text=row,font=("arial",14))
                lblidnumber.grid(row=4,column=1,sticky=W)

                #display Email::

                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotelmanagementsystem")
                my_cursor=conn.cursor()
                query=("select Email from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                labelemail=Label(label_frame_mid,text="Email:",font=("arial",14,"bold"))
                labelemail.grid(row=5,column=0,sticky=W)

                lblemail=Label(label_frame_mid,text=row,font=("arial",14))
                lblemail.grid(row=5,column=1,sticky=W)

                #display address::

                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotelmanagementsystem")
                my_cursor=conn.cursor()
                query=("select address from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                labeladdress=Label(label_frame_mid,text="Address:",font=("arial",14,"bold"))
                labeladdress.grid(row=6,column=0,sticky=W)

                lbladdress=Label(label_frame_mid,text=row,font=("arial",14))
                lbladdress.grid(row=6,column=1,sticky=W)

#----------------fetch data-----
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotelmanagementsystem")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
        
        conn.commit()
        conn.close()


    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotelmanagementsystem")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)

            conn.commit()
        conn.close()



    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        #food cost
        if((self.var_meal.get().upper())=="BREAKFAST"):
            q1=float(150)
        elif((self.var_meal.get().upper())=="LUNCH"):
            q1=float(250)
        elif((self.var_meal.get().upper())=="DINNER"):
            q1=float(400)
        elif((self.var_meal.get().upper())=="ALL"):
            q1=float(800)


        #room cost
        if((self.var_roomtype.get())=="Single"):
            q2=float(500)
        elif((self.var_roomtype.get())=="Double"):
            q2=float(1500)
        elif((self.var_roomtype.get())=="Suit"):
            q2=float(2500)
        elif((self.var_roomtype.get())=="Villa"):
            q2=float(4000)
        
        #calculation
        q3=float(self.var_noofdays.get())
        q5=float((q1*q3)+(q2*q3))

        Tax="RS. "+str("%.2f"%((q5)*0.1))
        ST="RS. "+str("%.2f"%((q5)))
        TT="RS. "+str("%.2f"%((q5)+((q5)*0.1)))
        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)





    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]
        
        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])

    #update
    def update_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","Please Enter a valid contact number",parent=self.root)

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotelmanagementsystem")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noofdays=%s where contact=%s",(
                                                                            self.var_checkin.get(),
                                                                            self.var_checkout.get(),
                                                                            self.var_roomtype.get(),
                                                                            self.var_roomavailable.get(),
                                                                            self.var_meal.get(),
                                                                            self.var_noofdays.get(),
                                                                            self.var_contact.get()                                                           
                                                                            ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated",parent=self.root)



    #add data to database
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin=="" or self.var_roomavailable=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotelmanagementsystem")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_contact.get(),
                                                                            self.var_checkin.get(),
                                                                            self.var_checkout.get(),
                                                                            self.var_roomtype.get(),
                                                                            self.var_roomavailable.get(),
                                                                            self.var_meal.get(),
                                                                            self.var_noofdays.get()                                                          
                                                                            ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Boked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)


    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want to delete this entry",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotelmanagementsystem")
            my_cursor=conn.cursor()
            #----method2----
            query="delete from room where roomavailable=%s"
            value=(self.var_roomavailable.get(),)
            my_cursor.execute(query,value)

        else:
            if not delete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()


    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

    






if __name__=="__main__":
    root=Tk()
    obj=room_booking(root)
    root.mainloop()