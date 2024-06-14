from fastapi import FastAPI
from all_instance import *
app = FastAPI()



#------------------------------------------------------------------  Ta's API
@app.post("/login_check")
async def login_chack(data : dict):
    usename_p = data["name_p"]
    password_p = data["pass_p"]
    status = S.checklogin(usename_p,password_p)
    return {"data" : status}

@app.post("/Register")
async def call_logincheck(data : dict):
    prefix_c = data["prefix_p"]
    fname_c  = data["fname_p"]   
    lname_c  = data["lname_p"]
    email_c  = data["email_p"]
    mobile_c = data["mobile_p"]
    pass_c   = data["pass_p"]
    exist = S.checkexist_email(email_c)
    print(exist)
    if exist == True:
        return {"data" : exist}
    person = S.create_user(prefix_c,fname_c,lname_c,email_c,mobile_c,pass_c)
    return {"data" : person}

#------------------------------------------------------------------------------



#-----------------------------------------------------------------  Run's API
@app.post("/get_show_pizza", tags=["pizza"])
async def get_pizza():
    print("APi Show")
    pizza_message = []
    for u in S.pizza_catalog.list:
        pizza_message.append([u.name, u.list_of_price[0], u.picture_name])      # เพิ่ม picture_name 
        print("API   ", [u.name, u.list_of_price[0], u.picture_name])

    return {"pizzadata" : pizza_message}
    
@app.post("/get_show_drink", tags=["drink"])
async def get_drink():  
    drink_message = []
    for u in S.drink_catalog.list:
        drink_message.append([u.name, u.list_of_price[0], u.picture_name])      # เพิ่ม picture_name 
    
    return {"drinkdata" : drink_message}

@app.post("/getbill", tags=["bill"])
async def get_bill():
    user1 = S.current_user
    payment1.total = user1.cart.total_price
    payment1.payment_date = date.today()

    bill1 = Bill(user1, address1, payment1)
    S.add_bill(bill1)
    return {"showbill" : bill1.showinfo()}

@app.post("/add_address")
async def get_address(data : dict):
    global address1
    address1 = Address(data["mooban"],data["house"],data["roadname"],data["soi"],data["subsoi"],data["district"],data["provoince"],data["postalcode"])

    
    return {"data" : "sucessful"}

@app.post("/cash")
async def cash(data : dict):
    global payment1
    payment1 = Cash("10apr","paid", "cash","599" )

    return {"cashdata" : "sucessful"}

@app.post("/creditcard")
async def creditcard(data : dict):
    global payment1
    payment1 = CreditCardInfomation("","paid", "creditcard", "599",data["card_name"],data["expiration_date"],data["card_numbers"],data["cvv"])

    return {"creditcarddata" : "sucessful"}
#---------------------------------------------------------------------------



#------------------------------------------------------------------  FIGHTER's API

@app.post('/create_pizza_item')
def create_pizza_item(data : dict) -> dict:
    pizza_name = data["pizza_name"]
    crust_value = int(data["crust_value"])
    cook_value = int(data["cook_value"])
    cheese_value = int(data["cheese_value"])
    sauce_value = int(data["sauce_value"])
    seasoning_package_value = int(data["seasoning_package_value"])
    quantity_value = data["quantity_value"]
    for pizza in S.pizza_catalog.list:
        if pizza_name == pizza.name:
            user1 = S.current_user
            user1.add_pizza_to_cart(pizza, \
                                    CrustSize(crust_value), \
                                    CookOption(cook_value), \
                                    CheeseOption(cheese_value), \
                                    SauceOption(sauce_value), \
                                    SeasoningPacket(seasoning_package_value), \
                                    quantity_value )
            print("Added pizza to cart  SHOW ITEM IN CART:")
            user1.cart.calculate_total_price()
            return {"status" : "success"}
    return {"status" : "fail"}
    
@app.post('/create_drink_item')
def create_drink_item(data : dict) -> dict:
    drink_name = data["drink_name"]
    #size_value = int(data["drink_value"])
    drink_quantity_value = data["drink_quantity_value"]
    for drink in S.drink_catalog.list:
        if drink_name == drink.name:
            user1 = S.current_user
            user1.add_drink_to_cart(drink, \
                                    drink_quantity_value )
            print("Added drink to cart  SHOW ITEM IN CART:")
            user1.cart.calculate_total_price()
            return {"status" : "success"}
    return {"status" : "fail"}

