n = 10
arr= list(map(int,input().split()))

ans = []
for i in range(len(arr)):
    if arr[i] >= 250:
       break
    ans.append(arr[i])
    

sum_ans = sum(ans)
avg_ans = sum_ans / len(ans)
print(f"{sum_ans} {avg_ans:.1f}")