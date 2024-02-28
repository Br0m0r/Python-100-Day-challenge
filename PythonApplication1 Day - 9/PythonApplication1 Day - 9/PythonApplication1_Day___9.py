'''
counter = 0
while counter < 20:
    print(counter)
    counter+=1
    
eXit = ""
while eXit != "yes" or eXit != "Yes":
    print("Hurray!")
    eXit = input("Exit?: ")
    '''

'''

exit_game = ""
while exit_game != "Yes":
    animal = input("What animal do you want: ")

    if animal == "Cow":
        print("A cow goes mooo.")
    elif animal == "Dog":
        print("A dog goes woof woof.")
    elif animal == "Cat":
        print("A cat goes meow.")
    elif animal == "Duck":
        print("A duck goes quack.")
    elif animal == "Lion":
        print("A lion goes roar.")
    else:
        print("Sorry, I don't know that animal. Try another one!")

    exit_game = input("Do you want to exit: ")
print("Ok bye bye!")
'''


'''
while True:
    print("This program is running")
    goAgain = input("Go Again? : ")
    if goAgain == "no":
        break
print("Aww i was having a good time")
'''


counter = 0
while True:
    answer = int(input("Enter a number"))
    print("Adding it up")
    counter += answer
    print("Current total is",counter)
    addAnother = input("Add another? ")
    if addAnother =="no":
        break
print("bye")    

   

    