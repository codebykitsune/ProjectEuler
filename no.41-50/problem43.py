import itertools

#12345
def is_Pan(n):
    #5
    d = len(str(n))
    #['1','2','3','4','5']
    s = [i for i in str(n)]

    f = True
    for i in range(0, d):
        #出現回数をチェック重複またはその数が使われてないなら false
        if s.count(str(i)) != 1:
            f = False
    return f
array = []

for i in itertools.permutations("0123456789"):
    n = ''.join(i)

    if is_Pan(int(n)) == True:
        subs = []
        for j in range(1, len(n)-2):
            subs.append(int(n[j:j+3]))

        primes =[2,3,5,7,11,13,17]
        f = True
        for j in range(7):
            if subs[j] % primes[j] != 0:
                f = False
                break
        if f == True:
            array.append(int(n))

print(array)
print(sum(array))