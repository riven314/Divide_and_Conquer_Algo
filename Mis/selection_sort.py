def selSort(arr):
    n = len(arr)
    for i in range(n-1,0,-1):
        max_index=0
        for j in range(0,i+1):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[max_index], arr[i] = arr[i], arr[max_index]
    return arr

x = [k for k in range(10,0,-1)]
print(x)
print(selSort(x))
