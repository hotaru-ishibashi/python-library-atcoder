def monotone_minima_select(H, W, select):
    ret = [-1] * H
    if H == 0 or W == 0:
        return ret

    def dfs(top, bottom, left, right):
        if top > bottom:
            return

        line = (top + bottom) // 2
        best = select(line, left, right + 1)
        ret[line] = best

        dfs(top, line - 1, left, best)
        dfs(line + 1, bottom, best, right)

    dfs(0, H - 1, 0, W - 1)
    return ret


def monotone_minima(H, W, comp):
    def select(row, left, right):
        best = left
        for column in range(left + 1, right):
            if comp(row, best, column):
                best = column
        return best

    return monotone_minima_select(H, W, select)


# 各行の最小値の列番号を求める
a = [
    [0, 1, 4, 9, 16],
    [1, 0, 1, 4, 9],
    [4, 1, 0, 1, 9000],
    [9, 4, 1, 0, 1],
    [16, 9, 4, 1, 0],
]
# row行目について、row[j]がrow[i]より†††真に†††良いとき、True
# 最小値を求める場合なのでrow[i] > row[j]となる
def cmp(row, i, j):
    return a[row][i] > a[row][j]
ans = monotone_minima(5,5,cmp)

print(ans)
# [0, 1, 2, 3, 4]