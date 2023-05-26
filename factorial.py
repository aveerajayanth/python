num=int(input("Enter the number:"))
fact=1
i=num
while(i!=0):
    fact *= i
    i= i-1
print("The factorial of",num ,"is:",fact)
