def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)

def permutasi(n, r):
    return round(faktorial(n)/faktorial(n - r))

def kombinasi(n, k):
    return round(faktorial(n)/(faktorial(n - k) * faktorial(k)))

# C(5, 3)
print(kombinasi(5, 3))
# P(10, 7)
print(permutasi(10, 7))