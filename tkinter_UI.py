from tkinter import *
import tkinter as tk
import requests
from tkinter import messagebox
from all_class import CrustSize
from all_class import CookOption
from all_class import CheeseOption
from all_class import SauceOption
from all_class import SeasoningPacket
import ast

ENDPOINT_USER_LOGIN = "http://127.0.0.1:8000/login_check"          
ENDPOINT_REGISTER = "http://127.0.0.1:8000/Register"

API_ADMIN_LOGIN = "http://127.0.0.1:8000/admin_login_check"

picture_folder = "img/"

root = Tk()
root.title("PIZZA MANIA")
root.geometry('800x500')

register_frame = Frame(root)
main_frame = Frame(root)
login_frame = Frame(root)

insert_address = Frame(root)
bill = Frame(root)

logo = PhotoImage(file = "img\LOGO.png")
root.iconphoto(False, logo)

showcatalog_frame = Frame(root)

admin_frame = Frame(root)

admin_view_bill_frame = Frame(root)

def login_page():
    root.geometry('800x450')
    main_frame.grid_forget()
    def login():
        payload = {
            "name_p"   : name.get(),
            "pass_p"   : password.get()
        }
        response = requests.post(ENDPOINT_USER_LOGIN, json=payload)
        if response.json()['data'] == True:
            messagebox.showinfo("showinfo", "Sucessfully")
            login_frame.grid_forget()
            catalog_page()
        else:
            messagebox.showinfo("showinfo", "Not found")
            login_frame.grid_forget()
            main_page()



    #------------------------------------------  for USER   ------------------------------------------
    name = StringVar()
    password = StringVar()
    login_label = Label(login_frame, text="USER Login", font=("Arial", 30))
    username_label = Label(login_frame, text="Username", font=("Arial", 16))
    username_entry = Entry(login_frame, textvariable=name ,font=("Arial", 16))
    password_entry = Entry(login_frame, textvariable=password, font=("Arial", 16))
    password_label = Label(login_frame, text="Password", font=("Arial", 16))
    login_button  = Button(login_frame, text="Login", font=("Arial", 16), command=login)

    login_label.grid(row=0, column=0, columnspan=2, pady=40)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1, pady=20)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1, pady=20)
    login_button.grid(row=3, column=0, columnspan=2, pady=30)
    #--------------------------------------------------------------------------------------------



    #------------------------------------------ for ADMIN ------------------------------------------
    def admin_login():
        payload = {
            "name_p"   : admin_name.get(),
            "pass_p"   : admin_password.get()
        }
        response = requests.post(API_ADMIN_LOGIN, json=payload)
        if response.json()["status"] == True:
            messagebox.showinfo("showinfo", "admin login Sucessfully")
            login_frame.grid_forget()
            admin_page()                # go to admin page
        else:
            messagebox.showinfo("showinfo", "Not found")
            login_frame.grid_forget()
            main_page()                 # ถ้า log in ไม่สำเร็จ    กลับไปที่   หน้าmain
    admin_name = StringVar()
    admin_password = StringVar()
    admin_login_label = Label(login_frame, text="ADMIN LOGIN", font = ("Arial", 30))
    admin_username_label = Label(login_frame, text="Username", font = ("Arial", 16))
    admin_username_entry = Entry(login_frame, textvariable = admin_name ,font = ("Arial", 16))
    admin_password_entry = Entry(login_frame, textvariable = admin_password, font = ("Arial", 16))
    admin_password_label = Label(login_frame, text = "Password", font = ("Arial", 16))
    admin_login_button  = Button(login_frame, text="ADMIN Login", font=("Arial", 16), command= admin_login)

    admin_login_label.grid(row=0, column=2, columnspan=2, pady=40)
    admin_username_label.grid(row=1, column=2)
    admin_username_entry.grid(row=1, column=3, pady=20)
    admin_password_label.grid(row=2, column=2)
    admin_password_entry.grid(row=2, column=3, pady=20)
    admin_login_button.grid(row=3, column=2, columnspan=2, pady=30)
    

    login_frame.grid(column=0, row=0)

def register_page():
    main_frame.grid_forget()
    root.geometry('360x580')

    def register():
        if input_prefix.get() == "" or input_fname.get() == "" or input_lname.get() == "" or input_email.get() == "" or input_mobile.get() == "" or input_password.get() == "" :
            messagebox.showerror("EROR", "Please fill all information")
            return
        try:
            int(input_mobile.get())
        except ValueError:
            messagebox.showerror("EROR", "Mobile must be number")
            return
        
        if len(input_mobile.get()) != 10:
            messagebox.showerror("EROR", "Mobile must be 10 number")
            return
        payload = {
            "prefix_p"  : input_prefix.get(),
            "fname_p"   : input_fname.get(),
            "lname_p"   : input_lname.get(),
            "email_p"   : input_email.get(),
            "mobile_p"  : input_mobile.get(),
            "pass_p"    : input_password.get()
            }
        response = requests.post(ENDPOINT_REGISTER, json=payload)
        if response.json()['data'] == True:
            messagebox.showerror("EROR", "Email has already in use")
            return
        messagebox.showinfo("showinfo", response.json()['data'])
        register_frame.grid_forget()
        main_page()

    input_fname    = StringVar()
    input_password = StringVar()
    input_prefix   = StringVar()
    input_lname    = StringVar()
    input_email    = StringVar()
    input_mobile   = StringVar()

    login_label     = Label(register_frame, text="Register", font=("Arial", 30))
    prefix_label    = Label(register_frame, text="Prefix", font=("Arial", 16))
    prefix_entry    = Entry(register_frame, textvariable=input_prefix, font=("Arial", 16))
    fname_label     = Label(register_frame, text="Firstrname", font=("Arial", 16))
    fname_entry     = Entry(register_frame, textvariable=input_fname ,font=("Arial", 16))
    lname_label     = Label(register_frame, text="Lastname", font=("Arial", 16))
    lname_entry     = Entry(register_frame, textvariable=input_lname ,font=("Arial", 16))
    email_label     = Label(register_frame, text="email", font=("Arial", 16))
    email_entry     = Entry(register_frame, textvariable=input_email, font=("Arial", 16))
    mobile_lable    = Label(register_frame, text="mobile", font=("Arial", 16))
    mobile_entry    = Entry(register_frame, textvariable=input_mobile, font=("Arial", 16))
    password_label  = Label(register_frame, text="Password", font=("Arial", 16))
    password_entry  = Entry(register_frame, textvariable=input_password, font=("Arial", 16))
    login_button    = Button(register_frame, text="Submit", font=("Arial", 16), command=register)

    login_label.grid(row=0, column=0, columnspan=2, pady=40)
    prefix_label.grid(row=1, column=0)
    prefix_entry.grid(row=1, column=1)
    fname_label.grid(row=2, column=0)
    fname_entry.grid(row=2, column=1, pady=20)
    lname_label.grid(row=3, column=0)
    lname_entry.grid(row=3, column=1, pady=10)
    email_label.grid(row=4, column=0)
    email_entry.grid(row=4, column=1, pady=10)
    mobile_lable.grid(row=5, column=0)
    mobile_entry.grid(row=5, column=1, pady=10)
    password_label.grid(row=6, column=0)
    password_entry.grid(row=6, column=1, pady=10)
    login_button.grid(row=7, column=0, columnspan=2, pady=30)

    register_frame.grid(column=0, row=0)

