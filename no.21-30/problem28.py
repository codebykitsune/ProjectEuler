##5*5のスタート地点
##1001×1001の螺旋を同じ方法で生成したとき, 対角線上の数字の和はいくつか?
# grid
# print(grid[2][2])
##print(grid[500][500])のところに1があってそこから螺旋状に動く
# grid[row]←何列目か[col]←その中の何番目か
##5*5 のとき
#一列目 1, 3,5,7,9 2ずつ
#二列目　13,17,21, 25 4ずつ
#n -1 /2 何列できるか
# 三列目　31, 37, 43, 49　 6ずつ

#n -1 /2 何列できるか
def row(n):
    if n % 2== 0:
        return n // 2
    else:
        return (n-1)//2

def corner(n):
    i = 1 
    list_corner = []
    list_corner.append(i)
    for k in range(1,n+1):
        for j in range(4):
            i += 2 * k
            list_corner.append(i)
    return sum(list_corner)

print(corner(row(1001)))
