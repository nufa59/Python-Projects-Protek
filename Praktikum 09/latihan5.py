
nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('='*52)
print('NIM'.ljust(11), end='')
print('NAMA'.ljust(11), end='')
print('N.MID'.rjust(6), end='')
print('N.UAS'.rjust(10), end='')
print()
print('-'*52)
for data in nilai:
    print(f"{data['nim']}".ljust(11), end='')
    print(f"{data['nama']}".ljust(11), end='')
    print(f"{data['mid']}".rjust(6), end='')
    print(f"{data['uas']}".rjust(10), end='')
    print()
print('-'*52)