def main_page():
    root.geometry('230x400')
    bill.grid_forget()
    showcatalog_frame.grid_forget()
    admin_frame.grid_forget()
    admin_view_bill_frame.grid_forget()

    welcome = Label(main_frame, text="Pizza mania", font=("Arial", 30))
    welcome.grid(row=1, column=0, columnspan=2, pady=40)

    loginbutt  = Button(main_frame, text="Login", font=("Arial", 16), command=login_page)
    loginbutt.grid(row=7, column=0, columnspan=2, pady=30)

    Registerbutt  = Button(main_frame, text="Register", font=("Arial", 16), command=register_page)
    Registerbutt.grid(row=9, column=0, columnspan=2, pady=30)

    main_frame.grid(column=0, row=0, columnspan=2, pady=30)

main_page()



#-----------------------------------------------------------   ADMIN    PAGE---------------------------------

API_ADMIN_CREATE_PIZZA_PRODUCT = "http://127.0.0.1:8000/create_pizza_product"
API_ADMIN_DELETE_PIZZA_PRODUCT = "http://127.0.0.1:8000/delete_pizza_product"
API_ADMIN_CREATE_DRINK_PRODUCT = "http://127.0.0.1:8000/create_drink_product"
API_ADMIN_DELETE_DRINK_PRODUCT = "http://127.0.0.1:8000/delete_drink_product"
API_ADMIN_VIEW_BILL = "http://127.0.0.1:8000/admin_view_bill"


