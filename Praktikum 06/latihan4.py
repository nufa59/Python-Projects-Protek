def starFormation1(n):        
    for i in range(n):
        for j in range(i + 1):
            print('*', end=' ')
        print(' ')

def starFormation2(n):        
    for i in range(n, 0, -1):
        for j in range(i):
            print('*', end=' ')
        print(' ')

def starFormation3(n):
    if n % 2 == 1:
        starFormation1(n//2+1)
    else:
        starFormation1(n//2)
    starFormation2(n//2)

starFormation3(6)