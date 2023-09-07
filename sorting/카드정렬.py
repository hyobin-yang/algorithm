n = int(input())
card = [int(input()) for _ in range(n)]

# min_card = []
# def sort(card):
#     temp = card.copy()

#     while len(temp) > 2:
#         if len(temp) == 1: return temp[0]
#         elif len(temp) == 2: return sum(temp)

#         for i in range(n):
#             for j in range(i+1, n):
#                 sum = temp[i] + temp[j]
#                 temp.pop(i)
#                 temp.pop(j)
#                 temp.append(sum)
#                 sort(temp)


# min_card.append(sort(card))

# print(min(min_card))



import heapq
heap = []
for i in range(n):
    heapq.heappush(heap, card[i])

sum_card = 0
while len(heap) > 1:

    if len(heap) == 1: break

    c1 = heapq.heappop(heap)
    c2 = heapq.heappop(heap)

    sum = c1 + c2
    sum_card += sum
    heapq.heappush(heap, sum)

print(sum_card)





