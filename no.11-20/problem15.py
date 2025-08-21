# //(n+n)!/n! * n!
def square(n):
    children = factorial(n*2)
    mother = factorial(n) * factorial(n)
    result = children/mother
    return result


# //階乗
def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

print(square(20))
