


def judge(x):
    pass


# Decimalは死ぬほど遅いのでfloatでやろう
ok = 0
ng = 1
# log2(abs(ok-ng) * 許容誤差^-1)くらいにする 92あればよほどOKなので、定数倍きつくなければいじらない
trial_num = 92 

ct = 0
while ct < trial_num:
    mid = (ok+ng) / 2
    res = judge(mid)
    # print(mid, res)
    if res:
        ok = mid
    else:
        ng = mid
    ct += 1

