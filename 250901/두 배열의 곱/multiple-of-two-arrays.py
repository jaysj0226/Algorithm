n = 3
arr1 = [list(map(int,input().split())) for i in range(n)]
input()
arr2 = [list(map(int,input().split())) for i in range(n)]

for i in range(n):
    for j in range(n):
        print(arr1[i][j] * arr2[i][j], end = " ")
    print()