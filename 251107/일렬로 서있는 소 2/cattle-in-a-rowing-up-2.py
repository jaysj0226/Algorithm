N = int(input())
A = list(map(int, input().split()))

# Please write your code here.

# 값 조건 확인용
def check_num(i, j, k):
    return A[i] <= A[j] <= A[k]

# 시뮬레이션
def simulate():
    cnt = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if check_num(i, j, k):
                    cnt += 1
    print(cnt)


simulate()