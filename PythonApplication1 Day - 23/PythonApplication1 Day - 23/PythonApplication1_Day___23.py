from ast import List
import os,time
ListOfEmails = []


def prettyPrint():
    os.system("cls")
    print("ListOfEmails")
    print()
   # counter = 1  #since i count with index we dont need this
    for index in range(len(ListOfEmails)):
        print(f'{index}: {ListOfEmails[index]}')
   #    counter += 1  
    time.sleep(1)
    

def spam():
    
    os.system("cls")
    for i in range(1,11):
        print(f'Email number: {i}')
        print()
        text = f'Dear {ListOfEmails[i]}\nSend this email to 10 of your friends,or else you are going to have 10 years of bad luck!\nPeace! ' 
        print(text)
        time.sleep(2)
        os.system("cls")
        




while True:
    print("Spammer Inc.")
    menu = input("1.Add email\n2.Remove email\n3.Show emails\n4.Get SPAMMING\n> ")
    if menu == "1":
        email = input("Email > ")
        ListOfEmails.append(email)
    elif menu == "2":
        email = input("Email > ")
        if email in ListOfEmails:
            ListOfEmails.remove(email)
    elif menu == "3":
        prettyPrint()
    elif menu == "4":
        spam()
    time.sleep(1)
    os.system("cls")
