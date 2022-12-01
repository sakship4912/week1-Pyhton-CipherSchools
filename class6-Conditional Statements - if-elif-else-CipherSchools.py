a = False
# a = True
if a:
    print("true value")
else:
    print("false value")
print("next")


a = 3
if a == 2:
    print("value is 2")
elif a == 3:
    print("value is 3")
else:
    print("value is neither 2 nor 3")

print("friend 1 or 0")
print("blocked 1 or 0")
print("admin 1 or 0")
print("owner 1 or 0")
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
d = int(input("d="))

if d == 1 and b == 1:
    print("has access")
elif d == 1:
    print("has access")
elif b == 1:
    print("access denied")
else:
    print("has access")
