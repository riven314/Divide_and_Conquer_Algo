# define the median of 3 rules
import statistics as stat
def median_sort(x):
    first_pivot = x[0]
    last_pivot = x[len(x)-1]
    if len(x)%2==0:
        middle_index = (len(x)//2)-1
    else:
        middle_index = len(x)//2
    middle_pivot = x[middle_index]
    return stat.median([first_pivot,middle_pivot,last_pivot])

#s = starting index
#e = ending index (e index inclusive)
def quick_sort(x,s,e):
    if e-s <= 0:
        return 0
    else:
        counter = e-s
        #Q3
        #if s-e<=2:
        #    median_index = x.index(median_sort(x[s:e+1]))
        #    x[median_index], x[s] = x[s], x[median_index]
        # Exchange the last element and first element
        #Q2
        #x[s], x[e] = x[e],x[s]
        pivot_pos = partition_first(x,s,e)
        counter_L = quick_sort(x,s,pivot_pos-1)
        counter_R = quick_sort(x,pivot_pos+1,e)
        return (counter + counter_L + counter_R)

# s,e are both index position instead of actual position
# Question1
def partition_first(x,s,e):
    pivot = x[s]
    i = s+1
    for j in range(s+1,e+1,1):
        if x[j] < pivot:
            x[j], x[i] = x[i], x[j]
            i+=1
    x[s], x[i-1] = x[i-1], x[s]
    position = x.index(pivot)
    return position

# Question2
def partition_second(x,s,e):
    pivot = x[e]
    i = s
    for j in range(s,e,1):
        if x[j] < pivot:
            x[j], x[i] = x[i], x[j]
            i+=1
    x[e], x[i] = x[i], x[e]
    position = x.index(pivot)
    return position


#A = [1,3,5,2,4,6]

# Read data from external file
filename = "test_case.txt"
f = open(filename, "r")
data = []
j=0

for line in f:
    data.append(line)

f.close()

# map() can smartly turn string into value
data = list(map(int,data))

#Test case ans
#10: 25 31 21
#100: 620 573 502
#1000: 11175 10957 9735

#Follow up: the quick_sort( ) cannot be applied in sorted list
