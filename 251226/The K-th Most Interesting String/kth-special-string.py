n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
def find_str(str):
    arr = []
    for i in str:
        if i.startswith(t):
            arr.append(i)

    return arr

def sort_arr(arr):
    arr = sorted(arr)
    return arr

str = find_str(str)
str = sort_arr(str)
res = str[k-1]

print(res)
