# write a python program that:
# 1. Accept marks for three Subjects.
# 2. Calculate total Marks.
# 3. Calculate AVG Marks
# 4. Calculate the Percentage, Assuming each subject is out of hundred

Sub1 = int(input("Enter marks of first Subject: "))
Sub2 = int(input("Enter marks of second Subject: "))
Sub3 = int(input("Enter marks of third Subject: "))

total_marks = Sub1+Sub2+Sub3
Avg_marks = total_marks/3
percentage = total_marks/300*100

print("Enter marks for Subject 1: ",Sub1)
print("Enter marks for Subject 2: ",Sub2)
print("Enter marks for Subject 3: ",Sub3)

print("Total Marks: ",total_marks)
print(f"Average marks:  {Avg_marks:.2f}")
print(f"Percentage: {percentage:.2f}")