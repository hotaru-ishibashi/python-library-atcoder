from math import isqrt

def sieve_of_eratosthenes(N):
    primes = [True] * (N + 1)
    primes[0] = primes[1] = False  # 0と1は素数ではない
    for i in range(2, int(N ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, N + 1, i):
                primes[j] = False
    return [x for x in range(N + 1) if primes[x]]

def seg_sieve(l: int, r: int) -> list[list[int]]:
    n = r - l
    # 1. 前処理: √r までの素数を通常のエラトステネスで列挙
    limit = isqrt(r - 1)        # r は開区間なので r-1 の平方根
    base_primes = sieve_of_eratosthenes(limit+1)
    
    isprime = [True] * n
    for p in base_primes:
        # 区間内で p の倍数が始まる最初の値
        start = max(p * p, ((l + p - 1) // p) * p)
        # start, start+p, …, < r を p ずつ進みながら合成数マーキング
        for x in range(start, r, p):
            isprime[x - l] = False

    # --- 3. 残っている True が素数 -------------------------------------
    return [l + i for i, ok in enumerate(isprime) if ok]
