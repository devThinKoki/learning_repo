# write your code here
all_applicants, depts = {}, sorted(["Mathematics", "Physics", "Biotech", "Chemistry", "Engineering"])
acceptances_dict_by_dept, accepted_students = {dept:[] for dept in depts}, set()

def init():
    global all_applicants
    with open(r'D:\LocalServer\learning_repo\JetBrains_Academy\Python_Development_Course\Medium_University-Admission-Procedure\04_Choose-your-path\example.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            first_name, last_name, gpa, prior1, prior2, prior3 = line.split()
            full_name = first_name + " " + last_name
            all_applicants[full_name] = [float(gpa), [prior1, prior2, prior3]]
            

def select_acceptances_by(prior):
    print(f"\nFunction select_acceptances_by({prior}) is executing.......")
    # global max_students
    global all_applicants, acceptances_dict_by_dept, accepted_students
    for dept in acceptances_dict_by_dept.keys():
        print()
        print(f"\tdept: {dept}")
        print(f"\tCurrent len(acceptances_dict_by_dept[dept]): {len(acceptances_dict_by_dept[dept])}")
        if len(acceptances_dict_by_dept[dept]) != max_students:    
            for full_name, info in all_applicants.items():
                if info[1][prior - 1] == dept and full_name not in accepted_students:
                    acceptances_dict_by_dept[dept].append([full_name, info[0]])
            order_applicants(dept, prior)
            choose_and_delete_applicants(dept)
        else:
            print("\tAlready full! Let's skip")

def order_applicants(dept, prior):
    print(f"\n\tFunction order_applicants({prior}) is executing....")
    global acceptances_dict_by_dept
    stud_list = acceptances_dict_by_dept[dept]
    acceptances_dict_by_dept[dept] = sorted(stud_list, key=lambda x: (-x[1], x[0]))[:max_students]
    ###
    print(f"\t\tlengtth: {len(acceptances_dict_by_dept[dept])}")
    print(f"\t\tprior: {prior}")
    print(f"\t\tdept: {dept}")
    for stud in acceptances_dict_by_dept[dept]:
        print(f"\t\t\t{stud}")
    ###


def choose_and_delete_applicants(dept):
    print("\n\tFunction choose_and_delete_applicants() is executing....")
    # global max_students
    global accepted_students, all_applicants, acceptances_dict_by_dept
    stud_list = acceptances_dict_by_dept[dept]
    for student in stud_list:
        full_name = student[0]
        print(f"\t\tChosen student is : {student}")
        if full_name not in accepted_students:
            print("\t\t\tis not in accepted_students! Let's added!")
            accepted_students.add(full_name)
            del all_applicants[full_name]
    print(f"\t\tCurrent accepted_students are: \n\t\t\t{accepted_students}")

def print_result():
    global acceptances_dict_by_dept
    for dept, dept_list in acceptances_dict_by_dept.items():
        print(dept)
        for acceptance in dept_list:
            print(acceptance[0], acceptance[1])
        print()


max_students = int(input())
init()
for i in range(1, 4):
    select_acceptances_by(i)

print_result()