#!/usr/bin/python3
#Calculator program
#Programmer: Death_Note

while 1:
    first_no = float(input('Please enter first number: '))
    operator = input('Please Enter Operator: ')
    second_no = float(input('Please enter second number: '))
    if operator == '+':
        result = first_no + second_no
    elif operator == '-':
        result = first_no - second_no
    elif operator == '*':
        result = first_no * second_no
    elif operator == '/':
        result = first_no / second_no
    elif operator == '%':
        result = first_no % second_no
    else:
        print("wrong operator! ")
    print("Result is ", result)

