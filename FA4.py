nstudents = int(input("Enter number of students: "))
nsubjects = int(input("Enter number of subjects: "))
classroomtotal = 0
for x in range(1, nstudents+1):
    print(f"Student {x}")
    totalscore = 0
    for y in range(1, nsubjects+1):
       score = int(input(f"Enter score {y}: "))
       totalscore += score
    average = float(round(totalscore / nsubjects, 2))
    classroomtotal += average
    print(f"Average for Student {x}: {average}")
classroomavg = float(round(classroomtotal / nstudents, 2))
print(f"Classroom Average: {classroomavg}")
