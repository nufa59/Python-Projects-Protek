def cari_termahal(data):
	nilai = max(tuple(data.values()))
	for key, value in data.items():
		if value == nilai:
			return key
	
buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print('Buah yang paling mahal adalah',cari_termahal(buah))