list_e = [1, 2, True, "Eren", (1, 2, 3), {"a": 12, "b": 7}]

# Reach elements is list
print(list_e[0])
print(list_e[-1])

# Change elements in list
list_e[2] = "Apple"
print(list_e)

# List Methods

# append()

Fruits = ["Apple", "Pie", "strawberry"]
print(Fruits)

# insert()
Fruits.insert(2, "watermelon")
print(Fruits)

# remove()
Fruits.append("plum")
print(Fruits)
Fruits.remove("plum")
print(Fruits)
# Fruits.remove("banana")  Error because banana is not in the list_e

# pop()
removed = Fruits.pop()
print(Fruits)
print(removed)
removed = Fruits.pop(1)
print(Fruits)
print(removed)

# sort()
numbers = [89, 42, 70, 12, 53, 89]
names = ["Zeynep", "Eren", "Fatma", "Muhammed", "Kerem"]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
names.sort()
print(names)
names.sort(reverse=True)
print(names)

# count() Gives you how many letter you have
name = "Yakup Acar"
characters = [x for x in name.lower()]
print(characters)
print(characters.count("c"))
print(characters.count("a"))

# matrices
students = [["Yakup", 70, 64, 85], ["Furkan", 90, 75, 80]]
print(f"{students[0][0]}'s notes: {students[0][1:]}")
