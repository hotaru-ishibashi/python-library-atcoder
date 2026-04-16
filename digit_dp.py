from collections import defaultdict

class DigitDP:
    def __init__(self, digits):
        self.digits = digits
        self.n = len(digits)


    def solve(self, init_state, transition, init_accum, op, e):
        """
        Args:
            init_state: dpの状態の初期値 
                Tips: 直近の桁を持つときの初期値は0にしておいて、leading_zeroで条件分岐するとよい
            transition: dpの状態、集計値の遷移関数(state, next_digit, leading_zero, accum) => next_state, next_accum
            init_accum: dpの集計値の初期値
            op: dpの集計値の合成関数
            e: dpの集計値の合成の単位元
        """
        dp = defaultdict(int)
        dp[(init_state, True, True)] = init_accum

        for pos in range(self.n):
            next_dp = defaultdict(lambda: e)
            limit_digit = self.digits[pos]

            for (state, tight, leading_zero), accum in dp.items():
                limit = limit_digit if tight else 9

                for d in range(limit + 1):
                    next_tight = tight and (d == limit)
                    next_leading_zero = leading_zero and (d == 0)

                    next_state, next_accum = transition(state, d, leading_zero, accum)
                    if next_state is None:
                        continue

                    next_dp[(next_state, next_tight, next_leading_zero)] = op(next_dp[(next_state, next_tight, next_leading_zero)], next_accum)

            dp = next_dp
        return dp
    

######################
# サンプル: N以下で、隣接する桁同士の積の和の最大値
######################
init_state = 0
init_accum = 0
def transition(state, d, leading_zero, accum):
    pre_d = state
    next_state = d
    next_accum = 0 if leading_zero else accum + d*pre_d

    return next_state, next_accum
def op(acu1, acu2):
    return max(acu1, acu2)
e = 0

N = [int(c) for c in input().strip()]
digitdp = DigitDP(N)
res = digitdp.solve(init_state, transition, init_accum, op, e)
for k, v in res.items():
    print(k, v)