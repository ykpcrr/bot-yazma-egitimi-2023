# Guess number game

import random
num = random.randint(1, 10)

pick = int(input("Guess the number: "))

while num != pick: # pick != num:
    if pick > num:
        print("guess a smaller number.")
    else:
        print("guess a bigger number.")
    pick = int(input("Guess another number: "))

print(f"Congratulations you guess the {num} number")