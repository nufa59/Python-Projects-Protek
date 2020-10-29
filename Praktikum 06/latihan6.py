import statistik as s

# a. 5, 10, 4, 9, 30, 16, 2, 11
num1 = (5, 10, 4, 9, 30, 16, 2, 11)
print(f'Data         : {num1}')
print('Rata-rata    :', s.average(*num1))
print('Nilai max    :', s.max(*num1))
print('Nilai min    :', s.min(*num1))

# b. 81, 98, 12, 83, 45, 77, 69, 30, 56
num2 = (81, 98, 12, 83, 45, 77, 69, 30, 56)
print(f'\nData         : {num2}')
print('Rata-rata    :', s.average(*num2))
print('Nilai max    :', s.max(*num2))
print('Nilai min    :', s.min(*num2))
