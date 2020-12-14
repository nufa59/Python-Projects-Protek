nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

kolom = {'nim': 11, 'nama': 11, 'mid': 6, 'uas': 10, 'akhir': 11, 'status': 12}
print('='*62)
print('NIM'.ljust(kolom['nim']), end='')
print('NAMA'.ljust(kolom['nama']), end='')
print('N.MID'.rjust(kolom['mid']), end='')
print('N.UAS'.rjust(kolom['uas']), end='')
print('N.AKHIR'.rjust(kolom['akhir']), end='')
print('STATUS'.rjust(kolom['status']), end='')
print()
print('-'*62)
for data in nilai:
    nilai_akhir = (data['mid'] + (2 * data['uas']))/3
    if nilai_akhir >= 60:
        status = 'LULUS'
    else:
        status = 'TIDAK LULUS'
    print(f"{data['nim']}".ljust(kolom['nim']), end='')
    print(f"{data['nama']}".ljust(kolom['nama']), end='')
    print(f"{data['mid']}".rjust(kolom['mid']), end='')
    print(f"{data['uas']}".rjust(kolom['uas']), end='')
    print(f"{nilai_akhir:.2f}".rjust(kolom['akhir']), end='')
    print(f"{status}".rjust(kolom['status']), end='')
    print()
print('-'*62)