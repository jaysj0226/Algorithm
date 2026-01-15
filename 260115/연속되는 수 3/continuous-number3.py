N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
def simulation():
    best = 0
    cnt = 1
    for i in range(N-1):
        if arr[i] > 0 and arr[i+1] > 0:
            cnt += 1
        elif arr[i] < 0 and arr[i+1] < 0:
            cnt += 1
        else:
            cnt = 1
        best = max(best,cnt)
    
    print(best)

simulation()
        