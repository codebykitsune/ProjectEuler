##n!を求める再帰関数
##f(n): if n = 1 then return 1
## else return n * f(n-1)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))
print(factorial(5))