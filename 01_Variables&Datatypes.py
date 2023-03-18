# VARİABLES

o = "Hello world"
p = 5
i = True


# DATA TYPES

# 1. Integers -> Int

a = 15
b = -15
c = 0

# 2. Floats

x = 3.43654
t = 1.0
y = -8.949
z = 0.1

# 3. Strings

hi = "WELCOME"
name = "Yakubi"
message = hi + " " + name

print(message)

# 4. Boolean (True || False)

q = True
w = False

print(q > w)  # True
print(q == w)  # False

# 5. Lists

fruits = ["apple", "piar", "cherry", "orange", "watermelon", "siu"]

print(fruits)
print(len(fruits))
print(fruits[len(fruits) - 1])
print(fruits[-1])  # That gives you the last element of list directly
print(fruits[-2])  # That gives you second to last
fruits[1] = "nokia"  # changes index

# 6. Tuples

numbers = (1, 2, 3)

print(numbers)
print(len(numbers))
print(numbers[0])
print(numbers[-1])

# Tuples are fixed you cant change them
# numbers[1] = "4"

# 7. Dictionary -> Dict

dic = {
    "company": "Apple",
    "model": "Macbook Pro",
    "year": 2020,
}
print(dic)
print(dic["model"])
print(dic.get("year"))
print(dic.get("cost", "NaN"))
dic["cost"] = 2000.0
print(dic)
print(dic.get("cost", "NaN"))

# 8. Set

sett = {1, 2, 3, 4, 5}

print(sett)
sett.add(6)
print(sett)
sett.add("Yakup")
print(sett)
sett.remove(6)
print(sett)
sett.update([6, 7, "Yakup", "Eren", "Yakup"])
print(sett)

# DATA TYPE CHANGES

num1 = 11  # input("1. write number 1: ")
num2 = 22  # input("1. write number 2: ")

# total = num1 + num2  # string values are concatenated

print(type(num1), type(num2))
num1 = int(num1)
num2 = int(num2)
total = num1 + num2
print(total)

q = 1
v = 0.8
qv = ["a", "b", "c", "a"]

print(q + v)
print(float(q))
print(int(v))
print(bool(q))
print(bool(v))
print(bool(0))
print(bool(0.8))
print(bool(-1))
print(bool(0))
print(bool(int(0.8)))
print(str(q))

print(qv)
print(tuple(qv))
print(set(qv))