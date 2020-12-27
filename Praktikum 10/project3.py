try:
    file = open('data2.txt', 'r')
    try:
        dataMhs = []
        for line in file.readlines():
            nim, nama, alamat = line.split('|')
            data = {'nim': nim, 'nama': nama, 'alamat': alamat[:-1]}
            dataMhs.append(data)
        print(dataMhs)
    finally:
        file.close()
except FileNotFoundError:
    print('File tidak ditemukan')