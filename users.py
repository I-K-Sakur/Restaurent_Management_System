from abc import ABC
from menu import Menu
from orders import Order
class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone

class Customer(User):
        def __init__(self, name, email, phone, address):
            super().__init__(name, phone, email, address)
            self.cart = Order()
        
        def view_menu(self,restaurent):
            restaurent.menu.show_menu()   
        def add_to_cart(self,restaurent,item_name,quantity):
            item = restaurent.menu.find_item(item_name)
            print(item.quantity)
            if item:
                if quantity > item.quantity:
                    print("Not enough quantity available")
                else:
                    item.quantity = quantity
                    self.cart.add_item(item)
                    print("item added to cart")
            else:
                print("Item not here")    
        def view_cart(self):
            print("***View Cart***")    
            print("Name\tPrice\tQuantity")   
            for item,quantity in self.cart.items.items():
                 print(f"{item.name}\t{item.price}\t{quantity}")   
            print("Total Price: ",self.cart.total_price)
        def pay_bill(self):
            print(f"Total{self.cart.total_price} paid successfully")
            self.cart.clear()
class Employee(User):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary

class Admin(User):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary
        
    def add_employee(self,restaurent,employee):
        restaurent.add_employee(employee)
        
    def view_employees(self,restaurent):
        restaurent.view_employee()
        
    def add_new_item(self,restaurent,item):
        restaurent.menu.add_menu_item(item)
    def remove_item(self,restaurent,item):
        restaurent.menu.remove_item(item)
    def view_items(self,restaurent):
        restaurent.menu.show_menu()


# name_rest = Restaurent("Food Palace")
# mn = Menu()
# item = FoodItem("Burger",20.5,2)
# item2= FoodItem("Pizza",30.5,1)
# item3= FoodItem("Pasta",40.5,4)
# item4= FoodItem("Pasta",40.5,3)
# mn.add_menu_item(item)
# mn.add_menu_item(item2)
# mn.add_menu_item(item3)
# mn.add_menu_item(item4)
# mn.show_menu()
# admin = Admin("Rahim","rahim@gmial.com",123234,"Dhaka",25,"Admin",50000)
# admin.add_new_item(name_rest,item)
# customer1= Customer("Rahim","rahim@gmial.com",123234,"Dhaka")
# customer1.view_menu(name_rest)
# item_name =  input("Enter the item name: ")
# quantity = int(input("Enter the quantity: "))
# customer1.add_to_cart(name_rest,item_name,quantity)
# customer1.view_cart()