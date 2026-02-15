#Student Performance Analyzer

n = int(input("Enter the number of students:-  "))
student_marks = [0]*n
student_name = [""]*n
student_roll = [0]*n
Valid = 0
Failed = 0

for i in range(n):
    student_name[i] = input("Enter your name:- ")
    student_roll[i] = int(input("Enter your roll number (XXXX):- "))
    student_marks[i] = int(input(f"{student_name[i].capitalize()} please enter your marks: "))
    print("\n")

for i in range(n):
    # Exclusive offer for Prit
    if(student_name[i].capitalize() == 'Prit' and student_roll[i]%100 == student_marks[i]):
        Valid += 1
        student_marks[i] = 98 if student_marks[i] < 95 else student_marks[i]
        print("Hey Prit! it's you. You have always been a topper!! \nYou have got ",
            student_marks[i], "Marks.\n" )
        continue

    # Offers for ALL other Students

    if len(student_name[i]) == 4:   
        student_marks[i] += 2
        print("4 letter legend bonus applied 😎")

    if '7' in str(student_roll[i]):
        if student_marks[i] > 0:
            print("Lucky 7 bonus unlocked 🎯")
            student_marks[i] += 7

    if (student_marks[i] < 40 and student_marks[i] > 0):
        print("Below average performance ❌ 5 marks penalty")
        student_marks[i] -= 5
    
    if (student_marks[i] >= 0 and student_marks[i] <= 100):
        Valid += 1
        if(student_marks[i] >= 90 and student_marks[i] <= 100):
            print(f"{student_name[i].capitalize()}\'s Marks: {student_marks[i]} ---> Excellent \n")
        elif(student_marks[i] >= 75 and student_marks[i] <= 89):
            print(f"{student_name[i].capitalize()}\'s Marks: {student_marks[i]} ---> Very Good \n")
        elif(student_marks[i] >= 60 and student_marks[i] <= 74):
            print(f"{student_name[i].capitalize()}\'s Marks: {student_marks[i]} ---> Good \n")
        elif(student_marks[i] >= 40 and student_marks[i] <= 59):
            print(f"{student_name[i].capitalize()}\'s Marks: {student_marks[i]} ---> Average \n")
        else:
            Failed += 1
            print(f"{student_name[i].capitalize()}\'s Marks: {student_marks[i]} ---> Fail \n")
    else:
        print(f"{student_name[i].capitalize()} has entered invalid marks.\n")

print("Total Valid Students: ",Valid)
print("Total Failed Students: ",Failed)
