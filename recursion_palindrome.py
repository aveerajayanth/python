def recur_palin(string):
    if len(string)<=1:
        return True
    elif string[0]!=string[-1]:
        return False
    else:
        return recur_palin(string[1:-1])
    
word='dads'
if recur_palin(word):
    print("It is palindrome")
else:
    print("It's not palindrome")