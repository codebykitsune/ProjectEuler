##max number 28123
##2つの過剰数の和として表せないすべての正の整数の合計
##ステップ
##1,過剰数を求める関数
##2,for in range(11,28124)で回して足していく
##3,2つの過剰数の和をセット化する {12,12}{12,18}....

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

sum_of_abundants = set()
for i in abundant_numbers:
  for j in abundant_numbers:
    s = i + j
    if s <= 28123:
      sum_of_abundants.add(s)

list_not_abundants =[]
for k in range(1, 28124):
  if k not in sum_of_abundants:
    list_not_abundants.append(k)

print(sum(list_not_abundants))
