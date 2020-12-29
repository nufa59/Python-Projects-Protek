from datetime import datetime

def diffDate(date):
    sekarang = datetime.now().date()
    tanggal = datetime.strptime(date, '%Y-%m-%d').date()
    return abs(sekarang-tanggal).days

with open('data.txt') as f:
    data_pinjam = []
    for line in f.readlines():
        line = line.strip('\n')
        data = line.split('|')
        data_pinjam.append(data)
print('-'*34)
print('|', 'PROGRAM PERPUSTAKAAN'.center(30), '|')
print('-'*34)
while True:
    kode = input('\nMasukan Kode Member         : ')
    data_kodmem = [x[0] for x in data_pinjam]
    if kode in data_kodmem:
        for data in data_pinjam:
            kode_member, nama_member, judul_buku, tanggal_mulai_pinjam, tanggal_maks_pengembalian = data
            if kode == kode_member:
                tanggal_pengembalian = datetime.now().date()
                terlambat = 0 if diffDate(tanggal_mulai_pinjam) <= 7 else diffDate(tanggal_maks_pengembalian)
                denda = terlambat * 2000
                
                print('\nData Peminjaman Buku')
                print(f'Kode Member                 : {kode_member}')
                print(f'Nama Member                 : {nama_member}')
                print(f'Judul Buku                  : {judul_buku}')
                print(f'Tanggal Mulai Peminjaman    : {tanggal_mulai_pinjam}')
                print(f'Tanggal Maks Peminjaman     : {tanggal_maks_pengembalian}')
                print(f'Tanggal Pengembalian        : {tanggal_pengembalian}')
                print(f'Terlambat                   : {terlambat} hari')
                print(f'Denda                       : Rp {denda}')
    else:
        print(f'Data Peminjaman dengan kode {kode} tidak ditemukan')
    lagi = input('\nUlang lagi (y/n)            : ')
    if lagi == 'n': break