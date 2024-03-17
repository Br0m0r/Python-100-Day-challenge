   



# while True:
#     item = input("What's next on the Agenda?: ")
#     myAgenta.append(item)
#     printList()
    
# while True:
#     menu = input("Add or Remove?:")
#     if menu == "Add":
#         item = input("Whats next on the agenda?: ")
#         myAgenda.append(item)
#     elif menu == "Remove":
#         item = input("What do you want to remove:? ")
#         if item in myAgenda:   # we make sure if it exists in the list to remove so we wont crash
#           myAgenda.remove(item)
#         else:
#             print(f'{item} was not in the list')
#     printList()        


import time,os
from colorama import init, Fore, Back, Style
init() 


def printList():
    print()
    for item in myAgenda:
        print(item)
    print() 
    
myAgenda = []

while True:
    print("\033[33m-----------------------------------------------------------------------------------------")
    List = ("MY LIST")
    print(f'{List:^75}')
    print("-----------------------------------------------------------------------------------------")
    print()
    print("1.Add to List")
    print("2.Remove from List")
    print("3.View List")
    print()
    prompt = input("What do you want to do: ")
    print()
    if prompt == "Add":
        item = input("What do you want to add?: ")
        myAgenda.append(item)
        time.sleep(0.5)
        os.system("cls")
    elif prompt == "Remove":
        item = input("What do you want to remove?: ")
        if item  in myAgenda:
           myAgenda.remove(item)
           time.sleep(0.5)
           os.system("cls")
        else:
            print("There is no such item in the List")
            time.sleep(0.5)
            os.system("cls")
    elif prompt == "View":
        printList()
        input()
        os.system("cls")
        
        





       

