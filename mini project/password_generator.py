import secrets,string

print("-----PASSWORD GENERATOR-----")
length=int(input("Enter the length of password:"))

if(length>0):
    type=int(input("\nCHOOSE THE PASSWORD TYPE\n1:Alphabetic\t2:Numberic\n3:Specialcase\t4:mixed\n"))

    password=''

    if type==1:
        for i in range(length):
            password= password+''.join(secrets.choice(string.ascii_letters))
    elif type==2:
        for i in range(length):
            password+=''.join(secrets.choice(string.digits))
    elif type==3:
        for i in range(length):
            password+=''.join(secrets.choice(string.punctuation))
    elif type==4:
        mixed=string.ascii_letters+string.digits+string.punctuation
        while(True):
            password=''
            for i in range(length):
                password+=''.join(secrets.choice(mixed))
            if(sum(char in string.ascii_letters for char in password)>0 and sum(char in string.digits for char in password)>0 and sum(char in string.punctuation for char in password)>0):
                break
    else:
        print("Choose the correct option.Thank you!")

    print(password)   
else:
    print("The password length must be greater than 0") 