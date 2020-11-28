import os

def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def beli_buah(data):
	data_nama = [x for x in data.keys()]
	print('Daftar Buah')
	for x,y in data.items():
		print(f'• {x.capitalize()} (Harga Rp {y}/Kg)')
	total = 0
	while True:
		while True:
			nama = input('Nama buah yang dibeli      : ').lower()
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
		
		confirm = input('Beli buah yang lain (y/n) ? ')
		if confirm == 'n':
			print('-'*35)
			print('Total harga                :', total)
			input('\nKlik enter untuk kembali: ') 
			clear()
			break
	
def tambah_data(data):
	data_nama = [x for x in data.keys()]
	while True:
		while True:
			nama = input('Masukan nama buah: ').lower()
			if nama in data_nama:
				print(f'Buah {nama} sudah ada pada data buah')
			else:
				break
		while True:
			try:
				harga = int(input('Masukan harga satuan: '));break
			except ValueError:
				print('Masukan angka')
		data[nama] = harga
		print('Data Buah')
		for i,j in data.items():
			print(f'- {i.capitalize()} (Harga Rp {j})')
		confirm = input('Tambah data lain (y/n) ? ')
		if confirm == 'n':
			input('\nKlik enter untuk kembali: ') 
			clear()
			break

def hapus_data(data):
	data_nama = [x for x in data.keys()]
	for i,j in data.items():
		print(f'- {i.capitalize()} (Harga Rp {j})')
	while True:
		while True:
			nama = input('Masukan nama buah: ').lower()
			if nama in data_nama:
				break
			else:
				print(f'Buah {nama} tidak ditemukan')
		del data[nama]
		print('Data Buah')
		for i,j in data.items():
			print(f'- {i.capitalize()} (Harga Rp {j})')
		confirm = input('Hapus data lain (y/n) ? ')
		if confirm == 'n':
			input('\nKlik enter untuk kembali: ') 
			clear()
			break

def menu(data):
	print('''
Menu: 
A. Tambah data buah
B. Beli buah	
C. Hapus data buah
D. Keluar
''')
	pilihan = input('Pilih menu diatas: ').upper()
	if pilihan == 'A':
		clear()
		tambah_data(data)
	elif pilihan == 'B':
		clear()
		beli_buah(data)
	elif pilihan == 'C':
		clear()
		hapus_data(data)
	elif pilihan == 'D':
		exit()
	else:
		print('Pilihan tidak ada dimenu')
		input('Klik enter untuk melanjutkan')
	

		
buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

while True:
	menu(buah)