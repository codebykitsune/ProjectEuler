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