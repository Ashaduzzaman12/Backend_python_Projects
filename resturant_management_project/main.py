from Fooditem import FoodItem
from menu import Menu
from orders import order
from restaurant import Restaurant
from user import customer ,Employee,Admin
mamar_res=Restaurant("mamar restaurent")
def customer_menu():
    name=input("enter your name:")
    email=input("enter your mail:")
    phone=input("Enter your phone:")
    address=input("enter your address")

    customer=customer(name=name,email=email,phone=phone,address=address)

    while True:
        print(f"Welcome {customer.name}")
        print("1.view menu")
        print("2.add item to cart")
        print("3.view cart ")
        print("4.pay bill")
        print("5.Exit")

        choice=int(input("Enter your choice :"))

        if choice==1:
            customer.view_menu(mamar_res)
        elif choice==2:
            item_name=input("enter item name")
            item_quantity=int(input("Enter item quantity:"))
            customer.add_to_cart(mamar_res,item_name,item_quantity)
        elif choice ==3:
            customer.view_cart()
        elif choice==4:
            customer.pay_bill()
        elif choice==5:
            break
        else:
            print("invalid input")
        
def admin_menu():
    name=input("enter your name:")
    email=input("enter your mail:")
    phone=input("Enter your phone:")
    address=input("enter your address")

    admin=Admin(name=name,email=email,phone=phone,address=address)

    while True:
        print(f"Welcome Admin {admin.name}")
        print("1.Add new item")
        print("2.Add new employee")
        print("3.view employee ")
        print("4.view item ")
        print("5.Delete item")
        print("6.Exit")

        choice=int(input("Enter your choice :"))

        if choice==1:
            item_name=input("item name")
            item_price=input("enter item price")
            item_quantity=input("enter item quantity")
            item=FoodItem(item_name,item_price,item_quantity)

            admin.add_new_item(mamar_res,item)
        elif choice==2:
            name=input("enter employee name")
            phone=input("enter phoner number")
            email=input("enter your mail:")
            age=input("Enter your age:")
            address=input("enter your address")
            designation=input("enter your designation")
            salary=input("enter salary:")
            admin.add_employee(name=name,phone=phone,email=email,address=address,age=age,designation=designation,salary=salary)
            
        elif choice ==3:
            admin.view_employee(mamar_res)
        elif choice==4:
            admin.view_menu()
        elif choice==5:
            item_name=input("Enter item name")
            admin.delete_item(mamar_res,item)
        elif choice==6:
            break
        else:
            print("invalid input")


while True:
    print("Welcome")
    print("1.customer")
    print("2.Admin")
    print("#.Exit")

    choice=input("Enter your choice:")
    if choice==1:
        customer_menu()
    elif choice==2:
        admin_menu()
    elif choice==3:
        break
    else:
        print("Invalid input")
