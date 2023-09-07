## 회의실 배정

# 한 개의 회의실에 여러 개(N개)의 회의 배정
# 회의 시작 = 회의 끝 시간 일 수 있음
# input: 회의의 수 N, N개의 회의 정보(시작, 끝 시간)

# output: 최대 사용할 수 있는 회의의 최대 개수


## 풀이

# 회의가 끝나는 시간이 빠른 순서대로 정렬 후 배정
# 시작시간과 끝시간이 같은 경우 결과 1 증가시키고 리스트에서 제외



n = int(input())
# 최종해
cnt = 0

meeting = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    # 시작시간 == 끝시간일 경우 리스트에 추가하지 않고 해 1증가
    if tmp[0] == tmp[1]: cnt += 1
    else: meeting.append(tmp)


# 끝시간 기준으로 오름차순 정렬
meeting = sorted(meeting, key= lambda x: x[1])
# 끝시간 기본값 설정
end = 0

for time in meeting:
    # 시작시간이 끝시간보다 늦으면
    if time[0] >= end:
        # 해 증가시키기
        cnt += 1
        # 끝시간 갱신
        end = time[1]

# 출력
print(cnt)