def jarak_tempuh(v_mula_mula, percepatan, waktu):
    return (v_mula_mula * waktu) + (percepatan * waktu ** 2) / 2

def jarak_tempuh_mobil():
    print('\nMenghitung Jarak Tempuh Mobil\n')
    while True:
        try:    
            kecepatan_mula_mula = int(input('Masukan kecepatan mula-mula (m/s): '))
            break
        except ValueError:
            print('Yang anda masukan bukan angka! coba lagi')
    while True:
        try:    
            percepatan = int(input('Masukan percepatan (m/s²): '))
            break
        except ValueError:
            print('Yang anda masukan bukan angka! coba lagi')

    print('\nJarak yang sudah ditempuh mobil untuk setiap detiknya (mulai dari t=1 hingga t = 10)\n')
    t = 0
    while True:
        t += 1
        jarakTempuh = jarak_tempuh(kecepatan_mula_mula, percepatan, t)
        print(f'- t = {t}, S(t) = {jarakTempuh}')
        if t == 10:
            break

if __name__ == '__main__':
    while True:
        jarak_tempuh_mobil()
        if input('\nHitung lagi? (y/n): ') == 'n':
            break
