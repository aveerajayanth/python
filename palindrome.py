def is_palindrome(str):
    str=str.lower()
    return str==str[::-1]

word=input("Enter the word:")
if is_palindrome(word):
    print(word,"is a palindrome!")
else:
    print(word,"is not a palindrome!")