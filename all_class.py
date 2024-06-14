from abc import ABC, abstractmethod
import enum
from datetime import date

class CrustSize(enum.Enum):
    WOOD_FIRED = 1 
    NEWYORKSTYLE = 2 
class CookOption(enum.Enum):
    NORMAL = 1
    WELDONE = 2
class CheeseOption(enum.Enum):
    NORMAL = 1
    NOCHEESE = 2
    LESSCHEESE = 3
    EXTRACHEESE = 4
    DOUBLECHEESE = 5
class SauceOption(enum.Enum):
    NORMAL = 1
    NOSAUCE = 2
    LESSSAUCE = 3
    EXTRASAUCE = 4
class SeasoningPacket(enum.Enum):
    YES = 1
    NO = 2
class DrinkSize(enum.Enum):
    CAN = 1
    BOTTLE = 2
class AccountStatus(enum.Enum):
	ACTIVE = 1
	BLOCKED = 2
	BANNED = 3
	ARCHIVED = 4
	UNKNOWN = 5
class PaymentStatus(enum.Enum):
    PENDING = 1
    CONFIRMED = 2
    CANCLED = 3
class CartRequirment(enum.Enum):
    ADDONE = 1      # quantity +1
    MINUSONE = 2    # quantity -1
    CANCLE = 3      # cancle item

class System:
    def __init__(self):
        self.__user_list = []
        self.__bill_list = []
        self.__current_user = None
        self.__catalog = []
        self.__admin = None
                      # เพิ่มใหม่           มีAdmin แค่ 1 คน เท่าั้น

    @property
    def current_user(self):
        return self.__current_user
    
    @current_user.setter
    def current_user(self, value):
        self.__current_user = value

    @property
    def pizza_catalog(self):
        return self.__catalog[0]
    @property
    def drink_catalog(self):
        return self.__catalog[1]
    
            #                               สั่งแล้ว   log in ใหม่ไม่ได้

    @property
    def bill_list(self):
        return self.__bill_list
    
    @property
    def admin(self):
        return self.__admin
    
    @admin.setter
    def admiin(self, new_admin):
        self.__admin = new_admin




    def add_catalog(self, catalog):
        self.__catalog.append(catalog)

    def set_current_user(self, value):          #setter function
        self.__current_user = value

    def add_bill(self, value):
        self.__bill_list.append(value)
    
    def add_user(self, value):
        self.__user_list.append(value)

    def checkexist_email(self,value):
        print(value)
        for user in self.__user_list:
            if value == user.register_data.email:
                return True
        return False

    def create_user(self, nprefix, fname, lname ,email ,mobile ,password):
        register_data = RegisterData(nprefix,fname,lname,email,mobile,password)
        cart = Cart()
        user = User(register_data,cart)
        self.add_user(user)
        return "sucessfully"
        
    def checklogin(self, username, password):
        for user in self.__user_list:
            if username == user.register_data.email:
                if password == user.register_data.password:
                    self.__current_user = user
                    return True
        return False
    
    def create_admin(self, username, password):
        admin1 = Admin(username, password)
        self.__admin = admin1
    def check_admin_login(self, username, password):
            if username == self.__admin.username and password == self.__admin.password:
                return True
            else:
                return False
            

    

    
class Admin:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    
    @property
    def username(self):
        return self.__username
    @property
    def password(self):
        return self.__password
    
    def create_pizza_product(self, name, list_of_price, picture_name):
        pizza = NormalPizza(name, list_of_price, picture_name)
        return pizza
    
    def delete_pizza_product(self, catalog_list, name):
        for product in catalog_list:
            if product.name == name:
                catalog_list.remove(product)

    def create_drink_product(self, name, list_of_price, picture_name):
        drink = Drink(name, list_of_price, picture_name)
        return drink
    
    def delete_drink_product(self, catalog_list, name):
        for product in catalog_list:
            if product.name == name:
                catalog_list.remove(product)
        

    

        


