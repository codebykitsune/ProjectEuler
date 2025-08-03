##2進法にして回文かどうか判断する、先頭が０の場合false
def change_into_bi(n):
    a = format(n, 'b')
    reversed_a = a[::-1]
    if reversed_a[0] == "0":
        return False
    elif a == reversed_a:
        return True

##10進法で回文かどうか判断する、先頭が０の場合false
def is_palindromic(n):
    new_n = str(n)
    reversed_n = new_n[::-1]
    if reversed_n[0] == "0":
        return False
    elif new_n == reversed_n:
        return True
   
def main():
    count = 0
    result = []  
    MAX = 1_000_000
    for i in range(MAX):
        if is_palindromic(i) and change_into_bi(i):
            count +=1
            result.append(i)
    print(count)
    sum_n = sum(result)
    print(result)
    print(sum_n)

main()