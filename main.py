# Build a shopping cart program with the following capabilities:

# 1) Takes in an input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, prints out a receipt of the items with total and quantity.


# name = {}
# greeting = (input('Hello, What is your name?'))
#     return "Hi,(name) Welcome to your shopping cart!"

print("""
    Add item, enter: 1
    Remove item, enter: 2
    View cart, enter: 3
    To Checkout, enter: 0    
""")


shopping_cart = {}
option = int(input("What would you like to do?"))
while option != 0:
    if option == 1:
        item = input("What item would you like to add?")
        qnty = int(input('How Many?'))
        shopping_cart[item] = qnty
    elif option == 2:
        item = input("Which item would you like to remove?")
        del(shopping_cart[item])
    elif option == 3:
        for item in shopping_cart:
            print(item,":",shopping_cart[item])
    elif option != 0:
        print("Not Possible")


    print("
    Add item, enter: 1
    Remove item, enter: 2
    View cart, enter: 3
    To Checkout, enter: 0    
")
    option = int(input("\n\nWhat would you like to do?:  "))
else:
    print(shopping_cart)

    print("\n\nShopping basket program closed.")