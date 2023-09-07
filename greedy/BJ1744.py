### 주유소

# 가장 싼 곳에서 많이 넣고 많이 가기

# 도시 개수
n = int(input())
# 도로 길이
road_len = list(map(int, input().split()))
# 기름값
oil_price = list(map(int, input().split()))

ans = 0

road = 1
while oil_price[0] < oil_price[road]:
    if road > n-2:
        break
    road += 1

for i in range(road):
    ans += oil_price[0] * road_len[i]



def moving(road):
    if oil_price[road] <= oil_price[road+1]:
        a=1

    return 


if road != n-2:
    moving(road)