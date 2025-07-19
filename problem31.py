# イギリスでは硬貨はポンド£とペンスpがあり，
# 一般的に流通している硬貨は以下の8種類である.

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

# 以下の方法で£2を作ることが可能である．

# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

# これらの硬貨を使って£2を作る方法は何通りあるか?

##再帰関数

def count_methods(price, coins):
    #残りが1pだった場合、
    #一通りなので１を返す
    if len(coins) == 0:
        return 1
    
    else:
        ##合計値変数の宣言
        s = 0
        #使うコインの種類[リストの先頭]
        c = coins[0]
        #そのコインを最大何枚使えるか(0枚-q枚)
        q = (price//c)
        for i in range(0, q +1):
            s += count_methods(price - c * i, coins[1:])
        return s
    
def main():
    price = 200
    coins = [200,100,50,20,10,5,2]
    print(count_methods(price,coins))

main()
