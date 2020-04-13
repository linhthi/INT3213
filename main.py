from ElGamal import ElGamal
from base26Cipher import Encrypt
import Prime
from random import randint

# f = open('input.txt')
# np = int(f.readline())
# na = int(f.readline())
# nk = int(f.readline())
# base = f.readline()

np = 4
na = 3
nk = 3
base = 'HOANGTHILINH'

p = Prime.randomPrime(np)
a = randint(10 ** (na - 1), 10 ** na - 1)
k = randint(10 ** (nk - 1), 10 ** nk - 1)
alpha = Prime.primitiveRoot(p)
x = Encrypt(base) % p


elGamal = ElGamal(p, a, k)
print(elGamal.beta)
y1, y2 = elGamal.enCode(x)
print((y1, y2))
print(elGamal.deCode(y1, y2))