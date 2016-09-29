"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from new_arithmetic import *


# Your code goes here

num = ""
while num != "q": # exit = user inputs "q"
    num = raw_input("> ")
    tokens = num.split(" ") # tokenization
    identifier = tokens[0]
    digits = {int(x) for x in tokens[1:]}

    if identifier == "+":
        print add(*digits)
    elif identifier == "-":
        print subtract(*digits)
    elif identifier == "*":
        print multiply(int(tokens[1]), int(tokens[2]))
    elif identifier == "/":
        print divide(int(tokens[1]), int(tokens[2]))
    elif identifier == "square":
        print square(int(tokens[1]))
    elif identifier == "cube":
        print cube(int(tokens[1]))
    elif identifier == "pow":
        print power(int(tokens[1]), int(tokens[2]))
    elif identifier == "mod":
        print mod(int(tokens[1]), int(tokens[2]))
