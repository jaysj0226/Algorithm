n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

# Please write your code here.
def sort_in_order(stu):
    stu.sort(key=lambda x: (x[0],-x[1]))
    return stu

def info(stu):
    for h, w, i in stu:
        print(h,w, i)
    return 

students = sort_in_order(students)
info(students)