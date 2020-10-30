def isPythagoras(a, b, c):
    return c**2 == a**2 + b**2

print(f'a = 3, b = 4, c = 5   -> {isPythagoras(3, 4, 5)}')
print(f'a = 5, b = 9, c = 12  -> {isPythagoras(5, 9, 12)}')
print(f'a = 8, b = 6, c = 10  -> {isPythagoras(8, 6, 10)}')
print(f'a = 7, b = 8, c = 11  -> {isPythagoras(7, 8, 11)}')