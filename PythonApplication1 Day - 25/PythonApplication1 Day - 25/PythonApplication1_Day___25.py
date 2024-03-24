# name = input("Whats your name?")
# if name.lower().strip()=="david":
#     print("Hello baldy!")
# else:
#     print("What a beautiful head of hair!")
    

# myList = []
# def printList():
#     print()
#     for i in myList:
#         print(i)
#     print()
    
# while True:
#     addItem = input("Item > ").strip().capitalize()
#     if addItem not in myList:
#         myList.append(addItem)
#     printList()    
    




NameList = []
def printNames():
    print()
    for i in NameList:
        print(i)
    print()



print("---------")
print("Name List")
print("---------")
FirstName = input("Whats your first name?").strip().capitalize()
LastName = input("Whats your last name?").strip().capitalize()
NameList.append(FirstName + " "+ LastName)
printNames()



