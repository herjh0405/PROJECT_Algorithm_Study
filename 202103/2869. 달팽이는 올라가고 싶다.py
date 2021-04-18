import math
a, b, v = map(int, input().split())

day = a-b
print(math.ceil((v-a)/day)+1)