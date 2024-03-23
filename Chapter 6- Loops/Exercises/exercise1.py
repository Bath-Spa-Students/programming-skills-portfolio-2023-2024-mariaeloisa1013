#intro
print ("\tWlecome to Pizza Hot!")  
print ("Once done, enter 'quit'")

#loop to ask for topping input
while True:
    pizza = str(input("What would you like on your pizza? "))
    if pizza != 'quit':
        #print pizza input
        print("\tYou have added " + pizza + " to your toppings")
    else:
        break
