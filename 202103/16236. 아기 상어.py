import sys
n = int(sys.stdin.readline())
matrix = []
for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    for j in range(len(arr)):
        if arr[j] == 9 :
            start = [i, j]
    matrix.append(arr)
# matrix = [[0, 0, 1], [0, 0, 0], [0, 9, 0]]

print(matrix, start)