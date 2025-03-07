import math
import time

a = (1, 2, 3, 4, 5)
x = math.prod(a)
print(x)

s = "UPPERlower"
up = list(filter(str.isupper, s))
low = list(filter(str.islower, s))
print(len(up), len(low))

p1 = 'madam'
p2 = 'madap'
p1r = ''.join(reversed(p1))
p2r = ''.join(reversed(p2))
if(p1 == p1r):
    print(p1, 'polindrom')
else:
    print(p1, 'not polindrom')
if(p2 == p2r):
    print(p2, 'polindrom')
else:
    print(p2, 'not polindrom')

n = 25100
t = 2123
start_time = time.time()
while (time.time() - start_time) < (t / 1000):  
    pass
print(math.sqrt(n))

mylist = [True, True, True]
x = all(mylist)
print(x)
mytuple = (0, True, False)
x = all(mytuple)
print(x)