##F1 =1, F2 = 1
## F3 = F1 + F2 ##2
##F4 = F2 + F3 ##3

##そもそもFibonacci
# def Fibonacci(n):
#     list_F =[1,1]
#     F1 = 1
#     F2 = 1
#     for i in range(n-2):
#         if n-2 < 0:
#             return list_F
#         Fn = F1 + F2
#         list_F.append(Fn)
#         F1 = F2
#         F2 = Fn
#     return list_F

import time
start = time.time()

F1 = 1
F2 = 1
index = 2
while True:
     Fn = F1 + F2
     index +=1
     if len(str(Fn)) >= 1000:
         break
     F1 = F2
     F2 = Fn
print(index)

end = time.time()
print(f"処理時間: {end - start:.5f}秒")
