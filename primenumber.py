num=int(input("Enter the number:"))
is_prime=True

if num>1:
    for i in range(2,int(num/2)+1):
        if num%i==0:
            is_prime=False
            break

else:
    is_prime=False

if is_prime:
    print("The number",num,"is prime.")
else:
    print("The number",num,"is not prime.")