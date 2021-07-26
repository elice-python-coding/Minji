import sys

N = int(input())
sort_arr = [sys.stdin.readline().rstrip() for _ in range(N)]

sort_arr.sort(reverse=True)

print(" ".join(sort_arr))
