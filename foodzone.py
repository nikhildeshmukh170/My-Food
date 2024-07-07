from tkinter import*
from pip import Image,ImageTk  #pip install pillow
from main import Bill_App


class foodzonesystem:
    def __init__(self,root):
        self.root=root
        self.root.title("My Food Zone")
        self.root.geometry("1550x800+0+0")


        # """"""""""""""""1st img"""""""""""""""""""""
        img1=Image.open(r"C:\Users\Nikhil\OneDrive\Desktop\food\images\top.jpg")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        # =================logo====================
        img2=Image.open(r"C:\Users\Nikhil\OneDrive\Desktop\food\images\log.jpg")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)


    
        # ==================title==================
        lbl_title=Label(self.root,text="My Food Zone",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=90)

        #====================main frame==================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=210,width=1550,height=620)

        # =================menu====================
        lbl_title=Label(main_frame,text="OUTLETS NAME",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=230)

        #====================main frame==================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn=Button(btn_frame,text="KATHI HOUSE",command=self.maggi_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        cust_btn.grid(row=0,column=0)

        room_btn=Button(btn_frame,text="NON-VEG KITCHEN",command=self.maggi_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        room_btn.grid(row=1,column=0)

        details_btn=Button(btn_frame,text="MAGGI HOTSPOT",command=self.maggi_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        details_btn.grid(row=2,column=0)

        food_btn=Button(btn_frame,text="QUINCH",command=self.maggi_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        food_btn.grid(row=3,column=0)

        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        logout_btn.grid(row=4,column=0)


        #========================right side img===========================
        img3=Image.open(r"C:\Users\Nikhil\OneDrive\Desktop\food\images\kathi+maggi.jpg")
        img3=img3.resize((1310,700),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=225,y=0,width=1310,height=590)

        #========================down side img===========================
        img4=Image.open(r"C:\Users\Nikhil\OneDrive\Desktop\food\images\log.jpg")
        img4=img4.resize((230,210),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=225,width=230,height=210)

        
        img5=Image.open(r"C:\Users\Nikhil\OneDrive\Desktop\food\10.jpg")
        img5=img5.resize((230,210),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=420,width=230,height=190)

    def logout(self):
        self.root.destroy()

    '''def Kathi_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Bill_App(self.new_window)'''

    def maggi_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Bill_App(self.new_window)

    '''def Quinch_details(self):
        self.new_window=Toplevel(self.root)
        self.app=quinch_Win(self.new_window)'''



if __name__=="__main__":
    root=Tk()
    obj=foodzonesystem(root)
    root.mainloop()