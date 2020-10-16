tarif1 = 200000
tarif2 = 10000
jamMulai = 6
menitMulai = 0
jamSelesai = 23
menitSelesai = 50
lamaSewa = (jamSelesai - jamMulai) + (menitSelesai - menitMulai)//60
sewaTarif2 = (lamaSewa-12)*tarif2
totalTarif = tarif1 + sewaTarif2
print('Biaya sewa mobil dari jam 06.00 - 23.50 adalah Rp{}'.format(totalTarif))