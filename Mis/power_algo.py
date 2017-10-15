import time
import math

def power_recur(x,n):
    if n==0:
        return 1
    if n%2==0:
        return power_recur(x,n//2)*power_recur(x,n//2)
    else:
        return x*(power_recur(x,n//2)*power_recur(x,n//2))

recur_start_time = time.time()
x = power_recur(2,100000)
recur_end_time = time.time() - recur_start_time
print("--- %s seconds ---" % recur_end_time,"::Ans: ",x)
