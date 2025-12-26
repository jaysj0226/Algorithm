n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
A.sort()
B.sort()

def find(A,B):
    cnt_arr = []
    for i in range(n):
        if A[i] in B:
            cnt_arr.append(1)
        else:
            cnt_arr.append(0)
    if sum(cnt_arr) == n:
        return "Yes"
    else:
        return "No"
res = find(A,B)
print(res)