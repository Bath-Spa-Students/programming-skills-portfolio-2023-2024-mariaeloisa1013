#list of pets info
pets = [
    {'name':'ramram',
          'animal':'cat',
          'breed':'scottish fold',
          'owner':'maria'},

    {'name':'louie',
          'animal':'dog',
          'breed':'german sheperd',
          'owner':'eloisa'},

    {'name':'jeep',
          'animal':'turtle',
          'breed':'snapping turtle',
          'owner':'pejero'},

    {'name':'goldy',
          'animal':'fish',
          'breed':'goldfish',
          'owner':'butaslac'}
]

#loop to print each info of pet
for animal in pets:
    print("everything i know about " + animal['name'].title() + ":")
    for x,y in animal.items():
        print("\t" + x + ": " + y )
    print("\n")
