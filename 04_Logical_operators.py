# Logical operator: and, or,not

a = 3
b = 5
c = 7

# and

print(a < b and b < c)  # true
print(a < b and b > c)  # false

# or

print(a < b or b < c)  # true
print(a < b or b > c)  # true

# not

print(not a > b)  # true
print(not a < b)  # false
print(a < b and not b < c)  # false
print(a < b and not b > c)  # true

