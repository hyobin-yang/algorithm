### 보물

# S = A[0] × B[0] + ... + A[N-1] × B[N-1]

n = int(input())

arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

arr_A.sort()
arr_B.sort(reverse=True)

ans = 0
for i in range(n):
    ans += arr_A[i] * arr_B[i]

print(ans)