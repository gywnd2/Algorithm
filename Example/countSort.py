def countSort(arr, r):
    count=[0 for _ in range(r+1)] 
    for digit in arr:
        count[digit]+=1

    for i in range(len(count)):
        if count[i]!=0:
            for _ in range(count[i]):
                print(i, end='')

#arr=[
#    1,3,2,4,3,2,5,3,1,2,
#    3,4,2,4,5,2,1,3,5,2,
#    1,2,2,4,4,2,3,1,2,5
#]
#countSort(arr, 5)