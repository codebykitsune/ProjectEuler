##max number 28123
##2つの過剰数の和として表せないすべての正の整数の合計
##ステップ
##過剰数を求める
##for in range(11,28123)で回して足していく

##non-abundant sums
##under 28123 over 12
##約数を求める
#1,2,3,4,6,= 16 is over 12
##this is abundant number

##the sum of the smallest abundant number is 24(12+12)

## if n is abundantNumber or not
def If_abundantNumber(n):
    total = 1 ## 1 is included in every number
    i = 2
    while i*i <= n:
      if n % i == 0:
         total += i
         if i != n / i:
            total += n // i
      i += 1
    return total > n


##28123までで数を調べる
abundant_numbers = []
for i in range(12, 28124):
    if If_abundantNumber(i):
       abundant_numbers.append(i)
