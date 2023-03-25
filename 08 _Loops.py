"""
for: Used to reach and use elements inside data types like lists, dicts and tuples

while: continuing as long as certain condition met
"""

# For
# List

list1 = [1, 2, "apple", "pear"]

for element in list1:
    print(element)

# Adding numbers

list2 = [1, 7, 3, 30, 2, 4.2]
addition = 0

for add in list2:
    a = addition
    addition += + add
    print(f"{a} + {add}: {addition}")

# Change list elements

list3 = [1, 2, 3, 4, 5]

for i, element in enumerate(list3):
    list3[i] = element ** 2

print(list3)

# Filtering element in list

list4 = [100, 101, 102, 103, 104, 105]
list5 = []

for element in list4:
    if element % 2 == 0:
        list5.append(element)

print(list5)

# Multidimensional list

matris = [
    list1,
    list4,
    [1, 2, 3],
    [3, 4, 5],
    [7, 8, 9]
]

for element in matris:
    print("---")
    for inside in element:
        print(inside)

# While
# Guess number game

"""
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
"""
# Factorial Calculation
# 5! = 5 * 4 * 3 * 2

number = 5 # int(input("Enter a number for Factorial Calculation: "))
firstnum = number
factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print(f"Factorial of {firstnum} is {factorial} ")

# Nested loops

for i in range(5, 10):
    print("-" * 10)
    print(f"element of the outer loop: {i}")
    j = 1
    while j < i:
        print(f"element of the inside loop: {j}")
        j += 1

# List Comprehension
# Long way normal loop

list = []

for i in range(5):
    list.append(i)

print(list)

# Short way: List comprehension

list = [i for i in range(5)]

print(list)

# Squaring list
# Short way

list3 = [i * i for i in list3]

print(list3)

# Filtering element in list
# Short way

flist = [i for i in list4 if i % 2 == 0]
print(flist)