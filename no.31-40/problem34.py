## 1! + 4! + 5! = 1+ 24 + 120 = 145

def factorial(n):
    if n == 1 or n == 0:
        return 1
    elif n >1:
        return n * factorial(n-1)
    

def making_factorial(a,b):
    list_factorial = []
    for i in range(a, b+1):
        i_new = factorial(i)
        list_factorial.append(i_new)
    return list_factorial

list_factorial = making_factorial(0,9)
# print(list_factorial[0])


limit = len(str(list_factorial[9] * 7)) * list_factorial[9]
print(limit)


def main():
    result = []
    for i in range(3, limit + 1):
        if i == sum(list_factorial[int(d)] for d in str(i)):
            result.append(i)
    return sum(result)

print(main())
