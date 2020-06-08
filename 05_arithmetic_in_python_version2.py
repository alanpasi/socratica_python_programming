# Numbers: int, long, float, complex
# Operations: + - * /

x = 5  # int
# y = 5L  # long not supported in version 3

x = 1.732  # float
print(x + 0j)
print(complex(x))

a = 2  # int
c = 6.0  # float
d = 12 + 0j  # complex number

# Rule: Widen numbers so they're the same type

# Addition
print(a + c)  # int + float

# Subtraction
print(c - a)  # float - int

# Multiplication
print(a * c)  # int * float

# Division
print(d / c)  # Complex / float

print(16 / 5)

print(16 % 5)

print(float(16) / 5)

print(2 / 0)  # ZeroDivisionError: division by zero

