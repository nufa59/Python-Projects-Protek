from datetime import datetime

def diffDate(date):
    sekarang = datetime.now().date()
    tanggal = datetime.strptime(date, '%Y-%m-%d').date()
    return abs(sekarang-tanggal).days

if __name__ == '__main__':
    tanggal = input('Masukan tanggal dengan format YYYY-MM-DD: ')
    selisih = diffDate(tanggal)
    print(f'Selisih hari antara tanggal {tanggal} dengan tanggal {datetime.now().date()} : {selisih} hari')