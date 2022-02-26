from tkinter import *
from PIL import Image,ImageTk
from customer import customer_window
from room import room_booking
from details import details


class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.attributes('-fullscreen',True)
        self.root.resizable(False,False)




        #--------------First Image------------------
        image1=Image.open(r"Images\coverpic.jpg")
        image1=image1.resize((1920,280),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(image1)


        lbl_image=Label(self.root,image=self.photoimage1,bd=4,relief=RIDGE)
        lbl_image.place(x=0,y=0,width=1920,height=140)

        #------------Logo-------------
        image2=Image.open(r"Images\logo.jpg")
        image2=image2.resize((140,140),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(image2)


        lbl_image=Label(self.root,image=self.photoimage2,bd=4,relief=RIDGE)
        lbl_image.place(x=0,y=0,width=140,height=140)

        #-------------Title--------------
        lbl_title=Label(self.root,text="Hotel Management System",font=("Simplifica",40,"bold"),bg="#ad4740",fg="lightgray",bd=2,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1920,height=50)

        #----------frame-----------------
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1920,height=670)

        #--------------------Exit button--------

        # exit_btn=Button(self.root,text="Exit",width=10,font=("times new roman",14,"bold"),bg="black",fg="white",bd=0,command=root.destroy,cursor="hand2")
        # exit_btn.pack(side=TOP,anchor=NE)


        #----------menu-----------------
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="#ad4740",fg="white",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        #----------button frame---------
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=230,height=115)


        #----------------button-----------
        cust_btn=Button(btn_frame,text="Customer Window",command=self.customer_details,width=22,font=("times new roman",14,"bold"),bg="#ad4740",fg="white",bd=0,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=0)

        room_btn=Button(btn_frame,text="Room Window",command=self.room_booking,width=22,font=("times new roman",14,"bold"),bg="#ad4740",fg="white",bd=0,cursor="hand2")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="Hotel",command=self.details,width=22,font=("times new roman",14,"bold"),bg="#ad4740",fg="white",bd=0,cursor="hand2")
        details_btn.grid(row=2,column=0,pady=1)
        
        # credit_btn=Button(btn_frame,text="Credit",width=22,command=self.credit,font=("times new roman",14,"bold"),bg="#ad4740",fg="white",bd=0,cursor="hand2")
        # credit_btn.grid(row=3,column=0,pady=1)

        # logout_btn=Button(btn_frame,text="Logout",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="#ad4740",fg="white",bd=0,cursor="hand2")
        # logout_btn.place(row=4,column=0,pady=1)


        #---------Right side image----------
        image3=Image.open(r"Images\front image.jpg")
        image3=image3.resize((1310,796),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(image3)


        lbl_image1=Label(main_frame,image=self.photoimage3,bd=4,relief=RIDGE)
        lbl_image1.place(x=225,y=0,width=1310,height=796)

        logout_btn=Button(self.root,text="Logout",command=self.logout,width=20,font=("times new roman",14,"bold"),bg="#ad4740",fg="white",bd=0,cursor="hand2")
        logout_btn.place(x=1300,y=825)

        #--------bottom left images---------
        image4=Image.open(r"Images\food.jpg")
        image4=image4.resize((230,210),Image.ANTIALIAS)
        self.photoimage4=ImageTk.PhotoImage(image4)
        lbl_image4=Label(main_frame,image=self.photoimage4,bd=4,relief=RIDGE)
        lbl_image4.place(x=0,y=150,width=225,height=160)


        
        image5=Image.open(r"Images\hotel.jpg")
        image5=image5.resize((225,210),Image.ANTIALIAS)
        self.photoimage5=ImageTk.PhotoImage(image5)
        lbl_image5=Label(main_frame,image=self.photoimage5,bd=4,relief=RIDGE)
        lbl_image5.place(x=0,y=310,width=225,height=210)




        image6=Image.open(r"Images\certification.jpg")
        image6=image6.resize((225,190),Image.ANTIALIAS)
        self.photoimage6=ImageTk.PhotoImage(image6)
        lbl_image6=Label(main_frame,image=self.photoimage6,bd=4,relief=RIDGE)
        lbl_image6.place(x=0,y=520,width=225,height=190)

    def customer_details(self):
        self.new_window=Toplevel(self.root)
        self.app=customer_window(self.new_window)

    def room_booking(self):
        self.new_window=Toplevel(self.root)
        self.app=room_booking(self.new_window)

    def details(self):
        self.new_window=Toplevel(self.root)
        self.app=details(self.new_window)

    def logout(self):
        self.root.destroy()

    # def logout(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=login(self.new_window)



        





if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()