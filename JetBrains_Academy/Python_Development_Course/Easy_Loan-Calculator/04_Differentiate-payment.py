import argparse
from math import ceil, log, pow
parser = argparse.ArgumentParser(description="This program prints output what you want to know.")

parser.add_argument("-t", "--type", choices=["annuity", "diff"])
parser.add_argument('-i', "--interest", type = float)
parser.add_argument("-pm", "--payment", type = float)
parser.add_argument('-pc', "--principal", type = int)
parser.add_argument("-pr", "--periods", type=int)
def print_err_msg(msg):
    print('Incorrect parameters.')

args = parser.parse_args().__dict__
if 'interest' not in args.keys():
    print('Incorrect parameters.')
    exit()

params = {arg : val for arg, val in args.items() if val}
for val in params.values():
    if isinstance(val, (int, float)) and float(val) < 0:
        print('Incorrect parameters.')
        exit()

if len(params) < 4:
    print('Incorrect parameters.')
    exit()
if params["type"] == "diff":
    sum = 0
    i = float(params["interest"]) / (100 * 12)
    P = int(params["principal"])
    n = int(params["periods"]) 
    for m in range(1, params["periods"] + 1):
        D_m = ceil((P / n) + (i * (P - (P * (m - 1) / n) ))) 
        sum += D_m
        print(f"Month {m}: paym ent is {D_m}")
    print(f"\nOverpayment = {sum - params['principal']}")

elif params["type"] == "annuity":
    if "periods" not in params.keys():
        P = int(params["principal"])
        payment = float(params["payment"])
        i = float(params["interest"]) / (100 * 12)
        if i == 0: 
            n = ceil(P/payment) 
        else: 
            n = ceil(log(payment / (payment - (i * P)), 1 + i))
        years, months, year_months = n // 12, n % 12, ""
        if years > 0:
            year_months += f"{years} year{'s' if years > 1 else ''}"
        if months > 0:
            year_months += f" and {months} month{'s' if months > 1 else ''}"
        print(f"It will take {year_months} to repay this loan!")
        print(f"Overpayment = {int(n * payment - P)}")
    elif "payment" not in params.keys():
        P = int(params["principal"])
        periods = int(params["periods"])
        i = float(params["interest"]) / (100 * 12)
        if i == 0:
            payment = ceil(P / periods) 
        else:
            payment = ceil(P * ((i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1)))
        print(f"Your annuity payment = {payment}!")
        print(f"Overpayment = {int(payment * periods - P)}")
    elif 'principal' not in params.keys():
        payment = float(params["payment"])
        periods = int(params["periods"])
        i = float(params["interest"]) / (100 * 12)
        if i == 0:
            P = payment * periods
        else:
            P = payment / ((i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1))
        print(f"Your loan principal = {P}!")    
        print(f"Overpayment = {int(payment * periods - P)}")
else:   
    print('Impossible here!')