n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
def simulation():
    best = 0
    cnt = 0
    for i in range(n):
        if i==0 or arr[i] != arr[i-1]:
            cnt = 0
        cnt += 1
        best = max(best,cnt)

    print(best)

simulation()
