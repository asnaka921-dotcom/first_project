def calculator(a, b, operator):
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Error: Division by zero"
    }
    if operator not in operations:
        return "Error: Invalid operator. Use +  -  *  /"
    return operations[operator](a, b)

print("\n=== CALCULATOR ===")
a = float(input("Enter first number: "))
operator = input("Enter operator (+  -  *  /): ")
b = float(input("Enter second number: "))
result = calculator(a, b, operator)
print(f"Result: {a} {operator} {b} = {result}")