def admin_page():
    root.geometry("800x500")
    login_frame.grid_forget()            #       main  ->  admin   จึงต้อง grid_forget()  เฟรมก่อหน้า  นั่นก์คือ main_frame
    

    def clear_frame():
        for widget in admin_view_bill_frame.winfo_children():
            widget.destroy()
    clear_frame()

    def add_pizza():
        
        payload = {
            "pizza_name"  : add_pizza_name.get(),
            "list_of_price"   : ast.literal_eval(pizza_list_of_price.get()),       #แปลงเป็น list ก่อนที่จะส่งไปที่ API
            "picture_name" : pizza_picture_name.get()

            }
        response = requests.post(API_ADMIN_CREATE_PIZZA_PRODUCT, json=payload)
        if response.json()["status"] == "success":
            messagebox.showinfo("STATUS" , "ADD PIZZA SUCCESS")


    def delete_pizza():
        payload = {
            "pizza_name" : delete_pizza_name.get()
        }
        response = requests.post(API_ADMIN_DELETE_PIZZA_PRODUCT, json = payload)
        if response.json()["status"] == "success":
            messagebox.showinfo("STATUS" , "DELETE PIZZA SUCCESS")

    def add_drink():
    
        payload = {
            "drink_name"  : add_drink_name.get(),
            "list_of_price"   : ast.literal_eval(drink_list_of_price.get()),       #แปลงเป็น list ก่อนที่จะส่งไปที่ API
            "picture_name" : drink_picture_name.get()

            }
        response = requests.post(API_ADMIN_CREATE_DRINK_PRODUCT, json = payload)
        if response.json()["status"] == "success":
            messagebox.showinfo("STATUS" , "ADD DRINK SUCCESS")

    def delete_drink():
        payload = {
            "drink_name" : delete_drink_name.get()
        }
        response = requests.post(API_ADMIN_DELETE_DRINK_PRODUCT, json = payload)
        if response.json()["status"] == "success":
            messagebox.showinfo("STATUS" , "DELETE DRINK SUCCESS")

    def view_bill():
        payload = {
            "req" : True
        }
        clear_frame()
        root.geometry("1400x500")
        response = requests.post(API_ADMIN_VIEW_BILL, json = payload)
        bill = response.json()["bill"]
        data_row = 6
        for data_bill in bill:
            fir_name = data_bill["_Bill__user"]['_User__register_data']['_RegisterData__firstname']
            las_name = data_bill["_Bill__user"]['_User__register_data']['_RegisterData__lastname']
            Label(admin_view_bill_frame ,text= fir_name + ' ' + las_name, bg = 'light coral').grid(row= data_row)
            data_row += 1
            cart_item_list = data_bill["_Bill__user"]['_User__cart']['_Cart__item_list']
            for item in cart_item_list:
                a = list(item.keys())
                if a[0] == '_PizzaItem__pizza':
                    Label(admin_view_bill_frame, text = "Pizza : " + str(item['_PizzaItem__pizza']['_Product__name']), bg = "goldenrod").grid(row = data_row + 1)
                    Label(admin_view_bill_frame, text = CrustSize(item['_PizzaItem__crust'])).grid(row =data_row + 2)
                    Label(admin_view_bill_frame, text = CookOption(item['_PizzaItem__cook'])).grid(row =data_row + 3)
                    Label(admin_view_bill_frame, text = CheeseOption(item['_PizzaItem__cheese'])).grid(row = data_row + 4)
                    Label(admin_view_bill_frame, text = SauceOption(item['_PizzaItem__sauce'])).grid(row = data_row + 5)
                    Label(admin_view_bill_frame, text = SeasoningPacket(item['_PizzaItem__seasoning_package'])).grid(row =data_row + 6)
                    Label(admin_view_bill_frame, text = "quantity : "+ str(item['_PizzaItem__quantity'])).grid(row =data_row + 7)
                    Label(admin_view_bill_frame, text= "*****************").grid(row= data_row  + 8)
                    data_row += 8

                elif a[0] == '_DrinkItem__drink':
                    Label(admin_view_bill_frame, text = "Drink : " + str(item['_DrinkItem__drink']['_Product__name']), bg= 'sky blue').grid(row = data_row + 1)
                    Label(admin_view_bill_frame, text = "quantity : "+ str(item['_DrinkItem__quantity'])).grid(row =data_row + 2)
                    Label(admin_view_bill_frame, text= "*****************").grid(row= data_row + 3)
                    data_row += 3

            addresst = data_bill['_Bill__address']
            Label(admin_view_bill_frame, text = "Addres : " + str(addresst)).grid(row = data_row)
            data_row += 1
            payment = data_bill['_Bill__payment']
            Label(admin_view_bill_frame, text = "Payment : " + str(payment)).grid(row = data_row)
            data_row += 1


    log_out_btn = Button(admin_frame, text = "LOG OUT", command= main_page)
    log_out_btn.grid(row = 5, columnspan= 50, pady= 10)

    admin_view_bill_frame.grid(row = 6)



    #--------------------------------------------------------   ADD PIZZA   -------------------------------
    add_pizza_name = StringVar()
    add_pizza_name.set("ex. PEPERONI")
    pizza_list_of_price = StringVar()
    pizza_list_of_price.set("ex. [10, 50]")
    pizza_picture_name = StringVar()
    pizza_picture_name.set("ex. PEPPERONI.png")

    Label(admin_frame, text = "Pizza name :").grid(row = 1, column=0)
    Label(admin_frame, text = "List Pizza Price :").grid(row = 2, column=0)
    Label(admin_frame, text = "Picture name :").grid(row = 3, column=0)
    
    add_pizza_label = Label(admin_frame, text="ADD PIZZA PRODUCT", bg = "orange")
    add_pizza_label.grid(row =0, column= 0, columnspan = 2 )

    
    add_pizza_name_entry = Entry(admin_frame, textvariable= add_pizza_name)
    add_pizza_name_entry.grid(row = 1, column = 1)

    pizza_list_of_price_entry = Entry(admin_frame, textvariable= pizza_list_of_price)
    pizza_list_of_price_entry.grid(row = 2, column = 1)

    pizza_picture_name_entry = Entry(admin_frame, textvariable = pizza_picture_name)
    pizza_picture_name_entry.grid(row = 3, column = 1,)
    

    add_pizza_submit_btn = Button(admin_frame, text= " SUBMIT ADD PIZZA PRODUCT",  command= add_pizza)
    add_pizza_submit_btn.grid(row = 4, column = 0, columnspan=2)
    #--------------------------------------------------------   ADD PIZZA   -------------------------------


    #--------------------------------------------------------   DELETE PIZZA   -------------------------------
    delete_pizza_label = Label(admin_frame, text="DELETE PIZZA PRODUCT", bg = "yellow")
    delete_pizza_label.grid(row =0, column= 2, columnspan = 2 )

    delete_pizza_name = StringVar()
    delete_pizza_name.set("ex. PEPERONI")
    
    Label(admin_frame, text= "Pizza name :").grid(row = 1, column = 2)
    
    delete_pizza_name_entry = Entry(admin_frame, textvariable= delete_pizza_name)
    delete_pizza_name_entry.grid(row = 1, column = 3)
    
    delete_pizza_submit_btn = Button(admin_frame, text="SUBMIT DELETE PIZZA PRODUCT", command= delete_pizza)
    delete_pizza_submit_btn.grid(row = 2, column= 2, columnspan=2)
    #--------------------------------------------------------   DELETE PIZZA   -------------------------------

    #--------------------------------------------------------   ADD DRINK   -------------------------------
    add_drink_name = StringVar()
    add_drink_name.set("ex. COKE BOTTLE - 1.25L")
    drink_list_of_price = StringVar()
    drink_list_of_price.set("ex. [10, 50]")
    drink_picture_name = StringVar()
    drink_picture_name.set("ex. COKE_BOTTLE.png")

    Label(admin_frame, text = "Drink name :").grid(row = 1, column = 4)
    Label(admin_frame, text = "List Drink Price :").grid(row = 2, column = 4)
    Label(admin_frame, text = "Picture name :").grid(row = 3, column = 4 )
    
    add_pizza_label = Label(admin_frame, text="ADD DRINK PRODUCT", bg="aquamarine1")
    add_pizza_label.grid(row =0, column= 4, columnspan = 2 )

    
    add_drink_name_entry = Entry(admin_frame, textvariable= add_drink_name)
    add_drink_name_entry.grid(row = 1, column = 5)

    drink_list_of_price_entry = Entry(admin_frame, textvariable= drink_list_of_price)
    drink_list_of_price_entry.grid(row = 2, column = 5)

    drink_picture_name_entry = Entry(admin_frame, textvariable = drink_picture_name)
    drink_picture_name_entry.grid(row = 3, column = 5)
    

    add_drink_submit_btn = Button(admin_frame, text= " SUBMIT ADD PIZZA PRODUCT",  command= add_drink)
    add_drink_submit_btn.grid(row = 4, column = 4, columnspan=2)
    #--------------------------------------------------------   ADD PIZZA   -------------------------------

    #--------------------------------------------------------   DELETE DRINK   -------------------------------
    delete_drink_label = Label(admin_frame, text="DELETEDRINK PRODUCT", bg = "aquamarine3")
    delete_drink_label.grid(row =0, column= 6, columnspan = 2 )

    delete_drink_name = StringVar()
    delete_drink_name.set("ex. COKE BOTTLE")
    
    Label(admin_frame, text= "Drink name :").grid(row = 1, column = 6)
    
    delete_drink_name_entry = Entry(admin_frame, textvariable= delete_drink_name)
    delete_drink_name_entry.grid(row = 1, column = 7)
    
    delete_drink_submit_btn = Button(admin_frame, text="SUBMIT DELETE DRINK PRODUCT", command= delete_drink)
    delete_drink_submit_btn.grid(row = 2, column= 6, columnspan=2)
    #--------------------------------------------------------   DELETE PIZZA   -------------------------------

    view_bill_btn = Button(admin_frame, text="VIEW BILL", command= view_bill)
    view_bill_btn.grid(row = 5, column= 0)


    admin_frame.grid(column=0, row=0)

    





API_ENDPOINT1 = "http://127.0.0.1:8000/get_show_pizza"
API_ENDPOINT2 = "http://127.0.0.1:8000/get_show_drink"
pizzacatalog_frame = Frame(root)
drinkcatalog_frame = Frame(root)

