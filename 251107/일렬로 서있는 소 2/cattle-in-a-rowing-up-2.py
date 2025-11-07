N = int(input())
A = list(map(int, input().split()))

# Please write your code here.

# 값 조건 확인용
def check_num(i,j,k):
    if A[i] < A[j] and A[j] < A[k]:
        return True
    else:
        return False
    return 0

# 시뮬레이션
def simulate():
    cnt = []
    for i in range(N):
        for j in range(i,N):
            for k in range(j,N):
                if check_num(i,j,k):
                    cnt.append(1)
                else:
                    continue
    print(sum(cnt))
    return 0

simulate()