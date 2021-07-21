limit_number, all_applicants = 0, []

def init():
    global limit_number, all_applicants
    total_applicants = int(input())
    limit_number = int(input())
    for _ in range(total_applicants):
        first, last, gpa = input().split()
        gpa = float(gpa)
        all_applicants.append([f"{first} {last}", gpa])


def order_applicants(applicants_list): 
    return sorted(applicants_list, key=lambda x: (-x[1], x[0]))


def print_success(limit_number, ordered_applicants):
    for i in range(limit_number):
       print(ordered_applicants[i][0])    

       
init()
print('Successful applicants:')
print_success(limit_number, order_applicants(all_applicants))
