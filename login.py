from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from main import HotelManagementSystem



class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1200x600+150+100")
        #self.root.attributes('-fullscreen',True)
            
        #-------Bg image----------
        self.bg=ImageTk.PhotoImage(file="Images/login.jpeg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)


        #-----login Frame-----
        frameLogin=Frame(self.root,bg="white")
        frameLogin.place(x=150,y=200,height=350,width=500)



        title=Label(frameLogin,text="Login Here",font=("Simplifica",35,"bold"),bg="white",fg="#d77337").place(x=100,y=30)


#login section
        label_user=Label(frameLogin,text="Username",font=("Goudy old style",15,"bold"),bg="white",fg="gray")
        label_user.place(x=100,y=140)


        #entry field
        self.txt_user=Entry(frameLogin,font=("Goudy old style",15),bg="lightgray",fg="gray")
        self.txt_user.place(x=100,y=170,width=350,height=35)


#password
        label_password=Label(frameLogin,text="Password",font=("Goudy old style",15,"bold"),bg="white",fg="gray")
        label_password.place(x=100,y=220)


        #entry field
        self.txt_password=Entry(frameLogin,font=("Goudy old style",15),bg="lightgray",fg="gray")
        self.txt_password.place(x=100,y=250,width=350,height=35)
        self.txt_password.config(show="*")


#forget button
        forget_btn=Button(frameLogin,text="Forget Password?",cursor="hand2",bg="white",font=("Goudy old style",13),bd=0,fg="#d25d17")
        forget_btn.place(x=100,y=290)

#login button
        login_btn=Button(self.root,text="Login",fg="white",command=self.login_function,cursor="hand2",font=("Goudy old style",15),bd=0,bg="#d25d17",width=10)
        login_btn.place(x=350,y=535)

        #--------------------Exit button--------

        # exit_btn=Button(self.root,text="Exit",width=10,font=("times new roman",14,"bold"),bg="black",fg="white",bd=0,command=root.destroy,cursor="hand2")
        # exit_btn.pack(side=TOP,anchor=NE)



    def login_function(self):
        if self.txt_password.get()=="" or self.txt_user.get=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        elif self.txt_password.get()!="Admin" or self.txt_user.get()!="Admin":
            messagebox.showerror("Error","Invalid Username/Password",parent=self.root)

        else:
            self.HotelManagementSystem()

        

    def HotelManagementSystem(self):
        self.new_window=Toplevel(self.root)
        self.app=HotelManagementSystem(self.new_window)









        





if __name__=="__main__":
    root=Tk()
    obj=login(root)
    root.mainloop()