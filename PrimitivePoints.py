def findPrimitivePoint(p,a,b):
    k = int((p+1) / 2)
    Q = set()
    E = []
    for i in range(1, k+1):
        x = i**2 % p
        Q.add(x)
    
    # print(Q)

    for x in range(0, p):
        sqrY = (x**3 + a*x + b) % p
        if sqrY in Q:
            for i in range(1, k+1):
                if i**2 % p == sqrY:
                    E.append((x, i))
                    break
        if len(E) == 1:
            return E[0]


# (x, y) = findPrimitivePoint(571, 28, 23)
# print(x, y)

