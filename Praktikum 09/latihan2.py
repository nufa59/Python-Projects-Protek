def bintang(n):
	for i in range(n):
		print(('*' * (i * 2 + 1)).center(n*2))

while True:
    try: 
        jumlah_bintang = int(input('Masukan nilai n: '))
        bintang(jumlah_bintang)
        break
    except ValueError:
        print('Yang anda masukan bukan angka')