X = int(input())

d = [0]*30001


def DivideToOne(X):

    for i in range(2, X+1):
        # 더 작은 값이 나온다면 해당 값으로 바꿀 수 있도록 설정
        d[i] = d[i-1]+1  # X를 1로 뺀 최적의 해
        if i % 2 == 0:  # X를 2로 나눈 최적의 해
            d[i] = min(d[i], d[i//2]+1)
        if i % 3 == 0:  # X를 3으로 나눈 최적의 해
            d[i] = min(d[i], d[i//3]+1)
        if i % 5 == 0:  # X를 5로 나눈 최적의 해
            d[i] = min(d[i], d[i//5]+1)


print(DivideToOne(X))

print(d[X])
