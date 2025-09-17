class PrefixOperation:
    def __init__(self, op, e, inv, vals):
        self.bucket = [e]
        self.op = op
        self.inv = inv
        for val in vals:
            self.bucket.append(op(self.bucket[-1], val))
    def query(self, l, r):
        return self.op(self.bucket[r], self.inv(self.bucket[l]))
        

class PrefixSum(PrefixOperation):
    def __init__(self, vals):
        super().__init__(lambda x, y: x+y, 0, lambda x: -x, vals)
    
class PrefixXor(PrefixOperation):
    def __init__(self, vals):
        super().__init__(lambda x, y: x^y, 0, lambda x: x, vals)
    
    
class PrefixProd(PrefixOperation):
    def __init__(self, vals, mod):
        super().__init__(lambda x, y: (x*y)%mod, 1, lambda x: pow(x, -1, mod), vals)