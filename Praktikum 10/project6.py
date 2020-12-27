import os, time

def clear():
    os.system('cls') if os.name == 'nt' else os.system('clear')

def sandi_caesar(teks='', n=0):
    result = ''
    for i in teks:
        charZ = ord('Z') if i.isupper() else ord('z')
        if i != ' ':
            geser = ord(i) + n
            result = result + chr(geser - 26) if geser > charZ else result + chr(geser)
        else:
            result += i
    return result
while True:
    print('''
PROGRAM SANDI CAESAR
[a] Enkripsi File
[b] Buat Teks
[c] Baca File
[d] Keluar
''')
    choose = input('Pilih menu diatas: ')
    clear()
    if choose == 'a':
        
        enkripsi = True
        while enkripsi:
            try:
                path = input('Masukan nama file yang akan dienkripsi: ')
                file = open(path, 'r')
                while True:
                    try:
                        langkah = int(input('Enkripsi berapa langkah: '))
                        break
                    except ValueError:
                        print('Masukan bilangan bulat')
                save_file = input('Masukan nama file untuk menyimpan hasil enkripsi: ')
                save = open(save_file, 'w')
                try:
                    for line in file.readlines():
                        teks = line.rstrip('\n')
                        save.write(sandi_caesar(teks, langkah) + '\n')
                    time.sleep(0.5)
                    print(f'\nFile {path} berhasil di enkripsi')
                    print(f'Periksa hasil enkripsi pada file {save_file}')
                    
                except IOError:
                    print(f'Terjadi error saat membuka file {path}')
                finally:
                    file.close()
                    save.close()
            except FileNotFoundError:
                print('File tidak ditemukan')
            conf = input('\nEnkripsi file lain ? (y/n): ')
            if conf == 'n':
                input('Klik enter untuk kembali ke menu')
                clear()
                break

    elif choose == 'b':
        path = input('Masukan nama file: ')
        try:
            file = open(path, 'a')
            try:
                lagi = ' '
                while lagi != 'n':
                    input_teks = input('Masukan teks: ')
                    file.write(input_teks + '\n')
                    lagi = input('\nLagi (y/n): ').lower()
            finally:
                file.close()
        except IOError:
            print(f'Terjadi error saat membuka file {path}')
        input('Klik enter untuk kembali ke menu')
        clear()
    elif choose == 'c':
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
            conf = input('Baca file lain ? (y/n): ')
            if conf == 'n':
                input('Klik enter untuk kembali ke menu')
                clear()
                break

    elif choose == 'd':
        exit()
    else:
        print(f'{choose} tidak ada pada menu')