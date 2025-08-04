# 辺の長さが整数の3つ組{a,b,c}である直角三角形を考え, 
# その周囲の長さを p とする. p = 120のときには3つの解が存在する:

# {20,48,52}, {24,45,51}, {30,40,50}

# p ≤ 1000 のとき解の個数が最大になる p はいくつか?

#c**2 = a **2 + b **2
#a<b<c
# a+ b+ c = p
# a is between 1 and p//3

def main():
    solutions ={}
    for p in range(1,1001):
        for a in range(1,p//3):
            b = (p*p -2*p*a)/(2*p - 2*a)
            if b % 1 == 0:
                c = p - a - b
                if a<b<c:
                    solutions[p] = solutions.get(p,0) + 1
    max_solution = max(solutions, key = solutions.get)
    return max_solution

print(main())