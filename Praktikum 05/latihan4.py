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
      pot_percent = '2.5 %'
elif golongan == 'B':
      gaji = 8500000
      potongan = floor(0.02*gaji)
      pot_percent = '2.0 %'
elif golongan == 'C':
      gaji = 7000000
      potongan = floor(0.015*gaji)
      pot_percent = '1.5 %'
else:
      gaji = 5500000
      potongan = floor(0.01*gaji)
      pot_percent = '1.0 %'

gaji_bersih = gaji - potongan
      
print('\n'+'='*36)
print('STRUK RINCIAN GAJI KARYAWAN'.center(36))
print('-'*36)
print('Nama Karyawan          :', nama_karyawan, '(Kode : {})'.format(kode_karyawan))
print('Golongan               :', golongan)
print('-'*36)
print('Gaji Pokok             : Rp', gaji)
print(f'Potongan ({pot_percent})        : Rp', potongan)
print('-'*36,'-')
print('Gaji Bersih            : Rp', gaji_bersih)
