i = 0
count = 0
jumlah = 0
while i <= 100:
    if i % 2 == 1:
        count += 1
        jumlah += i
        print(i)
    i += 1
print('Banyak bilangan ganjil :', count)
print('Jumlah seluruh bilangan :', jumlah)