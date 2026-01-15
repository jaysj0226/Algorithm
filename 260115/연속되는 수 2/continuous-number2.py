n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
def simulation():
    best = 0
    cnt = 0
    for i in range(n-1):
        if arr[i] != arr[i+1]:
            best = max(best,cnt)
            cnt = 0
        cnt += 1

    print(best)

simulation()
