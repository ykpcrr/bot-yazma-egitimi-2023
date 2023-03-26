# get a number than print negative zero or positive depends on the number

number = 9 # int(input("Enter a number: "))

if number > 0:
    print(f"Your number {number} is positive")
elif number < 0:
    print(f"Your number {number} is negative")
else:
    print("Your number is 0")

# calculate if a student pass the lesson student should get at leasat 60 mark for pass

passscore = 60
score = 60 # int(input("Enter your score: "))

if score >= passscore:
    print("you pass the lesson")
else:
    print("you could not pass the lesson study harder please")

# İf someone older than 18 print you can vote

border = 18
age = 16 # int(input("Enter your age: "))

if age >= border:
    print("you can vote")
else:
    print("you cannot vote")


# get a number print choose odd or even

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")

# get a balance and prince if the balance bigger than price you can buy it if not you cannot buy it

balance = int(input("Enter your balance: "))
price = int(input("Enter the price: "))

if price > balance:
    print("you are not able to buy it")
else:
    print("you can buy it")
