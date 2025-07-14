##Lexicographic Permutations
#0-9
#10!
## we want to get 1000000th number
##itertools
import itertools
list_eg = [0,1,2]
test = list(itertools.permutations(range(len(list_eg))))
print(test) ##[(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
print(test[1]) 

list_num = [0,1,2,3,4,5,6,7,8,9]
MILLION = 1000000
a = list(itertools.permutations(range(len(list_num))))
print(a[MILLION -1]) ##2783915460

