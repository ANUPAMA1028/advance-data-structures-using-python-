
Experiment 4c

Aim of the experiment - Write a program to perform the following operations: 4c)Search an element from a Min-Max heap

procedure for the experiment 1.heap can be used to search whether an element is in it or not with O(logN) time complexity. 2.You need to search through every element in the heap in order to determine if an element is inside. 3.If you have reached a node with a lower value than the element you are searching for, you don't need to search further from that node. However, even with this optimization, search is still O(N) (need to check N/2 nodes in average).
