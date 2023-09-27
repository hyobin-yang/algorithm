# 세로 R, 가로 C칸 보드
# 보드 각 칸에 대문자 알파벳 적힘
# 1행 1열에는 말
# 말은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 함
# 즉 같은 알파벳 두 번 지날 수 없음
# 말이 최대한 몇 칸을 지날 수 있는지 구하기
# 말이 지나는 칸은 1행 1열의 칸도 포함

r, c = map(int, input().split())
visited_alphabet = []

alphabet_list = [ list(input().rstrip()) for _ in range(r)]
visited_alphabet.append(alphabet_list[0][0])


directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [alphabet_list[0][0]]

def moving(cnt, visited, x, y):
    
    while True:
        if x == r-1 or y == c-1:
            continue
        
        if cnt > current_cnt:
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if (0 <= nx < r) and (0 <= ny < c):
                for dx, dy in directions:
                    
                    if not alphabet_list[dx][dy] in visited:
                        visited.append(alphabet_list[dx][dy])
                        current_cnt = moving(cnt, visited, dx, dy)
                    
                    if current_cnt > cnt:
                        cnt = current_cnt

    return cnt


result = moving(1, visited, 0, 0)
print(result)