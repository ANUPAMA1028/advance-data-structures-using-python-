def quick_sort(list):
  if len(list) <=1:
    return list
  else:
    pivort = list[len(list) // 2]
    left = [x for x in list if x < pivort]
    middle = [x for x in list if x == pivort]
    right = [x for x in list if x > pivort]
    return quick_sort(left) + middle + quick_sort(right)

list=[]
n=int(input("enter range for arrary :"))
print("enter elements to the array")
for i in range(0,n):
  ele =int(input())
  list.append(ele)
print("the elements of array are",list)
quick_sort(list)