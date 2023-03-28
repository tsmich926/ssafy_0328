# def getTriRun(result,strV):
#     strV = list(map(int,strV))
#     tri = run = 0
#     if strV[result[0]]==strV[result[1]] and strV[result[1]] ==strV[result[2]]:
#         tri += 1
#     if strV[result[3]] == strV[result[4]] and strV[result[4]] == strV[result[5]]:
#         tri += 1
#     # if 0,1,2 run확인
#     if strV[result[0]] + 1 == strV[result[1]] and strV[result[1]] + 1 == strV[result[2]]:
#         run += 1
#     # if 3,4,5 run확인
#     if strV[result[3]] + 1 == strV[result[4]] and strV[result[4]] + 1 == strV[5]:
#         run += 1
#
#     if run>=1 or tri>=1:
#         ans = True
#     else :
#         ans = False
#     return ans


def runtri(p1,p2):
    global ans
    #run검사
    for i in range(0,7,3):
        if p1[i]==1 and p1[i+1]==1 and p1[i+2]==1:
            return 1
    for i in range(10):
        if p1[i] == 3:
            return 1

    for i in range(0,7,3):
        if p2[i]==1 and p2[i+1]==1 and p2[i+2]==1:
            return 2

    for i in range(10):
        if p2[i] == 3:
            return 2

    return 0



T = int(input())
for tc in range(1,T+1):
    nums = [0] + list(map(int,input().split()))
    player1 = []
    p1 = [0]*10
    player2 = []
    p2= [0]*10
    ans = 0
    for i in range(1,13,2): #홀수출력
        player1.append(nums[i])
        player2.append(nums[i+1])

    for i in range(6):
        p1[player1[i]] += 1
        p2[player2[i]] += 1
        if i >= 2:
            runtri(p1,p2)
        if runtri == 1





#3개씩 보면서 babygin인지 확인

# 2 8 7 7 0 2 2 2 5 4 0 3
# 2  7 0 2 5 0
# 8 7 2 2 4 3
# [0,0,2,1,1,0,1,1,0,0]
#3이라고 표시된 부분이 trip
#연속해서 있는 부분이 run
