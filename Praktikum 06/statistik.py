def sum(*data):
    hasil = 0
    for i in data:
        hasil += i
    return hasil

def average(*data):
    return sum(*data)/len(data)

def min(*data):
    value = 999999999
    for i in data:
        if i < value:
            value = i
    return value

def max(*data):
    value = data[0]
    for i in data:
        if value < i:
            value = i
    return value