@app.post('/calculate_pizza_price')
def calculate_pizza_price(data : dict) -> dict:
    pizza_name = data["pizza_name"]
    crust_value = int(data["crust_value"])
    cook_value = int(data["cook_value"])
    cheese_value = int(data["cheese_value"])
    sauce_value = int(data["sauce_value"])
    seasoning_package_value = int(data["seasoning_package_value"])
    quantity_value = data["quantity_value"]
    for pizza in S.pizza_catalog.list:
        if pizza_name == pizza.name:
            pizza_item = PizzaItem(pizza, \
                                    CrustSize(crust_value), \
                                    CookOption(cook_value), \
                                    CheeseOption(cheese_value), \
                                    SauceOption(sauce_value), \
                                    SeasoningPacket(seasoning_package_value), \
                                    quantity_value )
            price = pizza_item.calculate_price()
            return {"price" : price}
        
@app.post('/calculate_drink_price')
def calculate_drink_price(data : dict) -> dict:
    drink_name = data["drink_name"]
    
    drink_quantity_value = data["drink_quantity_value"]
    for drink in S.drink_catalog.list:
        if drink_name == drink.name:
            
            drink_item = DrinkItem(drink, \
                                    drink_quantity_value )
            
            price = drink_item.calculate_price()
            return {"price" : price}
    
@app.post('/get_price_pizza_detail')
def get_price_pizza_detail(data : dict):
    pizza_name = data["pizza_name"]
    for pizza in S.pizza_catalog.list:
        if pizza_name == pizza.name:
            list_price = pizza.list_of_price
            return {"list_of_price" : list_price}
    return {"list_of_price" : "fail"}

@app.post('/get_price_drink_detail')
def get_price_pizza_detail(data : dict):
    drink_name = data["drink_name"]
    for drink in S.drink_catalog.list:
        if drink_name == drink.name:
            list_price = drink.list_of_price
            return {"list_of_price" : list_price}
    return {"list_of_price" : "fail"}


@app.post('/view_cart')
def view_cart(data: dict):
    req = data["req"]
    if req == 1:
        print("API FUNCTION     user want to view cart")
        user1 = S.current_user
        user1.cart.calculate_total_price()
        print("API FUNCTION     END Process")
        return {"return" : user1.cart.item_list}
    else:
        return {"return" : "API FUNC  view cart  failed" }
    
@app.post('/edit_item')
def edit_item(data: dict) -> dict:
    no_item = int(data["no_item"])
    req = int(data["req"])
    user = S.current_user
    print("API FUNCTION     user want to change quantity")
    print(f"no_item : {no_item}      req : {req}")
    if CartRequirment(req) == CartRequirment.ADDONE:
        user.cart.item_list[no_item].quantity += 1
        print("API FUNCTION     ADDED       END Process")
        return {"status" : "success"}
    elif CartRequirment(req) == CartRequirment.MINUSONE:
        user.cart.item_list[no_item].quantity -= 1
        print("API FUNCTION     MINUSED     END Process")
        return {"status" : "success"}
    elif CartRequirment(req) == CartRequirment.CANCLE:
        user.cart.item_list.pop(no_item)
        print("API FUNCTION     CANCLED     END Process")
        return {"status" : "success"}
    else:
        return {"status" : "fail"}
    



#---------------------------------------- API     ADMIN  ----------------------------------------------
@app.post('/admin_login_check')
def admin_login_check(data : dict):
    usename_p = data["name_p"]
    password_p = data["pass_p"]
    status = S.check_admin_login(usename_p, password_p)
    return { "status" : status }


@app.post('/create_pizza_product', tags= ["ADMIN"])
def create_pizza_product(data : dict) -> dict:
    pizza_name = data["pizza_name"]
    list_of_price = data["list_of_price"]
    picture_name = data["picture_name"]
    pizza = S.admin.create_pizza_product(pizza_name, list_of_price, picture_name)
    S.pizza_catalog.add_item_to_list(pizza)
    print(isinstance(pizza, NormalPizza))
    return {"status" : "success"}

@app.post('/delete_pizza_product', tags= ["ADMIN"])
def delete_pizza_product(data : dict):
    pizza_name = data["pizza_name"]
    S.admin.delete_pizza_product(S.pizza_catalog.list, pizza_name)
    return {"status" : "success"}

@app.post('/create_drink_product', tags= ["ADMIN"])
def create_drink_product(data : dict) -> dict:
    drink_name = data["drink_name"]
    list_of_price = data["list_of_price"]
    picture_name = data["picture_name"]
    drink = S.admin.create_drink_product(drink_name, list_of_price, picture_name)
    S.drink_catalog.add_item_to_list(drink)
    return {"status" : "success" }

@app.post('/delete_drink_product', tags= ["ADMIN"])
def delete_drink_product(data : dict):
    drink_name = data["drink_name"]
    S.admin.delete_drink_product(S.drink_catalog.list, drink_name)
    return {"status" : "success"}

@app.post('/admin_view_bill', tags= ["ADMIN"])
def view_bill(data : dict):
    if data["req"] == True:
        return {"bill" : S.bill_list}



        