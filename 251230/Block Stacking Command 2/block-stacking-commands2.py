n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

#음
diff = [0] * (n+2)

for a, b in commands:

    diff[a] += 1
    if b + 1 <= n:
        diff[b+1] -= 1
    else:
        diff[b+1] -= 1

cur = 0
ans = 0
for i in range(1,n+1):
    cur+=diff[i]
    if cur > ans:
        ans = cur
print(ans)