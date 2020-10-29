def starFormation1(n):
    for i in range(n):
        for j in range(i+1):
            print(i, end=' ')
        print(' ')

starFormation1(5)