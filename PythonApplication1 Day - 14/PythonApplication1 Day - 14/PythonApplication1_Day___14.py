'''
def rollDice():
    import random
    dice = random.randint(1,6)
    print(f'You rolled {dice}')
  
    
rollDice()

-------------------------------------------------------------------------------------

for i in range(20):
    rollDice()
    
-------------------------------------------------------------------------------------

def PassCheck():
    switch = True
    print("Login System")
    username = "bromor"
    password = 123456   
    while switch:
      askU = input("What is your username? : ")
      askP = input("What is your password? : ")
      if askU == username and askP == str(password):
         print("Welcome Back,our Majestic King")
         switch = False
      else:
         while True:   
           print("Nah ah ah!You didnt say the magic word!")
           
    
PassCheck();



def WhichCake(ingredient, base, coating):
    if ingredient == "chocolate":
        print("Mmm,chocolate cake is amazing")
    elif ingredient == "broccoli":
        print("You what mate?")
    else:
        print("Yeah thats great i suppose...")
    print(f'So you want a{ingredient} cake on a {base} base with {coating} on top?')  
    


user1 = input("Name an ingredient : ")
user2 = input("Name a base : ")
user3 = input("Name a topping for your cake : ")
WhichCake(user1,user2,user3);
'''



def ThrowDice(Number):
    switch = True 
    switch2 = True
    import random
    print("")
    while switch:
        Rnum = random.randint(1,Number)
        switch2 = True
        print(f'You rolled : {Rnum}')
        print("")
        while switch2:
            print("")    
            roll = input("Roll Again(Y/N) :")
            if roll == "Y":
               switch2 = False
            elif roll == "N":
               switch = False
               switch2 = False
            else:
               print("Choose either Y or N") 
    print("Thank you for playing!")           
               
Number = int(input("Choose a number for the sides of your dice! : "))
ThrowDice(Number)

       
    
    

       



