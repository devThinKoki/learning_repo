from math import ceil
def initial_prompt():
    loan_principal = int(input("Enter the loan principal:\n"))
    option = input("""What do you want to calculate?
    type "m" - for number of monthly payments,
    type "p" - for the monthly payment:\n""")
    return loan_principal, option

def calculate(principal, months = None, payment = None):
    if payment == None:
        payment = ceil(principal / months)
        last_payment = principal - (months - 1) * payment
        return payment, last_payment
    elif months == None:
        months = ceil(principal / payment)
        return months, None


def prompt_by_option(option):
    if option == 'm':
        monthly_payment = int(input("Enter the monthly payment:\n"))
        num_months = None

    elif option == 'p':
        num_months = int(input("Enter the number of months:\n"))
        monthly_payment = None

    return monthly_payment, num_months

def print_result(result1, result2):
    print()
    if result2 == None:
        if result1 == 1:
            print(f'It will take {result1} month to repay the loan')
        else:
            print(f'It will take {result1} months to repay the loan')
    else:
        if result1 == result2:
            print(f"Your monthly payment = {result1}")
        else:
            print(f"Your monthly payment = {result1} and the last payment = {result2}")