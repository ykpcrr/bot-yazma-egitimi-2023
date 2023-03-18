# if condition

age = 10  # int(input("Enter your age:"))

if age >= 18:
    print(f"You are an adult because you are {age} years old ")


# else condition

else:
    print(f"You are not an adult because you are {age} years old")

# elif condition

# Get a number from user
    # if that number over 10 print it and print it is older than 10
    # elif that number is 10 print you are 10 years old
    # else print as monthly and print it is younger than 10

monthly_age = age * 12

if age > 10:
    print(f"You are {age} years old", " and you are older than 10")
elif age == 10:
    print("you are 10 years old")
else:
    print(f"You are {monthly_age} months old", "and you are younger than 10")

# nested conditional statements

"""
if user_name == "ykp":
    print("hello yakup")

    if passwrd == 123456:
        print("password is correct")
        print("you are logged in")
"""

user_name = "ykp"
passwrd = 123456


if user_name == "ykp" and passwrd == 123456:
    print("hello ykp")
    print("password is correct")
    print("you are logged in")

# one-line conditional statements (ternary operators)

x = 10
y = 20

if x > y:
    maximum = x
else:
    maximum = y


# ternary usage
maximum = x if x > y else y

print(max)
