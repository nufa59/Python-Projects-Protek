def rerata(data):
    val = tuple(data.values())
    return sum(val)/len(val)

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print('Rata-rata harga buah adalah Rp', rerata(buah))