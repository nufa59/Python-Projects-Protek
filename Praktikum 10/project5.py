import time

try:
    file = open('data3.txt', 'r')
    try:
        print('Membaca file data3.txt')
        data_nilai = []
        for data in file.readlines():
            num1, num2 = data.split('|')
            jumlah = int(num1) + int(num2)
            data_nilai.append(jumlah)
        time.sleep(0.5)

        with open('data4.txt', 'w') as f:
            for i in data_nilai:
                f.write(str(i)+'\n')
        print('Data berhasil dijumlahkan, periksa file data4.txt') 
    finally:
        file.close()
except FileNotFoundError:
    print('File tidak ditemukan')