class User:                                                         #edit by fighter   
    def __init__(self, register_data, cart):
        self.__register_data = register_data
        self.__cart = cart
    
    @property
    def register_data(self):
        return self.__register_data
    
    @property
    def cart(self):
        return self.__cart


    def add_pizza_to_cart(self, pizza, crust, cook, cheese, sauce, seasoning_package, quantity):
        if pizza.list_of_price[crust.value - 1] == None:
            return "PIZZA Added Fail"
        else:
            item1 = PizzaItem(pizza, crust, cook, cheese, sauce, seasoning_package, quantity)
            self.__cart.recieve_item(item1)
            return "PIZZA Added Success"
    
    def add_drink_to_cart(self, drink, quantity):
        item1 = DrinkItem(drink, quantity)
        self.__cart.recieve_item(item1)
        return "DRINK Added Success"
                                                            #deleat <class> Person
                                                            #deleat <class> Admin(person)
                                                            #deleat <class> Customer(Person)

class RegisterData:
    def __init__(self, nprefix, fname, lname ,email ,mobile ,password):
        self.__nameprefix = nprefix
        self.__firstname = fname
        self.__lastname = lname
        self.__email = email
        self.__mobile = mobile
        self.__password = password   

    @property
    def nameprefix(self):
        return  self.__nameprefix
    
    @property
    def firstname(self):
        return self.__firstname
    
    @property
    def lastname(self):
        return self.__lastname

    @property
    def email(self):
        return self.__email
    
    @property 
    def mobile(self):
        return self.__mobile
    
    @property
    def password(self):
        return self.__password

    
class Address:
    def __init__(self, mooban, house, roadname, soi, subsoi, district, provoince, postalcode):
        self.__mooban = mooban
        self.__house = house
        self.__roadname = roadname
        self.__soi = soi
        self.__subsoi = subsoi
        self.__district = district
        self.__provoince = provoince
        self.__postalcode = postalcode

    @property
    def mooban(self):
        return self.__mooban
    @property
    def house(self):
        return self.__house
    @property
    def roadname(self):
        return self.__roadname
    @property
    def soi(self):
        return self.__soi
    @property
    def subsoi(self):
        return self.__subsoi
    @property
    def district(self):
        return self.__district
    @property
    def provoince(self):
        return self.__provoince
    @property
    def postalcode(self):
        return self.__postalcode


class Product():                                                  # edit by fighter
    def __init__(self, name, list_of_price, picture_name):
        self.__name = name
        self.__list_of_price = list_of_price
        self.__picture_name = picture_name

    @property
    def name(self):
        return self.__name
    @property
    def list_of_price(self):
        return self.__list_of_price
    @property
    def picture_name(self):
        return self.__picture_name



class NormalPizza(Product):                                         # edit by fighter
    def __init__(self, name, list_of_price, picture_name):
        Product.__init__(self, name, list_of_price, picture_name)

        

class Drink(Product):                                               # edit by fighter
    def __init__(self, name, list_of_price, picture_name):
        Product.__init__(self, name, list_of_price, picture_name)

    
class Item(ABC):
    @abstractmethod
    def calculate_price(self):
        pass
    
class Catalog:                       #run
    def __init__(self):
        self.list = []

    def add_item_to_list(self, item):
        self.list.append(item)



class PizzaItem(Item):                                                         #edit by fighter   deleat <class> item
    def __init__(self, pizza, crust, cook, cheese, sauce, seasoning_package, quantity):
        self.__pizza = pizza        # pizza1     
        self.__crust = crust        # enum
        self.__cook = cook          # enum
        self.__cheese = cheese      # enum
        self.__sauce = sauce        # enum
        self.__seasoning_package = seasoning_package        # enum
        self.__quantity = quantity  #int
        self.__item_price = 0       #int

    @property
    def pizza(self):
        return self.__pizza
    @property
    def crust(self):
        return self.__crust
    @property
    def cook(self):
        return self.__cook
    @property
    def cheese(self):
        return self.__cheese
    @property
    def sauce(self):
        return self.__sauce
    @property
    def seasoning_package(self):
        return self.__seasoning_package
    @property
    def quantity(self):
        return self.__quantity
    @property
    def item_price(self):
        return self.__item_price
    @quantity.setter
    def quantity(self, new_quantity):
        self.__quantity = new_quantity
    
    def calculate_price(self):              # this method is re-calc self.item price  and set value to self.item_price at the same timm
        self.__item_price = self.__pizza.list_of_price[self.crust.value - 1]
        if self.__cheese.value == 4:
            self.__item_price  += 30
        elif self.__cheese.value == 5:
            self.__item_price += 60
        self.__item_price *= self.__quantity
        return self.__item_price