def catalog_page():      
    root.geometry('230x600')
    view_cart_frame.grid_forget()
    create_pizza_order_frame.grid_forget()
    create_drink_order_frame.grid_forget()

    global picture_folder

   
    def clear_frame():                                          # ต้องเคลียปุ่มเก่าทิ้ง เพราะ ถ้าไม่เคลีย  สั่งลบเมนูไปแล้ว แต่ปุ่มยังอยู่
        for widget in pizzacatalog_frame.winfo_children():      # เคลียทั้ง pizza_frame   drink_frame ทีเดียวเลย
            widget.destroy()
        for widget in drinkcatalog_frame.winfo_children(): 
            widget.destroy()

    clear_frame()

    def show_pizza():   
        root.geometry('950x600')
        view_cart_frame.grid_forget()
        showcatalog_frame.grid_forget()
        drinkcatalog_frame.grid_forget()
    


        catalog_lable = Label(pizzacatalog_frame, text='Catalog', font=("Arial", 30))
        catalog_lable.grid(row=0, column=1,padx=40,pady=40)
        button2 = Button(pizzacatalog_frame,text = 'show drink',command = show_drink)
        button2.grid(row=1,  column=1,padx=40,pady=40)
        view_cart_button = Button(pizzacatalog_frame, text = "view cart", command= view_cart_page)
        view_cart_button.grid(row = 2, column= 1,padx=40,pady=40)
        response = requests.post(API_ENDPOINT1, json = {"data":1} )
        if response.ok:
            my_list = response.json()['pizzadata']          # my_list = [item1, item2, item3, ...]
            row_num = 0                                     # item ที่ส่งมา  เป็นลิสที่มี สมาชิก 3 ตัว  [ name, listof_price[0], picture_name ]
            clo_num = 2                                     
            img_cout = 0
    
            pizza_photo = []
            for item in my_list:                 
                pizza_photo.append(PhotoImage(file = picture_folder +  item[2]))        #  "img/"  + "ROSA.png" == "img/ROZA.png"
                Button(pizzacatalog_frame,text = item[0], image= pizza_photo[img_cout], compound = TOP,command =lambda i = item[0] : create_pizza_order_page(i)).grid(row=row_num, column=clo_num)
                Button.image = lambda i = img_cout : pizza_photo[i]             #ให้ artibute image ของ Class Button มี reference   ถ้าไม่มี reference  ภาพจะไม่โชว์
                                                                                # อ้างอิง https://python-forum.io/thread-34094.html
                                                                                # ใช้ lambda เพราะ ถ้าไม่ใช้      pizza_photo[i] จะอ้างอิงตัวสุดท้าย
                row_num += 1
                img_cout += 1
                if row_num % 4 == 0:
                    clo_num += 1
                    row_num = 0
            pizzacatalog_frame.grid(row=0,column=0)
        

    def show_drink():    
        root.geometry('1050x600')
        view_cart_frame.grid_forget()
        showcatalog_frame.grid_forget()
        pizzacatalog_frame.grid_forget()


        catalog_lable = Label(drinkcatalog_frame, text='Catalog', font=("Arial", 30))
        catalog_lable.grid(row=0, column=1,padx=40,pady=40)
        button = Button(drinkcatalog_frame,text = 'show pizza',command = show_pizza)
        button.grid(row=1, column=1,padx=40,pady=40)
        view_cart_button = Button(drinkcatalog_frame, text = "view cart", command= view_cart_page)
        view_cart_button.grid(row = 2, column= 1,padx=40,pady=40)

        response = requests.post(API_ENDPOINT2, json = {"data":2} )     
        my_list = response.json()['drinkdata']                          # my_list = [item1, item2, item3, ...]
        row_num = 0                                                      # item ที่ส่งมา  เป็นลิสที่มี สมาชิก 3 ตัว  [ name, listof_price[0], picture_name ]
        clo_num = 2
        img_cout = 0

        drink_photo = []
        for item in my_list:
            drink_photo.append(PhotoImage(file = picture_folder + item[2]))     #  "img/"  + "COKE.png" == "img/ROZA.png"
            Button(drinkcatalog_frame,text = item[0], image = drink_photo[img_cout], compound = TOP, command = lambda i = item[0] : create_drink_order_page(i)).grid(row=row_num, column=clo_num)
            Button.image = lambda i = img_cout : drink_photo[i]             #ให้ artibute image ของ Class Button มี reference   ถ้าไม่มี reference  ภาพจะไม่โชว์
            row_num += 1                                                    # อ้างอิง https://python-forum.io/thread-34094.html
            img_cout += 1                                                   # ใช้ lambda เพราะ ถ้าไม่ใช้      pizza_photo[i] จะอ้างอิงตัวสุดท้าย
            if row_num % 4 == 0:
                clo_num += 1
                row_num = 0
        drinkcatalog_frame.grid(row=0,column=0)

    catalog_lable = Label(showcatalog_frame, text='Catalog', font=("Arial", 30))
    catalog_lable.grid(row=0, column=1,padx=40, pady=40)
    button = Button(showcatalog_frame,text = 'show pizza',command = show_pizza)
    button.grid(row=1, column=1,padx=40, pady=40)
    button2 = Button(showcatalog_frame,text = 'show drink',command = show_drink)
    button2.grid(row=2,  column=1,padx=40, pady=40)
    view_cart_button = Button(showcatalog_frame, text = "view cart", command= view_cart_page)
    view_cart_button.grid(row = 3, column= 1,padx=40, pady=40)

    log_out_button = Button(showcatalog_frame, text= "LOG OUT", command= main_page)
    log_out_button.grid(row = 4, column= 1, padx=40, pady=40)


    showcatalog_frame.grid(row=0,column=0)




#-------------------------------------------------- TK   FIGHTER    --------------------------------------------------------

API_CREATE_PIZZA_ITEM = "http://127.0.0.1:8000/create_pizza_item"
API_CREATE_DRINK_ITEM = "http://127.0.0.1:8000/create_drink_item"
API_VIEW_CART = "http://127.0.0.1:8000/view_cart"
API_EDIT_ITEM = "http://127.0.0.1:8000/edit_item"
API_GET_PRICE_PIZZA_DETAIL = "http://127.0.0.1:8000/get_price_pizza_detail"
API_GET_PRICE_DRINK_DETAIL = "http://127.0.0.1:8000/get_price_drink_detail"
API_CALCULATE_PIZZA_PRICE = "http://127.0.0.1:8000/calculate_pizza_price"
API_CALCULATE_drink_PRICE = "http://127.0.0.1:8000/calculate_drink_price"


create_pizza_order_frame = Frame(root)


