from tkinter import*
from pip import Image,ImageTk  #pip install pillow
from tkinter import ttk
import random,os
from tkinter import messagebox
import math

class Bill_App:
        def __init__(self,root):
                
                self.root=root
                self.root.title("Kathi menu")
                self.root.geometry("1550x800")

                # ========================================Varial=bles===============================

                self.c_name=StringVar()
                self.c_Phone=StringVar()
                self.bill_no=StringVar()
                z=random.randint(1000,9999)
                self.bill_no.set(z)
                self.c_email=StringVar()
                self.search_bill=StringVar()
                self.product=StringVar()
                self.prices=StringVar()
                self.qty=IntVar()
                self.sub_total=StringVar()
                self.tax_input=StringVar()
                self.total=StringVar()


                #product_cat
                self.Category=["Select Option","noodles and more","Freshly Bread Express","Blended Cold Beverages & more" ]
                self.subCatnoodles=["special & select","Premium","Exotic","Limited "]

                        #special self
                self.special=["Original_Maggi","Double_Maggi","Butter Maggi","oregano Maggi","Rosemary","Corn"]
                self.price_Original_Maggi=40
                self.price_Double_Maggi=45
                self.price_Butter=50
                self.price_oregano_Maggi=50
                self.price_Rosemary=50
                self.price_corn=50

                        #Premium self
                self.Premium=["Atta Masala","Onion Capsicum","peri peri","Fusion Maggi","Oats Masala"]
                self.price_Atta=55
                self.price_onion=55
                self.price_peri=55
                self.price_Fusion=55
                self.price_oats=55

                        #exotic self

                self.exotic=["Butter Double masala","Chess Maggi","Butter Garlic","Sehezwan","Chili garlic","Cheese Macaroni"]
                self.price_butter=60
                self.price_chess=60
                self.price_garlic=60
                self.price_sehezwan=60
                self.price_Chili_garlic=60
                self.price_Cheese_Macaroni=60

                #Limited self
                
                self.limited=["Onion Capsicum Butter Maggi","Corn and cheese",'chilli Garlic Cheese']
                self.price_onion=70
                self.price_Corn=70
                self.price_chilli=70

                        #Freshly Bread Express
                self.subCatFreshly_Bread_Express=["Select","Premium","Exotic","Limited"]
                self.Select=["Espresso","cardamom Tea","Milk","Masala Tea"]
                self.price_Espresso=20
                self.price_cardamom=20
                self.price_milk=20
                self.price_masala=20

                        #premium in bread
                self.premium=["Cappuccino","Cafe latte","Ginger & honey tea"]
                self.price_Cappuccino=30
                self.price_Cafe_latte=30
                self.price_Ginger=30

                        #Exotic
                self.Exotic=["Cafe Macha","Hot chocolate"]
                self.price_Macha=35
                self.price_chocolate=35
        
                

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

                self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_Phone,font=("times new roman",12,"bold"),width=24)
                self.entry_mob.grid(row=0,column=1)

                self.lblCustName=Label(Cust_Frame,font=('arial',12,'bold'),bg="white",text="Customer Name",bd=4)
                self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

                self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=('arial',10,'bold'),width=24)
                self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)

                self.lblEmail=Label(Cust_Frame,font=('arial',12,'bold'),bg="white",text="Email",bd=4)
                self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

                self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=('arial',10,'bold'),width=24)
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
                self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)


                        #================================SubCategory=====================================
                self.lblSubCategory=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Subcategory",bd=4)
                self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

                self.ComboSubCategory=ttk.Combobox(Product_Frame,value=[""],state="readonly",font=('arial',10,'bold'),width=24)
                self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
                self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)

                        #=============================Product Name========================================================
                self.lblproduct=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Product Name",bd=4)
                self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

                self.ComboProduct=ttk.Combobox(Product_Frame,state="readonly",textvariable=self.product,font=('arial',10,'bold'),width=24)
                self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
                self.ComboProduct.bind("<<ComboboxSelected>>",self.price)
                        #========================================Price============================================
                self.lblPrice=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Price",bd=4)
                self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

                self.ComboPrice=ttk.Combobox(Product_Frame,value=[""],state="readonly",textvariable=self.prices,font=('arial',10,'bold'),width=24)
                self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)
                self.ComboPrice.bind("<<ComboboxSelected>>",self.price_add)


                        #========================================Qty======================================================
                self.lblQty=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Qty",bd=4)
                self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

                self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=('arial',10,'bold'),width=26)
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

                self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=('arial',10,'bold'),width=24)
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

                self.BtnAddToCart=Button(Btn_Frame,text="Add to Cart",command=self.AddItem,font=("arial",15,"bold"),bg="Orangered",fg="white",width=15,cursor="hand2")
                self.BtnAddToCart.grid(row=0,column=0)

                        # ==============================================

                self.Btngenerate_bill=Button(Btn_Frame,text="Generate",command=self.gen_bill,font=("arial",15,"bold"),bg="Orangered",fg="white",width=15,cursor="hand2")
                self.Btngenerate_bill.grid(row=0,column=1)

                        # =====================================================

                self.BtnSave=Button(Btn_Frame,text="Bill",command=self.save_bill,font=("arial",15,"bold"),bg="Orangered",fg="white",width=15,cursor="hand2")
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
                self.welcome()
        
                self.l=[]
        # ===============================Function Declaration===========================================
        def AddItem(self):
                self.n=self.prices.get()
                self.m=self.qty.get()*self.n
                self.l.append(self.m)
                if self.product.get()=="":
                        messagebox.showerror("Error","please select the Product Name")
                else:
                        self.textarea.insert(END,f"\n{self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
                        self.sub_total.set(str("Rs.%.2f"%(sum(self.l))))
                        self.tax_input.set(str('Rs.%,2f'%((((sum(self.l)) - (self.prices.get())))*18)/100))
                        self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*18)/100)))))
               

        def gen_bill(self):
                if self.product.get()=="":
                        messagebox.showerror("Error","Please Add To Cart Product")
                else:
                        text=self.textarea.get(10.0,(10.0+float(len(self.l))))
                        self.welcome()
                        self.textarea.insert(END,text)
                        self.textarea.insert(END,"\n==================================================")
                        self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
                        self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
                        self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
                        self.textarea.insert(END,"\n==================================================")
        
        def save_bill(self):
                op=messagebox.askyesno("Save Bill","Do you want to save the Bill ")
                if op>0:
                        self.bill_data=self.textarea.get(1.0,END)
                        f1=open("bills/"+str(self.bill_no.get())+".txt","w")
                        f1.write(self.bill_data)
                        op=messagebox.showinfo(f"Saved","Bill No:{self.bill_no.get()} saved successfully")
                        f1.close()


        def welcome(self):
                self.textarea.delete(1.0,END)
                self.textarea.insert(END,"\t Welcome to My Food")
                self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
                self.textarea.insert(END,f"\n Customer Number:{self.c_name.get()}")
                self.textarea.insert(END,f"\n Phone Number:{self.c_Phone.get()}")
                self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")

                self.textarea.insert(END,"\n==================================================")
                self.textarea.insert(END,f"\n Products\t\t\tQTY\t\tPrice")
                self.textarea.insert(END,"\n==================================================")
                # self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")






        def Categories(self,event=""):
                if self.Combo_Category.get()=="noodles and more":
                        self.ComboSubCategory.config(value=self.subCatnoodles)
                        self.ComboSubCategory.current(0)

                if self.Combo_Category.get()=="Freshly Bread Express":
                        self.ComboSubCategory.config(value=self.subCatFreshly_Bread_Express)
                        self.ComboSubCategory.current(0)

                if self.Combo_Category.get()=="Blended Cold Beverages & more":
                        self.ComboSubCategory.config(value=self.subCatnoodles)
                        self.ComboSubCategory.current(0)

        def Product_add(self,event=""):
                if self.ComboSubCategory.get()=="special & select":
                        self.ComboProduct.config(value=self.special)
                        self.ComboProduct.current(0)

                if self.ComboSubCategory.get()=="Premium":
                        self.ComboProduct.config(value=self.premium)
                        self.ComboProduct.current(0)

                if self.ComboSubCategory.get()=="Exotic":
                        self.ComboProduct.config(value=self.exotic)
                        self.ComboProduct.current(0)

                if self.ComboSubCategory.get()=="Limited":
                        self.ComboProduct.config(value=self.limited)
                        self.ComboProduct.current(0)

                # Freshly Bread Express

                if self.subCatFreshly_Bread_Express.get()=="Select":
                        self.ComboProduct.config(value=self.Select)
                        self.ComboProduct.current(0)

                if self.subCatFreshly_Bread_Express.get()=="Premium":
                        self.ComboProduct.config(value=self.premium)
                        self.ComboProduct.current(0)

                if self.subCatFreshly_Bread_Express.get()=="Exotic":
                        self.ComboProduct.config(value=self.Exotic)
                        self.ComboProduct.current(0)

                # Blended Cold Beverages & more

                if self.subCatFreshly_Bread_Express.get()=="Select":
                        self.ComboPrice.config(value=self.Select)
                        self.ComboProduct.current(0)

                if self.subCatFreshly_Bread_Express.get()=="Premium":
                        self.ComboProduct.config(value=self.premium)
                        self.ComboProduct.current(0)

                if self.subCatFreshly_Bread_Express.get()=="Exotic":
                        self.ComboProduct.config(value=self.Exotic)
                        self.ComboProduct.current(0)


        def price_add(self,event=""):

                if self.special.get()=="Original_Maggi":
                        self.ComboPrice.config(value=self.price_Original_Maggi)
                        self.ComboPrice.current(0)

                if self.special.get()=="Double_Maggi":
                        self.ComboPrice.config(value=self.price_Double_Maggi)
                        self.ComboPrice.current(0)

                if self.special.get()=="Butter Maggi":
                        self.ComboPrice.config(value=self.price_Butter)
                        self.ComboPrice.current(0)

                if self.special.get()=="oregano Maggi":
                        self.ComboPrice.config(value=self.price_oregano_Maggi)
                        self.ComboPrice.current(0)

                if self.special.get()=="Rosemary":
                        self.ComboPrice.config(value=self.price_Rosemary)
                        self.ComboPrice.current(0)

                if self.special.get()=="Corn":
                        self.ComboPrice.config(value=self.price_Corn)
                        self.ComboPrice.current(0)

                # Freshly Bread Express

                if self.subCatFreshly_Bread_Express.get()=="Select":
                        self.ComboPrice.config(value=self.Select)
                        self.ComboPrice.current(0)

                if self.subCatFreshly_Bread_Express.get()=="Premium":
                        self.ComboPrice.config(value=self.premium)
                        self.ComboPrice.current(0)

                if self.subCatFreshly_Bread_Express.get()=="Exotic":
                        self.ComboPrice.config(value=self.Exotic)
                        self.ComboPrice.current(0)

                # Blended Cold Beverages & more

                if self.subCatFreshly_Bread_Express.get()=="Select":
                        self.ComboPrice.config(value=self.Select)
                        self.ComboPrice.current(0)

                if self.subCatFreshly_Bread_Express.get()=="Premium":
                        self.ComboPrice.config(value=self.premium)
                        self.ComboPrice.current(0)

                if self.subCatFreshly_Bread_Express.get()=="Exotic":
                        self.ComboPrice.config(value=self.Exotic)
                        self.ComboPrice.current(0)
        def price(self,event=" "):
                #special
                if self.ComboProduct.get()=="Original_Maggi":
                        self.Comboprice.config(value=self.price_Original_Maggi) 
                        self.ComboPrice.current(0)
                        self.qty.set(1)               
                if self.ComboProduct.get()=="Double_Maggi":
                        self.ComboPrice.config(value=self.price_Double_Maggi)
                        self.Comboprice.current(0)
                        self.qty.set(1)
                if self.ComboProduct.get()=="Butter Maggi":
                        self.ComboPrice.config(value=self.price_Butter)
                        self.Comboprice.current(0)
                        self.qty.set(1)
                if self.ComboProduct.get()=="oregano Maggi":
                        self.ComboPrice.config(value=self.price_oregano_Maggi)
                        self.Comboprice.current(0)
                        self.qty.set(1)
                if self.ComboProduct.get()=="Rosemary":
                        self.ComboPrice.config(value=self.price_Rosemary)
                        self.Comboprice.current(0)
                        self.qty.set(1)
                if self.ComboProduct.get()=="Corn":
                        self.ComboPrice.config(value=self.price_corn)
                        self.Comboprice.current(0)
                        self.qty.set(1)

                #premium

                if self.ComboProduct.get()=="Attama Masala":
                        self.ComboPrice.config(value=self.price_Atta)
                        self.Comboprice.current(0)
                        self.qty.set(1)
                if self.ComboProduct.get()=="Onion Capsicum":
                        self.ComboPrice.config(value=self.price_onion)
                        self.Comboprice.current(0)
                        self.qty.set(1)
                if self.ComboProduct.get()=="peri peri":
                        self.ComboPrice.config(value=self.price_peri)
                        self.Comboprice.current(0)
                        self.qty.set(1)
                if self.ComboProduct.get()=="Fusion Maggi":
                        self.ComboPrice.config(value=self.price_Fusion)
                        self.Comboprice.current(0)
                        self.qty.set(1)
                if self.ComboProduct.get()=="Oats Masala":
                        self.ComboPrice.config(value=self.price_oats)
                        self.Comboprice.current(0)
                        self.qty.set(1)
                
                #exotic

                if self.ComboProduct.get()=="Butter Doble masala":
                        self.ComboPrice.config(value=self.price_butter)
                        self.Comboprice.current(0)
                        self.qty.set(1)
                if self.ComboProduct.get()=="chess Maggi":
                        self.ComboPrice.config(value=self.price_chess)
                        self.Comboprice.current(0)
                        self.qty.set(1)
                if self.ComboProduct.get()=="Butter Garlic":
                        self.ComboPrice.config(value=self.price_garlic)
                        self.Comboprice.current(0)
                        self.qty.set(1)
                if self.ComboProduct.get()=="sehzwan":
                        self.ComboPrice.config(value=self.price_sehezwan)
                        self.Comboprice.current(0)
                        self.qty.set(1)
                if self.ComboProduct.get()=="Chili garlic":
                        self.ComboPrice.config(value=self.price_Chili_garlic)
                        self.Comboprice.current(0)
                        self.qty.set(1)
                if self.ComboProduct.get()=="Chess Macaroni":
                        self.ComboPrice.config(value=self.price_Cheese_Macaroni)
                        self.Comboprice.current(0)
                        self.qty.set(1)

                #limited

                if self.ComboProduct.get()=="onion Capsicum Butter Maggi":
                        self.ComboPrice.config(value=self.price_onion)
                        self.Comboprice.current(0)
                        self.qty.set(1)
                if self.ComboProduct.get()=="Corn and cheese":
                        self.ComboPrice.config(value=self.price_Corn)
                        self.Comboprice.current(0)
                        self.qty.set(1)
                if self.ComboProduct.get()=="chilli Garlic Cheese":
                        self.ComboPrice.config(value=self.price_chilli)
                        self.Comboprice.current(0)
                        self.qty.set(1)















         











if __name__=="__main__":
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()