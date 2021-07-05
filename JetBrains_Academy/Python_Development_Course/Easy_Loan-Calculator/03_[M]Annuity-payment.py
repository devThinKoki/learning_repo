from math import ceil, log, pow
option = input("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount, 
type "p" for the monthly payment:\n""")
if option == 'n':
    loan_principal = int(input("Enter the loan principal:\n"))        
    annuity_monthly_payment = float(input("Enter the monthly payment:\n"))
    i =  float(input("Enter the loan interst:\n")) / (100 * 12)
    if i == 0: 
        total_months = ceil(loan_principal/annuity_monthly_payment) 
    else: 
        total_months = ceil(log(annuity_monthly_payment / (annuity_monthly_payment - (i * loan_principal)), 1 + i))
    years, months, year_months = total_months // 12, total_months % 12, ""
    if years > 0:
        year_months += f"{years} year{'s' if years > 1 else ''}"
    if months > 0:
        year_months += f" and {months} month{'s' if months > 1 else ''}"
    print(f"It will take {year_months} to repay this loan!")
elif option == 'a':
    loan_principal = int(input("Enter the loan principal:\n"))
    num_months = int(input("Enter the number of periods:\n"))
    i =  float(input("Enter the loan interst:\n")) / (100 * 12)
    if i == 0:
        annuity_monthly_payment = ceil(loan_principal / num_months) 
    else:
        annuity_monthly_payment = ceil(loan_principal * ((i * pow(1 + i, num_months)) / (pow(1 + i, num_months) - 1)))
    print(f"Your monthly payment = {annuity_monthly_payment}!")
elif option == 'p':
    annuity_monthly_payment = float(input("Enter the annuity payment:\n"))
    num_months = int(input("Enter the number of periods:\n"))
    i =  float(input("Enter the loan interst:\n")) / (100 * 12)
    if i == 0:
        loan_principal = ceil(annuity_monthly_payment * num_months)
    else:
        loan_principal = ceil(annuity_monthly_payment / ((i * pow(1 + i, num_months)) / (pow(1 + i, num_months) - 1)))
    print(f"Your loan principal = {loan_principal}!")