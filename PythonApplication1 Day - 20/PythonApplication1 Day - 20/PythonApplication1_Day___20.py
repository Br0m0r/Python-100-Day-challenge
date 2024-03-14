
# name = "Katie"
# age = 28

# print("This is",name,"and her age is",age)





# print("-------------------------------------")
# #Now we do it differently:
# print("This is {} and is {} years old".format(name,age)) #This inserts the variables in the brackets in the format order




# print("-------------------------------------")




# print("This is {name} and is {age} years old.Hello {name},how have you been enjoying your {age} years so far?".format(name = name,age = age))
# #By assigning name to the arguments,i can reuse as many times and in any order i want.
# #Works with different variable types(i can assign the whole thing to a variable )
# response = print("This is {name} and is {age} years old.Hello {name},how have you been enjoying your {age} years so far?".format(name = name,age = age))
# print("-------------------------------------")
# print(response)
# print("-------------------------------------")

# #Another way is to use f'' (Like ive been doing so far,way more convenient)
# response2 = print(f'This is {name} and is {age} years old')
# print(response2)
# print("")
# #I can also use triple quotes """     """ for multiple lines of text

# response3 = print(f""" this is {name}.
# her age is {age} yreas old.
#                Hello,{name}!             """)
# print(response3)
# print("")
# print("")



# for i in range(1,100):
#     print(f'Day {i:^3} of 100') 
 
# #the < indicates allignment of text < for left,> for right and ^ for center.The number indicates number(of characters) of gaps

# print("")

import time,os
print(f"20 days down,what did you think?")
print()
for i in range(1,21):
     answer = input(f'Day number {i}:\n')
     time.sleep(0.5)
     print()
     Show   = f'So you thought day {i} was :'
     print(f'{Show:^65}')
     print(f'{answer:^62}')
     print()
     time.sleep(1)
     os.system("cls")
    

