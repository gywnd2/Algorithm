arr=[
    1,3,2,4,3,2,5,3,1,2,
    3,4,2,4,5,2,1,3,5,2,
    1,2,2,4,4,2,3,1,2,5
]

def countSort(arr, digit):
    temp=[0 for _ in range(len(arr))]
    cnt=[0 for _ in range(10)]
    for i in range(len(arr)):
        cnt[(arr[i]//digit)%10]+=1
    for i in range(1, 10):
        cnt[i]=cnt[i]+cnt[i-1]
    for i in range(len(arr)-1, -1, -1):
        # ex) 251 이고 digit=1 : (251//1)%10=1
        #              digit=10 : (251//10)%10=5
        cntValue=(arr[i]//digit)%10
        newIdx=cnt[cntValue]-1
        temp[newIdx]=arr[i]
        cnt[cntValue]-=1
    #temp는 지역변수 이므로 return하지 않으면 소멸됨
    return temp


def radixSort(arr):
    i=1
    maxVal=max(arr)
    while maxVal//i>0:
        arr=countSort(arr, i)
        i*=10
    return arr
        
arr=radixSort(arr)
print(arr)