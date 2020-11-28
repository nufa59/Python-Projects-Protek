path = input('Masukan nama file: ')

try:
    file = open(path, 'r')
    print('Isi file', path, 'adalah: \n')
    print(file.read())
except FileNotFoundError:
    print('File tidak ditemukan')
except PermissionError:
    print('Akses ditolak')
