num1 = 10  # int(input("enter a number: "))
num2 = 10  # int(input("enter a number: "))

if num2 > 0 and num1 > 0:
    print("both of them are positive")
elif num2 == 0 or num1 == 0:
    print("At least one of them is 0")
else:
    print("at least one number is not positive")


str = str(input("enter at least one word: "))

if len(str) > 5 or "hello" in str:
    print("Hello to you")
else:
    print("No hello to you")


