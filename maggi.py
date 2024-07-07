from tkinter import*
from pil import Image,ImageTk  #pip install pillow
from tkinter import ttk


class maggi_Win: 
    def __init__(self,root):    
        self.root=root
        self.root.title("Kathi menu")
        self.root.geometry("1295x550+230+250")

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
        enty_ref=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        enty_ref.grid(row=0,column=1)

        label_menu=Label(labelframeleft,font=("arial",12,"bold"),text="Menu:",padx=2,pady=6)
        label_menu.grid(rows=3,column=0,sticky=W)
        
        combo_menu=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27,state="readonly")
        combo_menu["value"]=("Butter magii","Oregano maggi","Rosemary","Corn","Fusion Maggi","Oats Masala","Butter Double masala","Cheese Maggi"
                            "PeriPeri","Biryani Maggi","Masala Penne with Tomato","Tomato Pazzta","Chees Macaron","Onion Capsicum","Butter Maggi"
                            "Corn and Cheese","Chilli Garlic Cheese","Biryani Masala Sweet Corn") 
        combo_menu.current(0)
        combo_menu.grid(rows=3,column=1)

        label_menu=Label(labelframeleft,font=("arial",12,"bold"),text="Quantity:",padx=2,pady=6)
        label_menu.grid(rows=3,column=0,sticky=W)
        
        combo_menu=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27,state="readonly")
        combo_menu["value"]=("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16") 
        combo_menu.current(0)
        combo_menu.grid(rows=3,column=1)




        # ==========================button frame========================

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",font=("areail",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnDelete=Button(btn_frame,text="Reset",font=("areail",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=1,padx=1)

        btnReset=Button(btn_frame,text="Delete",font=("areail",11,"bold"),bg="red",fg="black",width=10)
        btnReset.grid(row=0,column=2,padx=1)

        btnupdate=Button(btn_frame,text="Done",font=("areail",11,"bold"),bg="green",fg="white",width=10)
        btnupdate.grid(row=0,column=3,padx=1)


        # =====================table frame==========================
    
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=50,width=860,height=490)
        lblsearchby=Label(Table_Frame,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W)

        combo_search=ttk.Combobox(Table_Frame,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Butter magii","Oregano maggi","Rosemary","Corn","Fusion Maggi","Oats Masala","Butter Double masala","Cheese Maggi"
                            "PeriPeri","Biryani Maggi","Masala Penne with Tomato","Tomato Pazzta","Chees Macaron","Onion Capsicum","Butter Maggi"
                            "Corn and Cheese","Chilli Garlic Cheese","Biryani Masala Sweet Corn") 
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

        self.Cust_details_table=ttk.Treeview(details_table,column=("ref","name","Menu","rate","quantity"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.Cust_details_table.xview)
        Scroll_y.config(command=self.Cust_details_table.yview)

        self.Cust_details_table.heading("ref",text="Refer No")
        self.Cust_details_table.heading("name",text="Name")
        self.Cust_details_table.heading("Menu",text="Menu")
        self.Cust_details_table.heading("rate",text="Rate")
        self.Cust_details_table.heading("quantity",text="Quantity")

        self.Cust_details_table["show"]="headings"
        self.Cust_details_table.pack(fill=BOTH,expand=1)




if __name__=="__main__":
    root=Tk()
    obj=maggi_Win(root)
    root.mainloop()