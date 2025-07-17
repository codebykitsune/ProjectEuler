
def mod_length(n):
    (i, remainder) = (1,1)
    list_mod =[]
    while True:
        ##1/n を小数にしていく筆算の流れ
        # 10の倍数をnで割ったときの余りをたどる
        remainder = (remainder * 10) % n 
        if remainder == 0:
            return 0
        list_mod.append(remainder)
        if remainder in list_mod[:-1]:
            length = i - (list_mod.index(remainder)+ 1)
            return length
        i +=1

def main():
    max_length = 0
    for i in range(2,1001):
        if mod_length(i) > max_length:
            max_length = mod_length(i)
            max_i = i
    print(max_i) ##longest one
    print(max_length)

main()