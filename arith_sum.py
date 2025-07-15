

def arith_sum(a1, an, d):
    n = ((an - a1) // d) + 1

    if n%2==0:
        return (a1+an) * (n//2) 
    else:
        return (a1+an) * (n//2) + (a1+an) // 2
    
def arith_sum2(a1, n, d):
    an = a1 + (n-1) * d

    return arith_sum(a1, an, d)