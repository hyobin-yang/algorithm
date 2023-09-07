### 수 고르기

# 오름차순 정렬
# 이진탐색
# 차이가 가장 작은 경우의 차이 출력
# 차이가 가장 큰 것(마지막 요소 - 첫 요소)를 기본값으로 설정
# 차이가 M 이상이어야 함
# 차이 = abs(뺄셈)


# 예제 맞음
# 반례 존재

n, m = map(int, input().split())
number_list = [int(input()) for _ in range(n)]
number_list.sort()


n, m = map(int, input().split())
number_list = [int(input()) for _ in range(n)]
number_list.sort()


def binary_search(arr, m):
    tmp = abs(arr[-1] - arr[0])
    left, right = 0, n-1

    while left <= right:
        minus = abs(arr[left] - arr[right])

        if (minus >= m) and (minus < tmp):
            tmp = minus
            left += 1
        elif (minus >= m) and (minus >= tmp):
            left += 1
        else: # m 이상이 아닌 경우, 차이가 더 커져야 함
            if left == 0 and right < n-1:
                right += 1
            elif left > 0:
                left -= 1
            else:
                break
   
    return tmp


ans = binary_search(number_list, m)
print(ans)