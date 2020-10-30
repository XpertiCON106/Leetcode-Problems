# Given a list of strings containing integers and arithmetic operators
# ordered by reverse polish notation, evaluate the expression.
# Valid operators are +, -, *, / .
# We will use truncated integer division here. For example, 13/6 = 2.
# For this question, you will get only +, *, -, and /, and have no invalid inputs.
# All lists will be in appropriate RPN order. If an empty list is provided, return 0.
# You are guaranteed the size of the list will not exceed 1,000,000
# Return all outputs as integers (not strings)

# How Reverse Polish Notation works
# In reverse polish notation, operators are put after the operands.
# So for example, instead of writing 3 - 4, we write 3 4 -.
# The steps to evaluating an RPN expression are as follows.

# 1. Evaluate operators left to right. Starting with the leftmost operator,
# 2. Given the operator you’re currently on, apply it to the two operands directly
#    before it. Remove the operator and its operands , and replace them with the result.
# 3. Repeat step one with the next operator on the left hand side, if there is one.
#    Otherwise, the final result is your answer.

"""
So for this problem, I will be using a stack.
Basically, I go through each items in the token list.
If token items is a number, I put it in the stack.
I keep doing this until i find an operator.

If i find a operator, I pop out two number from the stack, that will get rid of the items from the stack itself.

Then i perform the actual calculation. then I update the result with the calculation and
put that result into the stack and continue my search through the token list.

I keep doing this until i have exhausted my token list.

The result will the result of the last calculation that we did.

Space complexity is O(n) since we are storing a stack as we go through the token
Time complexity is O(n) as well since we go through the token list and go through it only once. 
"""
from typing import List
from collections import deque

def evalRPN(tokens: List[str]) -> int:
    if tokens == None:
        return 0

    if len(tokens) == 0:
        return 0

    result = 0
    numbers = deque()
    operators = deque()

    for x in tokens:
        if(x == "*"):
            n1 = numbers.pop()
            n2 = numbers.pop()
            result = int(n2) * int(n1)
            numbers.append(result)
        elif(x == "+"):
            n1 = numbers.pop()
            n2 = numbers.pop()
            result = int(n2) + int(n1)
            numbers.append(result)
        elif(x == "/"):
            n1 = numbers.pop()
            n2 = numbers.pop()
            result = int(n2) / int(n1)
            numbers.append(result)
        elif(x == "-"):
            n1 = numbers.pop()
            n2 = numbers.pop()
            result = int(n2) - int(n1)
            numbers.append(result)
        else:
            numbers.append(x)
    return result
