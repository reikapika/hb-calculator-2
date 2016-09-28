"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

num = ""
while num != "q": # exit = user inputs "q"
    num = raw_input("> ")
    tokens = num.split(" ") # tokens
    if tokens[0] is "+":
        print add(int(tokens[1]), int(tokens[2]))
    elif tokens[0] is "-":
        print subtract(int(tokens[1]), int(tokens[2]))
    elif tokens[0] is "*":
        print multiply(int(tokens[1]), int(tokens[2]))
    elif tokens[0] is "/":
        print divide(int(tokens[1]), int(tokens[2]))
    elif tokens[0] is "square":
        print square(int(tokens[1]), int(tokens[2]))
    elif tokens[0] is "cube":
        print cube(int(tokens[1]), int(tokens[2]))
    