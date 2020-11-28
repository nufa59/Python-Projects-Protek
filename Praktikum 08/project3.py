while True:
    try : jml = int(input('Masukan jumlah mahasiswa: ')); break
    except ValueError: print('Masukan angka')
nama_mhs = []
for _ in range(jml):
    nama = input('Masukan nama mahasiswa: ')
    nama_mhs.append(f'{nama} ({len(nama)} karakter)')
nama_mhs.sort()
print('\nData Mahasiswa:')
for nama in nama_mhs:
    print(nama)