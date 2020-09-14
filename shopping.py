cart = []

cart_number = []
number_of_items = 0

shopping_list = {
    'apple' : 180,
    'banana' : 50,
    'mango' : 60,
    'cheese' : 50,
    'bread' : 22,
    'toothpaste' : 33,
    'brush' : 21,
    'soap' : 67,
    'shampoo' : 83,
    'eggs' :  5
}

def customer():
    user_action = input("What would u like to do?")
    user_number = input("How many?")

    def print_bill():
        for i in range(1, len(cart_number + 1)):
            print(f'''
            Your bill:
            {cart[i]} {cart_number[i]}
            ''')  
    def check_out():
        
        print_bill()
        print("Thank you for coming! Hope u come again!" )
        global number_of_items
        number_of_items = 0

    def buy():
        if user_number == 0:
           print("Whaaaa......?")
        else:
            global number_of_items
            cart_number.append(user_number)
            print("Item added to cart")
            cart.append(user_action)
            number_of_items += 1

                




