def sortStringByChar(data):
    data = sorted(data, key=len, reverse=True)
    return data
    
myData = ['apel', 'rambutan', 'jeruk ']
print('Hasil sorting', sortStringByChar(myData))