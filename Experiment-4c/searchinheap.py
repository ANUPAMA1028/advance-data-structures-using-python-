def search():
  heap = []
  n = int(input('Enter the no of elements: '))
  for i in range (0,n):
    data=int(input())
    heap.insert(i,data)
  import heapq
  s=int(input("Enter the element to be searched:"))
  count=1
  for i in range(0,len(heap)):
      if(s==heap[i]):
          print("Element found at",i+1)
          count=0
          break
  if(not count==0):
    print("element not found")
search()