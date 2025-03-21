import math

# 引数の数字が素数がどうかチェック。素数ならTrue、違う場合はFalse
def is_prime(n):
    if n < 2:
        return False
    # iが2からnまでの範囲の場合
    #for i in range(2, n):
    for i in range(2, int(math.sqrt(n) + 1)):
        # %は余り
        if n % i == 0:
            return False
    return True
