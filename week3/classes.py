from math import sqrt

class first:    #1
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input('Write string: ')

    def printString(self):
        print(self.text.upper())

class Shape:    #2
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, lenght):
        self.lenght = lenght
    def area(self):
        return self.lenght * self.lenght
class Rectangle(Shape):     #3
    def __init__(self, lenght, widht):
        self.lenght = lenght
        self.width = widht
    def area(self):
        return self.lenght * self.width

class Point:    #4
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print('point = (', self.x, ';', self.y, ')')
    def move(self):
        self.x = int(input('Write new x: '))
        self.y = int(input('Write new y: '))
    def dist(self, p2):
        return sqrt((p2.x - self.x)**2 + (p2.y - self.y)**2)
    
class Account:      #5
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, value):
        self.balance += value
        print('Your balance: ', self.balance)
    def withdraw(self, value):
        if(value > self.balance):
            print('Error')
        else:
            self.balance -= value
        print('Your balance: ', self.balance)

def is_prime(x):    #6
    cnt = 0
    for i in range(1, x + 1):
        if x % i == 0:
            cnt += 1
    return cnt == 2 and x > 1

def filter_prime(nums):
    pr_nums = filter(lambda x: is_prime(int(x)), nums)
    return list(pr_nums)

    
example1 = first()
example1.getString()
example1.printString()

example2 = Square(int(input('Write lenght: ')))
print('Square area = ', example2.area())

value3 = input('Write lenght and width: ').split()
example3 = Rectangle(int(value3[0]), int(value3[1]))
print('Rectangle area = ', example3.area())

point1 = input('Write x and y for point 1: ').split()
point2 = input('Write x and y for point 2: ').split()
ex_p1 = Point(int(point1[0]), int(point1[1]))
ex_p2 = Point(int(point2[0]), int(point2[1]))
ex_p1.show()
ex_p1.move()
ex_p1.show()
print('Distence from p1 to p2 = ', ex_p1.dist(ex_p2))

value5 = input('Write name and balance: ').split()
example5 = Account(value5[0], int(value5[1]))
example5.deposit(int(input('write value to deposit: ')))
example5.withdraw(int(input('Write value to withdraw: ')))
example5.withdraw(int(input('Write value to withdraw: ')))

example6 = input('Write list of numbers: ').split()
print(*(filter_prime(example6)))
