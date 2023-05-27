# method1:
# def count_vowel(str):
#     count=0
#     vow="aeiou"
#     for i in str:
#         if i in vow:
#             count+=1
#     return count
# word="Hello woerld"
# res=count_vowel(word)
# print("The vowel count is:",res)

# method2:
def count_vowel(str):
    count=0
    vow="aeiou"
    for i in range(0,len(str)):
        if str[i] in vow:
            count+=1
    return count
word="Hello woerld"
res=count_vowel(word)
print("The vowel count is:",res)
