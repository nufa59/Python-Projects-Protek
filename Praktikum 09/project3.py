def bintang(n):
	if n % 2 == 1:
		n //= 2
		for i in range(n):
			print(('*' * (i * 2 + 1)).center(n*2+1))
		for i in reversed(range(n+1)):
			print(('*' * (i * 2 + 1)).center(n*2+1))
	else:
		print('Nilai n harus ganjil')

while True:
    try: 
        jumlah_bintang = int(input('Masukan nilai n: '))
        if jumlah_bintang % 2 == 1:
            bintang(jumlah_bintang)
            break
        else:
        	print('Nilai n harus ganjil')
    except ValueError:
        print('Yang anda masukan bukan angka')