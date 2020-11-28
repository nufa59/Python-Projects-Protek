print('='*30)
print('PROGRAM HITUNG RATA-RATA'.center(30))
print('='*30)

data = 0; count = 0
while True:
    try:
        value = int(input('Masukan bilangan bulat: '))
        data += value; count += 1
        confirm = input('Lagi (y/n)? : ')
        if confirm == 'n': break
    except ValueError: 
        print('Buakan bilangan bulat')
        
try: 
    print('\nRata-ratanya adalah:', data/count)
except: 
    print('Tidak ada data')