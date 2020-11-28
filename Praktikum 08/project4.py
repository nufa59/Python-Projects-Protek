import os, time

def clear():
    if os.name == 'nt': os.system('cls') 
    else: os.system('clear')

def tampilkan_data():
    print('\n Data Sayur: ')
    for x,y in enumerate(sayur): 
        print(f'[{x+1}] {y}')
    input('\nKlik enter untuk kembali ')
    clear()

def show_data():
    print('\n Data Sayur: ')
    for x,y in enumerate(sayur): 
        print(f'[{x+1}] {y.capitalize()}')

def tambah_data():
    show_data()
    while True:
        nama_sayur = input('\nMasukan nama sayur: ').lower()
        if nama_sayur in sayur:
            print(f'Sayur {nama_sayur} sudah ada')
            continue
        sayur.append(nama_sayur)
        print(f'Sayur {nama_sayur} berhasil ditambahkan')
        confirm = input('\nTambah data lain (y/n): ')
        if confirm == 'n': clear(); break

def hapus_data():
    show_data()
    while True:
        try:
            nama = input('\nMasukan nama sayur yang akan dihapus: ').lower()
            sayur.remove(nama)
            print(f'Sayur {nama} berhasil dihapus')
            confirm = input('\nHapus data lain (y/n): ')
            if confirm == 'n': clear(); break
        except ValueError: print('Data tidak ditemukan')

def menu():
    print('''
Menu: 
A. Tambah Data Sayur
B. Hapus Data Sayur
C. Tampilkan Data Sayur
E. Keluar
    ''')
    pilih = input('Pilihan Anda: ').upper()
    if pilih == 'A':
        clear()
        tambah_data()
    elif pilih == 'B':
        clear()
        hapus_data()
    elif pilih == 'C':
        clear()
        tampilkan_data()
    elif pilih == 'E':
        exit()
    else:
        print('Pilihan tidak ada dalam menu')
        time.sleep(1)

sayur = ['bayam', 'kangkung', 'wortel', 'selada']

while True:
    clear()
    menu()