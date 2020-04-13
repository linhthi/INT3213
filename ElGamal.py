from modularPower import power
import Prime

class ElGamal:
    
    def __init__(self, p, a, k):
        self.p = p
        self.a = a
        self.k = k
        self.alpha = Prime.primitiveRoot(p)
        self.beta = power(self.alpha, a, p)

    def enCode(self, x):
        y1 = power(self.alpha, self.k, self.p)
        y2 = ((x % self.p) * power(self.beta, self.k, self.p)) % self.p
        return (y1, y2)

    def deCode(self, y1, y2):
        dy1 = power(y1, self.p - self. a - 1, self.p)
        x = ((y2 % self.p) * dy1) % self.p
        return (x, dy1) 

        