from math import ceil, log, pow
def initial_prompt():
    # loan_principal = int(input("Enter the loan principal:\n"))
    option = input("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount, 
type "p" for the monthly payment:\n""")
    return option

def prompt_by_option(option):
    if option == 'n':
        loan_principal = int(input("Enter the loan principal:\n"))        
        annuity_monthly_payment = float(input("Enter the monthly payment:\n"))
        num_months = None

    elif option == 'a':
        loan_principal = int(input("Enter the loan principal:\n"))
        annuity_monthly_payment = None
        num_months = int(input("Enter the number of periods:\n"))

    elif option == 'p':
        loan_principal = None
        annuity_monthly_payment = float(input("Enter the annuity payment:\n"))
        num_months = int(input("Enter the number of periods:\n"))
    loan_interest = float(input("Enter the loan interst:\n"))
    
    return loan_principal, annuity_monthly_payment, num_months, loan_interest

def calculate(l_i, l_p = None, a_m_p = None, n_m = None):
    if l_i == 0:
        i = 0
    else:
        i = l_i/100/12
    if l_p == None:
        l_p = a_m_p / ((i * pow(1 + i, n_m)) / (pow(1 + i, n_m) - 1))
        return ceil(l_p), None, None
    elif a_m_p == None:
        a_m_p = l_p * ((i * pow(1 + i, n_m)) / (pow(1 + i, n_m) - 1))
        # payment = ceil(principal / months)
        return None, ceil(a_m_p), None
        # last_payment = l_p - (n_m - 1) * ceil(a_m_p)
        # return None, [ceil(a_m_p), last_payment], None
    elif n_m == None:
        if i == 0:
            n_m = l_p // a_m_p
            return None, None, ceil(n_m) 
        base = 1 + i
        x = a_m_p / (a_m_p - (i * l_p))
        n_m = log(x, base)
        return None, None, ceil(n_m)

def print_result(l_p = None, a_m_p = None, n_m = None):
    if n_m:
        year = n_m // 12
        month = n_m % 12
        if year == 1:
            year_str = f"{year} year"
        else:
            year_str = f"{year} years"

        if month == 1:
            month_str = f"{month} month" 
        else:
            month_str = f"{month} months"

        if year != 0 and month != 0:
            print(f"It will take {year_str} and {month_str} to repay this loan!")

        elif year == 0:
            print(f'It will take {month_str} to repay this loan')
        else:
            print(f"It will take {year_str} to repay this loan!")
    elif a_m_p:
        # if a_m_p[0] == a_m_p[1]:
        #     print(f"Your monthly payment = {a_m_p[0]}")
        # else:
        #     print(f"Your monthly payment = {a_m_p[0]} and the last payment = {a_m_p[1]}")
        print(f"Your monthly payment = {a_m_p}!")
    else:
        print(f"Your loan principal = {l_p}!")