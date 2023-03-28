def solve(w,t)
    wi = w.sort(reverse=True)
    ti = t.sort(revere = True)

    idx = 0
    sumV = 0
    for w in wi:
        if w <= ti[idx]:
            sumV += w
            idx += 1



T = int(input())
for tc in range(1,T+1):
    N = list(map(int,input().split()))
    M = list(map(int,input().split()))
