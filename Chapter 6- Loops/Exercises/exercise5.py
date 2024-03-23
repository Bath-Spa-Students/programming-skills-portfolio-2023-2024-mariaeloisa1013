print("\nWelcome to Sandwitch!\n")

#list sandwiches
sandwich_orders = ["pastrami","tuna", "pastrami", "pastrami", "ham", "club", "turkey"]
#empty list for finished sandwiches
finished_sandwiches = []

#loop for pastrami running out
print("\tThe deli has run out of pastrami\n")
while 'pastrami'in sandwich_orders:
    sandwich_orders.remove('pastrami')

#making the sandwiches
while sandwich_orders:
    made_sandwich = sandwich_orders.pop()
    print("we are making your " + made_sandwich + " sandwich")
    finished_sandwiches.append(made_sandwich)

#print finished sandwiches
print("\n")
for items in finished_sandwiches:
    print("we have made your " + items + " sandwich")
