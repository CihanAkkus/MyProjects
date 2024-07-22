import random
import time
print("""
**************************************

Welcome to the number guessing game...

Guess the number between 1 and 40 ^^
(Including 1 and 40)

**************************************
""")
Random_num = random.randint(1,40)

Right_to_try = 7

while True:
    num = int(input("Please enter the number = "))
    if(num < Random_num):
        print("information is being questioned...")
        time.sleep(1)

        print("Please enter a bigger number!")
        Right_to_try -= 1
    elif(num > Random_num):
        print("information is being questioned...")
        time.sleep(1)
        print("Please enter a smaller number!")
        Right_to_try -= 1
    else:
        print("information is being questioned...")
        time.sleep(1)
        print("You won the game :)","\nThe number was",Random_num)
        break
    if(Right_to_try == 0):
        print("Your trial is over")
        break