import time

def bmi(berat, tinggi):
    return berat/(tinggi/100)**2

def status(berat, tinggi):
    value = bmi(berat, tinggi)
    if value < 18:
        return 'KURUS'
    elif 18 <= value < 23:
        return 'IDEAL'
    elif 23 <= value < 27:
        return 'GEMUK'
    elif 27 <= value < 35:
        return 'OBESITAS'
    elif value >= 35:
        return 'OBESITAS MORBID'

def cek_status_bmi():
    print('\n')
    while True:
        while True:
            try:    
                tinggi = int(input('Masukan tinggi badan (cm): '))
                break
            except ValueError:
                print('Yang anda masukan bukan angka! coba lagi')
        while True:
            try:    
                berat = int(input('Masukan berat badan (kg): '))
                break
            except ValueError:
                print('Yang anda masukan bukan angka! coba lagi')
        if berat > 0 and tinggi > 0:
            result = status(berat, tinggi)
            print(f'Status berat badan : {result}')  
            break
        else:
            print('Masukan nilai yang lebih besar dari nol')
    
def menu():
    print('\nBody Mass Index (BMI)')
    print('''
[1] Cek Status Berat Badan
[2] Keluar   
    ''')
    while True:
        try:    
            pilihan = int(input('Pilih menu diatas: '))
            break
        except ValueError:
            print('Yang anda masukan bukan angka! coba lagi')
    
    if pilihan == 1:
        cek_status_bmi()
        time.sleep(1)
    elif pilihan == 2:
        exit()
    else:
        print('Menu tidak tersedia!')

if __name__ == '__main__':
    while True:
        menu()