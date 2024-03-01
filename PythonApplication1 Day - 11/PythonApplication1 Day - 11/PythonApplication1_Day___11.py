'''
counter = 0
while counter < 10:
    print (counter)
    counter += 1
    

for counter  in range (10):
    print(counter)
    

# the 2 blocks above do the same thing
#for counter(creates a new variable) in range(10)(creates a list of numbers)
#repeats code changin the variable to the next value in the list when it starts again

for i in range(10):
    print(i)
    
#the letter i is most commonly used(i as in index)

total = 0
for number in range(100): #dont forget parenthesis
    total += number
    print(total)
    
for days in range(7):
    print("Day",days)
   ''' 

interest = 0.05
balance = 1000
for year in range(10):
    balance += balance*0.05
    balance = round(balance,2)
    print("Year",year,"is",balance)
    
print("You paid",balance - 1000,"$ in interest")


