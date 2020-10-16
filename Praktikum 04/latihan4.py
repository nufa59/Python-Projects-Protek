from math import floor

jamBerangkat = int(input('Masukan jam keberangkatan : '))
menitBerangkat = int(input('Masukan menit keberangkatan : '))
jarak1 = 125
jarak2 = 256
kecepatan1 = 62
kecepatan2 = 70
istirahat = 45

waktu1 = jarak1/kecepatan1
waktu2 = jarak2/kecepatan2

jmlWaktu = waktu1+waktu2
jam = floor(jmlWaktu)
menit = int(float('{:.2f}'.format(jmlWaktu-jam))*100)
menit += istirahat + menitBerangkat
jamSampai = jamBerangkat + jam + (menit//60)
menitSampai = menit%60
print('\nJam berangkat {:02}.{:02}'.format(jamBerangkat, menitBerangkat))
print('Pak Amir akan sampai di kota C pada pukul {:02}.{:02}'.format(jamSampai, menitSampai))