def create_pizza_order_page(pizza_name):
    root.geometry("800x500")
    pizzacatalog_frame.grid_forget()

    

    def get_pizza_item_req():
        block_list = ['S', 'T', None]
        if  pizza_crust_value.get()[0] in block_list or pizza_cook_value.get()[0] in block_list or pizza_cheese_value.get()[0] in block_list \
             or pizza_sauce_value.get()[0] in block_list or pizza_seasoning_package_value.get()[0] in block_list:
            messagebox.showerror("Caution", "คุณยังกรอกข้อมูลสินค้าไม่ครบถ้วน")
        elif isinstance(pizza_quantity_value.get(), int) == False:
            messagebox.showerror("Caution", "ขออภัย   ช่อง Quantity กรุณากรอกแต่ ตัวเลข เท่านั้น")
        else:    
            payload = {
                        "pizza_name" : pizza_name,
                        "crust_value" : pizza_crust_value.get()[0],
                        "cook_value" : pizza_cook_value.get()[0],
                        "cheese_value" : pizza_cheese_value.get()[0],
                        "sauce_value" : pizza_sauce_value.get()[0],
                        "seasoning_package_value" : pizza_seasoning_package_value.get()[0],
                        "quantity_value" : pizza_quantity_value.get()
                        }
            response = requests.post(API_CREATE_PIZZA_ITEM, json = payload)
            if response.json()["status"] == "success":
                create_pizza_order_frame.grid_forget()     # ungrid pizza order frame
                catalog_page()
                return
    def calculate_pizza_price():
            block_list = ['S', 'T', None]
            if  pizza_crust_value.get()[0] in block_list or pizza_cook_value.get()[0] in block_list or pizza_cheese_value.get()[0] in block_list \
             or pizza_sauce_value.get()[0] in block_list or pizza_seasoning_package_value.get()[0] in block_list:
                messagebox.showerror("Caution", "คุณยังกรอกข้อมูลสินค้าไม่ครบถ้วน")
            elif isinstance(pizza_quantity_value.get(), int) == False:
                messagebox.showerror("Caution", "ขออภัย   ช่อง Quantity กรุณากรอกแต่ ตัวเลข เท่านั้น")
            else :payload = {
                        "pizza_name" : pizza_name,
                        "crust_value" : pizza_crust_value.get()[0],
                        "cook_value" : pizza_cook_value.get()[0],
                        "cheese_value" : pizza_cheese_value.get()[0],
                        "sauce_value" : pizza_sauce_value.get()[0],
                        "seasoning_package_value" : pizza_seasoning_package_value.get()[0],
                        "quantity_value" : pizza_quantity_value.get()
                        }
            response = requests.post(API_CALCULATE_PIZZA_PRICE, json = payload)
            price = response.json()["price"]        #490
            Label(create_pizza_order_frame, text = f"{price} Bath").grid(row = 14, column=1, padx = 10)

    def get_price_detail(pizza_name):
        payload = {
            "pizza_name" : pizza_name
                    }
        response = requests.post(API_GET_PRICE_PIZZA_DETAIL, json = payload)
        list_of_price = response.json()["list_of_price"]      #[90, 30]
        return list_of_price
            
            
    def clear_frame():
        for widget in create_pizza_order_frame.winfo_children(): 
            widget.destroy()
    clear_frame()
    # Create the list of options
    crust_list = ["1 WOOD_FIRED", "2 NEWYORKSTYLE"]
    cook_list  = ["1 NORMAL", "2 WELDONE"]
    cheese_list = ["1 NORMAL", "2 NOCHEESE", "3 LESSCHEESE", "4 EXTRACHEESE", "5 DOUBLECHEESE"]
    sauce_list = ["1 NORMAL", "2 NOSAUCE", "3 LESSSAUCE", "4 EXTRASAUCE"]
    seasoning_package_list = ["1 YES", "2 NO"]

    # Variable to keep track of the option
    # selected in OptionMenu
    pizza_crust_value = StringVar(create_pizza_order_frame)
    pizza_cook_value = StringVar(create_pizza_order_frame)
    pizza_cheese_value = StringVar(create_pizza_order_frame)
    pizza_sauce_value = StringVar(create_pizza_order_frame)
    pizza_seasoning_package_value = StringVar(create_pizza_order_frame)
    pizza_quantity_value = IntVar(create_pizza_order_frame)

    # Set the default value of the variable
    pizza_crust_value.set("Select Crust&Size")
    pizza_cook_value.set("Select Cook Option")
    pizza_cheese_value.set("Select Cheese Option")
    pizza_sauce_value.set("Select Sauce Options")
    pizza_seasoning_package_value.set("Select Seasoning Package")
    pizza_quantity_value.set("Type quantity")

    pizza_name_menu = Label(create_pizza_order_frame, text = str(pizza_name), width=20, justify="left")
    pizza_name_menu.grid(row = 1 , sticky='E')

    list_of_price = get_price_detail(pizza_name)
    show_price_WOOD_FIRED = Label(create_pizza_order_frame, text = f"1 WOOD_FIRED: {list_of_price[0]} Bath")
    show_price_WOOD_FIRED.grid(row = 2)
    show_price_NEWYORKSTYLE = Label(create_pizza_order_frame, text = f"2 NEWYORKSTYLE: {list_of_price[1]} Bath")
    show_price_NEWYORKSTYLE.grid(row = 3)
    show_price_EXTRACHEESE = Label(create_pizza_order_frame, text = "4 EXTRACHEESE: +30 Bath")
    show_price_EXTRACHEESE.grid(row = 4)
    show_price_DOUBLECHEESE = Label(create_pizza_order_frame, text = "5 DOUBLECHEESE: +60 Bath")
    show_price_DOUBLECHEESE.grid(row = 5)

    annoucement_label = Label(create_pizza_order_frame,text = "สามารถดูราคาสินค้าก่อนนำเข้าตะกร้า  ได้ที่ปุ่ม Calculate Price")       
    annoucement_label.grid(row = 6)
    clean_label = Label(create_pizza_order_frame)
    clean_label.grid(row = 7)

    crust_menu = OptionMenu(create_pizza_order_frame, pizza_crust_value, *crust_list)
    crust_menu.grid(row = 8 , sticky='E')
    cook_menu = OptionMenu(create_pizza_order_frame, pizza_cook_value, *cook_list)
    cook_menu.grid(row = 9 , sticky='E')
    cheese_menu = OptionMenu(create_pizza_order_frame, pizza_cheese_value, *cheese_list)
    cheese_menu.grid(row = 10 , sticky='E')
    sauce_menu = OptionMenu(create_pizza_order_frame, pizza_sauce_value, *sauce_list)
    sauce_menu.grid(row = 11 , sticky='E')
    seasoning_package_menu = OptionMenu(create_pizza_order_frame, pizza_seasoning_package_value, *seasoning_package_list)
    seasoning_package_menu.grid(row = 12 , sticky='E')
    quantity_menu = Entry(create_pizza_order_frame, textvariable=pizza_quantity_value, width=20, justify="left")
    quantity_menu.grid(row = 13 , sticky='E')
    # Submit button


    calculate_pizza_item_btn = Button(create_pizza_order_frame, text = "Calculate Price", command=calculate_pizza_price, bg = "orange")
    calculate_pizza_item_btn.grid(row = 14, sticky = 'E', pady =10)
    pizza_submit_button = Button(create_pizza_order_frame, text='Submit Pizza ITEM', command=get_pizza_item_req, bg="green")
    pizza_submit_button.grid(row = 15 , sticky='E', pady= 10)
    go_back_to_catalog_btn = Button(create_pizza_order_frame, text = "Go Back to Catalog", command = catalog_page, bg = "red")
    go_back_to_catalog_btn.grid(row = 16, sticky ='E', pady = 10)




    create_pizza_order_frame.grid()


