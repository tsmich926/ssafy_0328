def per(k,curs):
    global minV

    if curs > minV:
        return

    if k==N:
        print(result)
        # print(result)
        # sumV = 0
        # for idx in range(1,N):
        #     s = result[idx-1]
        #     e = result[idx]
        #     sumV += arr[s][e]
        #
        s = result[N-1]
        e = 0
        sumV =curs+arr[s][e]
        # print(sumV+arr[s][e])

        if minV > sumV:
            minV = sumV
        return

    for i in range(N):
        if not used[i]:
            result[k] = i
            s=result[k-1]
            # e=result[k]
            used[i] = True
            per(k+1,curs+arr[s][i])
            used[i] =False

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    minV =10000

    result= [-1]*N
    used = [False]*N

    result[0]=0
    used[0] = True
    per(1,0)
    print(f'#{tc} {minV}')