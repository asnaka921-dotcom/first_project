def fibonacci(n):
    series = []
    a, b = 0, 1
    while a <= n:
        series.append(a)
        a, b = b, a + b
    return series

print("\n=== FIBONACCI SERIES ===")
num = int(input("Enter a number: "))
result = fibonacci(num)
print(f"Fibonacci series up to {num}: {result}")
