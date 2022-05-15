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
    Hello! Welcome to your shopping cart!
    Choose your next action using digits (1-4).

    Add item: 1
    Remove item: 2
    View cart: 3
    To Checkout: 4    
""")

shopping_cart = {}
message = f'\n\nThank you for shopping! Here is your receipt:\n'
option = int(input("What would you like to do? "))

while option != 4:
    if option == 1:
        item = input("Please tell me what you would like to add? ")
        qnty = int(input('How Many? '))
        shopping_cart[item] = qnty
       
    elif option == 2:
        item = input("Which item would you like to remove? ")
        del(shopping_cart[item])
    elif option == 3:
        for item in shopping_cart:
            print(item,":",shopping_cart[item])
    elif option != 4:
        print("\nAction Not Possible")
    option = int(input("""\nWhat next? 
        Add: 1 Remove: 2 View Cart: 3 Checkout: 4
        """ ))
else:
    print(message)
    print(item,":",shopping_cart[item])
    print("\n\nSHOPPING CART CLOSED.")