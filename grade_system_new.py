# GRADE SYSTEM 
student=input("Enter name of the student: ")
print("Hello",student)

# marks obtained by student
print("MARKS OBTAINED BY", student,"ARE AS FOLLOWS:")
mar1=int(input("Enter marks in Maths: "))
mar2=int(input("Enter marks in Physics: "))
mar3=int(input("Enter marks in Chemistry: "))

# average of marks
avg=(mar1+mar2+mar3)/3
print("Average of marks:",avg)

# conditions
if(avg>=90):
    print("Grade A")
elif(avg>=89):
    print("Grade B")
elif(avg>=70):
    print("Grade B")
elif(avg>=60):
    print("Grade c")
else:
    print("Grade D")




