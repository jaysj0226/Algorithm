N, B = map(int, input().split())

# Please write your code here.
cnt = []
while True:
    if N < B:
        cnt.append(N % B)
        break
    cnt.append(N%B)
    N = N // B

for i in cnt[::-1]:
    print(i, end = "")