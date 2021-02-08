# Experiment 2- 2a,2b,2c
2a: Merge sort
### Aim of the experiment- Write a program for implementing the Merge sort


### Step-by-Step procedure for the experiment


Step 1 - The list is divided into left and right in each recursive call until two adjacent elements are obtained.

Step 2 - Now begins the sorting process. The i and j iterators traverse the two halves in each call. The k iterator traverses the whole lists and makes changes along the way.

Step 3 - If the value at i is smaller than the value at j, left[i] is assigned to the myList[k] slot and i is incremented. If not, then right[j] is chosen.

Step 4 - This way, the values being assigned through k are all sorted.

Step 5 - At the end of this loop, one of the halves may not have been traversed completely. Its values are simply assigned to the remaining slots in the list.

# 2b: Heap sort
## Aim of the experiment- Write a program for implementing the Heap sort


### Step-by-Step procedure for the experiment


Step 1 - Build a max heap from the input data.
Step 2 - At this point, the largest item is stored at the root of the heap. Replace it with the last item of the heap followed by reducing the size of heap by 1. ...
Step 3 - Repeat step 2 while size of heap is greater than 1.


# 2c: Quick sort
## Aim of the experiment- Write a program for implementing the Quick sort


### Step-by-Step procedure for the experiment

Step 1 - Consider the first element of the list as pivot (i.e., Element at first position in the list).
Step 2 - Define two variables i and j. Set i and j to first and last elements of the list respectively.
Step 3 - Increment i until list[i] > pivot then stop.
Step 4 - Decrement j until list[j] < pivot then stop.
Step 5 - If i < j then exchange list[i] and list[j].
Step 6 - Repeat steps 3,4 & 5 until i > j.
Step 7 - Exchange the pivot element with list[j] element.


