# すべての桁に 1 から n が一度だけ使われている数をn桁の数が
# パンデジタル (pandigital) であるということにしよう:
# 例えば5桁の数 15234 は1から5のパンデジタルである.

# 7254 は面白い性質を持っている. 39 × 186 = 7254 と書け, 
# 掛けられる数, 掛ける数, 積が1から9のパンデジタルとなる.

# 掛けられる数/掛ける数/積が1から9のパンデジタルとなるような積の総和を求めよ.

# ヒント: いくつかの積は, 
# 1通り以上の掛けられる数/掛ける数/積の組み合わせを持つが1回だけ数え上げよ.

##掛けた後の桁数を考える
##1から9のパンデジタルであるかどうか
def is_pandigital(a,b,c):
    s = str(a) + str(b) +str(c)
    for i in range(1,10):
        if str(i) not in s:
            return False
    return True

##先にsetで重複を避ける
answer = set()
##aが1桁1-9、bが４桁1000-9999の想定
for a in range(1,10):
    for b in range(1000, 10000):
        c = a * b
        if c >9999:
            break
        if is_pandigital(a,b,c):
            answer.add(c)
##aが2桁10-99、bが3桁100-999の想定
for a in range(10,100):
    for b in range(100, 1000):
        c = a * b
        if c >9999:
            break
        if is_pandigital(a,b,c):
            answer.add(c)

print(sum(answer))