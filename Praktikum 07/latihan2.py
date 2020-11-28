name = input('Masukan nama file: ')
try:
    file = open(name, 'a')
    while True:
        data = input('Data yang mau ditambahkan: ')
        file.write(data + '\n')
        confirm = input('Mau lagi (y/n): ')
        if confirm == 'n': break
    file.close()
except FileNotFoundError: 
    print('Nama file tidak Valid')
except OSError: 
    print('Nama file tidak valid')