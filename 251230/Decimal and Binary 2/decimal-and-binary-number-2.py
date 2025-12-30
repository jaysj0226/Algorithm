N = list(input())
# Please write your code here.
dex = 0
cnt = 0
for i in N[::-1]:
    dex = dex + int(i) * (2**cnt)
    cnt += 1 

dex = dex * 17

cnt = []
while True:
    if dex < 2:
        cnt.append(dex%2)
        break
    cnt.append(dex%2)
    dex = dex // 2

for i in cnt[::-1]:
    print(i,end="")