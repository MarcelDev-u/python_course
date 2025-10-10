a: int = int(input("Enter first number: "))
b: int = int(input("Enter second number: "))

add = a + b
diff = a - b
prod = a * b
quot = a / b if b != 0 else None
mod = a % b if b != 0 else None
power = a ** b
sqrt_a = a ** 0.5
sqrt_b = b ** 0.5
abs_a = abs(a)
abs_b = abs(b)

for operation, result in [
    ("Addition", add),
    ("Subtraction", diff),
    ("Multiplication", prod),
    ("Division", quot),
    ("Modulus", mod),
    ("Power", power),
    ("Square root of first number", sqrt_a),
    ("Square root of second number", sqrt_b),
    ("Absolute value of first number", abs_a),
    ("Absolute value of second number", abs_b)
]:
    print(f"{operation}: {result}")
