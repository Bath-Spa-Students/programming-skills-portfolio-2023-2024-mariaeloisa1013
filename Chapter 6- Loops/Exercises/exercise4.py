#list sandwiches
sandwich_orders = ["pastrami","tuna", "ham", "club", "turkey"]

#empty list for finished sandwiches later
finished_sandwiches = []

print("\n\tWelcome to SandWITCH!\n")
#loop each sandwich to be shown as being printed
while sandwich_orders:
    made_sandwich = sandwich_orders.pop()
    print("we are making your " + made_sandwich + " sandwich")
    #loop to add all sandwiches into finished
    finished_sandwiches.append(made_sandwich)

print("\n")
#loop to print all finished sandwiches
for items in finished_sandwiches:
    print("we have made your " + items + " sandwich")
