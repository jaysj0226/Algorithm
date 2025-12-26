n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
# 오름차순
nums = sorted(nums)
print(*nums)
# 내림차순
nums = nums[::-1]
print(*nums)
