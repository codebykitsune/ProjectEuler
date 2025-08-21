##出典
##https://odz.sakura.ne.jp/projecteuler/index.php?Problem+33
##49/98 は面白い分数である.「分子と分母からそれぞれ9を取り除くと, 49/98 = 4/8 となり, 
# 簡単な形にすることができる」
# と経験の浅い数学者が誤って思い込んでしまうかもしれないからである.
#  (方法は正しくないが，49/98 の場合にはたまたま正しい約分になってしまう．)

# 我々は 30/50 = 3/5 のようなタイプは自明な例だとする.

# このような分数のうち, 1より小さく
# 分子・分母がともに2桁の数になるような "自明でない" ものは, 4個ある.

# その4個の分数の積が約分された形で与えられたとき, 分母の値を答えよ.

##10-99で回す
##numerator and denominatorを文字化する
##49/98 if numerator and denominator has a same number(1-9) then return delete the number
## re-make numerator and denominator 
## if numerator and denominator can divide each other then return list.append(fraction)



##49/98 if numerator and denominator has a same number(1-9) then return delete the number
import math
def can_simplify(numerator, denominator):
    gcd = math.gcd(numerator, denominator)
    if gcd > 1:
        return numerator // gcd, denominator // gcd
    else:
        return False

def same_number(a,b):
    ##aが分子でbが分母
    if a >= b:
        return False
    a_str = str(a)
    b_str = str(b)
    for i in range(1,10):
        i_str = str(i)
        if i_str in a_str and i_str in b_str:
            a_new_str = a_str.replace(i_str,"",1)
            b_new_str = b_str.replace(i_str,"",1)
        ##ここからかつ割れるもの
        ##数値に戻す
            if a_new_str == "" or b_new_str == "":
                continue
            a_int = int(a_new_str) 
            b_int = int(b_new_str) 
            if b_int == 0:
                continue

            if a * b_int == b * a_int:
                return True
    return False

def main():
    fractions = []
    for i in range(10, 100):
        for j in range(10, 100):
            if same_number(i,j):
                fractions.append((i,j))
    num_product = 1
    den_product = 1
    for(n,d) in fractions:
        num_product *= n
        den_product *= d
    gcd = math.gcd(num_product, den_product)
    num_product //= gcd
    den_product //= gcd
    print(fractions)
    print(den_product)

main()
