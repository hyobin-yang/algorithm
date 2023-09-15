### 숨바꼭질 3
# 이동 x-1 or x+1
# 순간이동 0초 후 2*x 위치로 이동

n, k = map(int, input().split())

# directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]



# def dijkstra(x, y):
#     if x == n-1 and y == m-1:
#         continue
#     else:
#         for dx, dy in directions:
#             nx, ny = x + dx, y + dy



# 현재 위치에서 +-1 위치에 1 저장
# 현재 위치에서 +-*2 위치에 0 저장
# 최단경로 찾기

import heapq

def dijkstra(start, end):
    distances = [float('inf') for _ in range(100000)]
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_sec, current_pos = heapq.heappop(priority_queue)
        




dijkstra(n, k)
