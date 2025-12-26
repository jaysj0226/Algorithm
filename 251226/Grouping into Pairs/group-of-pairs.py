n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
# 완전탐색
# 변수 선언 및 입력

# nums를 정렬합니다.
nums.sort()

group_max = 0
for i in range(n):
    # i번째와 2n - 1 - i번째 원소를 매칭합니다.
    group_sum = nums[i] + nums[2*n - 1 - i]
    if group_sum > group_max:
        # 최댓값을 갱신합니다.
        group_max = group_sum

print(group_max)