create_drink_order_frame = Frame(root)
def create_drink_order_page(drink_name):
    root.geometry("800x500")
    drinkcatalog_frame.grid_forget()

    def clear_frame():
        for widget in create_drink_order_frame.winfo_children(): 
            widget.destroy()

    def get_drink_item_req():
        try: 
            isinstance(drink_quantity_value.get(), int) == False
        except: messagebox.showerror("Caution", "ขออภับ  Quantity กรอกได้แต่ ตัวเลข เท่านั้น")
        
             
        else :
            payload = {
                    "drink_name" : drink_name,
                    "drink_quantity_value" : drink_quantity_value.get()
                }
            response = requests.post(API_CREATE_DRINK_ITEM, json = payload)
            if response.ok:
                create_drink_order_frame.grid_forget()
                catalog_page()
       
            

    def calculate_drink_price():
        payload = {
                    "drink_name" : drink_name,
                    "drink_quantity_value" : drink_quantity_value.get()
                }
        response = requests.post(API_CALCULATE_drink_PRICE, json = payload)
        price = response.json()["price"]
        Label(create_drink_order_frame, text = f"{price} Bath").grid(row = 6, column= 1, sticky= 'E')



    def get_price_detail(drink_name):
        payload = {
            "drink_name" : drink_name
                    }
        response = requests.post(API_GET_PRICE_DRINK_DETAIL, json = payload)
        list_of_price = response.json()["list_of_price"]      #[90]
        return list_of_price
        
    clear_frame()

    drink_quantity_value = IntVar(create_drink_order_frame)

    drink_quantity_value.set("Type quantity")

    drink_name_menu = Label(create_drink_order_frame ,text = drink_name)
    drink_name_menu.grid(row = 1, sticky= 'E')

    list_of_price = get_price_detail(drink_name)
    show_price_PEICE_PER_UNIT = Label(create_drink_order_frame, text = f"PRICE PER UNIT: {list_of_price[0]} Bath")
    show_price_PEICE_PER_UNIT.grid(row = 2, sticky= 'E')
    

    annoucement_label = Label(create_drink_order_frame,text = "สามารถดูราคาสินค้าก่อนนำเข้าตะกร้า  ได้ที่ปุ่ม Calculate Price")       
    annoucement_label.grid(row = 3)
    clean_label = Label(create_pizza_order_frame)
    clean_label.grid(row = 4)


    drink_quantity_menu = Entry(create_drink_order_frame, textvariable=drink_quantity_value, width=20, justify="left")
    drink_quantity_menu.grid(row = 5 , sticky='E')

    calculate_drink_item_btn = Button(create_drink_order_frame, text = "Calculate Price", command=calculate_drink_price, bg = "orange")
    calculate_drink_item_btn.grid(row = 6, sticky = 'E', pady =10)

    drink_submit_button = Button(create_drink_order_frame, text="Add to Cart", command=get_drink_item_req, bg="green")
    drink_submit_button.grid(row = 7 , sticky='E', pady= 10)

    go_back_to_catalog_btn = Button(create_drink_order_frame, text = "Go Back to Catalog", command = catalog_page, bg= "red")
    go_back_to_catalog_btn.grid(row = 8, sticky ='E', pady = 10)

    create_drink_order_frame.grid()



view_cart_frame = Frame(root)

list_label = []
def view_cart_page():
    root.geometry("600x500")
    pizzacatalog_frame.grid_forget()
    drinkcatalog_frame.grid_forget()
    showcatalog_frame.grid_forget()
    global list_label
    
    def clear_frame():
        for widget in view_cart_frame.winfo_children(): 
            widget.destroy()


    def add_item(no_item):
        payload = {
            "req" : 1,
            "no_item" : no_item
        }
        response = requests.post(API_EDIT_ITEM, json=payload)
        if response.json()["status"] == "success":
            view_cart_page()

    def minus_item(no_item):
        payload = {
            "req" : 2,
            "no_item" : no_item
        }
        response = requests.post(API_EDIT_ITEM, json = payload)
        if response.json()["status"] == "success":
            view_cart_page()
    def cancle_item(no_item):
        payload = {
            "req" : 3,
            "no_item" : no_item
        }
        response = requests.post(API_EDIT_ITEM, json = payload)
        if response.json()["status"] == "success":
            view_cart_page()
        
    def check_item_before_check_out(price):
        if price == 0:
            messagebox.showerror("Caution" , "ไม่มี item ใน ตระกร้า")
        else:
            change_to_insert_address()
            
        
    payload = {
        "req" : 1
    }
    response = requests.post(API_VIEW_CART, json=payload)
    item_list = response.json()['return']
    row_counter = 0
    clear_frame()

