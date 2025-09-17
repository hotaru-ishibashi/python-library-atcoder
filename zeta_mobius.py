

def zeta_subset(f, N):
    for i in range(N):
        mask = 1<<i
        for b in range(1<<N):    
            if b & mask:
                f[b] += f[b ^ mask]
    return f


def zeta_superset(f, N):
    for i in range(N):
        mask = 1<<i
        for b in range(1<<N):    
            if not (b & mask):
                f[b] += f[b | mask]
    return f


def mobius_subset(f, N):
    for i in range(N):
        mask = 1<<i
        for b in range(1<<N):    
            if b & mask:
                f[b] -= f[b ^ mask]
    return f


def mobius_superset(f, N):
    for i in range(N):
        mask = 1<<i
        for b in range(1<<N):    
            if not (b & mask):
                f[b] -= f[b | mask]
    return f