# n桁パンデジタルであるとは, 
# 1からnまでの数を各桁に1つずつ持つこととする.

# #下のリンク先にあるような数学的定義とは異なる

# 例えば2143は4桁パンデジタル数であり, かつ素数である. 
# n桁（この問題の定義では9桁以下）
# パンデジタルな素数の中で最大の数を答えよ.

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    i = 3
    while i <= n ** 0.5:
        if n % i == 0:
            return False
        i +=2
    return True

