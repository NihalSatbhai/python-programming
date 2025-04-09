def patterns(n):
    for i in range(n-1):
        for j in range (i,n):
            print(' ', end=' ')
        for j in range (i+1):
            print('*', end=' ')
        for j in range (i):
            print('*', end=' ')
        print()
    for i in range(n):
        for j in range (i+1):
            print(' ', end=' ')
        for j in range (i,n):
            print('*', end=' ')
        for j in range (i,n-1):
            print('*', end=' ')
        print()
patterns(5)


def patterns(n):
    for i in range(n-1):
        for j in range(i,n):
            print(' ', end=' ')
        for j in range(i+1):
            print('*', end=' ')
        for j in range(i):
            print('*', end=' ')
        print()
    for i in range(n):
        for j in range(i+1):
            print(' ', end=' ')
        for j in range(i,n):
            print('*', end=' ')
        for j in range(i,n-1):
            print('*', end=' ')
        print()
patterns(5)


def patterns(n):
    for i in range(n):
        for j in range(i,n):
            print(' ',end=' ')
        for j in range(i+1):
            print('*',end=' ')
        print()
patterns(5)


def pattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ',end=' ')
        for j in range(i+1):
            print('*',end=' ')
        for j in range(i):
            print('*',end=' ')
        print()
    for i in range(n-1):
        for j in range(i+1):
            print(' ',end=' ')
        for j in range(n-1-i):
            print('*',end=' ')
        for j in range(n-2-i):
            print('*',end=' ')
        print()
pattern(5)