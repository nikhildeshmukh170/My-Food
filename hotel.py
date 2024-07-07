from tkinter import*
from pil import Image,ImageTk  #pip install pillow
from tkinter import ttk


class Bill_App: 
    def __init__(self,root):    
        self.root=root
        self.root.title("Kathi menu")
        self.root.geometry("1550x800")


     
        

        # ==================title==================
        lbl_title=Label(self.root,text="Select Food Item",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=0,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1550,height=50)


         # =================logo====================
        img=Image.open(r"C:\Users\Nikhil\OneDrive\Desktop\food\images\log.jpg")
        img=img.resize((100,50),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        lblimg=Label(self.root,image=self.photoimg,bd=0,relief=RIDGE)
        lblimg.place(x=20,y=0,width=100,height=50)

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=50,width=1530,height=620)

        #===================================================== Customer LabelFrame===========================================
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)

        self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white",fg="black")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,font=("times new roman",12,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

        self.lblCustName=Label(Cust_Frame,font=('arial',12,'bold'),bg="white",text="Customer Name",bd=4)
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtCustName=ttk.Entry(Cust_Frame,font=('arial',10,'bold'),width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblEmail=Label(Cust_Frame,font=('arial',12,'bold'),bg="white",text="Email",bd=4)
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtEmail=ttk.Entry(Cust_Frame,font=('arial',10,'bold'),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #===============================Product LabelFrame============================================
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=370,y=5,width=650,height=140)        

        #==============================Category====================================
        self.lblCategory=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Select Categories",bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,font=('arial',10,'bold'),value=self.Category,width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        #================================SubCategory=====================================
        self.lblSubCategory=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Subcategory",bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.ComboSubCategory=ttk.Combobox(Product_Frame,state="readonly",font=('arial',10,'bold'),width=24)
        self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        #=============================Product Name========================================================
        self.lblproduct=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Product Name",bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.ComboProduct=ttk.Combobox(Product_Frame,state="readonly",font=('arial',10,'bold'),width=24)
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #========================================Price============================================
        self.lblPrice=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Price",bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.ComboPrice=ttk.Combobox(Product_Frame,state="readonly",font=('arial',10,'bold'),width=24)
        self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        #========================================Qty======================================================
        self.lblQty=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Qty",bd=4)
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.ComboQty=ttk.Entry(Product_Frame,font=('arial',10,'bold'),width=26)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Middile frame@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=150,width=980,height=340)

        # Image1

        img21=Image.open(r"C:\Users\Nikhil\OneDrive\Desktop\food\images\kathi+maggi.jpg")
        img21=img21.resize((490,340),Image.ANTIALIAS)
        self.photoimg21=ImageTk.PhotoImage(img21)

        lbl_img21=Label(MiddleFrame,image=self.photoimg21)
        lbl_img21.place(x=0,y=0,width=490,height=340)


        # Search

        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=1020,y=15,width=500,height=40)

        self.lblBill=Label(Search_Frame,font=('arial',12,'bold'),bg="red",fg="white",text="Bill Number")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1,pady=1)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,font=('arial',10,'bold'),width=24)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)

        self.BtnSearch=Button(Search_Frame,text="Search",font=("arial",10,"bold"),bg="Orangered",fg="white",width=15,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)

        # RightFrame Bill Area=====================================
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Aria",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=1030,y=45,width=480,height=440)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="White",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)


        #===============================Bill Counter LabelFrame============================================
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=485,width=1520,height=125)  

        self.lblSubTotal=Label(Bottom_Frame,font=('arial',12,'bold'),bg="white",text="Sub Total",bd=4)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.EntySubTotal=ttk.Entry(Bottom_Frame,font=('arial',10,'bold'),width=26)
        self.EntySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

# ===================================================

        self.lbl_tax=Label(Bottom_Frame,font=('arial',12,'bold'),bg="white",text="GST",bd=4)
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(Bottom_Frame,font=('arial',10,'bold'),width=26)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

# ===================================================================

        self.lblAmountTotal=Label(Bottom_Frame,font=('arial',12,'bold'),bg="white",text="Total",bd=4)
        self.lblAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtAmountTotal=ttk.Entry(Bottom_Frame,font=('arial',10,'bold'),width=26)
        self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        # Button Frame===============================

        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="White")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart=Button(Btn_Frame,text="Add to Cart",font=("arial",15,"bold"),bg="Orangered",fg="white",width=15,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

# ==============================================

        self.Btngenerate_bill=Button(Btn_Frame,text="Generate Bill",font=("arial",15,"bold"),bg="Orangered",fg="white",width=15,cursor="hand2")
        self.Btngenerate_bill.grid(row=0,column=1)

# =====================================================

        self.BtnSave=Button(Btn_Frame,text="Save Bill",font=("arial",15,"bold"),bg="Orangered",fg="white",width=15,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)

# =====================================================================

        self.BtnPrint=Button(Btn_Frame,text="Print",font=("arial",15,"bold"),bg="Orangered",fg="white",width=15,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

# ==================================================

        self.BtnClear=Button(Btn_Frame,text="Clear",font=("arial",15,"bold"),bg="Orangered",fg="white",width=15,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

# =================================================================generate_bill
        self.BtnExit=Button(Btn_Frame,text="Exit",font=("arial",15,"bold"),bg="Orangered",fg="white",width=15,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)




         











if __name__=="__main__":
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()