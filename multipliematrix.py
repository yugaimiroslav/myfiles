n = int(input())
matrixA = [[int(i) for i in input().split()] for _ in range(n)]
matrixB = [[0] * n for _ in range(n)]
for i in range(n):
        for j in range(n):
            matrixB[i][j] = matrixA[i][j]
m = int(input())

for x in range(m - 1):
    matrixC = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for q in range(n):
                matrixC[i][j] += matrixA[i][q] * matrixB[q][j]
    for i in range(n):
        for j in range(n):
            matrixB[i][j] = matrixC[i][j]

for row in matrixC:
    print(*row)