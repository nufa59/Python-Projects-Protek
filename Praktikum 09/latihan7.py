mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

kolom = {'nim': 11, 'nama': 22, 'tgl_lahir': 16, 'tempat_lahir': 13}
panjang = 62
print('='*panjang)
print('NIM'.ljust(kolom['nim']), end='')
print('NAMA MAHASISWA'.ljust(kolom['nama']), end='')
print('TGL LAHIR'.ljust(kolom['tgl_lahir']), end='')
print('TEMPAT LAHIR'.ljust(kolom['tempat_lahir']), end='')
print()
print('-'*panjang)
for data in mhs:
    nim, nama, tgl_lahir, tempat_lahir = data.split(':')
    tgl_lahir = reversed(tgl_lahir.split('-'))
    tgl_lahir = '/'.join(tgl_lahir)
    print(f'{nim}'.ljust(kolom['nim']), end='')
    print(f'{nama}'.ljust(kolom['nama']), end='')
    print(f'{tgl_lahir}'.ljust(kolom['tgl_lahir']), end='')
    print(f'{tempat_lahir}'.ljust(kolom['tempat_lahir']), end='')
    print()
print('-'*panjang)
