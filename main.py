from food_item import FoodItem
from menu import Menu
from orders import Order
from restaurent import Restaurent
from users import User, Customer, Employee, Admin

# Initialize the restaurant
mamar_restaurent = Restaurent("Mamar Restaurent")

def customer_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")
    customer = Customer(name=name, email=email, phone=phone, address=address)
    
    while True:
        print(f"\nWelcome {customer.name} to the restaurant!")
        print("1. View Menu")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            customer.view_menu(mamar_restaurent)  # Assuming this method exists
        elif choice == 2:
            item_name = input("Enter the item name: ")
            item_quantity = int(input("Enter the quantity: "))
            customer.add_to_cart(mamar_restaurent, item_name, item_quantity)

        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice. Please try again.")

def admin_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")
    age = int(input("Enter your age: "))
    designation = input("Enter your designation: ")
    salary = float(input("Enter your salary: "))

    admin = Admin(name=name, email=email, phone=phone, address=address, age=age, designation=designation, salary=salary)  
    
    while True:
        print(f"\nWelcome {admin.name} to the restaurant!")
        print("1. Add New Item")
        print("2. Add Employee")
        print("3. View Employees")
        print("4. View Items")
        print("5. Delete Item")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            item_name = input("Enter Item Name: ")
            item_price = float(input("Enter Item Price: "))
            item_quantity = int(input("Enter Item Quantity: "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(mamar_restaurent, item)
        elif choice == 2:
            name = input("Enter Employee Name: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Employee Email: ")
            designation = input("Enter Employee Designation: ")
            age = int(input("Enter Employee Age: "))
            salary = float(input("Enter Employee Salary: "))
            address = input("Enter Employee Address: ")
            employee= Employee(name, email, phone, address, age, designation, salary)
            admin.add_employee(mamar_restaurent, employee)
        elif choice == 3:
            admin.view_employees(mamar_restaurent)
        elif choice == 4:
            admin.view_items(mamar_restaurent)
        elif choice == 5:
            item_name = input("Enter the name of the item to delete: ")
            admin.remove_item(mamar_restaurent, item_name)
        elif choice == 6:
            print("Exiting admin menu...")
            break
        else:
            print("Invalid choice. Please try again.")

# Main program loop
while True:
    print("\nWelcome to the Restaurant Management System!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice =int( input("Enter your choice: "))
    
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")