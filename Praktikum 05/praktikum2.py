print('Nomor 2')
i = 0
while (i < 10):
    print('Hello world')
    i += 1

print('\nNomor 5')
i = 2
while (i <= 20):
    print('Hello world')
    i += 2

print('\nNomor 6')
i = 0
while True:
    print('Hello world')
    i += 1
    if (i == 10):
        break

print('\nNomor 5')
i = 2
while (i <= 20):
    print('Hello world')
    i += 2
    
print('\nNomor 8\n')
# kotak bintang ajaib
kolom = 5
baris = 5

i = 0
while (i < baris):
    j = 0
    while (j < kolom):
        print('* ', end='')
        j += 1
    print('')
    i += 1

print('\nNomor 10')
kolom = 5
baris = 5

i = 0
while (i < baris):
    j = 0
    while (j <= i):
        print('* ', end='')
        j += 1
    print('')
    i += 1

print('\nNomor 11')
from random import randint
while True:
    bil = randint(0, 10)
    print(bil)
    if bil == 5:
        break

print('\nNomor 13')
from random import randint

count = 0
while True:
    bil = randint(0, 10)
    print(bil)
    count += 1
    if bil == 5:
        print('Jumlah perulangan: ', count)
        break