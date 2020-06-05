# Types os numbers: int, long, float, complex
# Whole numbers: int, long
import sys

a = 28  # This is a perfect number
print(type(a))
print(a)

print(sys.maxsize)

b = 9223372036854775807
print(type(b))
c = 9223372036854775808
print(type(c))

d = -sys.maxsize - 1
print(d)
print(type(d))

e = 2.718281828
print(e)
print(type(e))

z = 3 + 5.7j
print(z)
print(type(z))
print(z.real)
print(z.imag)