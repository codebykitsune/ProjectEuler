##Factorial Digit Sum

def factorial(n): #e.g. 10
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result ##3628800

def main(n):
    sum_n =0
    str_n = str(factorial(n))##"3628800"
    for i in str_n:
        ##print(i)
        sum_n += int(i)
    return sum_n ##27

print(main(10)) #27
print(main(100)) # the answer