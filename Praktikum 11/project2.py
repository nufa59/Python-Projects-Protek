from datetime import datetime, timedelta

print('-'*34)
print('|', 'PROGRAM PERPUSTAKAAN'.center(30), '|')
print('-'*34)

with open('data.txt', 'a') as f:
    while True:
        tanggal_pinjam = datetime.now().date()
        tanggal_pengembalian = tanggal_pinjam + timedelta(days=7)
        
        kode_member = input('\nMasukan Kode Member    : ')
        nama_member = input('Masukan Nama Member    : ')
        judul_buku  = input('Masukan Judul Buku     : ')
        
        data = '|'.join([kode_member, nama_member, judul_buku, str(tanggal_pinjam), str(tanggal_pengembalian)]) + '\n'
        f.write(data)      

        lagi        = input('\nUlangi lagi (y/n)      : ').lower()
        if lagi == 'n':
            print('Data berhasil ditambahkan, periksa pada file data.txt')
            break