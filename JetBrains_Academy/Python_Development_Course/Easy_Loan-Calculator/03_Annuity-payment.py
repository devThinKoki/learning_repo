from Functions import *

# write your code here
loan_pricipal, option = initial_prompt()
monthly_payment, num_months = prompt_by_option(option)
result1, result2 = calculate(loan_pricipal, num_months, monthly_payment)
print_result(result1, result2)