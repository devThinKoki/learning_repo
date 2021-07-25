n = int(input())  # max number of students for each department
applicants = []
with open('applicants.txt', 'r') as f:
    for line in f:
        first_name, last_name, gpa, choices = line.split(maxsplit=3)
        applicants.append([f'{first_name} {last_name}', float(gpa), *choices.split()])

departments = ['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics']
##Wow! dict.fromKeys(seq, value)를 사용하기!
#      seq: dict의 Key값으로 사용할 문자열들로 이뤄진 리스트
#      value: 각 key의 값으로 주어질 초기값(default: None)
accepted_students = dict.fromkeys(departments, [])

for i in range(2, 5):
    ranking_lists = dict.fromkeys(departments, [])

    for applicant in applicants:
        new = ranking_lists.get(applicant[i]) + [applicant]
        ranking_lists.update({applicant[i]: new})

    for department in departments:
        ranking_lists[department].sort(key=lambda a: (-a[1], a[0]))
        for applicant in ranking_lists[department]:
            if len(accepted_students[department]) < n:
                new = accepted_students.get(department) + [applicant]
                accepted_students.update({department: new})
                applicants.remove(applicant)

for department in departments:
    print(department)
    accepted_students[department].sort(key=lambda a: (-a[1], a[0]))
    for accepted_student in accepted_students[department]:
        print(*accepted_student[:2])
    print()