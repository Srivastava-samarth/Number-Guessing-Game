import random
import math

x = int(input("Enter Lower bound:- "))
y = int(input("Enter Upper bound:- "))

z = random.randint(x, y)
print("You have only",round(math.log(y - x + 1, 2)),"left")
count=0
while count<math.log(y - x + 1, 2):
    count+=1
    guess = int(input("Enter any number: "))
    if x==guess:
        print("Congratulation you guessed it right")
        break

    elif x>guess:
        print("you guessed a smaller number")

    else:
        print("you guessed a higher number")

if count>=math.log(y - x + 1, 2):
    print("Your chances are over, better luck next time")
    print("The number was ",z)
