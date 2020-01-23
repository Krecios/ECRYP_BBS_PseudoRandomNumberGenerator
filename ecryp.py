import sympy
import random

p = sympy.randprime(40000, 50000)

while p % 4 != 3:
    p = sympy.nextprime(p)              #generating the first prime number

q = sympy.randprime(40000, 50000)

while q % 4 != 3 and q != p:
    q = sympy.nextprime(q)              #generating the second prime number

M = p * q                               #calculating the M parameter

s = random.randrange(M)                 #generating random seed smaller then M
print('p: ' + str(p) + ' q: ' + str(q) + ' M: ' + str(M) + ' S: ' + str(s))
tab = []
outtab = []
outdec = 0
seqdec = []
size = 320
x0 = (s * s) % M

count = 0
while(count != size):                   #generating given quantity of numbers via the BBS algorithm
    x = (x0 * x0) % M
    tab.append(x0 & 1)                  #extracting the least significant bit form the generated number
    x0 = x
    count = count + 1

count = 1
power = 32
for i in tab:
    count = count + 1
    power = power - 1                   #spliting the sequence of bits into 32bit decimal numbers
    outdec = outdec + (i * (2 ** power))
    if count % 32 == 0:
        power = 32
        seqdec.append(outdec)
        outdec = 0
        outbin = 0

for i in seqdec:
    print(i)

