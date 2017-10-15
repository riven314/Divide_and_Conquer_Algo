# Define merge sort function
def merge_sort(x):
    x_len = len(x)
    if x_len<=1:
        return(x,0)
    else:
        x_L, inv_count_L = merge_sort(x[:x_len//2])
        x_R, inv_count_R = merge_sort(x[x_len//2:])
        x_sorted = []
        inv_count = 0
        i, j = 0, 0
        while len(x_L)!=0 and len(x_R)!=0:
            if x_L[0] > x_R[0]:
                inv_count += len(x_L)
                x_sorted.append(x_R[0])
                x_R.remove(x_R[0])
            elif x_L[0] < x_R[0]:
                x_sorted.append(x_L[0])
                x_L.remove(x_L[0])
        if len(x_L) == 0:
            x_sorted += x_R
        else:
            x_sorted += x_L
        return(x_sorted, (inv_count + inv_count_L+ inv_count_R))

# Read data from txt file
filename = "test_case.txt"
f = open(filename, "r")
data = []
j=0
for line in f:
    data.append(line)

# map() can smartly turn string into value
data = list(map(int,data))
sorted_data, inv_num = merge_sort(data)
print(inv_num)

#Test Case 1
#test_case1 = [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54]
#Ans: 2372
#Test_Case 2
#test_case2 = [37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45]
#Ans:590
