# ERROR TYPES

# 1. SyntaxError

# if x = 4:
#     print("x equal to 4", )

# 2. NameError

# print(c)

# 3. TypeError

# print("Number: " + 2)

# 4. IndexError

# list = [1, 2, 3]
#
# print(list[3])

# 5. KeyError

# ages = {
#     "Eren": 37,
#     "Zeynep": 20
# }
#
# print(ages["Hakan"])


# try ... except Blocks

while True:

    try:
        first_num = 5 # int(input("Please enter first number: "))
        second_num = 1 # int(input("Please enter second number: "))
        break
    except ValueError:
        print("Please enter  a number")

try:
    division = first_num / second_num

    print(division)
except ZeroDivisionError:
    print("Divide by 0 error")


""" 
Debugging Techniques
1. print
2. Logging modules
"""