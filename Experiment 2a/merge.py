def merge_sort(list):
    size = len(list)
    if size > 1:
        middle = size // 2
        left_arr = list[:middle]
        right_arr = list[middle:]
 
        merge_sort(left_arr)
        merge_sort(right_arr)
 
        p = 0
        q = 0
        r = 0
 
        left_size = len(left_arr)
        right_size = len(right_arr)
        while p < left_size and q < right_size:
            if left_arr[p] < right_arr[q]:
              list[r] = left_arr[p]
              p += 1
            else:
                list[r] = right_arr[q]
                q += 1
             
            r += 1
 
        
        while p < left_size:
            list[r] = left_arr[p]
            p += 1
            r += 1
 
        while q < right_size:
            list[r]=right_arr[q]
            q += 1
            r += 1
 
list=[]
n=int(input("enter range for arrary :"))
print("enter elements to the array")
for i in range(0,n):
  ele =int(input())
  list.append(ele)
print("Input Array is:\n")
print(list)
merge_sort(list)
print("Sorted Array is:\n")
print(list)