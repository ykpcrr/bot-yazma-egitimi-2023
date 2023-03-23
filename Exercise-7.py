# take name, weight and height datas and then calculate weight index

name = input("enter your name: ")
weight = float(input("enter your weight: "))
height = float(input("enter your height (please enter in metres) : "))

index = weight / height ** 2

print(f"Dear {name}, your weight index is: {index}")

if index < 18.4:
    print("you are weak")
elif index > 18.4 and index < 24.99:
    print("you are good ")
elif index > 24.99 and index < 29.9:
    print("You are fat")
elif index > 29.9 and index < 45.9:
    print("you are an obese")
else:
    print("your datas are not true")
