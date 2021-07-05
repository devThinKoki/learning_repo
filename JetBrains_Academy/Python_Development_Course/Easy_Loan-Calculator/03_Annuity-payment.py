from Functions import *
# write your code here
option = initial_prompt()
principal, payment, periods, interest = prompt_by_option(option)
principal, payment, periods = calculate(loan_interest, loan_principal, annuity_monthly_payment, num_months)
print_result(loan_principal, annuity_monthly_payment, num_months)