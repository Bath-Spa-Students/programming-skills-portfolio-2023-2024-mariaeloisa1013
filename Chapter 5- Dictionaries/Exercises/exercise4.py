#dictionary
print ("\n")
river = {'amazon river':'south america',
         'yangtze river':'china',
         'congo river': 'democratic republic of congo'}

#sentences
for x, y in river.items():
    print(x.title() + " can be visited within the country of " + y)

#river names
print ('\nRIVERS')
for x in river.items():
    print("\t", x[0])

#coutnries
print ('\nCOUNTRIES')
for y in river.items():
    print("\t", y[1])
