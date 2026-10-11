# Day 1: Program 3 - Simple Calculator
num1 = float(input("Enter first  number: "))
operator = input("Enter operator(+, -, *, /, %): - ")
num2 = float(input("Entter Second number: "))


if operator == "+":
    result = num1 + num2
    print("Result:", result)

elif operator == "-":
    result = num1 - num2
    print("Result:", result)

elif operator == "*":
    result = num1 * num2
    print("Result:", result)    

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Cannot divide by Zero!") 

elif operator == "%":
    if num2 != 0:
        result = num1 % num2
        print("Result:", result)
    else:
        print("Error: cannot calculate modulous with zero!")
else:
    print("invalid operator!")            




