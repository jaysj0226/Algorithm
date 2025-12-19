n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def max_value(a):
    if a == 0:
        return arr[0]
    return max(max_value(a - 1), arr[a])

print(max_value(n - 1))
