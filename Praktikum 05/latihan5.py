jumlah_anak = 0
kode_karyawan = input('Masukkan kode karyawan : ').upper()
nama_karyawan = input('Masukkan nama karyawan : ').upper()
golongan = input('Masukkan golongan      : ').upper()
status = int(input('Masukan status [0:Belum Menikah, 1:Sudah Menikah] : '))
if status == 1:
    jumlah_anak = int(input('Masukkan jumlah anak   : '))

gaji_pokok = {
    'a' : 10000000,
    'b' : 8500000,
    'c' : 7000000,
    'd' : 5500000
}

potongan = {
    'a' : 0.025*gaji_pokok['a'],
    'b' : 0.02*gaji_pokok['b'],
    'c' : 0.015*gaji_pokok['c'],
    'd' : 0.01*gaji_pokok['d']   
}
status_menikah = {
    0: 'Belum Menikah',
    1: 'Sudah Menikah'
}

tunjangan_menikah = {
    'a': 0.1*gaji_pokok['a']*status,
    'b': 0.1*gaji_pokok['b']*status,
    'c': 0.1*gaji_pokok['c']*status,
    'd': 0.1*gaji_pokok['d']*status
}

tunjangan_anak = {
    'a': (0.05 * gaji_pokok['a'])*jumlah_anak,
    'b': (0.05 * gaji_pokok['b'])*jumlah_anak,
    'c': (0.05 * gaji_pokok['c'])*jumlah_anak,
    'd': (0.05 * gaji_pokok['d'])*jumlah_anak
}

gaji_kotor = {
    'a': gaji_pokok['a'] + tunjangan_menikah['a'] + tunjangan_anak['a'],
    'b': gaji_pokok['b'] + tunjangan_menikah['b'] + tunjangan_anak['b'],
    'c': gaji_pokok['c'] + tunjangan_menikah['c'] + tunjangan_anak['c'],
    'd': gaji_pokok['d'] + tunjangan_menikah['d'] + tunjangan_anak['d']
}
gaji_bersih = {
    'a': gaji_kotor['a']-potongan['a'],
    'b': gaji_kotor['b']-potongan['b'], 
    'c': gaji_kotor['c']-potongan['c'], 
    'd': gaji_kotor['d']-potongan['d']
}

list_gol = ('A','B','C','D')

print('\n'+'='*44)
print('STRUK RINCIAN GAJI KARYAWAN'.center(44))
print('-'*44)
if golongan in list_gol:
    print('Nama Karyawan          :', nama_karyawan, '(Kode : {})'.format(kode_karyawan))
    print('Golongan               :', golongan)
    print('Status Menikah         :', status_menikah[status])
    if status == 1:
        print('Jumlah Anak            :', jumlah_anak)
    print('-'*44)
    if golongan == 'A':
        print('Gaji Pokok             : Rp', gaji_pokok['a'])
        if status == 1:
            print('Tunjangan Istri/Suami  : Rp', tunjangan_menikah['a'])
            print('Tunjangan Anak         : Rp', tunjangan_anak['a'])
        print('-'*44,'+')
        print('Gaji Kotor             : Rp', gaji_kotor['a'])
        print('Potongan               : Rp', potongan['a'])
        print('-'*44,'-')
        print('Gaji Bersih            : Rp', gaji_bersih['a'])
    elif golongan == 'B':
        print('Gaji Pokok             : Rp', gaji_pokok['b'])
        if status == 1:
            print('Tunjangan Istri/Suami  : Rp', tunjangan_menikah['b'])
            print('Tunjangan Anak         : Rp', tunjangan_anak['b'])
        print('-'*44,'+')
        print('Gaji Kotor             : Rp', gaji_kotor['b'])
        print('Potongan               : Rp', potongan['b'])
        print('-'*44,'-')
        print('Gaji Bersih            : Rp', gaji_bersih['b'])
    elif golongan == 'C':
        print('Gaji Pokok             : Rp', gaji_pokok['c'])
        if status == 1:
            print('Tunjangan Istri/Suami  : Rp', tunjangan_menikah['c'])
            print('Tunjangan Anak         : Rp', tunjangan_anak['c'])
        print('-'*44,'+')
        print('Gaji Kotor             : Rp', gaji_kotor['c'])
        print('Potongan               : Rp', potongan['c'])
        print('-'*44,'-')
        print('Gaji Bersih            : Rp', gaji_bersih['c'])
    else:
        print('Gaji Pokok             : Rp', gaji_pokok['d'])
        if status == 1:
            print('Tunjangan Istri/Suami  : Rp', tunjangan_menikah['d'])
            print('Tunjangan Anak         : Rp', tunjangan_anak['d'])
        print('-'*44,'+')
        print('Gaji Kotor             : Rp', gaji_kotor['d'])
        print('Potongan               : Rp', potongan['d'])
        print('-'*44,'-')
        print('Gaji Bersih            : Rp', gaji_bersih['d'])

else:
    print('Input golongan tidak valid')