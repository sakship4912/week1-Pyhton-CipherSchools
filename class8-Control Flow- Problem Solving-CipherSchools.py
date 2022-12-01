n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(max(i, j), end=" ")
    print()
print()
n = 5
for i in range(n):
    for j in range(n):
        print(max(n - i, n - j), end=" ")
    print()
print()
'''
code to print:
5 5 5 5 5
5 4 4 4 5
5 4 3 4 5
5 4 4 4 5
5 5 5 5 5
'''
n = 5
for i in range(n):
    for j in range(n):
        print(max(i + 1, j + 1, n - i, n - j), end=" ")
    print()
