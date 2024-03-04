from pickle import FALSE
import random 
'''
myNumber = random.randint(1,100)
print(myNumber)

print("-------------")
print("-------------")


for i in range(50):
  myNumber2 = random.randint(1,99999)
  print(myNumber2)
  '''
print("-------------")
print("-------------")



print("GUESS THE 5 NUMBERS!!!")
print("MORE CORRECT ANSWERS,BETTER PRIZES!!!")
BASE_PRICE = 0
COUNTER = 1

print("Numbers will be randomly generated between 1-10.So choose one between 1-10")
switch = True

while switch:
    for i in range(5):
        R1 = random.randint(1,10)
        answer = input("Guess the number : ")
        if int(answer) == R1:
           print("Correct!!")
           COUNTER += 1
           BASE_PRICE += 100*COUNTER
        else:
           print("Wrong!")
        choose = ""
    while choose !=  "Yes" and choose != "No" : 
        choose = input("Want to play again? (Yes/No) :")
        print("")
        if choose == "Yes":
           break
        elif choose == "No":
           switch = False
           break
        else:
           print("Please pick either Yes or No")
print("")
print(f'Your final score is : {BASE_PRICE}')
print("")           
print("Thank you for playing!")               
       

       
   
      
   
