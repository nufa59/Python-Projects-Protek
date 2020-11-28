def nilai_tertinggi(data):
    nilai = [(i['mid'] + (2 * i['uas']))/3 for i in data]
    nilai_max = max(nilai)
    index_max = nilai.index(nilai_max)
    nim = data[index_max]['nim']
    nama = data[index_max]['nama']
    return {'nim': nim, 'nama': nama}


nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},       
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, 
            {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

nilai_akhir = nilai_tertinggi(nilaiMhs)
print(f"Mahasiswa yang memperoleh nilai akhir tertinggi adalah saudara {nilai_akhir['nama']} NIM {nilai_akhir['nim']}")
