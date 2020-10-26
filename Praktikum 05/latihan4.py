from math import floor

gaji_a = 10000000
gaji_b = 8500000
gaji_c = 7000000
gaji_d = 5500000

pot_a = floor(0.025*gaji_a)
pot_b = floor(0.02*gaji_b)
pot_c = floor(0.015*gaji_c)
pot_d = floor(0.01*gaji_d)

gaji_bersih = {'a': gaji_a-pot_a, 'b': gaji_b-pot_b, 'c':gaji_c-pot_c, 'd': gaji_d-pot_d}

list_gol = ('A','B','C','D')

kode_karyawan = input('Masukkan kode karyawan : ').upper()
nama_karyawan = input('Masukkan nama karyawan : ').upper()
golongan = input('Masukkan golongan      : ').upper()

print('\n'+'='*36)
print('STRUK RINCIAN GAJI KARYAWAN'.center(36))
print('-'*36)
if golongan in list_gol:
    print('Nama Karyawan          :', nama_karyawan, '(Kode : {})'.format(kode_karyawan))
    print('Golongan               :', golongan)
    print('-'*36)
    if golongan == 'A':
        print('Gaji Pokok             : Rp', gaji_a)
        print('Potongan               : Rp', pot_a)
        print('-'*36,'-')
        print('Gaji Bersih            : Rp', gaji_bersih['a'])
    elif golongan == 'B':
        print('Gaji Pokok             : Rp', gaji_b)
        print('Potongan               : Rp', pot_b)
        print('-'*36,'-')
        print('Gaji Bersih            : Rp', gaji_bersih['b'])
    elif golongan == 'C':
        print('Gaji Pokok             : Rp', gaji_c)
        print('Potongan               : Rp', pot_c)
        print('-'*36,'-')
        print('Gaji Bersih            : Rp', gaji_bersih['c'])
    else:
        print('Gaji Pokok             : Rp', gaji_d)
        print('Potongan               : Rp', pot_d)
        print('-'*36,'-')
        print('Gaji Bersih            : Rp', gaji_bersih['d'])

else:
    print('Input golongan tidak valid')