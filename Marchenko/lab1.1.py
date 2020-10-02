print('Marchenko')
a = 945 / 26 / -22
print(a)
print(type(a))

b = 45678 // -4569 // 3
print(b)
print(type(b))

c = -465839 % 236 % 56
print(c)
print(type(c))

d = 5 ** 3.6 ** 2
print(d)
print(type(d))

print(0b10000111)
print(0o11000001)
print(0x0AAAA111)

print(bin(14999))
print(oct(25082003))
print(hex(201126))

import math
import cmath
x = -10
if -11 <= x <= -9:
   a = math.cos(2 / 54) + 13 * math.pi - 64 * math.e * 14 / (x + 12) / (x - 11) + 9 * math.acos(x + 10) - cmath.log(x - 15, 7)
elif x > 15:
   a = math.cos(2 / 54) + 13 * math.pi - 64 * math.e * 14 / (x + 12) / (x - 11) + 9 * cmath.acos(x + 10) - math.log(x - 15, 7)
else:
   a = math.cos(2 / 54) + 13 * math.pi - 64 * math.e * 14 / (x + 12) / (x - 11) + 9 * cmath.acos(x + 10) - cmath.log(x - 15, 7)
print(a)
