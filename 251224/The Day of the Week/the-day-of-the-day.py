m1, d1, m2, d2 = map(int, input().split())
A = input().strip()

week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 2024 윤년

def day_of_year(m, d):
    total = 0
    for i in range(1, m):
        total += days_in_month[i]   
    total += d
    return total

start = day_of_year(m1, d1)
end = day_of_year(m2, d2)
n = end - start + 1 

q, r = divmod(n, 7)
a_idx = week.index(A)

# 시작 요일이 월요일(week[0])이므로, 남는 r일은 week[0]~week[r-1]
ans = q + (1 if a_idx < r else 0)

print(ans)
