n, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
res = nums[k]
print(res-1)