class DrinkItem(Item):                                                         #edit by fighter
    def __init__(self, drink, quantity):
        self.__drink = drink  
        self.__quantity = quantity
        self.__item_price = 0
    @property
    def drink(self):
        return self.__drink
    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, new_quantity):
        self.__quantity = new_quantity
    @property
    def item_price(self):
        return self.__item_price
    
    def calculate_price(self):        # thsi method is re-calc self.item price  and set value to self.item_price at the same time
        total = 0
        total = self.__drink.list_of_price[0]
        total = total * self.__quantity
        self.__item_price = total
        return self.__item_price


class Cart:                             #run
    def __init__(self):
        self.__item_list = []
        self.__total_price = 0                            # fighter add

    def recieve_item(self, item):
        self.__item_list.append(item)
    
    def calculate_total_price(self):                    # fighter add
        total_price = 0
        for x in self.__item_list:
                total_price += x.calculate_price()
        self.__total_price = total_price
        print("updated total_price!!")
    
    @property
    def item_list(self):
        return self.__item_list
    @property
    def total_price(self):
        return self.__total_price


class Payment:
    def __init__(self, payment_date, payment_status, payment_method, total):
        self.__payment_date = payment_date
        self.__payment_status = payment_status
        self.__payment_method = payment_method
        self.__total = total
        

    @property
    def payment_date(self):
        return self.__payment_date
    @property
    def payment_status(self):
        return self.__payment_status
    @property
    def payment_method(self):
        return self.__payment_method
    @property
    def total(self):
        return self.__total
    
    @total.setter
    def total(self,total):
        self.__total = total
        
    @payment_date.setter
    def payment_date(self,payment_date):
        self.__payment_date = payment_date
    
class CreditCardInfomation(Payment):
    def __init__(self, payment_date, payment_status, payment_method, total,card_name,\
                  expiration_date, card_numbers, cvv):
        Payment.__init__(self, payment_date, payment_status, payment_method, total)
        self.__card_name = card_name
        self.__expiration_date = expiration_date
        self.__card_numbers = card_numbers
        self.__cvv = cvv
    @property
    def card_name(self):
        return self.__card_name
    @property
    def expiration_date(self):
        return self.__expiration_date
    @property
    def card_numbers(self):
        return self.__card_numbers
    @property
    def cvv(self):
        return self.__cvv
  
class Cash(Payment):
    def __init__(self, payment_date, payment_status, payment_method, total):
        Payment.__init__(self, payment_date, payment_status, payment_method, total)
       

class Bill:
    def __init__(self, user, address, payment):
        self.__user = user
        self.__address = address
        self.__payment = payment
    
    def add_item_list(self, item_list):
        self.item_list = item_list



    def showinfo(self):
        list_of_item = []
        for item in self.__user.cart.item_list:
            if isinstance(item, PizzaItem) == True:
                list_of_item_detail = []
                list_of_item_detail.append(item.pizza.name)
                list_of_item_detail.append(item.item_price)
                list_of_item.append(list_of_item_detail)
            if isinstance(item, DrinkItem) == True:
                list_of_item_detail = []
                list_of_item_detail.append(item.drink.name)
                list_of_item_detail.append(item.item_price)
                list_of_item.append(list_of_item_detail)

        self.item_list = list_of_item
        mylist = []
        mylist.append("           PIZZA MANIA")
        mylist.append(self.__user.register_data.firstname)
        mylist.append(" ")
        mylist.append(self.__user.register_data.lastname)
        mylist.append(" ---------------------------------")
        for i in self.item_list:
            mylist.append(i)
        mylist.append("total ")
        mylist.append(self.__payment.total)
        mylist.append(" ---------------------------------")
        mylist.append("delivery address  ")
        mylist.append(self.__address.mooban)
        mylist.append(self.__address.house)
        mylist.append(self.__address.roadname)
        mylist.append(self.__address.soi)
        mylist.append(self.__address.subsoi)
        mylist.append(self.__address.district)
        mylist.append(self.__address.provoince)
        mylist.append(self.__address.postalcode)
        
        
        mylist.append("payment method    ")
        mylist.append(self.__payment.payment_method)
        mylist.append("payment date      ")
        mylist.append(self.__payment.payment_date)
        # mylist.append("payment date      ")
        # mylist.append(self.__payment.payment_date)
        return mylist







