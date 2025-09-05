N = int(input())

arr = list(map(float, input().split()))

avg_arr = sum(arr) / N

print(f"{avg_arr:.1f}")

if avg_arr >= 4.0:
    print("Perfect")
elif avg_arr >= 3.0:
    print("Good")
else:
    print("Poor")