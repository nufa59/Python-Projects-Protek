from operation import *

# 2 + 4 * 6 – 4
print('Hasil dari 2 + 4 * 6 – 4 adalah', kurang(jumlah(2, kali(4, 6)), 4))
# (4 + 7) * (6 - 9)
print('Hasil dari (4 + 7) * (6 - 9) adalah', kali(jumlah(4, 7), kurang(6, 9)))
# (10 + 2) / (7 + 5) / (12 - 34) 
print('Hasil dari (10 + 2) / (7 + 5) / (12 - 34) ', bagi(bagi(jumlah(10, 2), jumlah(7, 5)), kurang(12, 34)))
