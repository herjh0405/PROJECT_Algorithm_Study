# 동전 갯수와 값 입력받기
n, k = map(int, input().split())
coin = []

for i in range(n):
    coin.append(int(input()))

coin = sorted(coin, reverse=True)

result = 0

for i in coin:
    if k//i != 0 :
        result += k//i
        k -= (k//i)*i
        if k == 0 :
            break

print(result)