strA = input()
strB = input()
lenA = len(strA)
lenB = len(strB)

listA = strA.split()
listB = strB.split()

if lenA > lenB:
    listB.append("*"*(lenA-lenB))
elif lenA < lenB:
    listA.append("*"*(lenB-lenA))


# 공통 문자열 밀려있을 경우 삽입을 사용하는 게 효율적
# 소수의 문자열만이 다를 시 교체가 효율적
# 없어야 하는 문자가 있다면 해당 문자열 삭제
# 있어야 하는 문자가 없다면 해당 문자열 삽입 or 교체


cnt = lenB
for i in range(len(listA)):
    if listA[i] != listB[i]:
        insert(i, cnt)
        remove(i, cnt)
        replace(i, cnt)




