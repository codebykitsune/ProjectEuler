n = 1000
total = 0
for i in range(1, n+1):
    total += i ** i
total = str(total)
print(total[-10:])