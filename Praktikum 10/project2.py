try:
    file = open('data2.txt', 'w')
    try:
        while True:
            nim_mhs = input('Masukan NIM                : ')
            nama_mhs = input('Masukan Nama Mhs           : ')
            alamat_mhs = input('Masukan Alamat             : ')
            data = nim_mhs, nama_mhs, alamat_mhs
            data = '|'.join(data)
            file.write(data+'\n')
            conf = input('\nUlangi input lagi (y/n)    : ').lower()
            print()
            if conf == 'n':
                break
    finally:
        file.close()
except FileNotFoundError:
    print('File tidak ditemukan')