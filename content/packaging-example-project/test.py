from calculator import add, subtract, integral

print("2 + 3 =", add(2, 3))
print("2 - 3 =", subtract(2, 3))
integral_x_squared, error = integral(lambda x: x * x, 0.0, 1.0)
print(f"{integral_x_squared = }")
