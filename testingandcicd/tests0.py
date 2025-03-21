from prime import is_prime

def test_prime(n, expected):
    # is_primeの実行結果が引数expectedと違った場合
    if is_prime(n) != expected:
        # エラーになる
        print(f"ERROR on is_prime({n}), expected {expected}")


#>>> python
#>>> from tests0 import test_prime
#>>> test_prime(5, True)
#>>> test_prime(6, True)
#>>> test_prime(6, False)
#ERROR on is_prime(6), expected False
