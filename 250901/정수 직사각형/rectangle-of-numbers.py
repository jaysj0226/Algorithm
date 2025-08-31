N,M = map(int,input().split())

cnt = 0
for i in range(N):
    for j in range(M):
        cnt = cnt + 1
        print(cnt, end = " ")
    print()