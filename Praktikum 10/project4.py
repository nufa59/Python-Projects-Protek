try:
    file = open('data2.txt', 'r')
    try:
        dataMhs = []
        for line in file.readlines():
            data = {}
            nim, nama, alamat = line.split('|')
            alamat = alamat[:-1]
            data['nim'] = nim
            data['nama'] = nama
            data['alamat'] = alamat
            dataMhs.append(data)

        while True:
            cari_nim = input('\nMasukkan NIM yang akan dicari: ')
            for mhs in dataMhs:
                if cari_nim == mhs['nim']:
                    print('Data Mahasiswa')
                    print(f"NIM    : {mhs['nim']}")
                    print(f"NAMA   : {mhs['nama']}")
                    print(f"ALAMAT : {mhs['alamat']}")
                    break
                elif mhs == dataMhs[-1]:
                    print('Data mahasiswa tidak ditemukan')
            conf = input('\nCari lagi (y/n): ').lower()
            if conf == 'n': break
    finally:
        file.close()
except FileNotFoundError:
    print('File tidak ditemukan')
