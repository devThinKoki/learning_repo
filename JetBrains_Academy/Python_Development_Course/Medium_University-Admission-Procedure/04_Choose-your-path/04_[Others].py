N = int(input("Enter number: "))
with open("applicant_list.txt", "r") as f:
    students = []
    for student in f:
        student = student.rstrip("\n")   # delete trailing newline
        ttt = student.split(" ")  # ['name', 'surname', 'GPA', '1st', '2nd', '3rd']
        students.append(ttt)

departments = ['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics']
admission = dict.fromkeys(departments, [])  # enrolled students be here
enrols = dict.fromkeys(departments, 0)  # counts places occupied
# enrolling
for priority in range(3, 6): # from 1st to 3rd priority
    students = sorted(students, key=lambda x: (-float(x[2]), x[0], x[1]))
    for g, student in enumerate(students):
        for dep in admission:
            if int(enrols[dep]) < N and student[priority] == dep:
                admission[dep].append(student)
                enrols[dep] += 1
                students[g] = ['0', '0', '0', '0', '0', '0']  # a small trick here to exclude enrolled student from list
                                                              # without removing the line itself
# printing result
for dep in admission:
    admission[dep] = sorted(admission[dep], key=lambda x: (-float(x[2]), x[0], x[1]))
    print(dep)
    for student in admission[dep]:
        studX = student[0] + " " + student[1] + " " + student[2]
        print(studX)
    print('\n')