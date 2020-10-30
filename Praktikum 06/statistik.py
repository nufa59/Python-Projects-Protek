def sum(*data):
    value = 0
    for i in data:
        value += i
    return value

def average(*data):
    return sum(*data)/len(data)

def min(*data):
    value = data[0]
    for i in data:
        if i < value:
            value = i
    return value

def max(*data):
    value = data[0]
    for i in data:
        if i > value:
            value = i
    return value

