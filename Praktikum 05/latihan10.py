from random import randint

acak = randint(0, 100)
print('\nHai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!')

while True:
    tebak = int(input('Tebakan Anda : '))
    if tebak < acak:
        print('Hehehe… Bilangan tebakan anda terlalu kecil')
    elif tebak > acak:
        print('Hehehe… Bilangan tebakan anda terlalu besar')
    elif tebak == acak:
        print('Yeeee… Bilangan tebakan anda BENAR :-)')
        break