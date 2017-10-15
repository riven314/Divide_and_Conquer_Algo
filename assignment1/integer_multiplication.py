# test case: x=12345678, y=87654321
# x*y = 1082152022374638
def recursive_mult(x,y):
    # // return integer
    n = len(str(x))//2
    if n ==0:
        return(x*y)
    # if n below a benmark threshold, terminate the recursion
    a, c = x//(10**n), y//(10**n)
    b, d = x - a*(10**n), y - c*(10**n)
    return((10**(2*n))*recursive_mult(a,c)+(10**n)*(recursive_mult(a,d)+recursive_mult(b,c))+recursive_mult(b,d))

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
print(recursive_mult(x,y))
#print(x*y)
