# 백준 10026 적록색약

# 적록색약 -> R/G 차이 못 느낌
# 상하좌우로 인접해있으면 같은 영역
# 적록색약 -> R, G를 하나로 통일한 후 계산해버리기
# 상하좌우에 있는 숫자로 통일 -> 최댓값 == 구역 개수

# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR
n = int(input())
arr = [list(map(str, input().split())) for _ in range(n)]

# 적록색약 색 통일
blindness_arr = arr
for i in range(n):
    for j in range(n):
        if blindness_arr[i][j] == "G":
            blindness_arr[i][j] = "R"




visited = [[False]*n for _ in range(n)]
color_cnt = [[0]*n for _ in range(n)]


visited[0][0] = 1


def section(tmp, x, y, cnt):
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] == tmp and visited[nx][ny] == False:
                color_cnt[nx][ny] = cnt
                visited[nx][ny] = 1
                section(tmp, nx, ny)


tmp = arr[0][0]
color_cnt[0][0] = 1
cnt = 1
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            tmp = arr[i][j]
            section(tmp, i, j, cnt)
        cnt += 1


result = color_cnt[n][n]