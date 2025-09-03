n = int(input())

# Please write your code here.

def task(n):
    cnt = 1
    for _ in range(n):
        for i in range(n):
            if cnt < 9:
                print(cnt, end = " ")
                cnt += 1
            else:
                print(cnt, end = " ")
                cnt = 1
        print()
task(n)