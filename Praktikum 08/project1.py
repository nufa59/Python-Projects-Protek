while True:
    try : jml = int(input('Jumlah data yang akan diinput: ')); break
    except ValueError: print('Masukan angka')
data = []
for _ in range(jml):
    while True:
        try :
            datum = int(input('Masukan bilangan bulat: '))
            data.append(datum)
            break
        except ValueError: print('Bukan bilangan bulat')
data.sort(reverse=True)
print('\nData dari urutan terbesar sampai terkecil', data)