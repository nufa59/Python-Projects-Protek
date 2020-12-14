def ubahHuruf(teks, a, b):
	char = list(teks)
	if a in char:
		proses = [x if x != a else b for x in char]
		result = ''.join(proses)
		return result
	else:
		return f'Huruf {a} tidak ada dalam teks {teks}'

print(ubahHuruf('MATEMATIKA', 'T', 'S'))