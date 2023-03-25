"""
    def function_name(parameter1, parameter2...):
        transactions are done
        return
"""


def add(a, b):
    result = a + b
    return result


addition = add(2, 9)
print(addition)


def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n-1)


f = factorial(5)
print(f)
