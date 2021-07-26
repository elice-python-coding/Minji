N = int(input())
sort_arr = []

for i in range(N):
    data = input().split()
    sort_arr.append((data[0],int(data[1])))

sort_arr.sort(key = lambda student: student[1])

for j in sort_arr:
    print(j[0], end = ' ')
