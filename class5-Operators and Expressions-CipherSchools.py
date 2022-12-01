# Arithmatic Operators
print(2 + 5)
print(5 - 2)
print(20 / 3)
# 6.666666667 output
print(20 // 3)
# 6 output // used for floor division gives quotient
print(20 % 3)
# 2 output % used to return reminder
print(20 ** 3)
# ** used for a power b a^b 2**3 =8
# string concatination and multiplication
print("A" + "a")
print("a" * 2)
# comparison operators
a = 10
b = 20
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
# lexicographical order(which alphabet will come first in dictionary
print("ab" < "z")
# Logical operators
print(True and False)
print(True or False)
print(1 and 0)
print(1 or 0)
print(True and 1)
print(True or 1)
print(1 and 5)
print(1 or 5)
print(isinstance(True, int))
# short-circuiting
'''
a or b = a (if a is truthy)
a or b = b (if a is falsy)
a and b = b (if a is truthy)
a and b = a (if a is falsy)
"" is considered falsy
'''
print(1.6 or 4)
print("" or 6)
print(1.6 and 3)
print("" and 4)
