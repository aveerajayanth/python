num=int(input("Enter the length of fibonacci:"))
fib=[0,1]

while(len(fib)<num):
    nextnum=fib[-1]+fib[-2]
    fib.append(nextnum)

print("Fibonacci Sequence is:",fib)