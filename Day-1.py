name = input("Please enter your Full Name:- ")
email = input ("Enter your email address:- ")
number = input("Enter your mobile number:- ")
age = int(input("Enter your age:- "))

vName = False
vEmail = False
vNum = False
vAge = False

if " " in name:
    if (name[0] != " " and name[len(name)-1] != " "):
        vName = True

if("@" in email and email[0] != "@"):
    vEmail = True

if(len(number) == 10 and number.isdigit() == True and number[0] != "0"):
    vNum = True

if(age >= 18 and age <=60):
    vAge = True

if(vAge and vEmail and vNum and vName):
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")