#{'_DrinkItem__drink': {'_Product__name': 'COKE - 325 ML', '_Product__list_of_price': [45], '_Product__description': "It's Coke.", '_Drink__size': 1}, '_DrinkItem__quantity': 3, '_DrinkItem__item_price': 135}
#{'_PizzaItem__pizza': {'_Product__name': 'CLASSIC CHEESE', '_Product__list_of_price': [285, 490], '_Product__description': 'Tomato sauce, mozzarella cheese', '_NormalPizza__spicy_level': 0, '_NormalPizza__suit_for_veget': 1}, '_PizzaItem__crust': 1, '_PizzaItem__cook': 1, '_PizzaItem__cheese': 1, '_PizzaItem__sauce': 1, '_PizzaItem__seasoning_package': 1, '_PizzaItem__quantity': 1, '_PizzaItem__item_price': 285}
    total_price = 0
    if len(item_list) == 0:
        total_price_label = Label(view_cart_frame, text = f"TOTAL : {total_price}", bg = "orange")
        total_price_label.grid(row = row_counter + 1, column = 6, pady = 10)
        go_to_catalog_btn = Button(view_cart_frame, text = "Continue Shopping", command = catalog_page, bg= "red")
        go_to_catalog_btn.grid(row = row_counter + 2, column = 6, pady = 10)
        
        go_to_add_address_btn = Button(view_cart_frame, text = "Proceed to Check out", command = lambda price = total_price : check_item_before_check_out(price), bg= "green")
        go_to_add_address_btn.grid(row = row_counter + 3, column = 6, pady = 10)
    for item in item_list:
            
        no_item = item_list.index(item)

        list_key_of_item = list(item.keys())

        if list_key_of_item[0] == '_PizzaItem__pizza':          #if this item is pizza 
      

            Label(view_cart_frame, text="Pizza Name: ", bg = "goldenrod").grid(row = row_counter + 1, column=0)
            Label(view_cart_frame, text=str(item["_PizzaItem__pizza"]["_Product__name"])).grid(row = row_counter + 1, column=1)

            
            Label(view_cart_frame, text="Crust: ").grid(row = row_counter + 2, column=0, )
            Label(view_cart_frame, text=str( CrustSize(item["_PizzaItem__crust"]) )).grid(row = row_counter + 2, column=1)

            Label(view_cart_frame, text="Cook: ").grid(row = row_counter + 3, column=0)
            Label(view_cart_frame, text=str(CookOption(item["_PizzaItem__cook"]))).grid(row = row_counter + 3, column=1)



            Label(view_cart_frame, text="Cheese: ").grid(row = row_counter + 4, column=0)
            Label(view_cart_frame, text=str(CheeseOption(item["_PizzaItem__cheese"]))).grid(row = row_counter + 4, column=1)



            Label(view_cart_frame, text="Sauce: ").grid(row = row_counter + 5, column=0)
            Label(view_cart_frame, text=str(SauceOption(item["_PizzaItem__sauce"]))).grid(row = row_counter + 5, column=1)



            Label(view_cart_frame, text="Seasoning Package: ").grid(row = row_counter + 6, column=0)
            Label(view_cart_frame, text=str(SeasoningPacket(item["_PizzaItem__seasoning_package"]))).grid(row = row_counter + 6, column=1)



            Label(view_cart_frame, text="Quantity: ").grid(row = row_counter + 7, column=0)
            Label(view_cart_frame, text=str(item["_PizzaItem__quantity"])).grid(row = row_counter + 7, column=1)



            Label(view_cart_frame, text="Price: ").grid(row = row_counter + 8, column=0)
            Label(view_cart_frame, text=str(item["_PizzaItem__item_price"])).grid(row = row_counter + 8, column=1)

            Label(view_cart_frame, text = "*********************").grid(row = row_counter + 9)

            

            total_price += item["_PizzaItem__item_price"]


            
            Button(view_cart_frame, text = '+', command = lambda no_item = no_item : add_item(no_item)).grid(row = row_counter + 7, column = 2)
            Button(view_cart_frame, text = '-', command = lambda no_item = no_item : minus_item(no_item)).grid(row = row_counter + 7, column = 3)
            Button(view_cart_frame, text = 'Cancle this Item', command = lambda no_item = no_item: cancle_item(no_item)).grid(row = row_counter + 7, column = 4)
            



            row_counter += 9

        elif list_key_of_item[0] == "_DrinkItem__drink":          #if this item is drink

            Label(view_cart_frame, text="Drink Name: ", bg = "sky blue").grid(row = row_counter + 1, column=0)
            Label(view_cart_frame, text=str(item["_DrinkItem__drink"]["_Product__name"])).grid(row = row_counter + 1, column=1)

            Label(view_cart_frame, text="Quantity: ").grid(row = row_counter + 2, column=0)
            Label(view_cart_frame, text=str(item["_DrinkItem__quantity"])).grid(row = row_counter + 2, column=1)

            Label(view_cart_frame, text="Price: ").grid(row = row_counter + 3, column=0)
            Label(view_cart_frame, text=str(item["_DrinkItem__item_price"])).grid(row = row_counter + 3, column=1)

            Label(view_cart_frame, text = "*********************").grid(row = row_counter + 4)

            total_price += item["_DrinkItem__item_price"]

            
            Button(view_cart_frame, text = '+', command = lambda no_item = no_item : add_item(no_item)).grid(row = row_counter + 2, column = 2)
            Button(view_cart_frame, text = '-', command = lambda no_item = no_item : minus_item(no_item)).grid(row = row_counter + 2, column = 3)
            Button(view_cart_frame, text = 'Cancle this Item', command = lambda no_item = no_item : cancle_item(no_item)).grid(row = row_counter + 2, column = 4)
        

            row_counter += 4

        # create button at final item
        
        if no_item == (len(item_list) - 1):

            Label(view_cart_frame, text = f"TOTAL : {total_price}", bg = "orange").grid(row = row_counter + 1, column = 6, pady = 10)

            Button(view_cart_frame, text = "Continue Shopping", command = catalog_page, bg= "red").grid(row = row_counter + 2, column = 6, pady = 10)
            Button(view_cart_frame, text = "Proceed to Check out", command = lambda price = total_price : check_item_before_check_out(price), bg= "green").grid(row = row_counter + 3, column = 6, pady = 10)
        
            row_counter += 2

    view_cart_frame.grid()


#--------------------------------------------------









#------------------------------------------------TK run      ADD drress     Cash and Credit Card   Cliclk Procedd TO CHECK OUT

API_ENDPOINT_add_address = "http://127.0.0.1:8000/add_address"
API_ENDPOINT_cash = "http://127.0.0.1:8000/cash"
API_ENDPOINT_creditcard = "http://127.0.0.1:8000/creditcard"
API_ENDPOINT_getbill = "http://127.0.0.1:8000/getbill"

submited = False
creditcard_submit = False

