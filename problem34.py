## 1! + 4! + 5! = 1+ 24 + 120 = 145

def factorial(n):
    if n == 1 or n == 0:
        return 1
    elif n >1:
        return n * factorial(n-1)

# print(factorial(9)) #362880

# print(factorial(3)) #6
# print(factorial(6)) #720
# print(factorial(2)) #2
# print(factorial(8)) #40320
# print(factorial(8)) #40320
# print(factorial(0)) #1
def making_factorial(a,b):
    list_factorial = []
    for i in range(a, b+1):
        i_new = factorial(i)
        list_factorial.append(i_new)
    return list_factorial

list_factorial = making_factorial(0,9)
# print(list_factorial)
max = 362880 *7
def main():
    list_sum = []
    for i in range(3, max + 1):
        sum = 0
        i_str = str(i)
        for j in i_str:
            j_int = int(j)
            sum += factorial(j_int)
        if i == sum:
            list_sum.append(i)
    return list_sum

main()
