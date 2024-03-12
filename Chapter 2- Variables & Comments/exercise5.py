#storyline: A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.
print ('''\tA girl heads to a computer shop to buy some USB sticks.
She loves USB sticks and wants as many as she can get for £50. 
They are £6 each.''')

#assign values in the problem to variables
money = 50
usbstock = 6

#print values in the priblem

#assign solution to calculate how many usb sticks she can buy to variable, usb
usb = money/usbstock

#asign change left to variable
change = (money-(usbstock*int(usb)))

#print the amount of usb sticks she can get 
print ("\nShe's able to buy", int(usb), "USB sticks.")

#print the change
print ("\tHer change will be: £", (change))
