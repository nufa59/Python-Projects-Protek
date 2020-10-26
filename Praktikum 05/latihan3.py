bhs = int(input('Masukkan nilai Bahasa Indonesia [1-100]: '))
ipa = int(input('Masukkan nilai IPA              [1-100]: '))
mtk = int(input('Masukkan nilai Matematika       [1-100]: '))

if (0<=bhs<=100) and (0<=ipa<=100) and (0<=mtk<=100):
    if (bhs >= 60) and (ipa >= 60) and (mtk >= 70):
        print('Status Kelulusan                       : LULUS')
    else:
        print('\nStatus Kelulusan                       : TIDAK LULUS')
        print('Sebab                                  :')
        if (bhs < 60):
            print('- Nilai Bahasa Indonesia kurang dari 60')
        if (ipa < 60):
            print('- Nilai IPA kurang dari 60')
        if (mtk < 70):
            print('- Nilai Matematika kurang dari 70')
else:
    print('\nMaaf input ada yang tidak valid')