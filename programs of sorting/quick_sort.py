def partition(list,min,max):
   i = ( min-1 )
   pivot = list[max] # pivot element
   for j in range(min , max):
      # If current element is smaller
      if list[j] <= pivot:
         # increment
         i = i+1
         list[i],list[j] = list[j],list[i]
   list[i+1],list[max] = list[max],list[i+1]
   return ( i+1 )
# sort
def quicksort(list,min,max):
   if min < max:
      # index
      pi = partition(list,min,max)
      # sort the partitions
      quicksort(list, min, pi-1)
      quicksort(list, pi+1, max)
# main
list = [2,5,3,8,6,5,4,7]
n = len(list)
quicksort(list,0,n-1)
print ("Sorted list is:")
for i in range(n):
   print (list[i],end=" ")