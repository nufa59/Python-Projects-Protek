from random import randint

acak = randint(0, 100)
score = 100
print('\nHai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!')

while True:
    if score < 0:
        print('\nYahh... score anda habis :(')
        break

    tebak = int(input('Tebakan Anda : '))
    if tebak < acak:
        print('Hehehe… Bilangan tebakan anda terlalu kecil')
        score -= 2
    elif tebak > acak:
        print('Hehehe… Bilangan tebakan anda terlalu besar')
        score -= 2
    elif tebak == acak:
        print('Yeeee… Bilangan tebakan anda BENAR :-)')
        print('\nScore anda :', score)
        break
    