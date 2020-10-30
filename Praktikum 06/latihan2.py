def starFormation1(n):
    for i in range(n):
        for j in range(i+1):
            print('*', end=' ')
        print(' ')

if __name__ == "__main__":
    starFormation1(5)