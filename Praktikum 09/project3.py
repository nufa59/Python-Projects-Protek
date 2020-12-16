def bintang(n):
	n //= 2
	for i in range(n):
		print(('*' * (i * 2 + 1)).center(n*2+1))
	for i in reversed(range(n+1)):
		print(('*' * (i * 2 + 1)).center(n*2+1))

while True:
    try: 
        tinggi = int(input('Masukan nilai n: '))
        if tinggi % 2 == 1 and tinggi > 0:
            bintang(tinggi)
            break
        else:
        	print('Nilai n harus ganjil dan lebih dari nol')
    except ValueError:
        print('Yang anda masukan bukan angka')