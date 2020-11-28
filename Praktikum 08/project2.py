def dataStat(x):
    a = sum(tuple(x))/len(x)
    b = max(tuple(x))
    c = min(tuple(x))
    return [a, b, c]

data = [2, 6, 1, 23, 56, 8, 152, 89]
data_stat = dataStat(data)
print(data)
print('Rata-rata        :', data_stat[0])
print('Nilai tertinggi  :', data_stat[1])
print('Nilai terendah   :', data_stat[2])