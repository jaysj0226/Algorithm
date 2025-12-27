n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def read_array(arr):
    sub_arr = []
    res_arr = []
    for i in range(len(arr)):
        sub_arr.append(arr[i])
        if (i+1) % 2:
            sub_arr = sorted(sub_arr)
            res_arr.append(sub_arr[i//2])    
    
    return res_arr

print(*read_array(arr))        
