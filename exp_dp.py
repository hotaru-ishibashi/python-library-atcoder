from functools import cache


@cache
def rec(state, depth):
    # 終了条件
    if depth == N:
        return state
    

    e = 0
    patterns = 100
    for i in range(patterns):
        new_state = state + i
        e += rec(new_state, depth+1)

    return e / patterns
    # return e * pow(patterns, -1, mod)




