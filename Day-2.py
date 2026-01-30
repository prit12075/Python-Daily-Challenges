StudentID = input("Enter your studentID (Format: CSE-XXX): ")
EmailID = input("Enter your student mailID: ")
Password = input("Enter your password: ")
Referral_Code = input("Enter your referal code: ")

vStudentID = False
vEmailID = False
vPassword = False
vReferralCode = False

if (StudentID[:3] == "CSE" and StudentID[3] == "-" and StudentID[4:].isdigit() == True):
    vStudentID = True

if ("@" in EmailID and EmailID[0] != "@" and EmailID[-4:] == ".edu"):
    vEmailID = True 

if (len(Password) >= 8 and Password[0].isupper() == True and any(char.isdigit() for char in Password)):
    vPassword = True 

if (Referral_Code[:3] == "REF" and Referral_Code[3:5].isdigit()==True and Referral_Code[-1] == "@"):
    vReferralCode = True

if (vEmailID and vPassword and vReferralCode and vStudentID):
    print("APPROVED")
else:
    print("REJECTED")