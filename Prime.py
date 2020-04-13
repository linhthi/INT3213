
import math
from random import randint
from modularPower import power

def is_prime(number):
    if number <= 1 or (number > 2 and number % 2 == 0):
        return False
    
    for factor in range(2, int(math.sqrt(number))+1):
        if number % factor == 0:
            return False
    return True

def isPrime(n):
    primes = SieveOfEratosthenes(n)
    return primes[n]

def randomPrime(lengthNumber):
    primes = SieveOfEratosthenes(10 ** (lengthNumber - 1) * 4)
    start = 10 ** (lengthNumber - 1)
    end = 4 * (10 ** (lengthNumber - 1))
    a = start
    while(primes[a] == True):
        a = randint(start, end)
    return a

def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1

    return prime

# Tim thanh phan nguyen thuy nho nhat cua n
def primeDivisors(n):
    prime = SieveOfEratosthenes(n)
    prime_divisor = []
    for i in range(2, n+1):
        if prime[i] and n % i == 0:
            prime_divisor.append(i)

    return prime_divisor


# Find the smallest primitive root
def primitiveRoot(n):
    # if isPrime(n) == False:
    #     return -1
    
    phi = n - 1
    s = primeDivisors(phi)

    # Check for every number from 2 to phi
    for i in range(2, phi + 1):
        flag = False
        for it in s:
            if power(i, phi // it, n) == 1:
                flag = True
                break
        
        if flag == False:
            return i
    return -1


# if __name__== '__main__':
#     n = 761
#     print(primeDivisors(n))
#     print(primitiveRoot(n))
