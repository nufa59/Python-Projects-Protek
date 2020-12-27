import os, time

def clear():
    os.system('cls') if os.name == 'nt' else os.system('clear')

def decrypt_caesar(teks='', n=0):
    result = ''
    for i in teks:
        charA = ord('A') if i.isupper() else ord('a')
        if i != ' ':
            geser = ord(i) - n
            result = result + chr(geser + 26) if geser < charA else result + chr(geser)
        else:
            result += i
    return result

while True:
    print('''
PROGRAM SANDI CAESAR
[a] Decrypt File
[b] Baca File
[c] Keluar
''')
    choose = input('Pilih menu diatas: ')
    clear()
    if choose == 'a':
        
        enkripsi = True
        while enkripsi:
            try:
                path = input('Masukan nama file yang akan didecrypt: ')
                file = open(path, 'r')
                while True:
                    try:
                        langkah = int(input('Enkripsi berapa langkah: '))
                        break
                    except ValueError:
                        print('Masukan bilangan bulat')
                save_file = input('Masukan nama file untuk menyimpan hasil decrypt: ')
                save = open(save_file, 'w')
                try:
                    for line in file.readlines():
                        teks = line.rstrip('\n')
                        save.write(decrypt_caesar(teks, langkah) + '\n')
                    time.sleep(0.5)
                    print(f'\nFile {path} berhasil didecrypt')
                    print(f'Periksa hasil decrypt pada file {save_file}')
                    
                except IOError:
                    print(f'Terjadi error saat membuka file {path}')
                finally:
                    file.close()
                    save.close()
            except FileNotFoundError:
                print('File tidak ditemukan')
            conf = input('\nDecrypt file lain ? (y/n): ')
            if conf == 'n':
                input('Klik enter untuk kembali ke menu')
                clear()
                break

    elif choose == 'b':
        baca = True
        while baca:
            try:
                path = input('Masukan nama file yang akan dibaca: ')
                file = open(path, 'r')
                try:
                    print(file.read())
                finally:
                    file.close()
            except FileNotFoundError:
                print('File tidak ditemukan')
            except IOError:
                    print(f'Terjadi error saat membuka file {path}')
            conf = input('Baca file lain ? (y/n): ')
            if conf == 'n':
                input('Klik enter untuk kembali ke menu')
                clear()
                break

    elif choose == 'c':
        exit()
    else:
        print(f'{choose} tidak ada pada menu')