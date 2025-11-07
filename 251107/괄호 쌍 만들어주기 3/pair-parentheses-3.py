A = input()
n = len(A)
# Please write your code here.


def print_ans(n,arr):
    cnt = []
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] == '(' and arr[j] == ')':
                cnt.append(1)
    print(sum(cnt))
    return 0


def simulate():
    print_ans(n,A)
    return 0

simulate()