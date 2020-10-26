bhs = int(input('Masukkan nilai Bahasa Indonesia [1-100]: '))
ipa = int(input('Masukkan nilai IPA              [1-100]: '))
mtk = int(input('Masukkan nilai Matematika       [1-100]: '))

if (bhs >= 60) and (ipa >= 60) and (mtk >= 70):
    print('Status Kelulusan                       : LULUS')
else:
    print('Status Kelulusan                       : TIDAK LULUS')