def change_to_insert_address():
    insert_address.grid()
    # un pack frame เก่า -------------------------------------------------------------------------------------------------------
    view_cart_frame.grid_forget()
    root.geometry("800x500")
    def address():
        global submited
        if input_mooban.get() == "" or input_house.get() == "" or input_roadname.get() == "" or input_soi.get() == "" or input_subsoi.get() == "" or input_district.get() == "" or input_provoince.get() == "" or input_postalcode.get() == "":
            submited = False
            messagebox.showerror("showinfo", "please insert all infomation")
        else :
            submited = True
            
        if submited == True:
            payload = {
                "mooban"  : input_mooban.get(),
                "house" : input_house.get(),
                "roadname" : input_roadname.get(),
                "soi" : input_soi.get(),
                "subsoi" : input_subsoi.get(),
                "district" : input_district.get(),
                "provoince" : input_provoince.get(),
                "postalcode" : input_postalcode.get()
                }
            response = requests.post(API_ENDPOINT_add_address, json=payload)
            messagebox.showinfo("showinfo", response.json()['data'])
    
    def cash():
        if submited == True:
            response = requests.post(API_ENDPOINT_cash, json = {"data":1})
            messagebox.showinfo("showinfo", response.json()['cashdata'])
            change_to_bill()
        else :
            messagebox.showerror("showinfo", "please submit delivery address")
        
    def creditcard():
        global creditcard_submit
        if input_card_name.get() == "" or input_expiration_date.get() == "" or input_card_numbers.get() == "" or input_cvv.get() == "":
            creditcard_submit = False
            messagebox.showerror("showinfo", "please insert all infomation")
        else :
            creditcard_submit = True
        if submited == True and creditcard_submit == True:
            payload = {
                "payment method"  : "creditcard",
                "card_name"  : input_card_name.get(),
                "expiration_date" :input_expiration_date.get(),
                "card_numbers" : input_card_numbers.get(),
                "cvv" : input_cvv.get()
                }
            response = requests.post(API_ENDPOINT_creditcard, json=payload)
            messagebox.showinfo("showinfo", response.json()['creditcarddata'])
            change_to_bill()
        elif submited == False:
            messagebox.showerror("showinfo", "please submit delivery address")



    input_mooban = StringVar()
    input_house = StringVar()
    input_roadname = StringVar()
    input_soi = StringVar()
    input_subsoi = StringVar()
    input_district = StringVar()
    input_provoince = StringVar()
    input_postalcode = StringVar()
    input_card_name = StringVar()
    input_expiration_date = StringVar()
    input_card_numbers = StringVar()
    input_cvv = StringVar()



    Address_label    = Label(insert_address, text="Insert Delivery Address", font=("Arial", 16))
    mooban_label    = Label(insert_address, text="mooban", font=("Arial", 16))
    house_label    = Label(insert_address, text="house", font=("Arial", 16))
    roadname_label = Label(insert_address, text="roadname", font=("Arial", 16))
    soi_label = Label(insert_address, text="soi", font=("Arial", 16))
    subsoi_label = Label(insert_address, text="subsoi", font=("Arial", 16))
    district_label = Label(insert_address, text="district", font=("Arial", 16))
    provoince_label = Label(insert_address, text="provoince", font=("Arial", 16))
    postalcode_label = Label(insert_address, text="postalcode", font=("Arial", 16))
    card_name_label = Label(insert_address, text="cardname", font=("Arial", 16))
    expiration_date_label = Label(insert_address, text="expiration date", font=("Arial", 16))
    card_numbers_label = Label(insert_address, text="card numbers", font=("Arial", 16))
    cvv_label = Label(insert_address, text="cvv", font=("Arial", 16))



    mooban_entry = Entry(insert_address, textvariable=input_mooban, font=("Arial", 16))
    house_entry = Entry(insert_address, textvariable=input_house, font=("Arial", 16))
    rosdname_entry = Entry(insert_address, textvariable=input_roadname, font=("Arial", 16))
    soi_entry = Entry(insert_address, textvariable=input_soi, font=("Arial", 16))
    subsoi_entry = Entry(insert_address, textvariable=input_subsoi, font=("Arial", 16))
    district_entry = Entry(insert_address, textvariable=input_district, font=("Arial", 16))
    provoince_entry = Entry(insert_address, textvariable=input_provoince, font=("Arial", 16))
    postalcode_entry = Entry(insert_address, textvariable=input_postalcode, font=("Arial", 16))
    card_name_entry = Entry(insert_address, textvariable=input_card_name, font=("Arial", 16))
    expiration_date_entry = Entry(insert_address, textvariable=input_expiration_date, font=("Arial", 16))
    card_numbers_entry = Entry(insert_address, textvariable=input_card_numbers, font=("Arial", 16))
    cvv_entry = Entry(insert_address, textvariable=input_cvv, font=("Arial", 16))


    submit_button = Button(insert_address, text="submit", font=("Arial", 16), command=address)

    Address_label.grid(row=0, column=1)

    mooban_label.grid(row=1, column=0)
    house_label.grid(row=2, column=0)
    roadname_label.grid(row=3, column=0)
    soi_label.grid(row=4, column=0)
    subsoi_label.grid(row=5, column=0)
    district_label.grid(row=6, column=0)
    provoince_label.grid(row=7, column=0)
    postalcode_label.grid(row=8, column=0)
    card_name_label.grid(row=1, column=2)
    expiration_date_label.grid(row=2, column=2)
    card_numbers_label.grid(row=3, column=2)
    cvv_label.grid(row=4, column=2)

    mooban_entry.grid(row=1, column=1)
    house_entry.grid(row=2, column=1)
    rosdname_entry.grid(row=3, column=1)
    soi_entry.grid(row=4, column=1)
    subsoi_entry.grid(row=5, column=1)
    district_entry.grid(row=6, column=1)
    provoince_entry.grid(row=7, column=1)
    postalcode_entry.grid(row=8, column=1)
    card_name_entry.grid(row=1, column=3)
    expiration_date_entry.grid(row=2, column=3)
    card_numbers_entry.grid(row=3, column=3)
    cvv_entry.grid(row=4, column=3)


    submit_button.grid(row=9, column=1)


    cash_button = Button(insert_address, text="cash", font=("Arial", 16), command=cash)
    creditcard_button = Button(insert_address, text="creditcard", font=("Arial", 16), command=creditcard)
    cash_button.grid(row=0, column=2)
    creditcard_button.grid(row=0, column=3)

def change_to_bill():
    root.geometry("560x580")
    bill.grid()
    insert_address.grid_forget()
    def showbill():
        
        response = requests.post(API_ENDPOINT_getbill, json = {"data":1} )
        #messagebox.showinfo("your bill", response.json()['showbill'])
        txt_output.delete(1.0,END)
        
        my_list = response.json()['showbill']
        print("my_list from API =  ", my_list)
        
        
        t = 0
        for item in my_list:
            txt_output.insert(END, item)
            if t <= len(my_list)-17 and t >= 4:
                txt_output.insert(END, "\n")
            elif t == 0:
                txt_output.insert(END, "\n")
            elif t == 3:
                txt_output.insert(END, "\n")
            elif t >= len(my_list)-15 and t <= len(my_list)-14:
                txt_output.insert(END, "\n")
            elif t == len(my_list)-5:
                txt_output.insert(END, "\n")
            elif t == len(my_list)-3:
                txt_output.insert(END, "\n")
            t += 1

    button = Button(bill,
        text = 'PROCEED TO CHECK OUT',
        command = showbill)
    button.grid(row = 0)  

    txt_output = Text(bill, height=30, width=70)
    txt_output.grid(row = 1)

    go_to_main_btn = Button(bill, text = "BACK TO MAIN", command= main_page)
    go_to_main_btn.grid(row = 2) 



root.mainloop()



