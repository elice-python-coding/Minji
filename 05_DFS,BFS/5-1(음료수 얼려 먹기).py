N, M = map(int,input().split(" "))
arr = [[0]*M for i in range(N)]
count = 0

for j in range(N):
    arr[j] = list(map(int,input()))

def dfs(x, y):
    if x <= -1 or y <= -1 or x >= N or y>= M:
        return False
    if arr[x][y] == 0:
        arr[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x, y+1)
        return True
    return False

for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            count += 1

print(count)
