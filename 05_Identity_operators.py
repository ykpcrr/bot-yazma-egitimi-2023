# Identity operators: is, is not

a = [1, 2, 3]
b = a

# is
print(b is a)  # true
c = [1, 2, 3]
print(c is a)  # false
print(c == a)  # true

# is not
