from math import ceil,floor

# karatsuba algorithm with recursive calls reduction
def karatsuba(x,y):
    if x<10 and y<10:
        return x*y
    n = max(len(str(x)), len(str(y)))
    m = int(ceil(float(n)/2))
    x_H = int(floor(x/10**m))
    x_L = int(x % (10**m))
    y_H = int(floor(y/ 10**m))
    y_L = int(y % (10**m))
    a = karatsuba(x_H,y_H)
    d = karatsuba(x_L,y_L)
    e = karatsuba(x_H + x_L,y_H + y_L) -a -d
    return int(a*(10**(m*2))+e*(10**m)+d)

# No recursive calls reduction

def recursive_mult(x,y):
    # // return integer
    n = len(str(x))//2
    if n ==0:
        return(x*y)
    # if n below a benmark threshold, terminate the recursion
    a, c = x//(10**n), y//(10**n)
    b, d = x - a*(10**n), y - c*(10**n)
    return((10**(2*n))*recursive_mult(a,c)+(10**n)*(recursive_mult(a,d)+recursive_mult(b,c))+recursive_mult(b,d))

import time
x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

start_time1 = time.time()
for i in range(1000):
    karatsuba(x,y)
duration1 = time.time() - start_time1

start_time2 = time.time()
for i in range(1000):
    recursive_mult(x,y)
duration2 = time.time() - start_time2

print("karatsuba",duration1)
print("recursive_mult",duration2)
