'''
adding = 4 + 3
print(adding);

subtraction = 8 - 9

print(subtraction);

multiplication = 4*23;
print(multiplication);

division = 50/5
print(division);

square = 5**2
print(square);

modulo = 15%4
print(modulo);

divisor = 15//7
print(divisor);

round rounds decimals ,see below for example
'''




myBill = float(input("What was the bill :"));
numberOfPeople = int(input("How many people?"));
answer = myBill / numberOfPeople;
answer = round(answer,2);
tip = int(input("how much u wanna tip (percentage e.g. 15) ?"));
answer = answer + (15/100)*answer;
print("You all owe",answer);
