def totient(x):
    n = x
    result = x
    p = 2

    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result = result // p * (p - 1)
        p += 1
    
    if n > 1:  # last prime factor > sqrt(x)
        result = result // n * (n - 1)
        
    return result

n = int(input("ENTER NO: "))
print(f"φ({n}) = {totient(n)}")

