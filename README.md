# Divide_and_Conquer_Algo
This repository aims to document my learning progress on a MOOC course "Divide and Conquer, Sorting and Searching, and Randomized Algorithms" by Stanford University

## Week1 Integer Multiplication
Week 1 offers an overview on time complexity analysis and various algorithm on integer multiplication. One of the interger multiplication to be highlighted is Karasutba Algorithm. We also examine method to improve its performance, measured by Big-O notation. 
(i.e by reducing recursive calls from 4 each time to 3 each time)

For programming assignment in week 1, I am required to write an Integer Multiplication Algorithm and apply it on a large input. On the meatime, I did a visualization to compare the performance of the algorithm with 4 recursive calls to the one with 3 recursive calls.

## Week2 Merge Sort and Matrix Multiplication
In week 2  we look at merge sort algorithm and inversion algorithm. It turns out that they works in similar logic. We also look at algorithm on Matrix Multiplication. There is a traditional way to perform it with longer running time, and a smarter way to perform it, namely Strassen Matrix Algoritmh, with running time significantly reduced with the help of divide and conquer method.

As a supplement, we also look into closest pairs algorithm. The purpose of the algorithm is to find out the smallest eucliean distance among an array of input points.

Programming assignment in week 2 require us to write an inversion algorithm and count the number of inversion for a large array input.

To be follow up:
1. Finish optional quiz

## Week3 Quick Sort
In week 3, instructor introduce the idea of randomization algorithm and its application on Quick Sort. Quick sort could have a runtime of O(n^2) in the worst case if the pivot is poorly selected. With the help of randomizing pivot, its average runtime can be dramatically improved to a complexity of O(nlogn).

On top of that, master method is introduced to offer us to framework to analyse the running time of a algorithm. (The framework assumes that the recursive calls have the same input size)

Programming assignment in week 3 require us to write a quick sort algorithm with different approach in choosing pivot (1. always choosing the last, always choosing the first, 3. choosing a "raw median"), and look into its number of operations. It turns out pivot with "raw median" gives a better performance in terms of number of operations.

To be follow up:
1. Write a closest set algorithm
2. Rumination on Master Method

## Week4 Selection Algorithm and Contraction Algorithm 
In week 4 we look at selection algorithm (selecting the nth order of data) and contraction algorithm on undirected graph. It turns out the selection algorithm is closely associated with sorting and with the help of divide and conquer method and randomization, selection algorithm could give a performance of O(nlogn). In contraction algorithm, we aim to find out the minimum cut of a graph with a number of nodes and edges. Randomizing the selection of edge to be contracted may lead to a wrong answer, but with a sufficient number of run, we could significantly increase the odd of getting a right answer.

In weeek 4 programming assignment, I am required to represent a graph in programme (by either adjacency list or adjacency matrix) and apply randomized contraction algorithm on a graph input to find out its minimum cut.

To be follow up:
1. Optimize my outstanding randomized contraction algorithm

## Miscellaneous
During my learning experience in the course, I also did research on other algorithms with application on divide and conquer method.
e.g Power Algorithm

Reference:
https://www.coursera.org/learn/algorithms-divide-conquer/home/welcome
