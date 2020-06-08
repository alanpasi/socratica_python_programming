# Numbers: int, float, complex
# Operations: + - * /

x = 28  # int
y = 28.0  # float
print(float(28))
print(3.14, " # float")  # float
print(int(3.14))

#  ints are narrower than floats
#  floats are wider than ints

x = 1.732  # float
print(x + 0j)

#  floats are narrower than complex numbers
#  complex numbers are wider than floats

a = 2  # int
b = 6.0  # float
c = 12 + 0j  # complex number

# Rule: Widen numbers so they're the same type

# Addition
print(a + b)  # int + float

# Subtraction
print(b - a)  # float - int

#  Multiplication
print(a * 7)  # int * int

# Division
print(c / b)  # complex / float

print(16 / 5)
print(20 / 5)
print(16 % 5)
print(16 // 5)
print(2 / 0)  # ZeroDivisionError: division by zero
