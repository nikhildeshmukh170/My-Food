from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from  tkinter import messagebox
class Bill_App:
    def AddItem(self):
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","plaease select the ")
        else:
            self.textarea.insert(END<"\n{self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_totl.set(str('Rs.%.2f'%(sum(self.1))))
            self.tax_input.set(str('Rs.%,2f'%((((sum(self.l)) - (self.prices.get())))*Tax)/100)))
            self.total.set(str('Rs,%,2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))
               