import math

degree = int(input('Write degree to convert to radians:'))    #1
print('radians:', round(math.radians(degree), 6))

trap = input('Write high, upper base and lower base to get trapezoidal area:').split()    #2  
print('area:', (int(trap[1]) + int(trap[2])) * int(trap[0]) / 2)

pol = input('Write num of sides and len of side to get the area of polygon:').split()    #3
print('area:', round((int(pol[0]) * int(pol[1])**2) / (4 * math.tan(math.pi / int(pol[0])))))

par = input('Write len and height to get the ares of parallelogram:').split()    #4
print('area:', float(par[0]) * float(par[1]))