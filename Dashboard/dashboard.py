from cProfile import label
from pydoc import text
from tkinter import *
from turtle import bgcolor
from tkmacosx import Button
from PIL import Image, ImageTk
from employee import employeeClass

#from sympy import root

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1450x1000+0+0')
        self.root.title('Inventory Management System')
        self.root.config(bg='white')

        #==== title session =====
        self.icon_title = PhotoImage(file='tesst_photo/logo5.png')
        title = Label(self.root,
        text='Inventory Management System',image= self.icon_title, compound=LEFT,
        font=('time new roman',40,'bold'),bg='#010c48',fg='white', anchor='w',padx=40).place(
            x=0, y=0, relwidth=1,height=70)

        #=== logout session ==== 
        btn_logout = Button(self.root,text='LogOut',
         font=('time new roman',15,'bold'),bg='#E42217',fg='white',cursor='hand2').place(
             x=1200, y=12,height=40, width=150)
       

        #=== Clock session ==== 
        self.lbl_clock =Label(self.root,text='Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS \t\t << Made By Assie H.O >>',
        font=('time new roman',15),bg='#4d636d',fg='white') 
        self.lbl_clock.place(x=0, y=70, relwidth=1,height=30)
        
        #=== Left Menus session ==== 
        #https://redketchup.io/icon-converter

        self.MenuLogo =Image.open('tesst_photo/Menu_logo8.png')
        self.MenuLogo= self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

        LetfMenu =Frame(self.root,bd=4, relief=RIDGE, bg='white')
        LetfMenu.place(x=0, y=102, width=200, height=800)

        lbl_menuLogo = Label(LetfMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side =TOP, fill=X)

         #=== Label Menu session ==== 
        self.icon_side = PhotoImage(file='tesst_photo/next_l 3.png') # button image

        lbl_menu = Label(LetfMenu,text='Menu',font=('time new roman',20,),bg='#009688').pack(side=TOP, fill=X)

        btn_employee = Button(LetfMenu,bd=6,text='Employee',command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",
        font=('time new roman',20,'bold'),bg='white',cursor='hand2').pack(side=TOP, fill=X)

        btn_supplier = Button(LetfMenu,bd=6,text='Supplier',image=self.icon_side,compound=LEFT,padx=5,anchor="w",
        font=('time new roman',20,'bold'),bg='white',cursor='hand2').pack(side=TOP, fill=X)

        btn_category = Button(LetfMenu,bd=6,text='Category',image=self.icon_side,compound=LEFT,padx=5,anchor="w",
        font=('time new roman',20,'bold'),bg='white',cursor='hand2').pack(side=TOP, fill=X)

        btn_product = Button(LetfMenu,bd=6,text='Product',image=self.icon_side,compound=LEFT,padx=5,anchor="w",
        font=('time new roman',20,'bold'),bg='white',cursor='hand2').pack(side=TOP, fill=X)

        btn_sale = Button(LetfMenu,bd=6,text='Sales',image=self.icon_side,compound=LEFT,padx=5,anchor="w",
        font=('time new roman',20,'bold'),bg='white',cursor='hand2').pack(side=TOP, fill=X)

        btn_exit = Button(LetfMenu,bd=6,text='Exit',image=self.icon_side,compound=LEFT,padx=5,anchor="w",
        font=('time new roman',20,'bold'),bg='white',cursor='hand2').pack(side=TOP, fill=X)

        lbl_menuLogo = Label(LetfMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side =BOTTOM, fill=X)

          #=== Content session ==== 
        self.lbl_employee = Label(self.root,bd=5,relief=RIDGE, text='Total Employees\n[0]',bg='#33bbf9',fg='white',font=('groudy old style',20, 'bold'))
        self.lbl_employee.place(x =300, y=120, height=150, width=300)

        self.lbl_supplier = Label(self.root,bd=5,relief=RIDGE, text='Total Suppliers\n[0]',bg='#ff5722',fg='white',font=('groudy old style',20, 'bold'))
        self.lbl_supplier.place(x =650, y=120, height=150, width=300)

        self.lbl_category= Label(self.root,bd=5,relief=RIDGE, text='Total Categories\n[0]',bg='#009688',fg='white',font=('groudy old style',20, 'bold'))
        self.lbl_category.place(x =1000, y=120, height=150, width=300)

        self.lbl_product = Label(self.root,bd=5,relief=RIDGE, text='Total Products\n[0]',bg='#607d8b',fg='white',font=('groudy old style',20, 'bold'))
        self.lbl_product.place(x =300, y=300, height=150, width=300)

        self.lbl_sales = Label(self.root,bd=5,relief=RIDGE, text='Total Sales\n[0]',bg='#ffc107',fg='white',font=('groudy old style',20, 'bold'))
        self.lbl_sales.place(x =650, y=300, height=150, width=300)
        

       #=== footer session ==== 
        lbl_footer =Label(self.root,
        text='IMS-Inventory Management System | Developed By<<Assie H Olivier>> In 2023\nFor any Technical Issue Contact: +225 0707xxx621',
        font=('time new roman',12),bg='#4d636d',fg='white').pack(side=BOTTOM,fill=X)

    ## ======================================================================================================================================================

    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)
 


       
if __name__=="__main__":
    root =Tk()
    obj = IMS(root)
    root.mainloop()
# 