def selection_sort(list):
    n=len(list)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if list[j]<list[min_index]:
                min_index=j
        list[i],list[min_index]=list[min_index],list[i]

list=[5,31,6,8,1,4]
selection_sort(list)
print(list)