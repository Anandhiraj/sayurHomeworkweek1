#write code for both for and while loop
#Get marks from 5  students and calculate avg

#For loop

totalMarks=0
for i in range(5):
    studentMarks= int(input(f"Enter the marks for student {i+1}: "))
    totalMarks += studentMarks
    avgMarks=totalMarks/5
print("The average mark is:",avgMarks)


# While Loop

totalMarks=0
numStudents=0

while numStudents<5:
    studentMarks= int(input(f"Enter the marks for student {i+1}: "))
    totalMarks += studentMarks
    numStudents+=1
    avgMarks=totalMarks/5
print("The average mark is:",avgMarks)