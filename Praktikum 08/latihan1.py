print('nomor 1')
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
print(a)
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
print(b)
print('\nnomor 2')
a.insert(3, 10)
print(a)
b.insert(2, 15)
print(b)
print('\nnomor 3')
a.append(4)
print(a)
b.append(8)
print(b)

print('\nnomor 4')
a.sort()
print(a)
b.sort()
print(b)

print('\nnomor 5')
c = a[:8]
print(c)
d = b[2:10]
print(d)

print('\nnomor 6')
e = []
for i in range(len(c)):
    e.append(c[i] + d[i])
print(e)

print('\nnomor 7')
e = tuple(e)
print(e)

print('\nnomor 8')
print('max list e:', max(e))
print('min list e:', min(e))
print('sum list e:', sum(e))

print('\nnomor 9')
myString = 'python adalah bahasa pemrograman yang menyenangkan'
print('myString:', myString)

print('\nnomor 10')
char = set(myString)
print('Karakter penyusun myString:', char)

print('\nnomor 11')
char = list(char)
char.sort()
print('Setelah di sort: ', char)

