import math
import random
import time

def Pk(k) :
	return ((k - int(k / (2**c))* 2**c) * d / 2**c, int(k / (2**c)) * d / 2**c)

def functionF(i,j,p) :
	(x, y) = p
	# print(i,j,x,y)
	(a, b) = w(i,x,y,d)
	(a, b) = ((1 / 2**c) * a, (1 / 2**c) * b)
	(a1, b1) = Pk(j)
	(a, b) = (a + a1, b + b1)
	return int(a),int(b)


def functionFInv(i,j,p) :
	(x, y) = p
	(a1, b1) = Pk(j)
	(a, b) = ((2**c * x) - (2**c * a1), (2**c * y) - (2**c * b1))
	if i == 3 :
		i = 1
	elif i == 1 :
		i = 3
	(a, b) = w(i,a,b,d)
	return int(a),int(b)

def w(i,x,y,d):
	if i == 0:
	 	return (x, y)
	elif i == 1:
		return (d - y, x)
	elif i == 2:
		return (d - x, d - y)
	elif i == 3:
		return (y, d - x)
	elif i == 4:
		return (d - y, d - x)
	elif i == 5:
		return (x, d - y)
	elif i == 6:
		return (y, x)
	elif i == 7:
		return (d - x, y)
	
ss = '110110'
c = 3
m = 3
l = 4**c

readBitsNum = int(math.sqrt(l))
s = int(len(ss) / readBitsNum)
# print("s =",s)

d = m * 2**(c * s)

ssReversed = ss[::-1]

start1 = time.time()
arr = [ssReversed[i:i+readBitsNum] for i in range(0, len(ssReversed), readBitsNum)]

for index in range(0,len(arr)) :
	arr[index] = arr[index][::-1]


t = random.sample(range(0, 8), l)
o = random.sample(range(0, 4), l)
# t = [0,3,4,7]
# o = [1,0,2,3]

# print(t)
# print(o)

Lambda = (t, o)

E = []

for index in range(1, m) :
	for index2 in range(1, m) :
		a = index * 2**(c*s)
		b = index2 * 2**(c*s)
		E.append((a, b))

# (x, y) = E[random.randint(0,len(E)-1)]
(x, y) = (8, 8)

# print(x,y)

# GET NUMBER FROM BINARY STRING ARRAY
#
# num = 0
#
# for index in range(0, len(arr)) :
# 	num = num + int(arr[index],2) * l**index
# 	print(arr[index])


X = (x, y)

for index in range(0, len(arr)) :
	i = t[int(arr[index],2)]
	j = o[int(arr[index],2)]
	X = functionF(i,j,X)
print(X)

(x,y) = X
k1 = x // m
# print("k1 =", k1)
k2 = y // m
# print("k2 =", k2)

k = k2 * 2**(c*s) + k1

print("k =", k)
print("---------------------------------------------------")
# print("old:",ss)

# num = 0
# for index in range(0, len(arr)) :
# 	num = num + int(arr[index],2) * l**index

# print("old:",num)
# print("new:",k)
# print("new:", bin(k)[2:])

end1 = time.time()

print("time1:",end1 - start1)
#
# F INVERSE
#

start2 = time.time()
oInv = []

for index in range(0, len(o)) :
	oInv.append(0)

for index in range(0, len(o)) :
	oInv[o[index]] = index


ss = s
pp = ''

X = (x, y)
for index in range(0,ss) :
	kk = int(y * 2**c / d) * 2**c + int(x * 2**c / d)
	# print("kk:",kk)

	pp = pp + str(bin(oInv[kk])[2:].zfill(readBitsNum))
	nn = oInv[kk]

	i = t[nn]
	j = o[nn]
	
	X = functionFInv(i,j,X)
	(x, y) = X
	# print(x,y)
	# print(pp)
print(pp)

end2 = time.time()

print("time2:",end2 - start2)