def add(*num):
    total = int()
    for d in num:
        total += d
    return total


def subtract(*num):
    total = num[0]
    for d in num:
        total -= d
    return total


def multiply(*num):
    total = 1
    for d in num:
        total = d * total
    return total


def divide(num1, num2):
    # Need to turn at least argument to float for division to
    # not be integer division
    return float(num1) / float(num2) 


def square(num1):
    # Needs only one argument
    return num1 * num1


def cube(num1):
    # Needs only one argument
    return num1 * num1 * num1


def power(num1, num2):
    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    return num1 % num2
