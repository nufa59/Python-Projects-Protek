def get_total_harga(data):
	data_nama = [x for x in data.keys()]
	print('Daftar Buah')
	for x,y in data.items():
		print(f'• {x.capitalize()} (Harga Rp {y}/Kg)')
	total = 0
	while True:
		while True:
			nama = input('\nNama buah yang dibeli      : ').lower()
			if nama in data_nama and nama != '':
				break
			else:
				print(f'Nama buah {nama} tidak ditemukan, masukan nama lain')
				
		while True:
			try:
				jumlah = int(input('Berapa Kg                  : '))
				if jumlah >= 0:
					total += data[nama] * jumlah
					break
				else:
					print('Masukan nilai yang lebih dari/sama dengan nol')
			except ValueError:
				print('Masukan angka')
		
		confirm = input('\nBeli buah yang lain (y/n) ? ')
		if confirm == 'n': break
	print('-'*35)
	print('Total harga                :', total)

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
get_total_harga(buah)