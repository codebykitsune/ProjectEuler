#Digit Fifth Powers
sum_a = 0
max = (9**5)*6
for i in range(1,max + 1):
    count = 0
    digit_string = str(i)
    for j in digit_string:
        count += int(j) ** 5
    if count == i and i != 1:
        print(count)
        sum_a += count

print(sum_a,"yay")

# print((9**5)*7) 
##7桁だけど出力は6桁　桁数と合計数の桁が同じになることはない
