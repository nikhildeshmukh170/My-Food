from tkinter import*
from pil import Image,ImageTk  #pip install pillow
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class kathi_Win: 
    def __init__(self,root):    
        self.root=root
        self.root.title("Kathi menu")
        self.root.geometry("1295x550+230+250")
        
        # =======================Variables=============================

        self.var_ref=StringVar()
        x=random.randint(1,1000)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_cust_Menu=StringVar()
        self.var_cust_Rate=StringVar()
        self.var_cust_quantity=StringVar()




        # ==================title==================
        lbl_title=Label(self.root,text="Select Food Item",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=0,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


         # =================logo====================
        img2=Image.open(r"C:\Users\Nikhil\OneDrive\Desktop\food\images\log.jpg")
        img2=img2.resize((100,50),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=20,y=0,width=100,height=50)


        # =============================Lable Frame ==========================================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        
        # =========================labels entry =================================
        
        # ref no@@@@@@@@@@@@@@@@@@@@@@@@@
        label_ref=Label(labelframeleft,font=("arial",12,"bold"),text="Ref NO.",padx=2,pady=6)
        label_ref.grid(rows=1,column=0,sticky=W)
  
        enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,font=("arial",13,"bold"),width=29,state="readonly")
        enty_ref.grid(row=0,column=1)

        # name @@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        label_name=Label(labelframeleft,font=("arial",12,"bold"),text="Name:",padx=2,pady=6)
        label_name.grid(rows=2,column=0,sticky=W)
  
        enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,font=("arial",13,"bold"),width=29)
        enty_ref.grid(row=2,column=1)

        # email id @@@@@@@@@@@@@@@@@@@@@@@@@

        label_Email=Label(labelframeleft,font=("arial",12,"bold"),text="Email ID:",padx=2,pady=6)
        label_Email.grid(rows=2,column=0,sticky=W)
  
        enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_cust_Rate,font=("arial",13,"bold"),width=29)
        enty_ref.grid(row=3,column=1)

        # mobile no.@@@@@@@@@@@@@@@@@@@@@@@@@@

        ''' label_mobile=Label(labelframeleft,font=("arial",12,"bold"),text="Mobile No:",padx=2,pady=6)
        label_mobile.grid(rows=2,column=0,sticky=W)
  
        enty_ref=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        enty_ref.grid(row=4,column=1)'''
        
        # Menu@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2
        label_menu=Label(labelframeleft,font=("arial",12,"bold"),text="Menu:",padx=2,pady=6)
        label_menu.grid(rows=3,column=0,sticky=W)
        
        combo_menu=ttk.Combobox(labelframeleft,textvariable=self.var_cust_Menu,font=("arial",12,"bold"),width=27,state="readonly")
        combo_menu["value"]=("Chatpata Aloo","Healyhy Veggies","Egg Roll","Egg Crearay","Paneer Shawarma Roll","Egg Paratha"
                            "Veg Manchow soup glass","Chilli Patato","Veg fride Rice","Egg Fride Rice","Chilli Panner","Chilli Manchurian",
                           "chlli Garlic","Plain Omelette","Butter Topping","Bun Omlette","All time Wrape","Noodles Roll","Egg Panner Roll"
                            "Noodles Egg Roll","Pao Bhaji","Chole Bhature","Veg Biryani","Chilli Paneer With Veg Fride Rice",
                             "Veg Manchurian With Veg Fride Rice","Mix Parantha","Paneer Pyaaz Paratha","Gobhi Prantha") 
        combo_menu.current(0)
        combo_menu.grid(rows=3,column=1)

        label_quantity=Label(labelframeleft,font=("arial",12,"bold"),text="Quantity:",padx=2,pady=6)
        label_quantity.grid(rows=3,column=0,sticky=W)
        
        combo_quantity=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27,state="readonly")
        combo_quantity["value"]=("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16") 
        combo_quantity.current(0)
        combo_quantity.grid(rows=3,column=1)




        # ==========================button frame========================

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("areail",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("areail",11,"bold"),bg="black",fg="gold",width=10)
        btnupdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.fetch_data,font=("areail",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",font=("areail",11,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=10,padx=1)

        # =====================table frame==========================
    
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=50,width=860,height=490)
        lblsearchby=Label(Table_Frame,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W)

        combo_search=ttk.Combobox(Table_Frame,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Chatpata Aloo","Healyhy Veggies","Egg Roll","Egg Crearay","Paneer Shawarma Roll","Egg Paratha"
                                "Veg Manchow soup glass","Chilli Patato","Veg fride Rice","Egg Fride Rice","Chilli Panner","Chilli Manchurian",
                                "Add chlli Garlic","Plain Omelette","Butter Topping","Bun Omlette","All time Wrape","Noodles Roll","Egg Panner Roll"
                                "Noodles Egg Roll","Pao Bhaji","Chole Bhature","Veg Biryani","Chilli Paneer With Veg Fride Rice",
                                 "Veg Manchurian With Veg Fride Rice","Mix Parantha","Paneer Pyaaz Paratha","Gobhi Prantha") 
        combo_search.current(0)
        combo_search.grid(row=0,column=1)

        txtsearch=ttk.Entry(Table_Frame,font=("arial",13,"bold"),width=24)
        txtsearch.grid(row=0,column=2)

        btnSearch=Button(Table_Frame,text="Search",font=("areail",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowall=Button(Table_Frame,text="Show All",font=("areail",11,"bold"),bg="black",fg="gold",width=10)
        btnShowall.grid(row=0,column=4,padx=1)

        

        # ===========================Show Data=================================
        

        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        Scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","Menu","rate","quantity"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        # Scroll_x.config(Command=self.Cust_Details_Table.xview)
        # Scroll_y.config(Command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("Menu",text="Menu")
        self.Cust_Details_Table.heading("rate",text="Rate")
        self.Cust_Details_Table.heading("quantity",text="Quantity")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("Menu",width=100)
        self.Cust_Details_Table.column("rate",width=100)
        self.Cust_Details_Table.column("quantity",width=100)
      
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_cust_name.get()=="" : #self.var_mobile_no.get()==""
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Nikhil@@1234",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into  kathi values(%s,%s,%s,%s,%s)",(
                                                                    self.var_ref.get(),
                                                                    self.var_cust_name.get(),
                                                                    self.var_cust_Menu.get(),
                                                                    self.var_cust_Rate.get(),
                                                                    self.var_cust_quantity.get()

                                                                ))
                
                
                conn.commit()
                conn.close()                                               
                messagebox.showinfo("success","Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Nikhil@@1234",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * FROM management.kathi")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,value=i)
        conn.commit()
        conn.close()

    def get_cursor(self,Event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_cust_Menu.set(row[2])
        self.var_cust_Rate.set(row[3])
        self.var_cust_quantity.set(row[4])

    def update(self):
        if self.var_cust_name.get()=="":
            messagebox.showerror("Error","Please enter name",parent=self.root)
        
        conn=mysql.connector.connect(host="localhost",username="root",password="Nikhil@@1234",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("update customer set name=%s,Menu=%s,Rate=%s,quantity=%s where ref=%s",(
                                                                    self.var_cust_name.get(),
                                                                    self.var_cust_Menu.get(),
                                                                    self.var_cust_Rate.get(),
                                                                    self.var_cust_quantity.get(),
                                                                    self.var_ref.get()
                                                                                            ))

        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)   
                 

        # =============================btn===================================


if __name__=="__main__":
    root=Tk()
    obj=kathi_Win(root)
    root.mainloop()