n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
# A = 0 1 2 3 2 6

min_sum = float('inf')
for i in range(n):
    sum_dist = 0
    for j in range(n):
        sum_dist += abs(j-i) * A[j]
    
    min_sum = min(min_sum, sum_dist)

print(min_sum)