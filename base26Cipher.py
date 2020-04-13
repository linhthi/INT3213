#Define alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

def Encrypt(statment):
    statment = statment.lower()
    n = len(statment)
    res = 0
    for i in range(n):
        res = res + alphabet.find(statment[i]) * (26 ** (n - i - 1))
    
    return res

def Decrypt(number):
    base = ''
    while(number):
        key = int(number % 26)
        number = number // 26
        base = alphabet[key] + base
    return base
