m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
def total_of_days(m,d):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0

    for i in range(1,m):
        total_days += days[i]

    total_days += d

    return total_days

def find_days(a):
    word_days = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
    return word_days[a % 7]


def simulation():
    diff = total_of_days(m2,d2) - total_of_days(m1,d1) + 1
    while diff < 0:
        diff += 7
    res = find_days(diff)

    return res

print(simulation())
