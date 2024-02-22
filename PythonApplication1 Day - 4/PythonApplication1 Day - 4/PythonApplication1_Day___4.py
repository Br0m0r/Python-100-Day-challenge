'''

tvShow = input("What is your favourite Tv Show?")
if tvShow == "peppa pig":
    print("ugh why")
    favechar = input("Who is your favourite character?")
    if favechar == "daddypig":
        print("right answer")
    else:
        print("Nah,daddy pig is the greatest")
elif tvShow == "paw patrol":
    print ("aww sad times")
else :
    print("Yeah ,thats cool and all")
'''


'''
favoriteCharacter = input("Who is your favourite 'Lord of the Rings' character? ")

if favoriteCharacter == "Gandalf":
    print("A wise choice indeed.")
    reason = input("Why do you like Gandalf? ")
    if reason == "wisdom":
        print("Indeed, his wisdom is unparalleled.")
    elif reason == "power":
        print("True, his power is formidable.")
    else:
        print("An interesting perspective!")
elif favoriteCharacter == "Frodo":
    print("A brave choice, burdened with the ring.")
elif favoriteCharacter == "Aragorn":
    print("The king returns! A leader by birth and by deed.")
elif favoriteCharacter == "Legolas":
    print("Sharp eyes and even sharper arrows, a true friend and warrior.")
elif favoriteCharacter == "Gimli":
    print("His axe is as sharp as his sense of honor.")
else:
    print("Not a bad choice,did not expect that!")
    
'''

'''
name = input("name :");
if name == "Dave" or name == "dave":
    print ("Hi Dave!");
else:
    print("Denied!");
    '''

    
print("Welcome to the 'Lord of the Rings' questionnaire!")

favorite_character = input("Who is your favorite character (Gandalf, Frodo, Aragorn, Legolas, Gimli)? ")

if favorite_character == "Gandalf":
    print("You appreciate wisdom and guidance.")
elif favorite_character == "Frodo":
    print("You value courage and resilience.")
elif favorite_character == "Aragorn":
    print("Leadership and bravery stand out to you.")
elif favorite_character == "Legolas":
    print("You admire skill and loyalty.")
elif favorite_character == "Gimli":
    print("Strength and honor are important to you.")
else:
    print("An interesting choice, every character brings something unique to the story.")


favorite_place = input("What is your favorite place (The Shire, Rivendell, Gondor, Mordor)? ")

if favorite_place == "The Shire":
    print("You love peace and tranquility.")
elif favorite_place == "Rivendell":
    print("The beauty and wisdom of the elves captivate you.")
elif favorite_place == "Gondor":
    print("The strength and resilience of men inspire you.")
elif favorite_place == "Mordor":
    print("You're intrigued by the challenges and darkness.")
else:
    print("Every place in Middle-Earth has its own story.")


seeks_adventure = input("Do you seek adventure (Yes or No)? ")

if seeks_adventure == "Yes" or seeks_adventure == "yes":
    print("You would have joined the Fellowship on their quest!")
elif seeks_adventure == "No" or seeks_adventure == "no":
    print("Perhaps a peaceful life in The Shire suits you best.")
else:
    print("An adventurer at heart, but unsure of the path to take.")

print("Thank you for participating in the 'Lord of the Rings' questionnaire!")

