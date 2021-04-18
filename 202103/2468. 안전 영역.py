size = int(input())
matrix =  [list(map(int, input().split())) for _ in range(size)]

area = 0

# 1, 0보다 True, False가 RunTime이 짧음