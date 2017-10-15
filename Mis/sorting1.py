#29 Oct 2017
#Bubble Sort
#It is a simple algorithm for sorting with O(n^2)

# worst case
y = []
for i in range(100,0,-1):
    y.append(i)

# slicing
x = y[:]

def BubbleSort(x):
    for i in range(len(x)-1,0,-1):
        for j in range(i):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return x

# record runtime time for each worst scenario with varying data volume
# How to record time in Python
# https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
import time
datasize_runtime = []
for n in range(10):
    data_sample = list(range(int(2**n),0,-1))
    start_time = time.time()
    BubbleSort(data_sample)
    end_time = time.time() - start_time
    datasize_runtime.append((len(data_sample),end_time))
    del end_time, data_sample, start_time

# scatter plot to visualize the performance of bubblesorting
import matplotlib.pyplot as plt
data_size = []
run_time = []
for datasize, runtime in datasize_runtime:
    data_size.append(datasize)
    run_time.append(runtime)

plt.scatter(data_size,run_time)
plt.show()
