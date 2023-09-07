### 단어수학


# 길이 가장 긴 단어 순서대로 정렬
# 9부터 할당

# 알파벳 리스트 만들기 [알파벳, 숫자]
# 리스트에 포함되어있는지 아닌지 확인


# 입력
n = int(input())
words_list = [input() for _ in range(n)]
words = words_list

# 단어 길이를 기준으로 내림차순 정렬
# words = sorted(words, key= lambda x: -len(x))

# 알파벳 리스트 생성
alphabet_store = {}

# 숫자 리스트 생성
number = []
for i in range(0, 10):
    number.append(str(i))


# 숫자로 변환한 단어 리스트
# word_change = []

# 영어단어를 숫자로 변환
# for word in words:
#     change = ""
#     for alphabet in word:
#         if alphabet in alphabet_store.keys():
#             change += alphabet_store[alphabet]
#         else:
#             num = number.pop()
#             change += num
#             alphabet_store[alphabet] = num

#     word_change.append(change)



# 값 할당한 문자 앞에서부터 잘라내고
# 계속 words 리스트 갱신 + sort하면서 값 할당하기

# 알파벳 리스트 생성
alphabet_store = {}

while True:
    words = sorted(words, key= lambda x: -len(x))

    word = words[0]

    if not word[0] in alphabet_store.keys():
        num = number.pop()
        alphabet_store[word[0]] = num
        if len(word) > 1:
            new_word = word[1:]
            words.remove(word)
            words.append(new_word)
        else:
            words.remove(word)

    if not words:
        break


ans = 0
for word in words_list:
    change = ""
    for alphabet in word:
        change += alphabet_store[alphabet]
    
    ans += int(change)
    
print(ans)



# ans = 0
# for num in word_change:
#     ans += int(num)

# print(ans)








