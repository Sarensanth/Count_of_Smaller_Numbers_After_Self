def count_of_small(array):
    res=[]
    for i in range(len(array)):
        count=0
        for j in range(i,len(array)):
            if array[i]>array[j]:
                count+=1
        res.append(count)
    return res

array=list(map(int,input().split()))
print(count_of_small(array))