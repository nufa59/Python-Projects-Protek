jam_berangkat = int(input('Masukan jam keberangkatan : '))
menit_berangkat = int(input('Masukan menit keberangkatan : '))
jarak1 = 125
jarak2 = 256
kecepatan1 = 62
kecepatan2 = 70
istirahat = 45

waktu1 = jarak1/kecepatan1
waktu2 = jarak2/kecepatan2

waktu_menit = ((waktu1+waktu2) * 60) + istirahat + menit_berangkat
jam = int(waktu_menit // 60) + jam_berangkat
menit = int(waktu_menit % 60)

print('\nWaktu berangkat pukul {:02}.{:02}'.format(jam_berangkat, menit_berangkat))
print('Pak Amir akan sampai di kota C pada pukul {:02}.{:02}'.format(jam, menit))
