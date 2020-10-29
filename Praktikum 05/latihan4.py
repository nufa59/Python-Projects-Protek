from math import floor

list_gol = ('A','B','C','D')

kode_karyawan = input('Masukkan kode karyawan : ').upper()
nama_karyawan = input('Masukkan nama karyawan : ').upper()
golongan = input('Masukkan golongan      : ').upper()
if golongan not in list_gol:
    print('Input golongan tidak valid')
    exit()

if golongan == 'A':
      gaji = 10000000
      potongan = floor(0.025*gaji)
      gaji_bersih = gaji - potongan
elif golongan == 'B':
      gaji = 8500000
      potongan = floor(0.02*gaji)
      gaji_bersih = gaji - potongan
elif golongan == 'C':
      gaji = 7000000
      potongan = floor(0.015*gaji)
      gaji_bersih = gaji - potongan
else:
      gaji = 5500000
      potongan = floor(0.01*gaji)
      gaji_bersih = gaji - potongan
      
print('\n'+'='*36)
print('STRUK RINCIAN GAJI KARYAWAN'.center(36))
print('-'*36)
print('Nama Karyawan          :', nama_karyawan, '(Kode : {})'.format(kode_karyawan))
print('Golongan               :', golongan)
print('-'*36)
print('Gaji Pokok             : Rp', gaji)
print('Potongan               : Rp', potongan)
print('-'*36,'-')
print('Gaji Bersih            : Rp', gaji_bersih)
