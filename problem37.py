def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    i = 3
    while i <= n ** 0.5:
        if n % i == 0:
            return False
        i +=2
    return True

def isTruncatable(n):
    for i in range(len(str(n))):
        if i == 0:
            if not is_prime(n):
                return False
        else:
            # 左からi桁を取り除いた数を作る (例: 3797でi=1なら "797")
            left_n = int(str(n)[i:])
            # 右からi桁を取り除いた数を作る (例: 3797でi=1なら "379")
            right_n = int(str(n)[:-i])
            # できた2つの数のどちらか一方でも素数でなければFalse
            if not is_prime(left_n) or not is_prime(right_n):
                return False
            
    return True

def main():
    num = 11
    result = 0
    count = 0
    number_of_prime = 11
    list_result = []
    while count < number_of_prime:
        if isTruncatable(num):
            result += num
            count += 1
            list_result.append(num)
        num += 1
    print(result)
    print(list_result)

main()