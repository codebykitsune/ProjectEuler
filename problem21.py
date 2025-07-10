##Amicable Numbers 
##$220$ are $1, 2, 4, 5, 10, 11, 20, 22, 44, 55$ and $110$; 
#therefore $d(220) = 284$.
##The proper divisors of $284$ are $1, 2, 4, 71$ and $142$; 
##so $d(284) = 220$.

def Amicable_Numbers(n):
    i =1
    table =[]
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            if i != (n//i):
                table.append(n//i)
        i += 1
    table = sorted(list(set(table)))
    table.remove(n)
    sum_table = sum(table)
    return sum_table

print(Amicable_Numbers(220))##284
print(Amicable_Numbers(284))##220
amicable_dict = {}
for i in range(1,10001):
    result = Amicable_Numbers(i)
    amicable_dict[i] = result 

sum_num = 0
for a in range(1,10001):
    b = amicable_dict[a]
    if b != a and b<=10000:
        if amicable_dict.get(b) == a:
            if a <b:
                sum_num = sum_num + a + b

print(sum_num)
   