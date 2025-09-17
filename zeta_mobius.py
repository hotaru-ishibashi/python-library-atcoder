
"""
retval: zeta[s]: sの部分集合tについてのf[t]の総和
"""
def zeta_subset(f, N):
    for i in range(N):
        mask = 1<<i
        for b in range(1<<N):    
            if b & mask:
                f[b] += f[b ^ mask]
    return f

"""
retval: zeta[s]: sの上位集合tについてのf[t]の総和
"""
def zeta_superset(f, N):
    for i in range(N):
        mask = 1<<i
        for b in range(1<<N):    
            if not (b & mask):
                f[b] += f[b | mask]
    return f

"""
retval: mobius[s]: zeta_subsetの逆変換 
"""
def mobius_subset(f, N):
    for i in range(N):
        mask = 1<<i
        for b in range(1<<N):    
            if b & mask:
                f[b] -= f[b ^ mask]
    return f

"""
retval: mobius[s]: zeta_supersetの逆変換
"""
def mobius_superset(f, N):
    for i in range(N):
        mask = 1<<i
        for b in range(1<<N):    
            if not (b & mask):
                f[b] -= f[b | mask]
    return f