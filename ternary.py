

get_t = lambda st, idx: st//(3**idx)%3
set_t = lambda st, idx, val: st - get_t(st, idx)*(3**idx) + val * 3**idx 