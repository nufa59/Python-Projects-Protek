try:
    file = open('d:/data.txt', 'r')
    sum = 0
    for data in file:
        sum = sum + int(data)
    print(sum)
except FileNotFoundError:
    print('File tidak ditemukan')
except ValueError:
    print('Nilai tidak valid')