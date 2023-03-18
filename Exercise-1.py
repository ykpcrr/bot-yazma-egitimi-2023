# Exercise 1

# We will write a string than try to reverse it and string
name = "yakup"
nameReverse = name[-1] + name[-2] + name[-3] + name[-4] + name[-5]
name = nameReverse
nameR = name[-1] + name[-2] + name[-3] + name[-4] + name[-5]
print(nameReverse)
print(nameR)

# Exercise 2

# Write a boolean value and print
nameBool = True
print(nameBool)

# Exercise 3

# Create a list that have numbers and try to spuare them
oddnumbers = [1, 3, 5, 7, 9]
squareof1 = oddnumbers[0]**2
squareof3 = oddnumbers[1]**2
squareof5 = oddnumbers[2]**2
squareof7 = oddnumbers[3]**2
squareof9 = oddnumbers[4]**2
print(squareof1)
print(squareof3)
print(squareof5)
print(squareof7)
print(squareof9)

# Exercise 4

# Create a dictionary (key, value)

main = {}
main[name] = "Yakup"
print(main)


# Exercise 5

# Write 2 set and calculate their intersection and union

set1 = {"Math", "Chemical", "Physical", "English"}
set2 = {"Math", "History", "Geography", "English"}

# Intersection
setInter = set1.intersection(set2)
print(setInter)

# Undo
setTotal = set1
setTotal.update(set2)
print(setTotal)
