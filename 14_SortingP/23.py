import sys

input = sys.stdin.readline
N = int(input())
student = []
for i in range(N):
    data = input().strip().split()
    student.append((data[0], int(data[1]), int(data[2]), int(data[3])))
#student = [list(input().strip().split(" ")) for _ in range(N)]


student = sorted(student, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in range(N):
    print(student[i][0])
#print("\n".join([student[i] for i in range(N)]))
# 원래 6-11 어케 정렬하는지 보기
