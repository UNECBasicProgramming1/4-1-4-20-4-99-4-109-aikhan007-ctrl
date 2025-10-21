#4.1
a = float(input())
b = float(input())
if a>b:
    print(a)
else:
    print(b)




#4.2
import math
x = float(input())
if x > 0:
    y = math.sin(x**2)
else:
    y = 1 - 2 * math.sin(x**2)
print(y)



#4.3
import math
x = float(input())
if x > 0:
    y = math.sin(x**2)
else:
    y = 1 + 2 * math.sin(x**2)
print(y)




#4.4
x = float(input())
y = float(input())
if x>4:
    print('попадает в 2 область')
else:
    print('попадает в 1 область')



#4.5
x = float(input())
y = float(input())
if y<3:
    print('попадает в 2 область')
else:
    print('попадает в 1 область')






#4.7
x = float(input())
def    f(x):
    if k(x) < x:
        return k * x
    else:
        return k + x
    
def    k():
    if math.sin(x) < 0:
        return x**2
    else:
        return abs(x)
print(f(x))



#4.9
a = float(input())
b = float(input())
if a>b:
    print('a = max')
    print('b = min')
else:
    print('b = max')
    print('a = min')



    #4.10
    m = float(input())
    f = float(input())
    futa = f * 0.3048
    if m > futa:
        print(f'{m} метров больше чем {f} фут')
    else:
        print(f'{f} фут больше чем {m} метров')


#4.11
kmh = float(input())
ms = float(input())
kmhinms = (kmh * 10)/36
if kmhinms > ms:
    print(f'{kmh} километров в час больше чем{ms} метров в секунду')
else:
    print(f'{ms} метров в секунду больше чем {kmh} километров в час')



#4.12
import math
r = float(input())
a = float(input())
if math.pi *r**2 > a**2:
    print('площадь круга больше тплощади квадрата')
else:
    print(' площадь квадрата больше площади круга')



#4.14
u1 = float(input())
u2 = float(input())
r1 = float(input())
r2 = float(input())
if u1 / r1 > u2 / r2:
    print('на первом участке протекает больший ток')
else:
    print('на втором участке протекает больший ток')



#4.15
a = float(input())
b = float(input())
c = float(input())
D = b**2 - 4 * a * c
if D > 0:
    print('уравнение имеет два корня')
elif D == 0:
    print('уравнение имеет один корень')
else:
    print(' уравнение не имеет корней')



#4.16
a = float(input())
b = float(input())
c = float(input())
D = b**2 - 4 * a * c
if D >= 0:
    x1 = (-b + D**0.5)/ (2 * a)
    x2 = (-b - D**0.5)/ (2 * a)
    if type(x1) == float or type(x2) == float:
        print(' корни вещественные')
    else:
        print('корни целочисленные')
else:
    print(' уравнение не имеет корней')



#4.18a #4.18b
r = float(input())
a = float(input())
if a * 2**0.5 > 2 *r:
    print('квадрат не поместится в круг')
else:
    print('квадрат поместится в круг')
if 2 * r > 2 * a:
    print('круг не поместится в квадрат')
else:
    print('круг поместится в квадрат')



#4.99a
a = float(input())
b = float(input())
if a>b:
    print(a)
else:
    print(b)


#4.99b
a = float(input())
b = float(input())
if a > b:
    print('a больше b')




#4.100a
a = float(input())
b = float(input())

if a > b:
    print("наибольшее =", a)
    print("наименьшее =", b)
if b > a:
    print("наибольшее =", b)
    print("наименьшее =", a)



#4.100b
a = float(input())
b = float(input())
maxnum = b
minnum = a
if a > b:
    max_num = a
    min_num = b

print("наибольшее =", max_num)
print("наименьшее =", min_num)




#4.102a
a = float(input())
b = float(input())
c = float(input())
d = float(input())
if a > b and a > c and a > d:
    print(a)
if b > a and b > c and b > d:
    print(b)
if c > b and c > a and c > d:
    print(c)
if d > b and d > c and d > a:
    print(d)


#4.102b
a = float(input())
b = float(input())
c = float(input())
d = float(input())
if a < b and a < c and a < d:
    print(a)
if b < a and b < c and b < d:
    print(b)
if c < b and c < a and c < d:
    print(c)
if d < b and d < c and d < a:
    print(d)



#4.103
a = float(input())
if a < 0:
    print(-a)
else:
    print(a)



#4.104a
a = float(input())
b = float(input())
if a > 0 and b > 0:
    print((a+b)/2)
if a < 0 and b > 0:
    print((-a + b)/2)
if a > 0 and b < 0:
    print((a + (-b)/2))
if a < 0 and b < 0:
    print(((-a) + (-b))/2)




#4.104b
a = float(input())
b = float(input())
if a > 0 and b > 0:
    print((a * b)**0.5)
if a < 0 and b > 0:
    print(((-a) * b)**0.5)
if a > 0 and b < 0:
    print((a * (-b))**0.5)
if a < 0 and b < 0:
    print((-a * (-b))**0.5)



#4.105
a = float(input())
b = float(input())
if abs(a) > abs(b):
    a = a/2





#4.106
a=int(input())
b=int(input())
if b**0.5<a:print(b*5)




#4.107
a=int(input())
b=int(input())
c=int(input())
if a%2==0:print(a)
if b%2==0:print(b)
if c%2==0:print(c)




#4.108
a=float(input())
b=float(input())
c=float(input())
if a%2==0:print(a*a)
if b%2==0:print(b*b)
if c%2==0:print(c*c)





#4.109
a=float(input())
b=float(input())
c=float(input())
if 1.6<=a<=3.8:print(a)
if 1.6<=b<=3.8:print(b)
if 1.6<=c<=3.8:print(c)