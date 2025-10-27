
N = 10
A = [3, 5, 11, 2, 0, 1, 9, 5, 2, 8]
thresh = 7

def syakutori(N, A, e, op, inv, P):
    '''
    :param int N: 数列長
    :param List[T] A: 走査対象数列
    :param T e: 単位元
    :param (T, T) -> T op: 演算
    :param T inv: 逆元
    :param (T, T) -> boolean P: 集計値が条件を満たすか
    '''
    l_memo = [None] * N

    right = 0
    accum = e
    for left in range(N):
        # 
        while right < N and P(accum, A[right]):
            accum = op(accum, A[right])
            right += 1

        # [left, right)が最大を満たす最大の区間
        # なんやかんやする
        # print(left, right, accum)
        l_memo[left] = [right, accum]
        
        if right == left:
            right += 1
        else:
            accum = op(accum, inv(A[left]))

    return l_memo

def P(accum, nex):
    return accum <= 7

res = syakutori(N, A, 0, lambda x, y: x+y, lambda x: -x, P)
print(res)
