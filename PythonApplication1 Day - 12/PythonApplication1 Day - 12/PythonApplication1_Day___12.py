'''
for i in range (100,110):  #first arg:starting value,second arg:ending value.It stops 1 before the ending value
    print(i)
   
print("")

print("Thirteen times table")
for i in range(1,11):
    print(i,"x 13 =",i*13)
    
print("")

for i in range (1,1000000,50): #third arg:a value that determines incrementation e.g. here it counts from 1-1000000 adding 50 each iteration
    print(i)
    
print("")

for i in range(10,0,-1):
    print(i)
'''

'''
print("List Generator")
print("--------------")
switch = True
while(switch == True):
    start = int(input("Insert a number to start from: "))
    end = int(input("Insert a number to end before: "))
    increment = int(input("Insert a number that will increment the starting number to reach the ending number: "))
    if end > start and increment <= 0:
        print("Insert valid input")
    elif end < start and increment >= 0:
        print("Insert valid input")
    else:
        break    
for i in range(start,end,increment):
        print(i)
'''    

while True:
        number = int(input("Choose a number from 1 to 20: "))
        if number >= 1 and number <= 20:
            break
        else:
            print("Invalid input. Please enter a number from 1 to 20.")

score = 0
for i in range(1, 11):
    while True:
        answer = (input(i,"times",number,"is: ")) #??? 
        if answer == i * number:
                score += 1
                break
        else:
            print("Wrong answer. Try again.")
print("Your score is ",score," out of 10.")

