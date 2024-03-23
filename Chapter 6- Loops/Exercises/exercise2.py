#instructions
start = '\n\tYou are about to purchase a ticket for "Barbie" '
start += '\nthe ticket prices will be based on your age'
start += '\nenter "quit" when done. please enter your age: ' 

#loop to ask age
while True:
    age = input(start)
    if age == 'quit':
        break
    age = int(age)
    #print ticket based on input age
    if  age < 3:
        print ("\tYour ticket will be FREE. Thank you and enjoy the movie.")
    elif age <= 12:
        print ("\tYour ticket will be $12. Thank you and enjoy the movie.")
    else:
        print ("\tYour ticket will be $15. Thank you and enjoy the movie.")
    


