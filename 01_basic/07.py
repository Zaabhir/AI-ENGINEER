# rogram that accepts a student's marks and prints their grade according to these rules:

# Marks	Grade
# 90–100 A
# 80–89	B
# 70–79	C
# 60–69	D
# Below 60	Fail

marks = int(input("Enter yours marks:" ))

if marks < 0 or marks > 100:
    print("Invalid marks! Enter marks between 0 and 100.")

elif marks >= 90:
    print("Your Grade is A",marks)

elif marks >= 80:
    print("your Grade is B" ,marks) 

elif marks >= 70:
    print("your grade is C" ,marks) 

elif marks >= 60:
    print("your grade is D" ,marks)

else:
    print("Fail! Keep Practicing")            
    
    

       
     