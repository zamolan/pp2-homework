def squares1(n):     #1
    for i in range(1, n + 1):
        yield i * i

def evens(n):     #2
    for i in range(0, n + 1, 2):
        yield i

def d34(n):     #3
    for i in range(1, n + 1):
        if (i % 3 and i % 4):
            yield i

def squares(a, b):     #4
    for i in range(a, b + 1):
        yield i * i

def less(n):
    for i in range(n, -1, -1):
        yield i

N = int(input('Write num to get list of squares till it:'))
for i in squares1(N):
    print(i)

N = int(input('Write num to get list of evens till it:'))
ev_n = []
for i in evens(N):
    ev_n.append(i)
print(*ev_n, sep=',')

N = int(input('Write num to get nums divisible be 3 amd 4 till it:'))
for i in d34(N):
    print(i)

n = input('Write a and b to get squares between it:')
for i in squares(int(n[0]), int(n[1])):
    print(i)

N = int(input('Write num to get nums from it to 0'))
for i in less(N):
    print(i)
    