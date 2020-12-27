try:
    file = open('data1.txt', 'r')
    try:
        ganjil = 0
        genap = 0
        for line in file.readlines():
            if int(line) % 2 == 0:
                genap += 1
            else:
                ganjil += 1              
        print(f'Banyaknya bilangan genap: {genap}')
        print(f'Banyaknya bilangan ganjil: {ganjil}')
    finally:
        file.close()
except FileNotFoundError:
    print('File tidak ditemukan')
