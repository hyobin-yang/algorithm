### 세 용액 문제

# 세 용액의 특성값의 합이 0에 가장 가깝게 하는 용액의 조합
# 해당 용액들의 특성값 오름차순으로 출력

n = int(input())
solution = list(map(int, input().split()))
solution.sort()

def near_zero(left, right):
    ans = float('inf')
    result = []
    for s in solution:
        tmp_arr = solution[:] # solution 리스트 변경하지 않고 복사
        tmp_arr.remove(s)
        compound = s

        while left < right:
            compound += (tmp_arr[left] + tmp_arr[right])
            
            if ans > abs(compound):
                result= [s, tmp_arr[left], tmp_arr[right]]
                ans = abs(compound)

            if compound < 0:
                left += 1
            elif compound > 0:
                right -= 1
            else:
                return result
    return result


answer = near_zero(0, n-2)
answer.sort()
print(answer[0], answer[1], answer[2])
