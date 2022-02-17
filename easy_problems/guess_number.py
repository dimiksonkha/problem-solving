import random

print("Guess Number (1-5)")
guess_number = int(input())
random_number = random.randint(1,5)

if guess_number == random_number:
    print("You won the game!!!")

else:
    print("You loose the game!!!")
