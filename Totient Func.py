def totient(): 
    x  = int(input("ENTER NO: "))
    prime_no = []
    prime_factors = []
    y = 1

    while y <= x/2:
        y = y + 1
        n = y
        i = 1
        
        while i <= n/2 :
            if n%i == 0:
                a = i
            i = i + 1
        if a == 1:
            prime_no.append(y)

    total = len(prime_no)
    index = 0

    while index < total:
        b = prime_no[index]
        if x % b == 0:
            prime_factors.append(b)
        index = index + 1
                                                  #Now we have the prime factors of the input, but without their respective exponents(just as needed for totient func)
    l = len(prime_factors)
    p = 0
    T = x
    
    while p < l:
        q = prime_factors[p]
        T = (T /q)* (q - 1)
        p = p + 1

    return T
    print("φ(" + str(x) + ") = " + str(T))

totient()

        
