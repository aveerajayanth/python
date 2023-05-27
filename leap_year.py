def is_leap(num):
    if num%4==0:
        if num%100==0:
            if num%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
num=int(input("Enter the year:"))
if is_leap(num):
    print("It's a leap year!")

else:
    print("It's not a leap year!")