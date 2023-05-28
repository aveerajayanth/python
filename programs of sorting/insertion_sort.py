def insertion_sort(list):
    for i in range(1,len(list)):
        j=i-1
        key=list[i]
        while(j>=0 and list[j]>key):
            list[j+1]=list[j]
            j-=1
        list[j+1]=key

l1=[4,3,2,10,12,1,5,6]
insertion_sort(l1)
print(l1)