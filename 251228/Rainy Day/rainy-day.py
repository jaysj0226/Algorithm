n = int(input())
weather_data = []

for _ in range(n):
    d, dy, w = input().split()
    weather_data.append((d,dy,w))

def find_date(w_arr):
    w_arr = sorted(w_arr)
    arr = []
    for i in range(len(w_arr)):
        if w_arr[i][2] == "Rain":
            arr.append(w_arr[i])
    
    return arr

print(*find_date(weather_data)[0])

