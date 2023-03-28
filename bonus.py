def change(k,value):
    global maxv
    
    # if 같은 k에서 value가 나온적이 있으면
    #     return
    # else:
    #     저장
    #
    # His = [[],[],[]...]


    # value를 가지고 다시 배열로
    arr = list(str(value))
    L = len(arr)
    if k == N:
        #교환끝
        if maxv < value:
            maxv = value

        return
    
    for i in range(L-1):
        for j in range(i+1,L):
            arr[i],arr[j] = arr[j],arr[i]
            #arr을 하나의 숫자로
            value = int(''.join(arr))
            change(k+1, value)
            arr[i], arr[j] = arr[j], arr[i]


T = int(input())
for tc in range(1,T+1):
    value,N = map(int,input().split())
    maxv = 0
    change(0,value) #0번 교환
    print(maxv)