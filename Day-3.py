#Student Performance Analyzer

n = int(input("Enter the number of students:-  "))
student_marks = [0]*n
student_name = [""]*n
Valid = 0
Failed = 0

for i in range(n):
    student_name[i] = input("Enter your name:- ")
    student_marks[i] = int(input(f"{student_name[i].capitalize()} please enter your marks: "))

for i in range(n):
    if (student_marks[i] >= 0 and student_marks[i] <= 100):
        Valid += 1
        if(student_marks[i] >= 90 and student_marks[i] <= 100):
            print(f"{student_name[i].capitalize()}\'s Marks: {student_marks[i]} ---> Excellent ")
        elif(student_marks[i] >= 75 and student_marks[i] <= 89):
            print(f"{student_name[i].capitalize()}\'s Marks: {student_marks[i]} ---> Very Good ")
        elif(student_marks[i] >= 60 and student_marks[i] <= 74):
            print(f"{student_name[i].capitalize()}\'s Marks: {student_marks[i]} ---> Good ")
        elif(student_marks[i] >= 40 and student_marks[i] <= 59):
            print(f"{student_name[i].capitalize()}\'s Marks: {student_marks[i]} ---> Average ")
        else:
            Failed += 1
            print(f"{student_name[i].capitalize()}\'s Marks: {student_marks[i]} ---> Fail ")

print("Total Valid Students: ",Valid)
print("Total Failed Students: ",Failed)
