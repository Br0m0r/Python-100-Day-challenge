#for i in range(0,100):
#   print(i)

#for i in range(0,100):
#    print(i, end = " " )
    
#for i in range(0,100):
#    print(i,end ="\n")   with \n(starts in new line) we have the same effect as if we didnt add the end argument  
                             # \t(tab indent)          \v(vertical tab indent)

#for i in range(0,100):
#   print(i, end = "\v " )
    
#for i in range(0,100):
#    print(i, end = "\t " )

from colorama import init, Fore, Back, Style #essential for color
import os,time
init()  # essential for color



print("If you put")
print("\033[33m",end = "") #yellow
print("nothing at the")
print("\033[35m",end = "") #purple
print("end character")
print("\033[32m",end = "") #green
print("then you don\"t")
print("\033[0m",end = "") #default
print("get odd gaps")

print("")

print(Fore.RED + "This will be red in the terminal" + Style.RESET_ALL)
print(Fore.GREEN + "This will be green" + Style.RESET_ALL)

print("")

print("If you put","\033[33m","nothing at the","\033[35m","end character","\033[32m","then you don\"t","\033[0m","get odd gaps",end = "")
#notice the double spaces in the terminal
print("")

print("If you put" , "\033[33m" , "nothing at the" , "\033[35m" , "end character" , "\033[32m" , "then you don\"t" , "\033[0m", "get odd gaps",sep = " ")
print("")

#end = string to place at the end
#sep = string to place between arguments

time.sleep(2)
os.system("cls")

print('\033[?25l',end='')#this removes the cursor from the terminal

for i in range(1,5):
    print(i)
    time.sleep(0.5)
    os.system('cls')
    
print('\033[?25h',end='')#this turns the cursor back on


time.sleep(1)
os.system('cls')

def SuperSubRoutine(color,text):
    print(f'This is the input from the user:" {text} " and from {color} now on the color is changed according to the user.We are ',"\033[0m","now changing the color back.",sep = "")
    

Purple = "\033[35m"
Green =  "\033[32m"
Yellow = "\033[33m"

Sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit." 

SuperSubRoutine(Yellow,Sentence)