
sum(n)
if n == 0:
    return 0
else:
    return n + sum(n - 1)

a = int(input("Enter Any Number for sum"))
b = sum(a)
print(b)