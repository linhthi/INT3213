from ElGamal import ElGamal
from base26Cipher import Encrypt
import Prime
from random import randint

# f = open('input.txt')
# np = int(f.readline())
# na = int(f.readline())
# nk = int(f.readline())
# base = f.readline()

base = 'Dexuatcachlyxahoivoinhomdiaphuongnguycocao'

p = 10**99 + 289
a = 10**59 + 1
k = 10**63 + 2
alpha = Prime.primitiveRoot(p)
print(alpha)


# p = Prime.randomPrime(np)
# a = randint(10 ** (na - 1), 10 ** na - 1)
# k = randint(10 ** (nk - 1), 10 ** nk - 1)
# alpha = Prime.primitiveRoot(p)
x = Encrypt(base) % p
print(x)

elGamal = ElGamal(p, a, k)
print(elGamal.beta)
y1, y2 = elGamal.enCode(x)
print((y1, y2))
print(elGamal.deCode(y1, y2))