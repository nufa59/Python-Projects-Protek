def luasSegitiga(a, t):
    luas = a * t / 2
    return luas

alas1 = 10
alas2 = 15
tinggi1 = 20
tinggi2 = 45
result = luasSegitiga(alas1, tinggi1) + luasSegitiga(alas2, tinggi2)
print(f'Total luas kedua segitiga adalah {result}')