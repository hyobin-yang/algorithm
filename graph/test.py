# 익은 토마토와 인접한 위치에 있는 익지 않은 토마토 => 하루 지나면 익음
# 익음: 1  / 안 익음: 0 / 들어있지 않음: -1

# 출력: 토마토가 모두 익을 때까지의 최소 날짜
# 모두 익지 못하는 상황에는 -1 출력
# 모두 익어있는 상황에는 0 출력


## 좌표 활용

m, n = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(n)]

def range_check(x, y, box, cnt):
    if (0 <= x < m) and (0 <= y < n):
        if box[x][y] == 0:
            box[x][y] = 1
            cnt += 1
    return cnt

def ripe(box):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                cnt = range_check(n-1, m, box, cnt)
                cnt = range_check(n+1, m, box, cnt)
                cnt = range_check(n, m-1, box, cnt)
                cnt = range_check(n, m+1, box, cnt)
    if cnt == 0:
        return False
    else:
        return True


day = 0
while True:
    ripe(box)
    if not ripe(box):
        break
    else:
        day += 1


if day == 0:
    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                day = -1
                break

print(box)
print(day)


# bfs