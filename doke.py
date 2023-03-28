T = int(input())
for tc in range(1,T+1):
    N = int(input())
    for i in range(N):
        time = list(map(int,input().split()))
        time.sort(key=lambda x: x[1], reverse=True)
print(time)
    #끝나는 시간이 빠른것을 기준으로 정렬

