from math import floor

jumlah_anak = 0
list_gol = ('A','B','C','D')

kode_karyawan = input('Masukkan kode karyawan : ').upper()
nama_karyawan = input('Masukkan nama karyawan : ').upper()
golongan = input('Masukkan golongan      : ').upper()
if golongan not in list_gol:
    print('Input golongan tidak valid')
    exit()
    
status = int(input('Masukan status [1:Sudah Menikah, 2:Belum Menikah] : '))
if status == 1:
    jumlah_anak = int(input('Masukkan jumlah anak   : '))
elif status == 2:
    status -= 2
else:
    print('Input status tidak valid')
    exit()    
    
status_menikah = {
    0: 'Belum Menikah',
    1: 'Sudah Menikah'
}

if golongan == 'A':
      gaji_pokok = 10000000
      potongan = 0.025*gaji_pokok
      tunjangan_menikah = 0.1 * gaji_pokok * status
      tunjangan_anak = 0.05 * gaji_pokok * jumlah_anak
elif golongan == 'B':
      gaji_pokok = 8500000
      potongan = 0.02*gaji_pokok
      tunjangan_menikah = 0.1 * gaji_pokok * status
      tunjangan_anak = 0.05 * gaji_pokok * jumlah_anak
elif golongan == 'C':
      gaji_pokok = 7000000
      potongan = 0.015*gaji_pokok
      tunjangan_menikah = 0.1 * gaji_pokok * status
      tunjangan_anak = 0.05 * gaji_pokok * jumlah_anak
else:
      gaji_pokok = 5500000
      potongan = 0.01*gaji_pokok
      tunjangan_menikah = 0.1 * gaji_pokok * status
      tunjangan_anak = 0.05 * gaji_pokok * jumlah_anak

gaji_kotor = gaji_pokok + tunjangan_menikah + tunjangan_anak
gaji_bersih = gaji_kotor - potongan

print('\n'+'='*44)
print('STRUK RINCIAN GAJI KARYAWAN'.center(44))
print('-'*44)
print('Nama Karyawan          :', nama_karyawan, '(Kode : {})'.format(kode_karyawan))
print('Golongan               :', golongan)
print('Status Menikah         :', status_menikah[status])
if status == 1:
    print('Jumlah Anak            :', jumlah_anak)
print('-'*44)
print('Gaji Pokok             : Rp', gaji_pokok)
if status == 1:
    print('Tunjangan Istri/Suami  : Rp', floor(tunjangan_menikah))
    print('Tunjangan Anak         : Rp', floor(tunjangan_anak))
print('-'*44,'+')
print('Gaji Kotor             : Rp', floor(gaji_kotor))
print('Potongan               : Rp', floor(potongan))
print('-'*44,'-')
print('Gaji Bersih            : Rp', floor(gaji_bersih))